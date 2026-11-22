"""A small catalogue shared by the CLI, host clients and MCP."""
from __future__ import annotations

import json
from pathlib import Path
import re

DATA = Path(__file__).parent / "data"


class Catalog:
    def __init__(self, extra: str | Path | None = None):
        self.extra = str(Path(extra).absolute()) if extra else None
        self.components: dict[str, dict] = {}
        self.modules: dict[str, dict] = {}
        self.fields: dict[str, dict] = {}
        self.roots: dict[str, Path] = {}
        paths = [DATA / "catalog.json"] + ([Path(self.extra)] if self.extra else [])
        for path in paths:
            value = json.loads(path.read_text(encoding="utf-8"))
            for kind in ("components", "modules"):
                for item in value.get(kind, []):
                    name = item.get("id", "")
                    if not re.fullmatch(r"[a-z][a-z0-9-]{0,79}", name):
                        raise ValueError(f"Invalid component or module name: {name!r}")
                    if name in self.components or name in self.modules:
                        raise ValueError(f"Duplicate component or module: {name}")
                    if not isinstance(item.get("title"), str):
                        raise ValueError(f"{name} needs a title")
                    getattr(self, kind)[name] = item
                    self.roots[name] = path.parent
            for field in value.get("fields", []):
                name = field["id"]
                if name in self.fields:
                    existing = self.fields[name]
                    if field["title"] != existing["title"]:
                        raise ValueError(f"Conflicting field title: {name}")
                    for direction in field["directions"]:
                        match = next((d for d in existing["directions"] if d["id"] == direction["id"]), None)
                        if match:
                            if match["title"] != direction["title"]:
                                raise ValueError(f"Conflicting direction title: {name}/{direction['id']}")
                            match["modules"] = list(dict.fromkeys([*match["modules"], *direction["modules"]]))
                        else:
                            existing["directions"].append(direction)
                    existing["resources"] = list(dict.fromkeys([*existing.get("resources", []), *field.get("resources", [])]))
                else:
                    self.fields[name] = field
        self.paths: dict[str, list[dict]] = {name: [] for name in self.modules}
        for field in self.fields.values():
            seen = set()
            for direction in field["directions"]:
                if direction["id"] in seen:
                    raise ValueError(f"Duplicate direction in {field['id']}: {direction['id']}")
                seen.add(direction["id"])
                for name in dict.fromkeys(direction["modules"]):
                    if name not in self.modules:
                        raise ValueError(f"{field['id']}/{direction['id']} refers to missing module {name}")
                    self.paths[name].append({"field": field["id"], "field_title": field["title"],
                                             "direction": direction["id"], "direction_title": direction["title"]})
            for name in field.get("resources", []):
                if name not in self.modules:
                    raise ValueError(f"{field['id']} refers to missing resource {name}")
                self.paths[name].append({"field": field["id"], "field_title": field["title"],
                                         "direction": "", "direction_title": "Related resources · 相关资源"})
        for component in self.components.values():
            kind = component.get("kind")
            if kind not in {"python", "environment", "command", "plugin", "connector"}:
                raise ValueError(f"Unknown component kind: {kind}")
            for field in ("requirements", "imports", "commands", "platforms", "conda"):
                entries = component.get(field, [])
                if not isinstance(entries, list) or any(not isinstance(x, str) or not x.strip() for x in entries):
                    raise ValueError(f"{component['id']}.{field} must contain nonempty strings")
            if kind == "python":
                if not component.get("requirements") or not component.get("imports"):
                    raise ValueError(f"{component['id']} needs requirements and imports")
                if any(x.startswith('-') for x in component['requirements']):
                    raise ValueError("Requirements cannot be installer options")
            if kind == "environment" and not component.get("imports"):
                raise ValueError(f"{component['id']} needs interpreter imports")
            if component.get("conda") and (kind != "environment" or any(x.startswith('-') for x in component['conda'])):
                raise ValueError(f"{component['id']} needs conda package names, not installer options")
            for parent in component.get("reuse_from", []):
                candidate = self.components.get(parent, {})
                if kind != "python" or candidate.get("kind") != "python":
                    raise ValueError(f"{component['id']} cannot reuse {parent}")
            if kind == "command" and not component.get("commands"):
                raise ValueError(f"{component['id']} needs executable names")
            if kind == "plugin" and not str(component.get("url", "")).startswith("https://"):
                raise ValueError(f"{component['id']} needs a plugin URL")
            if kind == "connector" and not isinstance(component.get("connection"), dict):
                raise ValueError(f"{component['id']} needs connection instructions")
        for name in self.modules:
            self.select([name])
            self.resource(name, self.modules[name]["guide"])
            example = self.modules[name].get("example")
            if example:
                _, components = self.select([name])
                if example["component"] not in components:
                    raise ValueError(f"{name} example needs a component outside its module")
                self.resource(name, example["file"])

    def select(self, names: list[str]) -> tuple[list[str], list[str]]:
        modules, components, visiting = [], [], set()

        def visit(name):
            if name in self.fields:
                raise ValueError(f"{name} is a field. Browse its directions and select individual modules.")
            if name in self.components:
                if name not in components:
                    components.append(name)
                return
            if name not in self.modules:
                raise ValueError(f"Unknown module or component: {name}")
            if name in visiting:
                raise ValueError(f"Circular module inclusion at {name}")
            if name in modules:
                return
            visiting.add(name)
            item = self.modules[name]
            for child in item.get("includes", []):
                visit(child)
            for child in item.get("components", []):
                if child not in self.components:
                    raise ValueError(f"{name} refers to missing component {child}")
                visit(child)
            visiting.remove(name)
            modules.append(name)

        for name in names:
            visit(name)
        return modules, components

    def browse(self, field=None):
        if field is not None and field not in self.fields:
            raise ValueError(f"Unknown field: {field}")
        fields = [{"id": item["id"], "title": item["title"],
                   "kind": item.get("kind", "research"), "direction_count": len(item["directions"]),
                   "resource_count": len(set(item.get("resources", []))),
                   "module_count": len({name for d in item["directions"] for name in d["modules"] if not self.modules[name].get("hidden")})}
                  for item in self.fields.values()]
        directions = [] if field is None else [
            {"id": d["id"], "title": d["title"], "module_count": len(set(d["modules"]))}
            for d in self.fields[field]["directions"]]
        visible = [m for m in self.modules.values() if not m.get("hidden")]
        return {"fields": fields, "field": field, "directions": directions,
                "resources": [] if field is None else [self._summary(self.modules[n]) for n in self.fields[field].get("resources", [])],
                "totals": {"fields": len(fields), "directions": sum(f["direction_count"] for f in fields),
                           "modules": sum(m.get("kind", "module") == "module" for m in visible),
                           "resources": sum(m.get("kind") == "resource" for m in visible)}}

    def _summary(self, item):
        _, components = self.select([item["id"]])
        return {**{k: item[k] for k in ("id", "title", "summary", "summary_en", "tags", "components", "includes") if k in item},
                "kind": item.get("kind", "module"), "paths": self.paths[item["id"]],
                "software": [{k: self.components[x][k] for k in ("id", "title", "kind")} for x in components]}

    def search(self, query="", limit=20, offset=0, field=None, direction=None):
        if not 1 <= limit <= 100 or offset < 0:
            raise ValueError("Use limit 1–100 and offset >= 0")
        if field is not None and field not in self.fields:
            raise ValueError(f"Unknown field: {field}")
        if direction is not None and (field is None or direction not in
                {d["id"] for d in self.fields[field]["directions"]}):
            raise ValueError("Choose a direction within its field")
        words = query.casefold().split()
        matches = []
        for item in self.modules.values():
            if item.get("hidden"):
                continue
            paths = self.paths[item["id"]]
            if field and not any(p["field"] == field and (direction is None or p["direction"] == direction) for p in paths):
                continue
            _, components = self.select([item["id"]])
            haystack = json.dumps([item, paths, [self.components[x] for x in components]], ensure_ascii=False).casefold()
            if all(word in haystack for word in words):
                matches.append(self._summary(item))
        return {"items": matches[offset:offset + limit], "total": len(matches),
                "next_offset": offset + limit if offset + limit < len(matches) else None}

    def show(self, name):
        if name in self.components:
            return dict(self.components[name])
        modules, components = self.select([name])
        return {**self.modules[name], "resolved_modules": modules,
                "paths": self.paths[name],
                "software": [self.components[key] for key in components]}

    def resource(self, name, relative):
        root = self.roots[name].resolve()
        path = (root / relative).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError(f"Missing module resource: {name}/{relative}")
        return path

    def guide(self, name):
        if name not in self.modules:
            raise ValueError(f"Unknown module: {name}")
        return self.resource(name, self.modules[name]["guide"]).read_text(encoding="utf-8")

    def example(self, name):
        if name not in self.modules:
            raise ValueError(f"Unknown module: {name}")
        example = self.modules[name].get("example")
        if not example:
            raise ValueError("This module links to upstream examples in its guide")
        return {"module": name, **example, "uri": "seedenv://examples/" + name,
                "content": self.resource(name, example["file"]).read_text(encoding="utf-8")}
