# Research databases · 研究数据库

先确认表中一行代表什么，主键、连接关系、单位和缺失值含义是什么，再写查询。需要关联大表时把筛选和聚合交给数据库；在 Python 中继续做统计和绘图。

使用产品已有的数据库连接，将连接信息交给 SQLAlchemy 或 psycopg。SeedEnv 准备客户端库；数据库地址、账户和具体数据范围由所在产品管理。安装客户端不代表远程数据库已经连接。

起步程序使用本地内存数据库演示参数化写入和分组计算，不需要服务器：

`seedenv example databases --output database.py`

`seedenv run python-databases -- database.py`

上游文档：
- https://docs.sqlalchemy.org/en/20/tutorial/
- https://www.psycopg.org/psycopg3/docs/
- https://www.postgresql.org/docs/current/libpq-connect.html
