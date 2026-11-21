# Implementation status · 2026-11-21

Implemented: composition of 27 research modules; isolated Python preparation;
existing-interpreter and native-command binding; persistent SQLite state;
background preparation, progress and cancellation; CLI; stdio MCP; host plugin
exports; an Origo preparation adapter; TypeScript and Rust clients; an embeddable
module picker with Chinese and English controls.

The Python package has no runtime dependencies. Scientific software is downloaded
only for selected components. Guides are short, task-specific resources loaded
when needed. Services and specialized plugins remain visible as separate
connection steps, with their upstream documentation.

On Linux x86-64 / Python 3.12, all 21 Python components were installed and imported.
The 19 local Python examples ran with those interpreters. These include a
thin-film calculation with R + T = 1 within numerical precision, a finite-element
Poisson solution with zero boundary values, a silicon structure conversion,
RDKit descriptors, synthetic financial backtesting, NIfTI spatial metadata, a CAD
solid, quantum evolution and SQL aggregation. Example inputs are demonstrations.
An additional HTTP example retrieved actual DOI metadata from Crossref, bringing
the executed Python examples to 20. No instrument or external database was
connected during this work.

Twelve process-level Python tests passed, including preparation from local
wheels, reuse from a second process, cancellation, failed additions, composition,
MCP messages, multilingual pipes and relocated plugin exports. The TypeScript client and picker tests
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
