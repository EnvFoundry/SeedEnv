"""One command surface for people, native hosts and scripts."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys

from .catalog import Catalog
from .hosts import export_plugin, origo_requests
from .manager import Manager


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(prog="seedenv", description="Prepare and reuse research tools")
    location = parser.add_mutually_exclusive_group()
    location.add_argument("--home", help="Persistent software and state directory")
    location.add_argument("--research-space", help="User research space; software lives in its system/seedenv directory")
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
    plan.add_argument("selections", nargs="+")
    plan.add_argument("--target", choices=["linux", "darwin", "windows"])
    plan.add_argument("--host", choices=["origo"])
    for action in ("prepare", "discover"):
        p = sub.add_parser(action)
        p.add_argument("selections", nargs="+")
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
    example.add_argument("--output", required=True)
    for action in ("status", "cancel"):
        p = sub.add_parser(action)
        p.add_argument("job")
    sub.add_parser("installed")
    sub.add_parser("mcp")
    connect = sub.add_parser("connect")
    connect.add_argument("host", choices=["origo", "mcp"])
    connect.add_argument("--output", required=True)
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
        elif action == "discover":
            value = manager.discover(args.selections, args.python)
        elif action == "prepare":
            options = dict(python=args.python, offline=args.offline, find_links=args.find_links)
            value = manager.start(args.selections, **options) if args.background else manager.prepare(args.selections, **options)
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
            return subprocess.call([*manager.entry(args.component)["command"], *arguments])
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
            value = export_plugin(args.output, args.host, str(manager.home) if args.home or args.research_space else None, args.catalog)
        else:
            from .mcp import serve
            serve(manager)
            return 0
        print(value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, indent=2))
        return 2 if action == "prepare" and not args.background and (value["failed"] or value["pending"]) else 0
    except (ValueError, OSError, RuntimeError, KeyError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("Preparation interrupted; completed components remain available", file=sys.stderr)
        return 130
