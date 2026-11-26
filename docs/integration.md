# Product integration

The same catalogue and installation service support first-run setup and settings.
The product owns its execution hosts, research spaces, permissions, account
connections and job UI. SeedEnv owns module composition and software preparation.

## Host-owned preparation

For the product integration, run SeedEnv on the **selected execution host** inside
the product's existing job. Use its user-level persistent directory, not a session
directory. `prepare-request` is synchronous and starts no detached worker:

```sh
python -m seedenv --home /user/Research/System/env/seedenv prepare-request --file request.json
```

The same JSON may be supplied on stdin:

```json
{
  "selections": ["scientific-python", "writing"],
  "existing": [
    {"command": ["/existing/science/bin/python"]},
    {"components": ["tool-tex"], "command": ["/existing/tex/bin/latexmk"]}
  ],
  "options": {"offline": false}
}
```

Supply only entries from that execution host's registry. Omit unavailable entries
or provide an empty array. An unlabelled command is considered a Python interpreter;
native programs must name their components. `options` accepts `python` (base
interpreter for new venvs), `offline`, and `find_links`. Existing interpreters are
matched against the requested imports; this does not solve arbitrary project
dependency constraints. A project with different requirements retains its own
environment. `Manager.reuse(selections, existing)` can bind the supplied entries
before displaying a preparation plan; it returns reused and unmatched components.

The result contains `modules`, `ready`, `pending` and `failed`. Each ready entry
has `component`, an argument-array `command`, `location`, and `managed`. TeX entries
also contain `commands` (named executables) and, for managed TeX, `environment`
(PATH and writable TeX caches). Preserve these values when the native registry
creates its execution binding. A Python entry is its actual interpreter; do not
replace it with the product service's Python. An external entry is connected in
place and has `managed: false`.

Read progress from stderr and the final result from stdout. Exit 0 means all selected
components are ready; 2 returns a partial result with the outstanding items; 130
means interruption. The TypeScript `prepareOnHost` and Rust `prepare_on_host`
methods retain partial results. Python hosts can call `Manager.prepare_request`
directly. The host may supply `--cancel-file PATH` and create that file to cancel;
on POSIX it may also send SIGTERM to the request process. Retry the same request
after interruption. Completed components and unfinished pip/TeX preparation stay
available. This does not resume a lost scientific calculation or a conda transaction.

The product owns job identity, host identity, permissions and research execution.
SeedEnv's SQL state is a local component-to-command lookup for standalone reuse;
it does not schedule a second product job or replace the host's environment registry.
Use the same home for product calls and its SeedEnv MCP connection.

The recipe, TeX package selection, writing methods, templates and builder now live
in SeedEnv. When wiring this route, Origo should consume those resources and retire
its corresponding duplicate recipes/assets. Its own service Python stays product
owned. This repository implements the shared side; it does not modify Origo's
installer, native environment registration, or existing running installations.

## Writing resources without installation

`seedenv templates --language zh --form article` lists layouts. `seedenv manuscript
standard-article-zh --output PROJECT` creates only an editable project. It never
prepares software or replaces an existing directory. The Python functions are
`seedenv.writing.templates` and `create_manuscript`. The TypeScript/Rust clients
and MCP expose the same operations. `seedenv build PROJECT/main.tex` uses prepared
TeX or an explicit `--latexmk`; it does not install packages. `build` returns status,
PDF path and compiler output paths, with exit 2 on a compilation failure.

Use `seedenv connect mcp --group scientific-writing --output PACKAGE` to export
all writing metadata and resources. `--group scientific-basics` supplies the
computing group. This exports small resources, not preinstalled scientific software.
Selected exports include templates only when `writing-templates` is selected.

## Direct Python preparation

```python
from seedenv import Manager

environments = Manager(research_space='/path/to/user-space')
directions = environments.catalog.browse('optics')
modules = environments.catalog.search(field='optics', direction='films-scattering')
plan = environments.plan(['thin-films', 'molecules'])
job = environments.start(['thin-films', 'molecules'])
if job['job'] is not None:
    progress = environments.status(job['job'])
```

Call `prepare` synchronously when the product already schedules work. `start`
uses a detached worker for standalone clients and MCP. A terminated machine or
container does not keep that worker alive. Repeating a preparation reuses completed
components. pip reuses its unfinished destination and cache; TeX retains its partial
archive and extracted installation. Download resumption also depends on the server.
`plan([])`, `prepare([])` and `start([])` are valid: nothing is installed and
`start` returns `state: "ready", job: null`. Browsing does not create user files.

The host's process environment supplies package indexes and certificates. Account
tokens for research services stay in host connection settings, outside catalogues.
For remote computers, run this code through the product's existing remote worker.

Pass the user-level space, shared by sessions, to `research_space` (or
`SEEDENV_RESEARCH_SPACE`). Software and SQL state live in `System/env/seedenv` beneath
it. An explicit `home` / `SEEDENV_HOME` still selects the environment directory
directly. This does not move earlier installations. The product selects a space
on each execution host; passing a desktop path to a server does not mount it.
An existing legacy `system/seedenv` remains in use if the canonical location does
not exist. When both exist, the canonical location wins; select `--home` explicitly
to continue another existing installation. There is no background migration.

`browse` only navigates. `search` supports `field` and `direction` filters and
returns each module's software and navigation paths. Only module/component IDs
are accepted by `plan` and `prepare`. A field cannot act as an install-everything
shortcut. Several paths may reference the same module or component.

`browse` distinguishes `research` fields from `shared` entry groups, includes
unique task counts, and returns related `resources` separately. `context` accepts
module IDs and returns only their guides, examples, actual software commands and
outstanding setup. A `share` plan action names the selected larger component that
will supply a smaller one; this action does not start another installation.

Python recipes use isolated environments. Conda recipes use a conda-family manager
already available on that worker, with packages and caches under the same user
space. SeedEnv does not install a second package manager. Native commands, account
connections and host plugins keep their explicit setup routes.

Physical tasks include a shared `connector-laboratory` description. Its
`connection.type` is `laboratory`; the host supplies an execution host and named
devices, each with its driver, address and configuration. `PlanAction.modules`
lists the selected tasks using a component, so one connection step can present
the relevant microscope, motion and acquisition requirements together. The
description does not merge those physical devices into one device instance.

SeedEnv returns prepared software in `ready` and the host connection in `pending`.
The host resolves that step against its existing device manager or IOP and owns
live device status. SeedEnv's `context.ready` therefore remains false when an
external connection is outstanding; it is not a live device-status query. Repeating
preparation reuses the software even while the connection is pending. Preparing
software never opens serial ports, starts scans, homes stages or flashes boards.

Launch native tools from the worker environment where their upstream setup has
been activated. In particular, registering a `ros2` executable does not reproduce
the ROS workspace's environment in a fresh unrelated process. Hardware drivers
can impose narrower OS/architecture requirements than their Python clients.

## Compatibility with Origo's existing environment API

The older adapter below remains for existing callers. Prefer `prepare-request`
for the shared implementation above, including independent TeX preparation.

`seedenv --research-space PATH plan thin-films writing --host origo` returns
`installation_root`, `preparations` and `connections`.
Each preparation has the shape accepted by Origo's existing `prepareEnvironment`:
`execution_id`, `id`, `version`, `destination`, and either `requirements` or
`preset: "research-tex"`. The host keeps its current preparation, cancellation and
environment-registration flow. Each request's `destination` is relative to
`installation_root`, not to the active project. The product must map that root to
the chosen user's persistent space before submitting its native preparation
request. This mapping is a required product integration change; the adapter does
not change Origo's filesystem or execution service by itself.

After the host prepares a Python environment, bind its actual Python command to
the corresponding SeedEnv component. This avoids a second installation on the
next selection. Use the same `SEEDENV_HOME` for product calls and the MCP process.
The native registry remains responsible for launching research in that environment.

`connections` retain existing software, shared components, conda environments,
plugins and data services. Conda actions must run through SeedEnv's `prepare` on
the chosen worker; Origo's existing pip/preset request is not a conda installer.
After host preparation, bind the actual interpreters before preparing dependent
shared modules. Route plugins and data services to the product's connection UI.

## Module picker

Build `clients/typescript`, then import the browser component separately from the
Node client. No Node imports are included in the picker bundle.

```ts
import { SeedEnv } from '@envfoundry/seedenv'; // product backend
const environments = new SeedEnv({ command: ['/path/to/python'], researchSpace: '/path/to/user-space' });
```

```ts
import '@envfoundry/seedenv/picker'; // browser frontend
const picker = document.createElement('seedenv-picker');
picker.lang = 'zh';
picker.api = hostEnvironmentBridge;
container.append(picker);
```

Implement `ResearchEnvironmentAPI` over the product's IPC or HTTP boundary:
`browse`, `search`, `plan`, `prepare`, `status`, `cancel`. The direct Node client implements
that interface; in a browser its calls travel through the host bridge. Keep the
chosen execution host fixed during a preparation. The component does not create
a second desktop service or request filesystem permissions.

The picker starts with field navigation and no selected modules. Shared capabilities
have their own field group, and related resources have a distinct label. Direction
filters and search do not clear the selection basket. Researchers can remove a
selected module even when it is outside the current filter. Before preparation,
the picker displays the unique component actions, shared installation count and
destination. Unknown download/disk estimates are null, not zero. The catalogue's
small metadata and guides do not trigger solver, model or dataset downloads.

The picker emits `seedenv-started`, `seedenv-finished`, and `seedenv-skip`.
Store the started job ID in product state. Removing the picker does not cancel
the installation; call `picker.resume(jobId)` when reopening the page, or use
`status` in the product's job view. A temporary status error keeps the job ID and
offers a refresh action, without starting another installation.
Chinese and English labels use the `lang` attribute.

## Agent package

`seedenv connect origo --output PATH` creates `plugin.json`, a self-contained
Python server, and `skills/seedenv/SKILL.md`. Move or archive the directory, import
it in Origo, and activate it. Export with `--research-space PATH` to configure
`PATH/System/env/seedenv`, or have the host supply `SEEDENV_RESEARCH_SPACE` at launch.
Without either setting, standalone behavior remains `~/.seedenv`. The package no
longer derives software storage from a project or session workspace placeholder.

`seedenv connect mcp --modules thin-films molecular-dynamics --output PATH`
exports only those modules and their software metadata, guides and examples,
including local catalogue additions. It contains `mcp.json`, `configure.py`, the
Python server and a skill. After moving it, run
`python configure.py --research-space /path/to/user-space` on the receiving machine
to regenerate its interpreter and server paths, then import `mcp.json` in the
agent host. This does not copy installed solvers or prepare software yet.

MCP provides module discovery, plans, preparation, progress, existing-software
binding and invocation entries. Module guides are resources; `seedenv_context`
and the `start-research` prompt load the selected guides and real software state.
`seedenv_example` reads a selected starting program directly; the same source is
available through `seedenv://examples/MODULE`. An MCP-only host does not need a
separate CLI installation to obtain it.
Research execution uses the host's
normal interpreter or terminal interface, including the full upstream API.

The exported plugin and adapters run independently. This repository does not
change Origo's shipped installer, automatically activate plugins, or create
external accounts.

## Environment descriptions and files

The Origo package exports `environment.presentation`, keyed by language tag,
and `environment.resources` from `data/environment.json`. Each resource has a
`kind`, a fallback `title`, optional translated `titles`, and a `package_path`
relative to the exported package. Only resources included in the selected export
are listed. The host resolves them to installed locations when it displays them.

These declarations describe packaged content. They do not establish that Python
packages, TeX, external services or instruments have been prepared; use the
existing preparation result and environment registrations for that state.

## Declarative environment preparation

The exported environment names its MCP server and exact installed, plan and prepare
operations. Catalogue resources include repository paths for browsing before any
installation. `seedenv_preparation_installed` returns selected and ready modules
separately from ready, pending and failed components; the older `seedenv_installed`
array remains unchanged. Pure guidance and templates need no software installation.

MCP Tasks wrap the existing preparation jobs: call `seedenv_prepare` with `task: {}`
and read `tasks/get` and `tasks/result`. `tasks/cancel` waits for the existing worker
to stop. Completed components survive cancellation and reconnects; an unexpectedly
terminated worker is reported rather than left running forever. The host-owned
`prepare-request` process and its cancellation contract remain available.
