"""Dependency-free MCP stdio surface; preparations run outside the connection."""
import json
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from .tasks import Tasks

from .manager import Manager
from .writing import templates, create_manuscript


def field(kind, description=""):
    return {"type": kind, "description": description}


SELECTION = {"type": "array", "items": {"type": "string"}}


class MethodNotFound(ValueError):
    pass


def tools():
    definitions = [
        ("seedenv_browse", "Browse fields, then research directions. Navigation never selects or installs all modules in a field.",
         {"field": field("string")}, [], True),
        ("seedenv_search", "Find research modules by task, discipline or software; supports Chinese and English.",
         {"query": field("string"), "limit": field("integer"), "offset": field("integer"),
          "field": field("string"), "direction": field("string")}, [], True),
        ("seedenv_show", "Read a module and its complete software requirements, or one component.",
         {"name": field("string")}, ["name"], True),
        ("seedenv_guide", "Read practical working instructions for one selected research module.",
         {"name": field("string")}, ["name"], True),
        ("seedenv_example", "Read the editable starting program for a selected module, without writing or running it.",
         {"name": field("string")}, ["name"], True),
        ("seedenv_context", "Get only selected modules' working guides, examples and actual software commands. Does not install anything.",
         {"selections": SELECTION}, ["selections"], True),
        ("seedenv_plan", "Combine modules, reuse known installations, and describe remaining preparation.",
         {"selections": SELECTION, "target": {"type": "string", "enum": ["linux", "darwin", "windows"]}}, ["selections"], True),
        ("seedenv_discover", "Look for selected software in an explicit Python interpreter or on PATH.",
         {"selections": SELECTION, "python": field("string")}, ["selections"], True),
        ("seedenv_bind", "Register an existing interpreter or executable for a component.",
         {"name": field("string"), "command": SELECTION}, ["name", "command"], False),
        ("seedenv_prepare", "Prepare selected modules; returns a job, or ready with no job for an empty selection. Uses network unless offline.",
         {"selections": SELECTION, "python": field("string"), "offline": field("boolean"), "find_links": {"type": "array", "items": {"type": "string"}}}, ["selections"], False),
        ("seedenv_status", "Read preparation progress and a bounded tail of installer output.",
         {"job": field("string")}, ["job"], True),
        ("seedenv_cancel", "Stop an unfinished preparation, retaining already prepared components.",
         {"job": field("string")}, ["job"], False),
        ("seedenv_installed", "List persistent software installations and their invocation commands.", {}, [], True),
        ("seedenv_preparation_installed", "Read selected modules, ready modules and outstanding software preparation.", {}, [], True),
        ("seedenv_remove", "Uninstall selected modules and their unreferenced managed software; retain shared installations and research files.",
         {"selections": SELECTION}, ["selections"], False),
        ("seedenv_entry", "Get the exact command for a prepared component; use it to run full native research programs.",
         {"component": field("string")}, ["component"], True),
        ("seedenv_templates", "List editable scientific writing layouts by language, form or style. Does not install software.",
         {"language": field("string"), "form": field("string"), "style": field("string")}, [], True),
        ("seedenv_manuscript", "Copy a selected writing template into a new project directory. Does not download TeX or replace an existing project.",
         {"template": field("string"), "output": field("string")}, ["template", "output"], False),
        ("seedenv_build", "Compile an existing LaTeX manuscript with prepared TeX or an explicitly supplied latexmk. Never installs software.",
         {"source": field("string"), "output": field("string"), "build_dir": field("string"),
          "engine": {"type":"string", "enum":["lualatex", "xelatex"]}, "latexmk": field("string")}, ["source"], False),
    ]
    return [{"name": name, "description": description,
             **({"execution": {"taskSupport": "optional"}} if name == "seedenv_prepare" else {}),
             "inputSchema": {"type": "object", "properties": properties, "required": required, "additionalProperties": False},
             "annotations": {"readOnlyHint": read, "destructiveHint": name == "seedenv_remove", "openWorldHint": not read}}
            for name, description, properties, required, read in definitions]


def call(manager, name, args):
    spec = next((x for x in tools() if x["name"] == name), None)
    if spec is None:
        raise ValueError(f"Unknown tool: {name}")
    schema = spec["inputSchema"]
    if not isinstance(args, dict) or set(args) - set(schema["properties"]) or set(schema["required"]) - set(args):
        raise ValueError("Tool arguments do not match the declared fields")
    for key, value in args.items():
        typ = schema["properties"][key]["type"]
        expected = {"string": str, "integer": int, "boolean": bool, "array": list}[typ]
        if type(value) is not expected:
            raise ValueError(f"{key} must be {typ}")
        if typ == "array" and any(not isinstance(x, str) or not x for x in value):
            raise ValueError(f"{key} must contain strings")
    operations = {
        "seedenv_browse": manager.catalog.browse,
        "seedenv_search": manager.catalog.search, "seedenv_show": manager.catalog.show,
        "seedenv_guide": manager.catalog.guide, "seedenv_plan": manager.plan,
        "seedenv_example": manager.catalog.example,
        "seedenv_context": manager.context,
        "seedenv_discover": lambda selections, **kw: manager.discover(selections, **kw),
        "seedenv_bind": manager.bind, "seedenv_prepare": manager.start,
        "seedenv_status": manager.status, "seedenv_cancel": manager.cancel,
        "seedenv_installed": manager.state.list, "seedenv_entry": manager.entry,
        "seedenv_preparation_installed": manager.installed_summary,
        "seedenv_remove": manager.remove,
        "seedenv_templates": templates, "seedenv_manuscript": create_manuscript,
        "seedenv_build": manager.build,
    }
    return operations[name](**args)


def dispatch(manager, request):
    method, params = request.get("method"), request.get("params", {})
    if method == "initialize":
        supported = {"2024-11-05", "2025-03-26", "2025-06-18", "2025-11-25"}
        protocol = params.get("protocolVersion")
        return {"protocolVersion": protocol if protocol in supported else "2025-11-25",
                "capabilities": {"tools": {}, "resources": {}, "prompts": {},
                                 "tasks": {"requests": {"tools": {"call": {}}}, "cancel": {}}},
                "serverInfo": {"name": "seedenv", "version": "0.1.0"}}
    if method == "ping":
        return {}
    if method == "tools/list":
        return {"tools": tools()}
    if method in {"tasks/get", "tasks/result", "tasks/cancel"}:
        return getattr(Tasks(manager), method.split("/")[1])(params["taskId"])
    if method == "tools/call":
        if "task" in params and params["name"] != "seedenv_prepare":
            raise MethodNotFound("This tool does not support tasks")
        try:
            result = call(manager, params["name"], params.get("arguments", {}))
            if "task" in params:
                return Tasks(manager).start(result, params.get("arguments", {}).get("selections", []))
            return {"content": [{"type": "text", "text": result if isinstance(result, str) else json.dumps(result, ensure_ascii=False)}],
                    **({"structuredContent": result} if isinstance(result, dict) else {})}
        except (ValueError, OSError, RuntimeError, TypeError, KeyError) as error:
            return {"content": [{"type": "text", "text": str(error)}], "isError": True}
    if method == "resources/list":
        visible = {name: item for name, item in manager.catalog.modules.items() if not item.get("hidden")}
        return {"resources": [{"uri": "seedenv://guides/" + name, "name": item["title"], "mimeType": "text/markdown"}
                              for name, item in visible.items()] +
                             [{"uri": "seedenv://examples/" + name, "name": item["title"] + " example", "mimeType": "text/plain"}
                              for name, item in visible.items() if item.get("example")]}
    if method == "resources/templates/list":
        return {"resourceTemplates": []}
    if method == "resources/read":
        uri = params["uri"]
        if uri.startswith("seedenv://examples/"):
            example = manager.catalog.example(uri.removeprefix("seedenv://examples/"))
            return {"contents": [{"uri": uri, "mimeType": "text/plain", "text": example["content"]}]}
        if not uri.startswith("seedenv://guides/"):
            raise ValueError("Unknown resource")
        return {"contents": [{"uri": uri, "mimeType": "text/markdown", "text": manager.catalog.guide(uri.removeprefix("seedenv://guides/"))}]}
    if method == "prompts/list":
        return {"prompts": [{"name": "start-research", "description": "Start working with an installed research module",
                             "arguments": [{"name": "module", "description": "Module ID", "required": True}]}]}
    if method == "prompts/get":
        if params.get("name") != "start-research":
            raise ValueError("Unknown prompt")
        context = manager.context([params.get("arguments", {})["module"]])
        return {"messages": [{"role": "user", "content": {"type": "text", "text": json.dumps(context, ensure_ascii=False)}}]}
    raise MethodNotFound(f"Unknown method: {method}")


def serve(manager=None):
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    manager = manager or Manager()
    output_lock = threading.Lock()

    def respond(line):
        request = None
        try:
            request = json.loads(line)
            if not isinstance(request, dict) or request.get("jsonrpc") != "2.0" or not isinstance(request.get("method"), str):
                raise ValueError("Expected a JSON-RPC request")
            if "id" not in request:
                return
            response = {"jsonrpc": "2.0", "id": request["id"], "result": dispatch(manager, request)}
        except MethodNotFound as error:
            response = {"jsonrpc": "2.0", "id": request["id"],
                        "error": {"code": -32601, "message": str(error)}}
        except Exception as error:
            response = {"jsonrpc": "2.0", "id": request.get("id") if isinstance(request, dict) else None,
                        "error": {"code": -32600, "message": str(error)}}
        with output_lock:
            sys.stdout.write(json.dumps(response, ensure_ascii=False) + "\n")
            sys.stdout.flush()

    with ThreadPoolExecutor(thread_name_prefix="seedenv-mcp") as calls:
        for line in sys.stdin:
            try:
                method = json.loads(line).get("method")
            except (ValueError, AttributeError):
                method = None
            if method in {"tasks/result", "tasks/cancel"}:
                calls.submit(respond, line)
            else:
                respond(line)
