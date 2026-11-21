# Circuit simulation · 电路模拟

连接 ngspice，运行原生电路网表。

1. 明确电路节点、器件参数与模型，写出原生 SPICE 网表。
2. 按研究目标选择直流、交流或瞬态分析，调用 ngspice -b 运行。
3. 保留网表、器件模型及带单位的输出；需要绘图时组合科学计算模块。

查看组件与准备方式：`seedenv show circuits`。准备后用 `seedenv entry COMPONENT` 获取实际命令。通过该解释器或程序使用完整上游接口。

上游文档：

- https://ngspice.sourceforge.io/download.html
