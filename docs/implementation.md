# Implementation · 2026-11-22

SeedEnv has 14 research fields and 2 shared entry groups, with 85 directions and
groupings, 171 distinct task modules and 8 related resources. The
[catalogue](catalogue.md) is generated from the same data used by the CLI, MCP,
TypeScript picker and Rust client. Several directions may reference one module;
several modules may use one software component.

The picker starts with no selection. Browsing and empty preparation create no
software directory or background job. Selected software is prepared beneath the
user research space's `system/seedenv`, with isolated environments, local caches
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

This round prepared and ran the following new examples on Linux x86-64 / Python
3.12. Inputs are illustrative, not empirical research results.

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

Earlier work exercised the base scientific stack and optics programs, including
thin films, RCWA, paraxial imaging, polarization, coherence, speckle statistics,
quantum evolution and a DEVSIM capacitor. The catalogue's other installation
routes have not all been exercised on every platform. Native GPU workloads,
instruments and external accounts were not connected in this round. The earlier
host TeX installation lacked its XeLaTeX formats; a working TeX installation or
the host's TeX preparation flow is still needed for that writing example.

Twenty-two Python process tests pass, covering real local-wheel installation,
reuse across processes, cancellation, failed additions, empty selection, shared
environments, selected context, local extensions and relocated MCP packages.
The TypeScript client/picker tests and Rust client tests pass. Repository CI runs
the Python process tests on Linux, Windows and macOS; this tests SeedEnv's core,
not every upstream scientific package on those operating systems.

The Origo package and preparation adapter are implemented. The native Origo
adapter translates pip and TeX requests; conda preparation runs through SeedEnv on
the selected worker. Wiring the picker and persistent user-space mapping into
Origo's shipped installer is a separate product change and has not been made in
this repository. Other agent hosts can use the CLI, Python API or exported MCP
package directly.
