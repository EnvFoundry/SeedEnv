# Biological sequences · 生物序列

FASTA/GenBank、序列变换和基础统计。

1. 保留序列 ID、物种、链方向与注释，明确 DNA/RNA/蛋白质类型。
2. 使用 SeqIO 读写记录、Seq 操作序列；统计和变换输出保持与原记录可关联。
3. 比对、组装或大规模组学任务按需要连接对应软件；起步程序展示基础序列处理。

查看组件与准备方式：`seedenv show sequences`。准备后用 `seedenv entry COMPONENT` 获取实际命令。通过该解释器或程序使用完整上游接口。

起步程序：`seedenv example sequences --output sequences.py`，然后运行 `seedenv run python-sequences -- sequences.py`。示例输入是演示数据，可替换为自己的研究数据。

上游文档：

- https://biopython.org/download/
