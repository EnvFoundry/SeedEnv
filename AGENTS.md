# SeedEnv

Keep module content separate from preparation code. Add disciplines through the
catalogue, guides and useful programs; reuse upstream APIs. Do not build a new
agent harness, package manager, solver or collection of expert personas here.

Research programs must remain editable and able to use the full upstream API.
Keep agent context small: search first, then load only relevant guides.

Python owns preparation and catalogue composition. TypeScript and Rust clients
call that implementation. Native tools, host plugins and account connections
must retain their actual setup state in product-facing results.

When changing preparation behavior, run the local-wheel process tests. When
changing a scientific example, run that example with its real software. Keep the
English and Chinese entry pages consistent. Use a task branch for later changes.
