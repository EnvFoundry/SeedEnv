# Implementation status · 2026-11-21

Implemented: field → direction → module navigation with 16 fields and 88 visible
modules; optics has 14 directions and 54 distinct modules. The picker starts with
no selection, supports cross-field selection and removal, and shows software
before preparation. CLI, MCP and both native clients use the same catalogue.

Preparation includes isolated Python environments;
existing-interpreter and native-command binding; persistent SQLite state;
background preparation, progress and cancellation; CLI; stdio MCP; host plugin
exports; an Origo preparation adapter; TypeScript and Rust clients; an embeddable
module picker with Chinese and English controls and module summaries.

The Python package has no runtime dependencies. Scientific software is downloaded
only for selected components. Guides are short, task-specific resources loaded
when needed. Services and specialized plugins remain visible as separate
connection steps, with their upstream documentation.

In the earlier base catalogue, all 21 Python components were installed and imported
on Linux x86-64 / Python 3.12.
The 19 local Python examples ran with those interpreters. These include a
thin-film calculation with R + T = 1 within numerical precision, a finite-element
Poisson solution with zero boundary values, a silicon structure conversion,
RDKit descriptors, synthetic financial backtesting, NIfTI spatial metadata, a CAD
solid, quantum evolution and SQL aggregation. Example inputs are demonstrations.
An additional HTTP example retrieved actual DOI metadata from Crossref, bringing
the executed Python examples to 20. No instrument or external database was
connected during this work.

For the finer module selections, a fresh user space prepared only tmm and NumPy
beneath `system/seedenv/environments`, ran the thin-film calculation, and reused
the same environment in a subsequent process. An earlier combined optics
environment supplied both split modules without another installation. Shared
NumPy/SciPy and QuTiP selections likewise resolve to one component each.

New runs include a paraxial imaging matrix (B = 0, magnification −1), Malus' law
(transmission 0.5), a grcwa dielectric slab (R + T = 1), mutual-coherence
propagation (total intensity 1.6), independent-speckle contrasts near 1, 0.5 and
0.25, a phase-matching factor, and a class-B rate-equation solution approaching
inversion 1 and photon population 0.5. The latter two use explicitly illustrative
parameters, not calibrated material or laser-device models.

DEVSIM needed its native math library, so the x86-64 Linux/Windows recipe includes
MKL and NumPy. Its upstream two-region capacitor program then ran successfully.
The standalone thin-film environment occupied about 79 MiB and the DEVSIM/MKL
environment about 1068 MiB on this Linux machine, excluding download caches and
research data. These are observed installations, not cross-platform size estimates.
The plan keeps unknown download/disk sizes empty. New pip caches stay under the
selected `system/seedenv/cache` rather than another persistent user directory.

Seventeen process-level Python tests passed, including preparation from local
wheels, reuse from a second process, cancellation, failed additions, composition,
MCP messages, multilingual pipes, relocated plugin exports, field navigation,
cross-field composition, split-environment reuse and user-space placement.
The TypeScript client and picker tests
and the Rust client test also passed. These local runs do not establish Windows
or macOS research-package compatibility; the repository includes a three-platform
workflow for the core preparation tests.

The available system TeX executable was found, but its XeLaTeX formats were
missing, so a Chinese document did not compile on this machine. The module
supports an existing working TeX installation or Origo's existing TeX preparation
flow. Native installers, accounts, drivers and instrument connections remain
host or upstream setup steps.

The exported Origo plugin and API adapter are implemented here. This work has
not changed an Origo release or connected the picker to its shipped installer.
The product must map the adapter's explicit `installation_root` to the user space;
destinations no longer derive from an active project. The additional catalogue
recipes have not all been installed on every platform. Solver bindings, large
datasets and hardware backends retain their separate setup states.
