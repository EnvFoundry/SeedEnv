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
        for component in self.components.values():
            kind = component.get("kind")
            if kind not in {"python", "command", "plugin", "connector"}:
                raise ValueError(f"Unknown component kind: {kind}")
            for field in ("requirements", "imports", "commands", "platforms"):
                entries = component.get(field, [])
                if not isinstance(entries, list) or any(not isinstance(x, str) or not x.strip() for x in entries):
                    raise ValueError(f"{component['id']}.{field} must contain nonempty strings")
            if kind == "python":
                if not component.get("requirements") or not component.get("imports"):
                    raise ValueError(f"{component['id']} needs requirements and imports")
                if any(x.startswith('-') for x in component['requirements']):
                    raise ValueError("Requirements cannot be installer options")
            if kind == "command" and not component.get("commands"):
                raise ValueError(f"{component['id']} needs executable names")
            if kind == "plugin" and not str(component.get("url", "")).startswith("https://"):
                raise ValueError(f"{component['id']} needs a plugin URL")
            if kind == "connector" and not isinstance(component.get("connection"), dict):
                raise ValueError(f"{component['id']} needs connection instructions")
        for name in self.modules:
            self.select([name])
            self.guide(name)
            example = self.modules[name].get("example")
            if example:
                _, components = self.select([name])
                if example["component"] not in components:
                    raise ValueError(f"{name} example needs a component outside its module")
                self.resource(name, example["file"])

    def select(self, names: list[str]) -> tuple[list[str], list[str]]:
        if not names:
            raise ValueError("Select at least one research module or component")
        modules, components, visiting = [], [], set()

        def visit(name):
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

    def search(self, query="", limit=20, offset=0):
        if not 1 <= limit <= 100 or offset < 0:
            raise ValueError("Use limit 1–100 and offset >= 0")
        words = query.casefold().split()
        matches = []
        for item in self.modules.values():
            _, components = self.select([item["id"]])
            haystack = json.dumps([item, [self.components[x] for x in components]], ensure_ascii=False).casefold()
            if all(word in haystack for word in words):
                matches.append({k: item[k] for k in ("id", "title", "summary", "tags", "components", "includes") if k in item})
        return {"items": matches[offset:offset + limit], "total": len(matches),
                "next_offset": offset + limit if offset + limit < len(matches) else None}

    def show(self, name):
        if name in self.components:
            return dict(self.components[name])
        modules, components = self.select([name])
        return {**self.modules[name], "resolved_modules": modules,
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
