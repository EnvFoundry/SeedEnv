"""A preparation survives the requesting terminal or MCP connection."""
import json
from pathlib import Path
import sys

from .catalog import Catalog
from .manager import Manager
from .process import Cancelled
from .state import State


def main():
    home, job = sys.argv[1:]
    folder = Path(home) / "jobs" / job
    state_store = State(home)
    try:
        request = json.loads((folder / "request.json").read_text(encoding="utf-8"))
        manager = Manager(home, Catalog(request.get("catalog")))
        state_store.set_job(job, "running")
        result = manager.prepare(request["selections"], cancel=folder / "cancel", **request["options"])
        state = "partial" if result["pending"] or result["failed"] else "ready"
        state_store.set_job(job, state, result=result)
    except Cancelled:
        state_store.set_job(job, "cancelled")
    except Exception as error:
        state_store.set_job(job, "failed", error=str(error))


if __name__ == "__main__":
    main()
