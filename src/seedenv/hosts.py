"""Host packages use the same catalogue and preparer as standalone clients."""
import json
from pathlib import Path
import shutil
import sys
import uuid

from .catalog import DATA, Catalog


def origo_requests(manager, selections, destination="environments"):
    plan = manager.plan(selections)
    requests, connections = [], []
    # The existing Origo API owns jobs and installation. Its required identity
    # fields stay inside this adapter, away from module descriptions and UI.
    for item in plan["actions"]:
        component = manager.catalog.components[item["component"]]
        if item["action"] == "install" and component["kind"] == "python":
            token = uuid.uuid4().hex[:12]
            requests.append({"component": item["component"], "request": {
                "execution_id": "seedenv-" + uuid.uuid4().hex,
                "id": item["component"], "version": token,
                "destination": destination.rstrip("/") + "/" + item["component"] + "-" + token,
                "requirements": component["requirements"],
            }})
        elif component.get("origo_preset") and item["action"] in {"setup", "install"}:
            token = uuid.uuid4().hex[:12]
            requests.append({"component": item["component"], "request": {
                "execution_id": "seedenv-" + uuid.uuid4().hex,
                "id": item["component"], "version": token,
                "destination": destination.rstrip("/") + "/" + item["component"] + "-" + token,
                "preset": component["origo_preset"],
            }})
        else:
            connections.append(item)
    return {"modules": plan["modules"], "installation_root": str(manager.home),
            "preparations": requests, "connections": connections}


def export_plugin(output, host="origo", home=None, catalog=None, selections=None):
    output = Path(output).absolute()
    if output.exists():
        raise FileExistsError(f"Choose a new output directory: {output}")
    if host not in {"origo", "mcp"}:
        raise ValueError("host must be origo or mcp")
    source = Catalog(catalog)
    names, ids = source.select(list(source.modules) + list(source.components) if selections is None else selections)
    # Keep metadata for known predecessors so existing installations remain reusable.
    for component in ids:
        ids.extend(p for p in source.components[component].get("reuse_from", []) if p not in ids)
    output.mkdir(parents=True)
    shutil.copytree(Path(__file__).parent, output / "seedenv", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    data = output / "seedenv" / "data"
    if "writing-templates" not in names:
        shutil.rmtree(data / "writing", ignore_errors=True)
    for directory in ("guides", "examples"):
        shutil.rmtree(data / directory)
        (data / directory).mkdir()
    modules = []
    for name in names:
        item = dict(source.modules[name])
        guide = f"guides/{name}.md"
        shutil.copy2(source.resource(name, item["guide"]), data / guide)
        item["guide"] = guide
        if item.get("example"):
            example = dict(item["example"])
            original = source.resource(name, example["file"])
            example["file"] = f"examples/{name}{original.suffix}"
            shutil.copy2(original, data / example["file"])
            item["example"] = example
        modules.append(item)
    fields = []
    for field in source.fields.values():
        directions = [{**d, "modules": [n for n in d["modules"] if n in names]} for d in field["directions"]]
        directions = [d for d in directions if d["modules"]]
        resources = [n for n in field.get("resources", []) if n in names]
        if directions or resources:
            fields.append({**field, "directions": directions, "resources": resources})
    (data / "catalog.json").write_text(json.dumps({"components": [source.components[n] for n in ids],
        "modules": modules, "fields": fields}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (output / "server.py").write_text("from seedenv.mcp import serve\nserve()\n", encoding="utf-8")
    environment = {}
    if home:
        environment["SEEDENV_HOME"] = str(Path(home).expanduser().absolute())
    skill = output / "skills" / "seedenv"
    skill.mkdir(parents=True)
    shutil.copy2(DATA / "agent-guide.md", skill / "SKILL.md")
    if host == "mcp":
        shutil.copy2(DATA / "configure_mcp.py", output / "configure.py")
        value = {"mcpServers": {"seedenv": {"command": sys.executable,
                 "args": ["-B", str(output / "server.py")], "env": environment}}}
        (output / "mcp.json").write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    else:
        value = {"name": "seedenv", "version": "0.1.0", "description": "Prepare and reuse research tools across disciplines",
                 "skills": ["skills/seedenv"], "environment": {"resources": []},
                 "mcpServers": {"seedenv": {"transport": "stdio", "command": "${RESEARCH_PYTHON}",
                    "args": ["-B", "${PACKAGE_ROOT}/server.py"], "protocol_version": "2025-11-25",
                    "env": environment}}}
        (output / "plugin.json").write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    return {"host": host, "path": str(output), "installed": False, "modules": names,
            "next": ("Import mcp.json in your agent host. After moving this package, run "
                     "python configure.py --research-space PATH on the receiving computer first."
                     if host == "mcp" else "Import this package in the host, then activate SeedEnv")}
