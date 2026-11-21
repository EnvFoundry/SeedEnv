# Finite elements · 有限元基础

网格、弱形式、边界条件与 PDE 求解。

1. 写出方程、计算区域、弱形式和边界条件，然后选择单元与网格。
2. scikit-fem 负责组装与求解，meshio 交换网格。几何单位、材料参数和边界标记一起保存。
3. 改变网格或离散方式时比较所研究物理量的变化；复杂多物理场可以接入其他求解器。

查看组件与准备方式：`seedenv show finite-elements`。准备后用 `seedenv entry COMPONENT` 获取实际命令。通过该解释器或程序使用完整上游接口。

起步程序：`seedenv example finite-elements --output fem.py`，然后运行 `seedenv run python-fem -- fem.py`。示例输入是演示数据，可替换为自己的研究数据。

上游文档：

- https://scikit-fem.readthedocs.io/en/stable/gettingstarted.html
