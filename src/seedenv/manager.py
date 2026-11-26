"""Select components, reuse software and prepare isolated installations."""
from __future__ import annotations

from contextlib import ExitStack
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import uuid
from datetime import datetime, timezone

from .catalog import Catalog
from .process import Cancelled, installation_lock, run
from .state import State
from . import tex


def research_home(space):
    space = Path(space).expanduser()
    current = space / "System/software/seedenv"
    return next((path for path in (current, space / "System/env/seedenv", space / "system/seedenv")
                 if path.exists()), current)


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
        default = research_home(space) if space else Path.home() / ".seedenv"
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
            if item.get("preparer") == "tex":
                try:
                    tex.describe(saved["command"])
                except (OSError, ValueError, subprocess.TimeoutExpired):
                    return None
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
            row = {"component": name, "title": item["title"], "kind": item["kind"],
                   "modules": [m for m in modules if name in self.catalog.modules[m].get("components", [])]}
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
                command = tex.find_existing() if local and item.get("preparer") == "tex" else None
                found = next((shutil.which(x) for x in item["commands"] if shutil.which(x)), None) if local and not item.get("preparer") else None
                command = command or ([str(Path(found).absolute())] if found else None)
                managed = item.get("preparer") == "tex"
                row.update(action="connect" if command else "install" if managed else "setup", command=command,
                           instructions=item.get("instructions", ""), sources=item.get("sources", []))
                if managed:
                    row["preparer"] = "tex"
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
                if item.get("preparer") == "tex":
                    command = tex.find_existing()
                else:
                    found = next((shutil.which(x) for x in item["commands"] if shutil.which(x)), None)
                    command = [str(Path(found).absolute())] if found else None
                if command:
                    result.append({"component": name, "command": command, "action": "bind"})
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
        if item.get("preparer") == "tex":
            tex.describe(command)
        with installation_lock(self.home / "locks" / (name + ".lock")):
            existing = self.state.get(name)
            if existing and existing["command"] == command:
                return self.state.bind(name, item, command, existing["location"], existing["managed"])
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
            pending = self.home / "preparing" / (name + ".json")
            request = {"component": name, "definition": item, "python": base}
            saved_request = json.loads(pending.read_text(encoding="utf-8")) if pending.is_file() else None
            if saved_request and saved_request["request"] == request:
                prefix = Path(saved_request["location"])
                if prefix.parent != directory or not prefix.name.startswith(name + "-"):
                    raise ValueError("Unfinished environment is outside this component's installation directory")
            else:
                prefix = Path(tempfile.mkdtemp(prefix=name + "-", dir=directory))
                if item["kind"] == "python":
                    pending.parent.mkdir(parents=True, exist_ok=True)
                    pending.write_text(json.dumps({"request": request, "location": str(prefix)}) + "\n", encoding="utf-8")
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
                    interpreter = prefix / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
                    if not interpreter.is_file() or not python_works([str(interpreter)], ["pip"]):
                        run([base, "-I", "-m", "venv", str(prefix)], env=env, cancel=cancel)
                    options = ["--no-index"] if offline else []
                    for location in find_links:
                        options.extend(["--find-links", str(location)])
                    run([str(interpreter), "-I", "-m", "pip", "install", "--no-input", *options, *item["requirements"]], env=env, cancel=cancel)
                    launch = [str(interpreter)]
                if not python_works(launch, item["imports"]):
                    raise RuntimeError(f"Installed packages for {name} could not be imported")
                if cancel and cancel.exists():
                    raise Cancelled("Preparation cancelled")
                result = self.state.bind(name, item, launch, prefix, True)
                pending.unlink(missing_ok=True)
                return result
            except BaseException:
                # pip can continue this private destination on the next request.
                # An unfinished environment is never returned as ready.
                if item["kind"] != "python":
                    shutil.rmtree(prefix, ignore_errors=True)
                raise

    def prepare(self, selections, *, python=None, offline=False, find_links=(), cancel=None):
        plan = self.plan(selections)
        if plan["actions"]:
            self.state.select(selections)
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
                elif action["action"] == "install" and item.get("preparer") == "tex":
                    command, location = tex.prepare(self.home, offline=offline, cancel=cancel)
                    saved = self.state.bind(name, item, command, location, True)
                elif action["action"] == "reuse":
                    saved = self._available(item)
                elif action["action"] == "connect":
                    saved = self.bind(name, action["command"])
                else:
                    result["pending"].append(action)
                    continue
                result["ready"].append({**self.entry(name), "managed": saved["managed"]})
            except (OSError, RuntimeError, ValueError, TimeoutError) as error:
                result["failed"].append({"component": name, "error": str(error)})
        return result

    def installed_summary(self):
        entries = self.state.list()
        ready = [entry for entry in entries if entry["command"] and Path(entry["command"][0]).is_file()]
        available = {entry["component"] for entry in ready}
        selected = [name for name in self.state.selected()
                    if name in self.catalog.modules or name in self.catalog.components]
        modules, _ = self.catalog.select(selected)
        required = {name: set(self.catalog.select([name])[1]) for name in modules}
        return {"modules": modules, "ready_modules": [name for name in modules if required[name] <= available],
                "ready": ready,
                "pending": [{"component": name, "status": "not_prepared"}
                            for name in sorted(set().union(*required.values()) - available)],
                "failed": [{"component": entry["component"], "error": "The registered executable is unavailable"}
                           for entry in entries if entry["component"] not in available]}

    def remove(self, selections):
        requested_modules, requested_components = self.catalog.select(selections)
        if not self.state.path.is_file():
            return {"removed": [], "files": [], "retained": []}
        with ExitStack() as locks:
            for name in sorted(requested_components):
                locks.enter_context(installation_lock(self.home / "locks" / (name + ".lock")))
            locks.enter_context(installation_lock(self.home / "locks/registry.lock", wait=True))
            recorded = self.state.selected()
            known_recorded = [name for name in recorded
                              if name in self.catalog.modules or name in self.catalog.components]
            recorded_modules, _ = self.catalog.select(known_recorded)
            remaining = [name for name in recorded if name not in selections]
            known_remaining = [name for name in remaining
                               if name in self.catalog.modules or name in self.catalog.components]
            remaining_modules, remaining_components = self.catalog.select(known_remaining)
            required = set(selections) & (set(remaining_modules) | set(remaining_components))
            if required:
                raise ValueError("Still required by installed modules: " + ", ".join(sorted(required)))
            candidates = set(requested_components) - set(remaining_components)
            with self.state.db(write=True) as db:
                rows = [self.state.installation(row) for row in db.execute("SELECT * FROM installations")]
                kept = [Path(row["location"]).resolve() for row in rows if row["component"] not in candidates]
                files, retained = set(), set()
                for row in rows:
                    if row["component"] not in candidates:
                        continue
                    location = Path(row["location"])
                    resolved = location.resolve()
                    shared = any(resolved == other or resolved.is_relative_to(other) or other.is_relative_to(resolved)
                                 for other in kept)
                    owned = row["managed"] and any(resolved.parent == (self.home / area).resolve()
                                                   for area in ("environments", "software"))
                    if owned and not shared and not location.is_symlink():
                        if location.is_dir():
                            shutil.rmtree(location)
                            files.add(str(location))
                    elif location.exists():
                        retained.add(str(location))
                    db.execute("DELETE FROM installations WHERE component=?", (row["component"],))
                    db.commit()
                for name in sorted(candidates):
                    pending = self.home / "preparing" / (name + ".json")
                    if not pending.is_file():
                        continue
                    location = Path(json.loads(pending.read_text(encoding="utf-8"))["location"])
                    if location.resolve().parent != (self.home / "environments").resolve() or location.is_symlink():
                        raise ValueError(f"Unfinished installation for {name} is outside its managed directory")
                    if location.is_dir() and not any(location.resolve() == other for other in kept):
                        shutil.rmtree(location)
                        files.add(str(location))
                    pending.unlink()
                db.executemany("DELETE FROM selections WHERE module=?", ((name,) for name in selections))
        return {"removed": sorted(set(requested_modules) & set(recorded_modules) - set(remaining_modules)),
                "files": sorted(files), "retained": sorted(retained)}

    def entry(self, component):
        saved = self._available(self._component(component))
        if saved is None or not Path(saved["command"][0]).is_file():
            raise ValueError(f"Prepare or bind {component} first")
        value = {"component": component, "command": saved["command"], "location": saved["location"]}
        if self._component(component).get("preparer") == "tex":
            value["commands"] = tex.describe(saved["command"])
            if saved["managed"]:
                value["environment"] = tex.environment(self.home, saved["command"])
        return value

    def reuse(self, selections, environments):
        """Bind only requested components to entries supplied by this host.

        Each entry supplies command and optional components. The host selects
        the execution machine before calling; no remote paths are guessed here.
        """
        _, ids = self.catalog.select(selections)
        found, remaining = [], list(ids)
        for entry in environments:
            command = entry.get("command")
            if not isinstance(command, list) or not command or any(not isinstance(x, str) or not x for x in command):
                raise ValueError("Each existing environment needs a command array")
            candidates = entry.get("components", remaining)
            if not isinstance(candidates, list) or any(not isinstance(x, str) for x in candidates):
                raise ValueError("Existing environment components must be an array of component IDs")
            for name in list(remaining):
                item = self._component(name)
                if name not in candidates or item["kind"] in {"plugin", "connector"}:
                    continue
                # Unlabelled entries are Python interpreters. Native commands
                # must name their components, so a solver cannot become latexmk.
                if item["kind"] == "command" and "components" not in entry:
                    continue
                try:
                    self.bind(name, command)
                except (ValueError, OSError, subprocess.TimeoutExpired):
                    continue
                found.append(self.entry(name))
                remaining.remove(name)
        return {"reused": found, "unmatched": remaining}

    def prepare_request(self, request, *, cancel=None):
        """Synchronous worker entry: the caller owns scheduling and cancellation."""
        if not isinstance(request, dict) or set(request) - {"selections", "existing", "options"}:
            raise ValueError("Use selections, existing and options in a preparation request")
        selections = request.get("selections", [])
        if not isinstance(selections, list) or any(not isinstance(x, str) for x in selections):
            raise ValueError("selections must be an array of module or component IDs")
        existing = request.get("existing", [])
        if not isinstance(existing, list) or any(not isinstance(x, dict) for x in existing):
            raise ValueError("existing must be an array of host environment entries")
        options = request.get("options", {})
        if not isinstance(options, dict) or set(options) - {"python", "offline", "find_links"}:
            raise ValueError("Preparation options are python, offline and find_links")
        if "offline" in options and not isinstance(options["offline"], bool):
            raise ValueError("offline must be true or false")
        if "python" in options and options["python"] is not None and not isinstance(options["python"], str):
            raise ValueError("python must be an executable path")
        links = options.get("find_links", [])
        if not isinstance(links, list) or any(not isinstance(p, str) for p in links):
            raise ValueError("find_links must be an array of paths or URLs")
        if cancel and cancel.exists():
            raise Cancelled("Preparation cancelled")
        self.reuse(selections, existing)
        return self.prepare(selections, cancel=cancel, **options)

    def build(self, source, *, output=None, build_dir=None, engine="lualatex", latexmk=None):
        from .writing import build_manuscript
        environment = None
        if latexmk is None and "tool-tex" in self.catalog.components:
            saved = self._available(self._component("tool-tex"))
            if saved:
                entry = self.entry("tool-tex")
                latexmk = entry["command"][0]
                environment = entry.get("environment")
        return build_manuscript(Path(source), output=Path(output) if output else None,
                                build_dir=Path(build_dir) if build_dir else None,
                                engine=engine, latexmk=latexmk or "latexmk", environment=environment)

    def start(self, selections, **options):
        modules, components = self.catalog.select(selections)
        if not components:
            return {"job": None, "state": "ready", "result": {"modules": modules, "ready": [], "pending": [], "failed": []}}
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
                child = subprocess.Popen([sys.executable, "-m", "seedenv.worker", str(self.home), job],
                                         stdin=subprocess.DEVNULL, stdout=log, stderr=log, env=env, **kwargs)
            threading.Thread(target=child.wait, daemon=True).start()
        except OSError as error:
            self.state.set_job(job, "failed", error=str(error))
            raise
        return {"job": job, "state": "queued"}

    def status(self, job):
        value = self.state.job(job)
        if value["state"] in {"queued", "running"}:
            folder = self.home / "jobs" / job
            age = time.time() - datetime.fromisoformat(value["created_at"]).replace(tzinfo=timezone.utc).timestamp()
            try:
                with installation_lock(folder / "worker.lock"):
                    if (folder / "started").exists() or age > 30:
                        current = self.state.job(job)
                        if current["state"] in {"queued", "running"}:
                            self.state.set_job(job, "failed", error="Preparation worker stopped; completed components are retained")
            except RuntimeError:
                pass
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
