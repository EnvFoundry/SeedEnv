# Genomic alignment files · 基因组比对文件

Read, index and query SAM, BAM, CRAM and variants.

Keep reference sequences available for CRAM and state coordinate conventions at API boundaries. Use indexed regional access when possible; include read flags and multi-mapping policy in summaries.

读取、索引与查询比对及变异文件。

CRAM 保留配套参考序列，接口交界处明确坐标约定。优先使用索引区域读取，汇总时说明读段标志和多重映射处理。

Software / 软件：pysam (`python-pysam`).

Use `seedenv context genomic-alignments` for software entries and setup on this host.

- https://pysam.readthedocs.io/en/latest/installation.html
