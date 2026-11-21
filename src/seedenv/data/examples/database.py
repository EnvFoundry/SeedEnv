"""Exercise the SQL API locally; use a host-provided connection for remote data."""
import json
from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:")
with engine.begin() as connection:
    connection.execute(text("CREATE TABLE observations (sample TEXT, value REAL)"))
    connection.execute(text("INSERT INTO observations VALUES (:sample, :value)"),
                       [{"sample": "A", "value": 1.2}, {"sample": "A", "value": 1.4}, {"sample": "B", "value": 2.0}])
    result = connection.execute(text("SELECT sample, AVG(value) AS mean FROM observations GROUP BY sample"))
    print(json.dumps([dict(row) for row in result.mappings()]))
