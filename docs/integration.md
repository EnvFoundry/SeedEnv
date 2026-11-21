# Product integration

The same catalogue and installation service support first-run setup and settings.
The product owns its execution hosts, research spaces, permissions, account
connections and job UI. SeedEnv owns module composition and software preparation.

## Direct Python preparation

```python
from seedenv import Manager

environments = Manager(research_space='/path/to/user-space')
directions = environments.catalog.browse('optics')
modules = environments.catalog.search(field='optics', direction='films-scattering')
plan = environments.plan(['thin-films', 'molecules'])
job = environments.start(['thin-films', 'molecules'])
progress = environments.status(job['job'])
```

Call `prepare` synchronously when the product already schedules work. `start`
uses a detached worker for standalone clients and MCP. A terminated machine or
container does not keep that worker alive. Repeating a preparation reuses completed
components; it does not resume an individual interrupted package download.

The host's process environment supplies package indexes and certificates. Account
tokens for research services stay in host connection settings, outside catalogues.
For remote computers, run this code through the product's existing remote worker.

Pass the user-level space, shared by sessions, to `research_space` (or
`SEEDENV_RESEARCH_SPACE`). Software and SQL state live in `system/seedenv` beneath
it. An explicit `home` / `SEEDENV_HOME` still selects the environment directory
directly. This does not move earlier installations. The product selects a space
on each execution host; passing a desktop path to a server does not mount it.

`browse` only navigates. `search` supports `field` and `direction` filters and
returns each module's software and navigation paths. Only module/component IDs
are accepted by `plan` and `prepare`. A field cannot act as an install-everything
shortcut. Several paths may reference the same module or component.

## Origo's existing environment API

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

`connections` retain existing software, plugins and data services. Send those to
the product's respective connection screens. They are not failed Python installs.

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

The picker starts with field navigation and no selected modules. Direction
filters and search do not clear the selection basket. Researchers can remove a
selected module even when it is outside the current filter. Before preparation,
the picker displays the unique component actions, shared installation count and
destination. Unknown download/disk estimates are null, not zero. The catalogue's
small metadata and guides do not trigger solver, model or dataset downloads.

The picker emits `seedenv-started`, `seedenv-finished`, and `seedenv-skip`.
Store the started job ID in product state. Removing the picker does not cancel
the installation; use `status` in the product's job view to continue tracking it.
Chinese and English labels use the `lang` attribute.

## Agent package

`seedenv connect origo --output PATH` creates `plugin.json`, a self-contained
Python server, and `skills/seedenv/SKILL.md`. Move or archive the directory, import
it in Origo, and activate it. Export with `--research-space PATH` to configure
`PATH/system/seedenv`, or have the host supply `SEEDENV_RESEARCH_SPACE` at launch.
Without either setting, standalone behavior remains `~/.seedenv`. The package no
longer derives software storage from a project or session workspace placeholder.

MCP provides module discovery, plans, preparation, progress, existing-software
binding and invocation entries. Module guides are resources; `start-research`
is a prompt that loads the selected guide. Research execution uses the host's
normal interpreter or terminal interface, including the full upstream API.

The exported plugin and adapters run independently. This repository does not
change Origo's shipped installer, automatically activate plugins, or create
external accounts.
