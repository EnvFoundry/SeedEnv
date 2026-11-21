# Quantum dynamics · 量子动力学

量子态、算符与开放系统动力学。

1. 明确希尔伯特空间截断、基底、单位和哈密顿量，写出观测算符。
2. 先用 sesolve 做封闭系统演化；需要耗散时在 mesolve 中给出对应塌缩算符。
3. 时间步和空间截断由研究问题决定；输出观测量并保留所用模型。

查看组件与准备方式：`seedenv show quantum`。准备后用 `seedenv entry COMPONENT` 获取实际命令。通过该解释器或程序使用完整上游接口。

起步程序：`seedenv example quantum --output quantum.py`，然后运行 `seedenv run python-quantum -- quantum.py`。示例输入是演示数据，可替换为自己的研究数据。

上游文档：

- https://qutip.readthedocs.io/en/stable/installation.html
