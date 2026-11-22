---
name: seedenv
description: Find, prepare and reuse research software for a task or discipline. Use when selecting research modules, connecting existing software, preparing dependencies, or finding a module's working guide.
---

# SeedEnv

Browse a field and direction with `seedenv_browse`, or search the actual task
with `seedenv_search`. Fields are navigation, not install-all bundles. An empty
selection is valid. Read the matching module
with `seedenv_show`; use `seedenv_guide` when its working instructions are needed.
Choose modules for the actual task. Common components are shared across modules.

Scientific Basics and Scientific Writing are shared navigation groups. Select
`scientific-python` for the common NumPy/SciPy/SymPy/Matplotlib/pandas base, or
individual computing tasks for smaller installations. Keep specialist software
optional and use the interpreter returned for the chosen task.

For writing, read `writing-methods` only when composition guidance helps. Use
`seedenv_templates` to select a layout and `seedenv_manuscript` to copy it into a
new manuscript directory. Templates alone do not require TeX. Reuse an existing
manuscript and author choices. Prepare `writing` only when a compiler is needed;
`seedenv_build` compiles the existing source without installing anything. It
returns the actual PDF path or the compiler output location. Keep references
and figures with the manuscript; adapt section names to the research argument.

Call `seedenv_plan` for a combined selection. Reuse registered software. If the
user has an interpreter or native installation, inspect it with `seedenv_discover`
and register the selected command with `seedenv_bind`.

Start missing software with `seedenv_prepare`; retain a returned job ID and use
`seedenv_status` for progress. `seedenv_cancel` stops unfinished preparation and
retains completed components. A partial result names the specific software,
external installation or plugin still needed. Configure those through their
upstream or host interface.

Repeat the same request after an interrupted installation. Python retains its
unfinished destination; TeX retains its archive and extracted installation.
In a product job, the host calls `prepare-request` synchronously and supplies its
existing environment entries. The host owns scheduling and registration; this
route does not create an additional background worker.

Use `seedenv_context` with only the selected modules to obtain their working
guides, editable examples, real invocation commands and outstanding setup.
Related resources and specialist labs remain explicit connections. Do not infer
that a dataset, model weight, plugin or account is ready merely from a module
selection. A conda recipe uses the host's existing conda-family manager.

For physical experiments, select the measurement, acquisition, motion or timing
task. Prepare its software, then resolve the named devices through the host's
existing laboratory connections. A shared laboratory connector describes setup;
each instrument retains its own driver, address, units and experiment settings.
Use actual device readbacks and timestamps in research records. Keep simulated
and loopback examples identified as such. Timing-critical control stays with the
device controller; the agent chooses and analyzes experiments through its native
interface. Software preparation does not move equipment, flash boards or start
an acquisition.

After preparation, obtain the actual invocation with `seedenv_entry`. Write and
run complete programs using the software's native API. Read a starting program
with `seedenv_example`, or copy it with `seedenv example MODULE --output program.py`,
then adapt it to the question.
Keep research inputs and outputs in the research workspace, outside software
directories. Read only relevant guides; do not load the whole catalogue into
the conversation.

For another agent host, export only the desired modules with
`seedenv connect mcp --modules MODULE... --output DIRECTORY`. The package contains
their metadata, working guides and examples; research software is prepared on
the receiving execution host. Local catalogue additions are included in the
export instead of retaining paths to the source checkout.
After moving a generic MCP package, run its `configure.py` on the receiving
computer with the chosen `--research-space` before importing `mcp.json`.

SeedEnv prepares environments on the machine running its process. Use the host's
existing remote connection to run it on another computer. Account credentials,
instrument ownership and research execution remain with the selected host.
