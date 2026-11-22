# Distributed arrays · 分块与分布式数据计算

Process arrays and tables larger than one worker memory.

Choose chunk sizes from the operation and worker memory, not only file size. Keep lazy arrays lazy until an output is needed; connect to the host scheduler rather than starting an unrelated cluster.

处理超出单个工作进程内存的数组与表格。

按操作和工作进程内存选择分块。需要输出前保持延迟计算；连接宿主已有调度器，避免另起无关集群。

Software / 软件：Dask (`python-dask`).

Use `seedenv context distributed-arrays` for software entries and setup on this host.

- https://docs.dask.org/en/stable/install.html
