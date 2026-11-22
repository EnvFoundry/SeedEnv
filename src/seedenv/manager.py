"""Select components, reuse software and prepare isolated installations."""
from __future__ import annotations

import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import uuid

from .catalog import Catalog
from .process import Cancelled, installation_lock, run
from .state import State


def executable(value):
    found = shutil.which(str(Path(value).expanduser()))
    if not found:
        raise ValueError(f"Executable not found: {value}")
    # Keep venv symlinks: resolving one changes the interpreter's environment.
    return str(Path(found).absolute())


def python_works(command, modules):
    source = "import importlib,json,sys; [importlib.import_module(x) for x in json.loads(sys.argv[1])]"
    try:
        result = subprocess.run([*command, "-I", "-c", source, json.dumps(modules)],
                                stdin=subprocess.DEVNULL, capture_output=True, timeout=30)
        return result.returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        return False


def available_space(path):
    while not path.exists() and path != path.parent:
        path = path.parent
    return shutil.disk_usage(path).free


def conda_command():
    return next((path for name in ("micromamba", "mamba", "conda")
                 if (path := shutil.which(name)) and Path(path).suffix.lower() not in {".bat", ".cmd"}), None)


class Manager:
    def __init__(self, home=None, catalog=None, research_space=None):
        space = research_space or os.environ.get("SEEDENV_RESEARCH_SPACE")
        default = Path(space).expanduser() / "system" / "seedenv" if space else Path.home() / ".seedenv"
        location = home or (default if research_space else os.environ.get("SEEDENV_HOME", default))
        self.home = Path(os.path.abspath(Path(location).expanduser()))
        self.catalog = catalog or Catalog(os.environ.get("SEEDENV_CATALOG"))
        self.state = State(self.home)

    def _component(self, name):
        if name not in self.catalog.components:
            raise ValueError(f"Unknown component: {name}")
        return self.catalog.components[name]

    def _available(self, item):
        saved = self.state.get(item["id"])
        fields = ("kind", "requirements", "imports")
        if saved and Path(saved["command"][0]).is_file() and all(
                saved["definition"].get(key) == item.get(key) for key in fields):
            if item["kind"] not in {"python", "environment"} or python_works(saved["command"], item["imports"]):
                return saved
        # A smaller module may use a previously prepared larger environment.
        # Only explicit compatible predecessors are considered; no machine scan.
        for parent in item.get("reuse_from", []):
            saved = self.state.get(parent)
            if (saved and Path(saved["command"][0]).is_file()
                    and saved["definition"].get("kind") == "python"
                    and python_works(saved["command"], item["imports"])):
                return saved
        return None

    def plan(self, selections, target=None):
        target = target or platform.system().lower()
        if target not in {"linux", "darwin", "windows"}:
            raise ValueError("target must be linux, darwin or windows")
        local = target == platform.system().lower()
        modules, components = self.catalog.select(selections)
        # Put a selected larger environment before smaller tasks that can use it.
        ordered, visiting = [], set()
        def order(name):
            if name in visiting:
                raise ValueError(f"Circular software reuse at {name}")
            if name in ordered:
                return
            visiting.add(name)
            for parent in self._component(name).get("reuse_from", []):
                if parent in components:
                    order(parent)
            visiting.remove(name)
            ordered.append(name)
        for name in components:
            order(name)
        actions = []
        for name in ordered:
            item = self._component(name)
            saved = self._available(item) if local else None
            row = {"component": name, "title": item["title"], "kind": item["kind"]}
            if item.get("instructions"):
                row["instructions"] = item["instructions"]
            if item.get("sources"):
                row["sources"] = item["sources"]
            if item.get("platforms") and target not in item["platforms"]:
                row.update(action="choose-host", platforms=item["platforms"], instructions=item.get("instructions", "Choose a supported execution host"))
            elif saved:
                row.update(action="reuse", command=saved["command"], location=saved["location"], provided_by=saved["component"])
            elif item["kind"] == "python":
                shared = next((a for a in actions if a["component"] in item.get("reuse_from", [])
                               and a["action"] in {"install", "share"}), None)
                if shared:
                    row.update(action="share", provided_by=shared["component"])
                else:
                    row.update(action="install", requirements=item["requirements"], python=item.get("python", "3.11+"))
            elif item["kind"] == "command":
                found = next((shutil.which(x) for x in item["commands"] if shutil.which(x)), None) if local else None
                row.update(action="connect" if found else "setup", command=[str(Path(found).absolute())] if found else None,
                           instructions=item.get("instructions", ""), sources=item.get("sources", []))
            elif item["kind"] == "environment":
                installer = conda_command() if local and item.get("conda") else None
                row.update(action="install" if installer else "setup", imports=item["imports"], instructions=item["instructions"], sources=item.get("sources", []))
                if item.get("conda"):
                    row.update(packages=item["conda"], installer=installer, channel="conda-forge")
            elif item["kind"] == "connector":
                row.update(action="configure-connector", connection=item["connection"],
                           instructions=item.get("instructions", ""), sources=item.get("sources", []))
            else:
                row.update(action="add-plugin", url=item["url"], instructions=item.get("instructions", ""))
            actions.append(row)
        no_download = all(a["action"] in {"reuse", "connect"} for a in actions)
        return {"modules": modules, "target": target, "actions": actions,
                "storage": {"root": str(self.home), "new_environments": sum(a["action"] == "install" for a in actions),
                            "reused_environments": len({tuple(a["command"]) for a in actions if a["action"] == "reuse"}),
                            "download_bytes": 0 if no_download else None,
                            "additional_disk_bytes": 0 if no_download else None,
                            "free_bytes": available_space(self.home) if local else None},
                "guides": [{"module": name, "title": self.catalog.modules[name]["title"]} for name in modules]}

    def context(self, selections):
        """Return only the chosen working guides and the actual execution entries."""
        plan = self.plan(selections)
        modules = []
        for name in plan["modules"]:
            item = self.catalog.modules[name]
            example = {**item["example"], "uri": "seedenv://examples/" + name} if item.get("example") else None
            modules.append({"id": name, "title": item["title"], "guide": self.catalog.guide(name),
                            "example": example, "paths": self.catalog.paths[name]})
        return {"modules": modules, "software": plan["actions"], "storage": plan["storage"],
                "ready": all(a["action"] in {"reuse", "connect"} for a in plan["actions"])}

    def discover(self, names, python=None):
        """Inspect an explicit interpreter or PATH. Does not import every installed package."""
        _, ids = self.catalog.select(names)
        candidate = [executable(python or sys.executable)]
        result = []
        for name in ids:
            item = self._component(name)
            if item["kind"] in {"python", "environment"} and python_works(candidate, item["imports"]):
                result.append({"component": name, "command": candidate, "action": "bind"})
            elif item["kind"] == "command":
                found = next((shutil.which(x) for x in item["commands"] if shutil.which(x)), None)
                if found:
                    result.append({"component": name, "command": [str(Path(found).absolute())], "action": "bind"})
        return {"found": result}

    def bind(self, name, command):
        item = self._component(name)
        if item["kind"] in {"plugin", "connector"}:
            raise ValueError("Connect and activate this integration in the host's integration manager")
        if not command or any(not isinstance(x, str) or not x for x in command):
            raise ValueError("command must be an executable and its arguments")
        command = [executable(command[0]), *command[1:]]
        if item["kind"] in {"python", "environment"} and not python_works(command, item["imports"]):
            raise ValueError(f"This interpreter cannot import the packages required by {name}")
        with installation_lock(self.home / "locks" / (name + ".lock")):
            return self.state.bind(name, item, command, Path(command[0]).parent, False)

    def _prepare_managed(self, item, *, python=None, offline=False, find_links=(), cancel=None):
        name = item["id"]
        with installation_lock(self.home / "locks" / (name + ".lock")):
            existing = self._available(item)
            if existing and python_works(existing["command"], item["imports"]):
                if existing["component"] != name:
                    return self.state.bind(name, item, existing["command"], existing["location"], existing["managed"])
                return existing
            base = executable(python or sys.executable)
            directory = self.home / "environments"
            directory.mkdir(parents=True, exist_ok=True)
            prefix = Path(tempfile.mkdtemp(prefix=name + "-", dir=directory))
            # Explicit pip options own the target. Environment variables may supply
            # an index or certificate but cannot redirect installation elsewhere.
            env = dict(os.environ)
            for key in ("PIP_TARGET", "PIP_PREFIX", "PIP_USER", "PYTHONHOME", "PYTHONPATH", "VIRTUAL_ENV"):
                env.pop(key, None)
            env["PIP_CONFIG_FILE"] = os.devnull
            env["PIP_DISABLE_PIP_VERSION_CHECK"] = "1"
            env["PIP_CACHE_DIR"] = str(self.home / "cache" / "pip")
            env["PYTHONNOUSERSITE"] = "1"
            try:
                if item["kind"] == "environment":
                    installer = conda_command()
                    if not installer or not item.get("conda"):
                        raise ValueError("Connect an existing solver interpreter or make micromamba, mamba or conda available")
                    env["CONDA_PKGS_DIRS"] = str(self.home / "cache" / "conda")
                    env["MAMBA_ROOT_PREFIX"] = str(self.home / "cache" / "mamba")
                    run([installer, "create", "--yes", "--prefix", str(prefix), "--override-channels", "--channel", "conda-forge",
                         *(["--offline"] if offline else []), *item["conda"]], env=env, cancel=cancel)
                    interpreter = prefix / ("python.exe" if os.name == "nt" else "bin/python")
                    # Native libraries may need activation, especially on Windows.
                    launch = [installer, "run", "--prefix", str(prefix)]
                    if Path(installer).stem.lower() == "conda":
                        launch.append("--no-capture-output")
                    else:
                        launch += ["--root-prefix", str(self.home / "cache" / "mamba")]
                    launch.append(str(interpreter))
                else:
                    run([base, "-I", "-m", "venv", str(prefix)], env=env, cancel=cancel)
                    interpreter = prefix / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
                    options = ["--no-index"] if offline else []
                    for location in find_links:
                        options.extend(["--find-links", str(location)])
                    run([str(interpreter), "-I", "-m", "pip", "install", "--no-input", *options, *item["requirements"]], env=env, cancel=cancel)
                    launch = [str(interpreter)]
                if not python_works(launch, item["imports"]):
                    raise RuntimeError(f"Installed packages for {name} could not be imported")
                if cancel and cancel.exists():
                    raise Cancelled("Preparation cancelled")
                return self.state.bind(name, item, launch, prefix, True)
            except BaseException:
                # This directory was created by this call and never published.
                shutil.rmtree(prefix, ignore_errors=True)
                raise

    def prepare(self, selections, *, python=None, offline=False, find_links=(), cancel=None):
        plan = self.plan(selections)
        result = {"modules": plan["modules"], "ready": [], "pending": [], "failed": []}
        for action in plan["actions"]:
            if cancel and cancel.exists():
                raise Cancelled("Preparation cancelled")
            name = action["component"]
            item = self._component(name)
            try:
                if action["action"] in {"reuse", "install", "share"} and item["kind"] in {"python", "environment"}:
                    if action["action"] == "share" and not self._available(item):
                        raise RuntimeError(f"Selected shared software {action['provided_by']} is not ready")
                    saved = self._prepare_managed(item, python=python, offline=offline, find_links=find_links, cancel=cancel)
                elif action["action"] == "reuse":
                    saved = self._available(item)
                elif action["action"] == "connect":
                    saved = self.bind(name, action["command"])
                else:
                    result["pending"].append(action)
                    continue
                result["ready"].append({k: saved[k] for k in ("component", "command", "location", "managed")})
            except (OSError, RuntimeError, ValueError, TimeoutError) as error:
                result["failed"].append({"component": name, "error": str(error)})
        return result

    def entry(self, component):
        saved = self._available(self._component(component))
        if saved is None or not Path(saved["command"][0]).is_file():
            raise ValueError(f"Prepare or bind {component} first")
        return {"component": component, "command": saved["command"], "location": saved["location"]}

    def start(self, selections, **options):
        self.catalog.select(selections)
        if not selections:
            return {"job": None, "state": "ready", "result": {"modules": [], "ready": [], "pending": [], "failed": []}}
        job = uuid.uuid4().hex
        folder = self.home / "jobs" / job
        folder.mkdir(parents=True)
        request = {"selections": selections, "options": options, "catalog": self.catalog.extra}
        (folder / "request.json").write_text(json.dumps(request), encoding="utf-8")
        self.state.add_job(job, selections)
        try:
            with (folder / "output.log").open("wb") as log:
                env = dict(os.environ)
                env["PYTHONPATH"] = str(Path(__file__).parent.parent)
                kwargs = {"creationflags": subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS} if os.name == "nt" else {"start_new_session": True}
                subprocess.Popen([sys.executable, "-m", "seedenv.worker", str(self.home), job],
                                 stdin=subprocess.DEVNULL, stdout=log, stderr=log, env=env, **kwargs)
        except OSError as error:
            self.state.set_job(job, "failed", error=str(error))
            raise
        return {"job": job, "state": "queued"}

    def status(self, job):
        value = self.state.job(job)
        log = self.home / "jobs" / job / "output.log"
        if log.is_file():
            with log.open("rb") as stream:
                stream.seek(max(0, log.stat().st_size - 6000))
                value["output"] = stream.read(6000).decode("utf-8", errors="replace")
        return value

    def cancel(self, job):
        value = self.state.job(job)
        if value["state"] in {"queued", "running"}:
            (self.home / "jobs" / job / "cancel").touch()
            return {"job": job, "state": "cancelling"}
        return {"job": job, "state": value["state"]}
