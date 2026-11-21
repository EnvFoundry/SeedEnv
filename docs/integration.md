# Product integration

The same catalogue and installation service support first-run setup and settings.
The product owns its execution hosts, research spaces, permissions, account
connections and job UI. SeedEnv owns module composition and software preparation.

## Direct Python preparation

```python
from seedenv import Manager

environments = Manager('/persistent/software/seedenv')
plan = environments.plan(['optics', 'molecules'])
job = environments.start(['optics', 'molecules'])
progress = environments.status(job['job'])
```

Call `prepare` synchronously when the product already schedules work. `start`
uses a detached worker for standalone clients and MCP. A terminated machine or
container does not keep that worker alive. Repeating a preparation reuses completed
components; it does not resume an individual interrupted package download.

The host's process environment supplies package indexes and certificates. Account
tokens for research services stay in host connection settings, outside catalogues.
For remote computers, run this code through the product's existing remote worker.

## Origo's existing environment API

`seedenv plan optics writing --host origo` returns `preparations` and `connections`.
Each preparation has the shape accepted by Origo's existing `prepareEnvironment`:
`execution_id`, `id`, `version`, `destination`, and either `requirements` or
`preset: "research-tex"`. The host keeps its current preparation, cancellation and
environment-registration flow. Translate workspace-relative destinations using
the active workspace, as in Origo's existing environment UI.

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
const environments = new SeedEnv({ command: ['/path/to/python'], home: '/persistent/software/seedenv' });
```

```ts
import '@envfoundry/seedenv/picker'; // browser frontend
const picker = document.createElement('seedenv-picker');
picker.lang = 'zh';
picker.api = hostEnvironmentBridge;
container.append(picker);
```

Implement `ResearchEnvironmentAPI` over the product's IPC or HTTP boundary:
`search`, `plan`, `prepare`, `status`, `cancel`. The direct Node client implements
that interface; in a browser its calls travel through the host bridge. Keep the
chosen execution host fixed during a preparation. The component does not create
a second desktop service or request filesystem permissions.

The picker emits `seedenv-started`, `seedenv-finished`, and `seedenv-skip`.
Store the started job ID in product state. Removing the picker does not cancel
the installation; use `status` in the product's job view to continue tracking it.
Chinese and English labels use the `lang` attribute.

## Agent package

`seedenv connect origo --output PATH` creates `plugin.json`, a self-contained
Python server, and `skills/seedenv/SKILL.md`. Move or archive the directory, import
it in Origo, and activate it. The package keeps software beneath the workspace's
`System/software/seedenv` by default; the product can choose a shared persistent
location through `SEEDENV_HOME`.

MCP provides module discovery, plans, preparation, progress, existing-software
binding and invocation entries. Module guides are resources; `start-research`
is a prompt that loads the selected guide. Research execution uses the host's
normal interpreter or terminal interface, including the full upstream API.

The exported plugin and adapters run independently. This repository does not
change Origo's shipped installer, automatically activate plugins, or create
external accounts.
