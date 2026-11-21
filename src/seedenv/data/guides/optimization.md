# Optimization · 优化与运筹

凸优化、线性规划和约束建模。

1. 分别写出决策变量、目标和约束，先核对量纲与可行性。
2. CVXPY 用于表达符合其规则的优化问题；HiGHS 用于线性与混合整数模型。算法选择取决于问题结构。
3. 输出最优变量、目标值和求解状态；参数扫描复用同一建模程序。

查看组件与准备方式：`seedenv show optimization`。准备后用 `seedenv entry COMPONENT` 获取实际命令。通过该解释器或程序使用完整上游接口。

起步程序：`seedenv example optimization --output optimization.py`，然后运行 `seedenv run python-optimization -- optimization.py`。示例输入是演示数据，可替换为自己的研究数据。

上游文档：

- https://www.cvxpy.org/install/
