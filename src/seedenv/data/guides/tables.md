# Tables and local data · 表格与本地数据

CSV、Parquet、Arrow 与本地 SQL 分析。

1. 先读取字段、类型、缺失值与标识列。对大数据先投影必要列和过滤条件，再聚合。
2. Polars 用于表格变换，DuckDB 用于跨文件 SQL，Arrow/Parquet 用于交换。连接数据时明确键与重复关系。
3. 外部数据连接使用用户已有服务和账户；本模块准备本地分析能力。

查看组件与准备方式：`seedenv show tables`。准备后用 `seedenv entry COMPONENT` 获取实际命令。通过该解释器或程序使用完整上游接口。

起步程序：`seedenv example tables --output tables.py`，然后运行 `seedenv run python-tables -- tables.py`。示例输入是演示数据，可替换为自己的研究数据。

上游文档：

- https://duckdb.org/docs/stable/clients/python/overview
