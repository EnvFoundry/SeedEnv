"""Host packages use the same catalogue and preparer as standalone clients."""
import json
from pathlib import Path
import shutil
import sys
import uuid

from .catalog import DATA


def origo_requests(manager, selections, destination="System/software/seedenv"):
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
        elif component.get("origo_preset") and item["action"] == "setup":
            token = uuid.uuid4().hex[:12]
            requests.append({"component": item["component"], "request": {
                "execution_id": "seedenv-" + uuid.uuid4().hex,
                "id": item["component"], "version": token,
                "destination": destination.rstrip("/") + "/" + item["component"] + "-" + token,
                "preset": component["origo_preset"],
            }})
        else:
            connections.append(item)
    return {"modules": plan["modules"], "preparations": requests, "connections": connections}


def export_plugin(output, host="origo", home=None, catalog=None):
    output = Path(output).absolute()
    if output.exists():
        raise FileExistsError(f"Choose a new output directory: {output}")
    if host not in {"origo", "mcp"}:
        raise ValueError("host must be origo or mcp")
    output.mkdir(parents=True)
    shutil.copytree(Path(__file__).parent, output / "seedenv", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    (output / "server.py").write_text("from seedenv.mcp import serve\nserve()\n", encoding="utf-8")
    environment = {}
    if home:
        environment["SEEDENV_HOME"] = str(Path(home).expanduser().absolute())
    if catalog:
        environment["SEEDENV_CATALOG"] = str(Path(catalog).absolute())
    if host == "mcp":
        value = {"mcpServers": {"seedenv": {"command": sys.executable,
                 "args": ["-B", str(output / "server.py")], "env": environment}}}
        (output / "mcp.json").write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    else:
        skill = output / "skills" / "seedenv"
        skill.mkdir(parents=True)
        shutil.copy2(DATA / "agent-guide.md", skill / "SKILL.md")
        value = {"name": "seedenv", "version": "0.1.0", "description": "Prepare and reuse research tools across disciplines",
                 "skills": ["skills/seedenv"], "environment": {"resources": []},
                 "mcpServers": {"seedenv": {"transport": "stdio", "command": "${RESEARCH_PYTHON}",
                    "args": ["-B", "${PACKAGE_ROOT}/server.py"], "protocol_version": "2025-11-25",
                    "env": {"SEEDENV_HOME": "${WORKSPACE_ROOT}/System/software/seedenv", **environment}}}}
        (output / "plugin.json").write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    return {"host": host, "path": str(output), "installed": False,
            "next": "Import this package in the host, then activate SeedEnv"}
