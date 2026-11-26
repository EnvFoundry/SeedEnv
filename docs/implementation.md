# Implementation · 2026-11-22

SeedEnv has 14 research fields and 3 shared entry groups, with 99 directions and
groupings, 202 distinct task modules, 188 shared components and 8 related resources. The
[catalogue](catalogue.md) is generated from the same data used by the CLI, MCP,
TypeScript picker and Rust client. Several directions may reference one module;
several modules may use one software component.

The picker starts with no selection. Browsing and empty preparation create no
software directory or background job. Selected software is prepared beneath the
user research space's `System/software/seedenv`, with isolated environments, local caches
and persistent SQLite state. Existing interpreters and executables can be bound.
Known compatible larger environments supply smaller modules; selection order
does not cause duplicate installation. Preparation supports background progress,
cancellation and reuse across processes. Reopening the picker can resume tracking
an existing job, including after a temporary status error.

Python recipes use pip. Native Python environments with conda recipes use an
existing micromamba, mamba or conda, including activation when obtaining their
invocation command. Other native programs, plugins, external data and account
connections retain their actual setup steps. Platform restrictions direct a
selection to a supported execution host rather than attempting an unsupported
installation. Download and additional disk sizes remain unknown until dependency
resolution; the API and picker do not report these as zero.

`context` returns only selected working guides, examples and actual invocation
entries. MCP can read example source directly through `seedenv_example`.
Modules use the complete upstream APIs. Exported agent packages can
contain only chosen modules and local catalogue extensions. A copied generic MCP
package includes `configure.py` to regenerate paths on its receiving machine.
Exporting the package does not claim its scientific software has been installed.

Scientific Basics now groups 17 tasks under four directions. Scientific Writing
groups six tasks under five directions, including software-free methods and
templates. The 22 English/Chinese layout choices share 17 distinct source files;
only the chosen template is copied into a new manuscript project. TeX preparation,
templates, composition guidance and the manuscript builder are maintained here
for standalone use and product consumption.

The current integration was exercised on Linux: a fresh scientific Python venv
ran the fitting example; native TinyTeX compiled all 17 distinct templates. LuaLaTeX
with BibTeX and Biber, and XeLaTeX with BibTeX, also produced Chinese/English PDFs.
Repeated offline preparation returned the same Python and TeX commands. The new
writing workflow exercises native TinyTeX and these templates on Linux and Windows.

The synchronous `prepare-request` interface accepts the selected modules and
existing command entries from the product worker, and returns actual invocation
commands and locations. The host owns its job, execution host and environment
registry. TypeScript and Rust call this same interface. Cancellation uses a host
file on every platform; unfinished pip destinations and TeX downloads are retained
for retry. Existing managed entries keep their location and management state when
the host passes them back.

Earlier development prepared and ran the following examples on Linux x86-64 /
Python 3.12. Inputs are illustrative, not empirical research results.

| Software | Executed calculation | Result |
| --- | --- | --- |
| PySCF | H₂, RHF/STO-3G, bond 0.74 Å | Energy −1.1167593074 hartree |
| OpenMM | One-particle harmonic oscillator, 1,000 steps | Total energy 0.5000000364 kJ/mol from 0.5 kJ/mol |
| Cantera | CH₄/air constant-enthalpy equilibrium | 2225.5246 K; relative enthalpy change 1.8 × 10⁻¹⁰ |
| Phonopy | Silicon finite-displacement supercell | 16 atoms; displacement 0.01 Å; force calculation remains the next research operation |
| Scanpy | Synthetic 40 × 30 count matrix | Normalization, logarithm, 5 PCA coordinates and neighbor graph |
| SimpleITK | Synthetic labelled volume | Physical point (11.5, −1, 13); identity resampling retains label |
| lifelines | Censored synthetic observations | Kaplan–Meier S(3) = 0.375 |
| QuantLib | Synthetic European call and put | Put–call parity error 1.8 × 10⁻¹⁵ |
| python-control | Unit step for 1/(s+1) | Maximum error against analytic response 5.8 × 10⁻¹⁵ |
| OR-Tools | Small discrete allocation | Optimal objective 7 |

The physical-experiment extension adds 27 tasks, including acquisition, motion,
robotics, timing, microscopy, liquid handling and field instruments. Eighteen
selected Python components were prepared or reused on this Linux worker;
software imports succeeded. Native apparatus such as ARTIQ, ROS 2 and labscript
retain their upstream connection routes. No physical apparatus was operated.

The following additional examples ran using their actual upstream libraries:

| Software | Executed program | Result |
| --- | --- | --- |
| PyVISA-sim | Query the upstream simulated serial instrument | `LSG Serial #1234` |
| python-can | Exchange a frame over a virtual bus | ID 291, bytes `[9, 196]`; decoded under the example's declared units |
| pytransform3d | Compose sample/tool/base transforms | Sample origin `(0.11, 0.22, 0.33)` m; inverse returns the original point |
| MuJoCo | Headless damped pendulum, 2 seconds | Finite trajectory; total energy decreases |
| NumPy / SciPy | Synthetic linear calibration and inverse prediction | 2.517647 K with standard uncertainty 0.031769 K |
| Bluesky / Ophyd / SciPy | Adaptive sampling of a virtual detector | Peak found at 0.699991 versus the supplied model's 0.7 |
| PyLabRobot | Chatterbox transfer with volume tracking | Source 200 → 150 µL, destination 0 → 50 µL; no physical transfer |

These are software simulations and synthetic calculations. Hardware compatibility,
timing accuracy and physical measurement performance require the user's actual
device and apparatus configuration. The host connection remains explicit after
software preparation; repeated preparation does not reinstall its Python components.

Earlier work exercised the base scientific stack and optics programs, including
thin films, RCWA, paraxial imaging, polarization, coherence, speckle statistics,
quantum evolution and a DEVSIM capacitor. The catalogue's other installation
routes have not all been exercised on every platform. Native GPU workloads,
instruments and external accounts were not connected in this round.

Twenty-nine Python process tests pass, covering real local-wheel installation,
reuse across processes, cancellation, failed additions, empty selection, shared
environments, selected context, local extensions, relocated MCP packages and
prepared software with a still-pending laboratory connection. They also exercise
the host's existing-environment handoff, interrupted preparation retry and templates
without software installation. The two TypeScript client/picker tests and the
Rust client test also pass locally. Repository CI runs the Python process tests on Linux, Windows and macOS; this tests SeedEnv's core,
not every upstream scientific package on those operating systems.

The Origo export and earlier preset adapter remain available. The shared
`prepare-request` route prepares pip, TeX and supported conda recipes on the selected
worker. Origo still needs to wire its picker, persistent location, task progress
and environment registration to this interface, then retire its duplicate recipes
and writing assets. That product change has not been made in this repository.
Other agent hosts can use the CLI, Python API or exported MCP package directly.
