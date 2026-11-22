# Digital HDL simulation · 数字 HDL 仿真

Compile and simulate digital logic testbenches.

Declare timescale, clock/reset behavior and top-level module. Compile with iverilog and run with vvp; save waveforms for relevant signals and distinguish simulated timing from a synthesized hardware timing model.

编译并运行数字逻辑测试台。

明确时间尺度、时钟复位行为与顶层模块。iverilog 编译后由 vvp 运行，保存目标信号波形，并区分仿真时序与综合后的硬件时序模型。

Software / 软件：Icarus Verilog (`tool-iverilog`).

Use `seedenv context digital-hdl` for software entries and setup on this host.

- https://steveicarus.github.io/iverilog/
