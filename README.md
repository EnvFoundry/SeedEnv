# SeedEnv

[中文](README.zh-CN.md)

Prepare research tools once, then use them across sessions.

SeedEnv lets a researcher choose modules for their work, install missing software,
connect existing installations, and give an agent the commands and guidance to use
them. It serves Origo's initial setup and later environment management through
the same interfaces. Specialized environments such as Optics-Photonics-AI-Lab and
IOP keep their own scientific methods, software integrations and research assets.

## Start

Python 3.11 or later is required. From this checkout:

```sh
python -m pip install .
seedenv search optics
seedenv plan optics molecules writing
seedenv prepare optics molecules
seedenv example optics --output thin_film.py
seedenv run python-optics -- thin_film.py
```

Software is kept in `~/.seedenv`. Set `SEEDENV_HOME` or use
`seedenv --home PATH ...` to choose another persistent location. Research scripts,
data and results belong in the research workspace. Installing a module does not
change the agent's access to that workspace or other directories.

The example is a starting point. `seedenv entry python-optics` returns the actual
interpreter, so researchers and agents can use the complete upstream API.

## Modules

The initial catalogue contains **27 modules**. A module combines components,
practical guidance and, where useful, a small working program. Components are
shared by reference; new fields of research do not require another runtime.

| Work | Module IDs | Software or integration |
| --- | --- | --- |
| Numerical work and data | `science`, `tables`, `optimization` | NumPy, SciPy, SymPy, pandas, Polars, DuckDB, CVXPY |
| Statistics and finance research | `time-series`, `backtesting` | statsmodels, Backtesting.py |
| Machine learning and graphs | `machine-learning`, `networks` | scikit-learn, NetworkX |
| Chemistry and materials | `molecules`, `materials` | RDKit, ASE, pymatgen |
| Biology and imaging | `sequences`, `medical-imaging`, `images` | Biopython, NiBabel, pydicom, scikit-image |
| Geospatial and astronomy | `geospatial`, `astronomy` | GeoPandas, Rasterio, xarray, Astropy |
| Engineering | `finite-elements`, `cad`, `circuits` | scikit-fem, CadQuery, existing ngspice |
| Optics and experiments | `optics`, `quantum`, `instruments` | tmm, miepython, QuTiP, PyVISA |
| Writing and other languages | `writing`, `r-statistics`, `julia-science` | Existing LaTeX, R and Julia; Origo TeX preparation |
| Research data access | `references`, `databases` | httpx, Crossref, SQLAlchemy, psycopg, host database connections |
| Specialized research environments | `optical-lab`, `experimental-lab` | Existing Optics-Photonics-AI-Lab and IOP plugins |

Python components install into separate environments. Native tools are connected
from an explicit executable or PATH; standalone SeedEnv does not install system
packages. Plugin activation and account connections are completed in the host.
The plan and preparation result distinguish these steps from installed software.
Connecting an executable records its location; it does not promise that every
optional backend, font, driver or device is already configured.

## Reuse and continue

```sh
seedenv discover science --python /path/to/existing/python
seedenv bind python-science -- /path/to/existing/python
seedenv installed
seedenv prepare optics --background
seedenv status JOB_ID
seedenv cancel JOB_ID
```

Repeat preparation to reuse completed components. A changed dependency recipe
is prepared in a new directory; existing directories remain available to running
programs. A failed addition does not replace an existing installation. The host
must keep the worker machine running for a background preparation to continue.

For an offline wheel directory, use `prepare ... --offline --find-links PATH`.
Select modules on the machine where calculations will run. A remote product can
invoke the same API on its worker through its existing remote transport.

## Use in a product or agent

```sh
seedenv mcp
seedenv connect origo --output ./seedenv-origo
seedenv connect mcp --output ./seedenv-mcp
seedenv plan optics writing --host origo
```

The Origo export is a self-contained plugin with an MCP server and a compact
Skill. Import and activate it through the product's plugin manager. The generic
MCP export also includes the server code and names the current Python installation.
Guides are loaded on demand through MCP resources or `seedenv guide MODULE`.

`clients/typescript` provides a Node client and an embeddable `<seedenv-picker>`
for onboarding and settings. `clients/rust` is a small native-host client. Both
call the Python implementation; SQLite stores installed locations and preparation
progress. Existing scientific software supplies its own C/C++ kernels and other
native libraries. SeedEnv adds no separate solver or execution engine.

See [product integration](docs/integration.md) and [adding modules](docs/modules.md).
The adapters and picker are delivered here; activating the plugin and wiring the
picker into an Origo release are separate product integration steps.

## Development

```sh
python -m pip install -e .
python -m unittest discover -s tests -v
cd clients/typescript
npm ci
npm run build
npm test
```

With SeedEnv installed in the Python named by `SEEDENV_TEST_PYTHON`, run
`cargo test --manifest-path clients/rust/Cargo.toml` from the repository root.
The Python tests use local wheels and real child processes; no research packages
or network access are needed. `scripts/run_examples.py --home PATH` runs the
bundled programs against already prepared software. Linux research runs are
described in [the implementation note](docs/implementation.md); Windows and macOS
scientific-package support must follow each upstream package's platform support.

MIT license for SeedEnv. Upstream software keeps its own licenses.
