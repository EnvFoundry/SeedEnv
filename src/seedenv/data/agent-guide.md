---
name: seedenv
description: Find, prepare and reuse research software for a task or discipline. Use when selecting research modules, connecting existing software, preparing dependencies, or finding a module's working guide.
---

# SeedEnv

Search for the research task with `seedenv_search`. Read the matching module
with `seedenv_show`; use `seedenv_guide` when its working instructions are needed.
Choose modules for the actual task. Common components are shared across modules.

Call `seedenv_plan` for a combined selection. Reuse registered software. If the
user has an interpreter or native installation, inspect it with `seedenv_discover`
and register the selected command with `seedenv_bind`.

Start missing software with `seedenv_prepare`; retain its job ID and use
`seedenv_status` for progress. `seedenv_cancel` stops unfinished preparation and
retains completed components. A partial result names the specific software,
external installation or plugin still needed. Configure those through their
upstream or host interface.

After preparation, obtain the actual invocation with `seedenv_entry`. Write and
run complete programs using the software's native API. Copy a starting program
with `seedenv example MODULE --output program.py`, then adapt it to the question.
Keep research inputs and outputs in the research workspace, outside software
directories. Read only relevant guides; do not load the whole catalogue into
the conversation.

SeedEnv prepares environments on the machine running its process. Use the host's
existing remote connection to run it on another computer. Account credentials,
instrument ownership and research execution remain with the selected host.
