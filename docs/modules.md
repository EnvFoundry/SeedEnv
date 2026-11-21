# Adding a research module

A module points to shared components and a short guide. Add an example when it
helps someone begin real work. Prefer upstream software and documentation to new
wrappers. A guide should explain what inputs mean, how to choose an appropriate
method, and how to continue with the complete software interface.

Additional catalogues are local JSON files loaded with `--catalog PATH`. Their
guide and example paths are relative to that file. Names must be distinct from
the bundled catalogue. Components can be selected directly or through modules.

```json
{
  "components": [{
    "id": "python-my-tool",
    "title": "My research tool",
    "kind": "python",
    "requirements": ["upstream-package"],
    "imports": ["upstream_module"],
    "sources": ["https://upstream.example/documentation"]
  }],
  "modules": [{
    "id": "my-research-task",
    "title": "A specific research task",
    "summary": "The inputs and calculation this module supports.",
    "tags": ["task", "discipline"],
    "includes": ["science"],
    "components": ["python-my-tool"],
    "guide": "guides/my-task.md",
    "example": {"component": "python-my-tool", "file": "examples/my-task.py"}
  }]
}
```

Use `kind: "command"` with `commands` for an existing executable, `kind: "plugin"`
with an upstream `url` for a host plugin, or `kind: "connector"` with a `connection`
description for an external service. Connector descriptions identify the protocol,
endpoint and required field names. Put actual credentials in the host's connection
settings. MCP service connections can use the same connector form; the host owns
their transport and authentication.

Optional `platforms` restrict a component to `linux`, `darwin` or `windows`.
An unsupported host receives `choose-host`, so the product can select WSL, a server
or another supported worker. Omitting this field does not establish upstream
support; maintain it when a package has known restrictions.

Scientific assumptions belong in the guide. Runtime conditions belong in the
component. Specialized research methods and large datasets belong in the relevant
upstream research environment, which a module can reference as a plugin.
