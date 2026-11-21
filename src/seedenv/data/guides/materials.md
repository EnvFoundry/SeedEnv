# Atomic structures and materials · 原子结构与材料

晶体、原子结构、文件转换和计算器接入。

1. 明确晶格、周期边界、坐标和长度单位，保留物种与结构标识。
2. ASE 操作原子结构与计算器，pymatgen 处理晶体和材料数据。能量计算需要另行选择实际计算器。
3. 先完成结构往返读写与所需量的计算，再扩展优化或批处理。

查看组件与准备方式：`seedenv show materials`。准备后用 `seedenv entry COMPONENT` 获取实际命令。通过该解释器或程序使用完整上游接口。

起步程序：`seedenv example materials --output materials.py`，然后运行 `seedenv run python-materials -- materials.py`。示例输入是演示数据，可替换为自己的研究数据。

上游文档：

- https://pymatgen.org/installation.html
