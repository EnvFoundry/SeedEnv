import json
import time
import uuid


TERMINAL = {"ready", "partial", "failed", "cancelled"}


class Tasks:
    def __init__(self, manager):
        self.manager = manager

    @staticmethod
    def describe(row, *, starting=False):
        result = row.get("result") or {}
        status = "working" if starting or row["state"] not in TERMINAL else (
            "cancelled" if row["state"] == "cancelled" else
            "failed" if row["state"] == "failed" or result.get("failed") else "completed")
        value = {"taskId": row["id"], "status": status, "createdAt": row["created_at"].replace(" ", "T") + "Z",
                 "lastUpdatedAt": row["updated_at"].replace(" ", "T") + "Z", "ttl": None, "pollInterval": 1000}
        message = row.get("error") or "; ".join(item["error"] for item in result.get("failed", []) if item.get("error"))
        if message:
            value["statusMessage"] = message
        return value

    def start(self, response, selections):
        task_id = response.get("job")
        if task_id is None:
            task_id = uuid.uuid4().hex
            self.manager.state.select(selections)
            self.manager.state.add_job(task_id, selections)
            self.manager.state.set_job(task_id, "ready", result=response["result"])
        return {"task": self.describe(self.manager.state.job(task_id), starting=True)}

    def get(self, task_id):
        return self.describe(self.manager.status(task_id))

    def result(self, task_id):
        while (row := self.manager.status(task_id))["state"] not in TERMINAL:
            time.sleep(.1)
        result = row["result"]
        if result is None:
            result = self.manager.installed_summary()
            result["error"] = row.get("error") or row["state"]
        error = row["state"] in {"failed", "cancelled"} or bool(result.get("failed"))
        return {"content": [{"type": "text", "text": json.dumps(result, ensure_ascii=False)}],
                "structuredContent": result, "isError": error,
                "_meta": {"io.modelcontextprotocol/related-task": {"taskId": task_id}}}

    def cancel(self, task_id):
        if self.manager.status(task_id)["state"] in TERMINAL:
            raise ValueError("The preparation task is already terminal")
        self.manager.cancel(task_id)
        while self.manager.status(task_id)["state"] not in TERMINAL:
            time.sleep(.1)
        return self.get(task_id)
