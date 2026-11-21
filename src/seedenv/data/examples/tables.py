"""Aggregate a local table with its original sample groups."""
import json
import duckdb
import polars as pl

frame = pl.DataFrame({"group": ["a", "a", "b", "b"], "value": [1., 3., 4., 8.]})
with duckdb.connect() as db:
    db.register("samples", frame.to_arrow())
    rows = db.sql("SELECT \"group\", count(*) AS n, avg(value) AS mean FROM samples GROUP BY 1 ORDER BY 1").fetchall()
print(json.dumps(rows))
