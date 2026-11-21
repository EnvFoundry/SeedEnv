# Literature metadata · 文献元数据

用 Crossref 的 DOI 元数据连接论文、作者、期刊和参考文献。`references.py` 是实际 HTTP 客户端，能查询传入的 DOI；研究需要其他筛选条件时直接调用上游 API。

保留 DOI 与原始元数据，把文章内容和元数据分开。检索结果是寻找原文的入口；研究论点应当回到原文、方法和数据中理解。批量获取时遵循服务返回的限流信息。

已有文献连接器时直接复用产品中的连接。否则用 httpx 访问公开接口；无需在 SeedEnv 中保存账户信息。

`seedenv example references --output references.py`

`seedenv run python-http -- references.py 10.1038/nphys2525`

上游文档：https://www.crossref.org/documentation/retrieve-metadata/rest-api/
