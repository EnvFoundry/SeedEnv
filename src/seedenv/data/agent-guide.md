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

Call `seedenv_plan` for a combined selection. Reuse registered software. If the
user has an interpreter or native installation, inspect it with `seedenv_discover`
and register the selected command with `seedenv_bind`.

Start missing software with `seedenv_prepare`; retain a returned job ID and use
`seedenv_status` for progress. `seedenv_cancel` stops unfinished preparation and
retains completed components. A partial result names the specific software,
external installation or plugin still needed. Configure those through their
upstream or host interface.

Use `seedenv_context` with only the selected modules to obtain their working
guides, editable examples, real invocation commands and outstanding setup.
Related resources and specialist labs remain explicit connections. Do not infer
that a dataset, model weight, plugin or account is ready merely from a module
selection. A conda recipe uses the host's existing conda-family manager.

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
