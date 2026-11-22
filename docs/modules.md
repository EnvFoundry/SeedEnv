# Fields, directions and research modules

A module points to shared components and a short guide. Add an example when it
helps someone begin real work. Prefer upstream software and documentation to new
wrappers. A guide should explain what inputs mean, how to choose an appropriate
method, and how to continue with the complete software interface.

Additional catalogues are local JSON files loaded with `--catalog PATH`. Their
guide and example paths are relative to that file. Component and module IDs must
be distinct from the bundled catalogue. Components can be selected directly or
through modules.

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
    "includes": [],
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

Use `kind: "environment"` with `imports`, `instructions` and `sources` for a
solver interpreter that needs an upstream environment. SeedEnv can discover and
bind it. An optional `conda` list, such as `["python=3.12", "phonopy"]`, also lets
an existing micromamba, mamba or conda prepare it from conda-forge. Without that
manager it remains a connection step. The registered command includes activation
for native libraries. Do not substitute a similarly named PyPI package for a
native solver. Large data, model weights and accelerator choices remain separate.

Place the module in a field and direction:

```json
{
  "fields": [{
    "id": "my-field",
    "title": "My field · 研究领域",
    "directions": [{
      "id": "my-direction",
      "title": "My direction · 研究方向",
      "modules": ["my-research-task"]
    }]
  }]
}
```

This belongs alongside `components` and `modules` in the same catalogue file.
Additional catalogues may append directions, module references or related
resources to an existing field, retaining its existing IDs and titles. A module may appear in multiple
directions. Navigation never implies preparation; only explicit module selections
are resolved. Unplaced extension modules remain searchable.

Choose module boundaries by research operations and meaningful software choices:
carrier transport and nonlinear pulse propagation need separate selections;
three QuTiP tasks can share one QuTiP component. Do not copy one component per
navigation entry or make a field include every module. Keep `includes` narrowly
scoped to genuinely needed task modules, rather than a whole scientific stack.

Use field `kind: "shared"` for a cross-disciplinary entry such as research writing
or instrument connections; research fields default to `kind: "research"`.
Place datasets and specialist labs in the field's `resources` list, and give
those module records `kind: "resource"`. They stay searchable and selectable,
but are displayed separately from research directions. Their credentials, data
downloads and specialist software remain explicit preparation or connection steps.

For a deliberate split of an earlier Python stack, `reuse_from` may name existing
compatible components. SeedEnv checks the required imports before reusing their
registered interpreter, then registers the smaller component without another
installation. Use this only for known compatible predecessors, like tmm within
the earlier tmm/miepython stack. If both are selected, prepare the larger component
first and connect the smaller one after it succeeds. Unrelated environments stay
separate; this is not a general dependency solver.

Optional `platforms` restrict a component to `linux`, `darwin` or `windows`.
An unsupported host receives `choose-host`, so the product can select WSL, a server
or another supported worker. Omitting this field does not establish upstream
support; maintain it when a package has known restrictions.

Scientific assumptions belong in the guide. Runtime conditions belong in the
component. Specialized research methods and large datasets belong in the relevant
upstream research environment, which a module can reference as a plugin.

`seedenv context MODULE...` returns only the selected guides, examples and actual
software entries. `seedenv connect mcp --modules MODULE... --output PATH` embeds
that selection and its local extensions in an independent package. After changing
the bundled catalogue, regenerate its navigation reference with
`python scripts/render_catalogue.py` from an editable installation.
