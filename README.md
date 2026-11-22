# SeedEnv

[中文](README.zh-CN.md)

**Find a field, choose the modules your research needs, and reuse them across sessions.**

SeedEnv supplies one selection, preparation and connection interface for Origo's
first-run setup and environment management. Modules can include software, runtime
environments, data connections, plugins and practical guidance. Specialist
environments such as Optics-Photonics-AI-Lab and IOP retain their own scientific
methods, knowledge and experimental workflows.

## Choose research tools

Browse **field → research direction → module**. Fields and directions are
navigation, not installation bundles. Nothing is selected by default. Search by
task or software also supports selections across fields.

The catalogue has **14 research fields and 2 shared groups**, with 85 directions
and groupings, **171 distinct task modules**, and 8 related resources. Optics and
photonics has 13 research directions and 51 task modules. Datasets and specialist
labs appear separately as related resources. See the complete
[field, direction and module catalogue](docs/catalogue.md). These are selectable
starting points, not an exhaustive list of research methods.

| Research task | Selectable module | Direct software |
| --- | --- | --- |
| Multilayer reflection and transmission | `thin-films` | tmm, NumPy |
| Molecular electronic structure | `electronic-molecules` | PySCF |
| Molecular dynamics | `molecular-dynamics` | OpenMM |
| Lattice vibrations | `phonons` | Phonopy |
| Single-cell analysis | `single-cell` | Scanpy |
| Medical volume processing | `volume-processing` | SimpleITK |
| Derivatives pricing | `derivatives-pricing` | QuantLib |
| Feedback and dynamics | `control-systems` | python-control |

Modules can appear under several directions without duplicating their software.

## Start

Python 3.11 or later is required. From this checkout:

```sh
python -m pip install .
seedenv browse
seedenv browse --field optics
seedenv search --field optics --direction optoelectronic-devices
seedenv --research-space /path/to/user-space plan thin-films writing
seedenv --research-space /path/to/user-space prepare thin-films
seedenv --research-space /path/to/user-space context thin-films
seedenv --research-space /path/to/user-space example thin-films --output thin_film.py
seedenv --research-space /path/to/user-space run python-tmm -- thin_film.py
```

`--research-space` names the **user-level research space**, shared across projects
and sessions. Software and installation state live in its `system/seedenv`.
Research programs, inputs and outputs stay in their own projects. Do not pass a
temporary session workspace. `SEEDENV_RESEARCH_SPACE` provides the same setting.

Existing `--home` and `SEEDENV_HOME` directly select the environment directory.
Unconfigured standalone commands retain `~/.seedenv`; existing software is not
moved or deleted.

## Storage and reuse

Browsing reads small metadata; guides load only when requested. An empty selection
is valid and creates no software directories or background job. Only selected modules enter a plan,
which shows new software, reusable environments and the destination. Per-platform
download and additional disk estimates are not yet resolved: the API returns null
and the picker explicitly shows that size is unknown.

A shared component is prepared once. A compatible larger environment can also
supply smaller selections, regardless of selection order. Different dependencies may use separate
environments, so component reuse does not imply global deduplication of underlying
libraries. Large data, weights, accelerator backends and drivers are separate
selections or connections.

The old `python-optics` environment can supply the smaller thin-film and sphere
scattering modules. `optics` now names a field; replace the old broad command with
`thin-films` or `sphere-scattering`. The original combined module remains explicitly
accessible as `thin-film-and-scattering`.

```sh
seedenv discover thin-films --python /existing/environment/bin/python
seedenv bind python-tmm -- /existing/environment/bin/python
seedenv installed
seedenv prepare thin-films --background
seedenv status JOB_ID
seedenv cancel JOB_ID
```

Continue using the same location arguments or environment variables. Sessions do
not delete installations. Failed additions preserve existing software. Background
preparation requires its execution machine to remain running.

Python recipes can be prepared automatically. Conda recipes, including Meep and
Phonopy, use an existing micromamba, mamba or conda and a separate environment
under the same user space. Existing solver environments can be bound by their
actual interpreters. Native tools,
drivers, plugins and data connections retain their own setup steps. The interface
is shared across platforms; upstream software determines supported execution
locations. WSL and servers use the product's existing connections.

## Product and agent integration

```sh
seedenv --research-space /path/to/user-space connect origo --output ./seedenv-origo
seedenv connect mcp --modules thin-films molecular-dynamics --output ./seedenv-mcp
seedenv --research-space /path/to/user-space plan thin-films writing --host origo
```

TypeScript supplies the client and field/direction/module picker; Rust supplies
the native client. Python owns composition and preparation; SQLite stores installed
locations and progress. Scientific software supplies its own C/C++ kernels.

Exported packages contain their selected catalogue, guides and examples, including
local additions. After copying an MCP package to another computer, run
`python configure.py --research-space /path/to/user-space` inside it, then import
its `mcp.json`. Software is prepared on the receiving execution host.

Agents browse or search, request `context` for the selected modules, obtain the real interpreter, and
write complete research programs using the upstream API. Examples are editable
starting points. Installation locations do not change agent file access.

These components are implemented here. Wiring the picker and user-space mapping
into a shipped Origo release remains a product integration step. See
[integration](docs/integration.md), [adding modules](docs/modules.md), and
[implemented and exercised behavior](docs/implementation.md).

## Development

```sh
python -m pip install -e .
python -m unittest discover -s tests -v
cd clients/typescript
npm ci
npm run build
npm test
```

With SeedEnv available to `SEEDENV_TEST_PYTHON`, run
`cargo test --manifest-path clients/rust/Cargo.toml` from the repository root.
Core process tests use local wheels and no research downloads.
`scripts/run_examples.py --home PATH` runs examples whose software is prepared.
Append module IDs to run a specific selection. No software is installed by this script.

MIT license for SeedEnv. Upstream software keeps its own licenses.
