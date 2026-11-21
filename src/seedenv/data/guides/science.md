# Scientific computing · 科学计算

数组、数值求解、符号运算、拟合和绘图。

1. 先明确变量、单位和要计算的量。代数推导用 SymPy；数值数组和求解用 NumPy/SciPy；图表直接使用计算输出。
2. 将输入、求解与输出分开。数组同时保留轴含义、单位和采样方式，避免不同程序之间重新猜测。
3. 需要具体模型时阅读对应专业文档；该环境允许任意 Python 研究程序。

查看组件与准备方式：`seedenv show science`。准备后用 `seedenv entry COMPONENT` 获取实际命令。通过该解释器或程序使用完整上游接口。

起步程序：`seedenv example science --output fit.py`，然后运行 `seedenv run python-science -- fit.py`。示例输入是演示数据，可替换为自己的研究数据。

上游文档：

- https://scipy.org/install/
