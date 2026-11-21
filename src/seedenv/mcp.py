"""Dependency-free MCP stdio surface; preparations run outside the connection."""
import json
import sys

from .manager import Manager


def field(kind, description=""):
    return {"type": kind, "description": description}


SELECTION = {"type": "array", "items": {"type": "string"}, "minItems": 1}


def tools():
    definitions = [
        ("seedenv_search", "Find research modules by task, discipline or software; supports Chinese and English.",
         {"query": field("string"), "limit": field("integer"), "offset": field("integer")}, [], True),
        ("seedenv_show", "Read a module and its complete software requirements, or one component.",
         {"name": field("string")}, ["name"], True),
        ("seedenv_guide", "Read practical working instructions for one selected research module.",
         {"name": field("string")}, ["name"], True),
        ("seedenv_plan", "Combine modules, reuse known installations, and describe remaining preparation.",
         {"selections": SELECTION, "target": {"type": "string", "enum": ["linux", "darwin", "windows"]}}, ["selections"], True),
        ("seedenv_discover", "Look for selected software in an explicit Python interpreter or on PATH.",
         {"selections": SELECTION, "python": field("string")}, ["selections"], True),
        ("seedenv_bind", "Register an existing interpreter or executable for a component.",
         {"name": field("string"), "command": SELECTION}, ["name", "command"], False),
        ("seedenv_prepare", "Start preparing selected research modules; returns a job immediately. Uses network unless offline.",
         {"selections": SELECTION, "python": field("string"), "offline": field("boolean"), "find_links": {"type": "array", "items": {"type": "string"}}}, ["selections"], False),
        ("seedenv_status", "Read preparation progress and a bounded tail of installer output.",
         {"job": field("string")}, ["job"], True),
        ("seedenv_cancel", "Stop an unfinished preparation, retaining already prepared components.",
         {"job": field("string")}, ["job"], False),
        ("seedenv_installed", "List persistent software installations and their invocation commands.", {}, [], True),
        ("seedenv_entry", "Get the exact command for a prepared component; use it to run full native research programs.",
         {"component": field("string")}, ["component"], True),
    ]
    return [{"name": name, "description": description,
             "inputSchema": {"type": "object", "properties": properties, "required": required, "additionalProperties": False},
             "annotations": {"readOnlyHint": read, "destructiveHint": False, "openWorldHint": not read}}
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
        "seedenv_search": manager.catalog.search, "seedenv_show": manager.catalog.show,
        "seedenv_guide": manager.catalog.guide, "seedenv_plan": manager.plan,
        "seedenv_discover": lambda selections, **kw: manager.discover(selections, **kw),
        "seedenv_bind": manager.bind, "seedenv_prepare": manager.start,
        "seedenv_status": manager.status, "seedenv_cancel": manager.cancel,
        "seedenv_installed": manager.state.list, "seedenv_entry": manager.entry,
    }
    return operations[name](**args)


def dispatch(manager, request):
    method, params = request.get("method"), request.get("params", {})
    if method == "initialize":
        supported = {"2024-11-05", "2025-03-26", "2025-06-18", "2025-11-25"}
        protocol = params.get("protocolVersion")
        return {"protocolVersion": protocol if protocol in supported else "2025-11-25",
                "capabilities": {"tools": {}, "resources": {}, "prompts": {}},
                "serverInfo": {"name": "seedenv", "version": "0.1.0"}}
    if method == "ping":
        return {}
    if method == "tools/list":
        return {"tools": tools()}
    if method == "tools/call":
        try:
            result = call(manager, params["name"], params.get("arguments", {}))
            return {"content": [{"type": "text", "text": result if isinstance(result, str) else json.dumps(result, ensure_ascii=False)}]}
        except (ValueError, OSError, RuntimeError, TypeError, KeyError) as error:
            return {"content": [{"type": "text", "text": str(error)}], "isError": True}
    if method == "resources/list":
        return {"resources": [{"uri": "seedenv://guides/" + name, "name": item["title"], "mimeType": "text/markdown"}
                              for name, item in manager.catalog.modules.items()]}
    if method == "resources/read":
        uri = params["uri"]
        if not uri.startswith("seedenv://guides/"):
            raise ValueError("Unknown resource")
        return {"contents": [{"uri": uri, "mimeType": "text/markdown", "text": manager.catalog.guide(uri.removeprefix("seedenv://guides/"))}]}
    if method == "prompts/list":
        return {"prompts": [{"name": "start-research", "description": "Start working with an installed research module",
                             "arguments": [{"name": "module", "description": "Module ID", "required": True}]}]}
    if method == "prompts/get" and params.get("name") == "start-research":
        guide = manager.catalog.guide(params.get("arguments", {})["module"])
        return {"messages": [{"role": "user", "content": {"type": "text", "text": guide}}]}
    raise ValueError(f"Unknown method: {method}")


def serve(manager=None):
    manager = manager or Manager()
    for line in sys.stdin:
        request = None
        try:
            request = json.loads(line)
            if not isinstance(request, dict) or request.get("jsonrpc") != "2.0" or not isinstance(request.get("method"), str):
                raise ValueError("Expected a JSON-RPC request")
            if "id" not in request:
                continue
            response = {"jsonrpc": "2.0", "id": request["id"], "result": dispatch(manager, request)}
        except Exception as error:
            response = {"jsonrpc": "2.0", "id": request.get("id") if isinstance(request, dict) else None,
                        "error": {"code": -32600, "message": str(error)}}
        sys.stdout.write(json.dumps(response, ensure_ascii=False) + "\n")
        sys.stdout.flush()
