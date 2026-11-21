# Molecular data · 分子数据

分子结构读取、描述符、子结构与格式转换。

1. 从 SMILES/SDF 建立分子对象，保留原始标识，明确盐、价态与立体化学处理。
2. 使用 RDKit 的结构、子结构和描述符接口。批量处理保留无法解析记录与原因，避免行号错配。
3. 描述符计算提供结构特征；能量、活性或动力学研究需要相应模型与数据。

查看组件与准备方式：`seedenv show molecules`。准备后用 `seedenv entry COMPONENT` 获取实际命令。通过该解释器或程序使用完整上游接口。

起步程序：`seedenv example molecules --output molecules.py`，然后运行 `seedenv run python-molecules -- molecules.py`。示例输入是演示数据，可替换为自己的研究数据。

上游文档：

- https://rdkit.org/docs/Install.html
