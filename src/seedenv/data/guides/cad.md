# Parametric geometry · 参数化几何

用程序构建几何并导出 STEP/STL。

1. 将关键尺寸作为参数，建立几何对象和装配关系。
2. STEP 用于保留实体几何，STL 用于三角面表示；导出时说明长度单位。
3. 制造、公差与后续仿真各有独立要求，继续使用 CadQuery 的完整建模接口。

查看组件与准备方式：`seedenv show cad`。准备后用 `seedenv entry COMPONENT` 获取实际命令。通过该解释器或程序使用完整上游接口。

起步程序：`seedenv example cad --output cad.py`，然后运行 `seedenv run python-cad -- cad.py`。示例输入是演示数据，可替换为自己的研究数据。

上游文档：

- https://cadquery.readthedocs.io/en/latest/installation.html
