"""One command surface for people, native hosts and scripts."""
import argparse
import json
import os
from pathlib import Path
import signal
import shutil
import subprocess
import sys

from .catalog import Catalog
from .hosts import export_plugin, origo_requests
from .manager import Manager
from .process import Cancelled
from .writing import templates, create_manuscript


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(prog="seedenv", description="Prepare and reuse research tools")
    location = parser.add_mutually_exclusive_group()
    location.add_argument("--home", help="Persistent software and state directory")
    location.add_argument("--research-space", help="User research space; uses System/env/seedenv and retains existing older locations")
    parser.add_argument("--catalog", help="Additional local module catalogue")
    sub = parser.add_subparsers(dest="action", required=True)
    search = sub.add_parser("search", help="Find research modules")
    search.add_argument("query", nargs="?", default="")
    search.add_argument("--limit", type=int, default=20)
    search.add_argument("--offset", type=int, default=0)
    search.add_argument("--field")
    search.add_argument("--direction")
    browse = sub.add_parser("browse", help="Browse fields and research directions without selecting software")
    browse.add_argument("--field")
    for action in ("show", "guide", "entry"):
        p = sub.add_parser(action)
        p.add_argument("name")
    plan = sub.add_parser("plan")
    plan.add_argument("selections", nargs="*")
    plan.add_argument("--target", choices=["linux", "darwin", "windows"])
    plan.add_argument("--host", choices=["origo"])
    context = sub.add_parser("context", help="Read selected working guides and actual software entries")
    context.add_argument("selections", nargs="*")
    for action in ("prepare", "discover"):
        p = sub.add_parser(action)
        p.add_argument("selections", nargs="*")
        p.add_argument("--python")
        if action == "prepare":
            p.add_argument("--background", action="store_true")
            p.add_argument("--offline", action="store_true")
            p.add_argument("--find-links", action="append", default=[])
    bind = sub.add_parser("bind")
    bind.add_argument("component")
    bind.add_argument("command", nargs=argparse.REMAINDER)
    run = sub.add_parser("run")
    run.add_argument("component")
    run.add_argument("arguments", nargs=argparse.REMAINDER)
    example = sub.add_parser("example")
    example.add_argument("module")
    example.add_argument("--output", help="Copy the program here; omit to read its source")
    for action in ("status", "cancel"):
        p = sub.add_parser(action)
        p.add_argument("job")
    sub.add_parser("installed")
    sub.add_parser("mcp")
    worker = sub.add_parser("prepare-request", help="Run a host preparation request synchronously; JSON from stdin or a file")
    worker.add_argument("--file")
    worker.add_argument("--cancel-file", help="Host-owned file whose creation stops this preparation")
    layouts = sub.add_parser("templates", help="List writing templates without installing software")
    layouts.add_argument("--language", choices=["en", "zh"])
    layouts.add_argument("--form", choices=["article", "report", "book", "supplementary"])
    layouts.add_argument("--style", choices=["standard", "compact", "submission"])
    manuscript = sub.add_parser("manuscript", help="Copy one editable manuscript into a new project directory")
    manuscript.add_argument("template")
    manuscript.add_argument("--output", required=True)
    build = sub.add_parser("build", help="Compile an existing manuscript with the selected TeX")
    build.add_argument("source")
    build.add_argument("--output")
    build.add_argument("--build-dir")
    build.add_argument("--engine", choices=["lualatex", "xelatex"], default="lualatex")
    build.add_argument("--latexmk", help="Explicit existing latexmk; otherwise use the registered toolchain or PATH")
    connect = sub.add_parser("connect")
    connect.add_argument("host", choices=["origo", "mcp"])
    connect.add_argument("--output", required=True)
    connect.add_argument("--modules", nargs="*", help="Export only these modules and their dependencies")
    connect.add_argument("--group", choices=["scientific-basics", "scientific-writing"], help="Export a public group's metadata and resources; does not install its software")
    args = parser.parse_args(argv)
    try:
        manager = Manager(args.home, Catalog(args.catalog), args.research_space)
        action = args.action
        if action == "search":
            value = manager.catalog.search(args.query, args.limit, args.offset, args.field, args.direction)
        elif action == "browse":
            value = manager.catalog.browse(args.field)
        elif action == "show":
            value = manager.catalog.show(args.name)
        elif action == "guide":
            value = manager.catalog.guide(args.name)
        elif action == "plan":
            value = origo_requests(manager, args.selections) if args.host else manager.plan(args.selections, args.target)
        elif action == "context":
            value = manager.context(args.selections)
        elif action == "discover":
            value = manager.discover(args.selections, args.python)
        elif action == "prepare":
            options = dict(python=args.python, offline=args.offline, find_links=args.find_links)
            value = manager.start(args.selections, **options) if args.background else manager.prepare(args.selections, **options)
        elif action == "prepare-request":
            def interrupted(signum, frame):
                raise Cancelled("Preparation cancelled by host")
            signal.signal(signal.SIGTERM, interrupted)
            request = json.loads(Path(args.file).read_text(encoding="utf-8") if args.file else sys.stdin.read())
            value = manager.prepare_request(request, cancel=Path(args.cancel_file) if args.cancel_file else None)
        elif action == "templates":
            value = templates(args.language, args.form, args.style)
        elif action == "manuscript":
            value = create_manuscript(args.template, args.output)
        elif action == "build":
            value = manager.build(args.source, output=args.output, build_dir=args.build_dir,
                                  engine=args.engine, latexmk=args.latexmk)
        elif action == "bind":
            command = args.command[1:] if args.command[:1] == ["--"] else args.command
            value = manager.bind(args.component, command)
        elif action == "entry":
            value = manager.entry(args.name)
        elif action == "installed":
            value = manager.state.list()
        elif action in {"status", "cancel"}:
            value = getattr(manager, action)(args.job)
        elif action == "run":
            arguments = args.arguments[1:] if args.arguments[:1] == ["--"] else args.arguments
            if not arguments:
                raise ValueError("Provide a research script or executable arguments after --")
            entry = manager.entry(args.component)
            return subprocess.call([*entry["command"], *arguments], env={**os.environ, **entry.get("environment", {})})
        elif action == "example" and not args.output:
            value = manager.catalog.example(args.module)
        elif action == "example":
            item = manager.catalog.modules[args.module]
            example = item.get("example")
            if not example:
                raise ValueError("This module links to upstream examples in its guide")
            target = Path(args.output).absolute()
            if target.exists():
                raise FileExistsError(f"Output already exists: {target}")
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(manager.catalog.resource(args.module, example["file"]), target)
            common = ["seedenv", "--home", str(manager.home)]
            if manager.catalog.extra:
                common += ["--catalog", manager.catalog.extra]
            value = {"path": str(target), "component": example["component"],
                     "run": [*common, "run", example["component"], "--", *example.get("args", []), str(target)]}
        elif action == "connect":
            names = args.modules
            if args.group:
                group = manager.catalog.fields[args.group]
                names = list(dict.fromkeys([*(names or []), *(n for d in group["directions"] for n in d["modules"])]))
            value = export_plugin(args.output, args.host, str(manager.home) if args.home or args.research_space else None, args.catalog, names)
        else:
            from .mcp import serve
            serve(manager)
            return 0
        print(value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, indent=2))
        partial = action == "prepare-request" or (action == "prepare" and not args.background)
        if partial and (value["failed"] or value["pending"]):
            return 2
        return 2 if action == "build" and value["status"] == "failed" else 0
    except (ValueError, OSError, RuntimeError, KeyError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1
    except (KeyboardInterrupt, Cancelled):
        print("Preparation interrupted; completed components remain available", file=sys.stderr)
        return 130
