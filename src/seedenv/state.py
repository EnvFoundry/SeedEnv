"""Only installed locations and preparation progress live in SQL."""
from contextlib import contextmanager
import json
from pathlib import Path
import sqlite3

from .catalog import DATA


class State:
    def __init__(self, home):
        self.home = Path(home)
        self.home.mkdir(parents=True, exist_ok=True)
        with self.db() as db:
            db.executescript((DATA / "state.sql").read_text())

    @contextmanager
    def db(self):
        db = sqlite3.connect(self.home / "state.sqlite3", timeout=30)
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    @staticmethod
    def installation(row):
        if row is None:
            return None
        value = dict(row)
        value["command"] = json.loads(value["command"])
        value["definition"] = json.loads(value["definition"])
        value["managed"] = bool(value["managed"])
        return value

    def get(self, component):
        with self.db() as db:
            return self.installation(db.execute("SELECT * FROM installations WHERE component=?", (component,)).fetchone())

    def list(self):
        with self.db() as db:
            return [self.installation(row) for row in db.execute("SELECT * FROM installations ORDER BY component")]

    def bind(self, component, definition, command, location, managed):
        with self.db() as db:
            db.execute("""INSERT INTO installations(component,definition,command,managed,location)
                VALUES(?,?,?,?,?) ON CONFLICT(component) DO UPDATE SET
                definition=excluded.definition,command=excluded.command,managed=excluded.managed,
                location=excluded.location,prepared_at=CURRENT_TIMESTAMP""",
                (component, json.dumps(definition, sort_keys=True), json.dumps(command), int(managed), str(location)))
        return self.get(component)

    def add_job(self, job, names):
        with self.db() as db:
            db.execute("INSERT INTO jobs(id,state,selection) VALUES(?,?,?)", (job, "queued", json.dumps(names)))

    def set_job(self, job, state, result=None, error=None):
        with self.db() as db:
            db.execute("UPDATE jobs SET state=?,result=?,error=?,updated_at=CURRENT_TIMESTAMP WHERE id=?",
                       (state, json.dumps(result) if result is not None else None, error, job))

    def job(self, job):
        with self.db() as db:
            row = db.execute("SELECT * FROM jobs WHERE id=?", (job,)).fetchone()
        if row is None:
            raise ValueError(f"Unknown preparation: {job}")
        value = dict(row)
        value["selection"] = json.loads(value["selection"])
        if value["result"] is not None:
            value["result"] = json.loads(value["result"])
        return value
