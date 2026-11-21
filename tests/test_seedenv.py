"""Exercise actual process boundaries and environment reuse without downloads."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
import zipfile

from seedenv.catalog import Catalog
from seedenv.hosts import export_plugin, origo_requests
from seedenv.manager import Manager
from seedenv.process import Cancelled, installation_lock, run

ROOT = Path(__file__).resolve().parents[1]


class SeedEnvTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="seedenv test ")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.home = self.root / "software"
        self.wheels = self.root / "wheels"
        self.wheels.mkdir()
        self.make_wheel()
        self.extra = self.root / "catalog.json"
        self.definition = {"components": [
            {"id": "fixture-python", "title": "Local calculation", "kind": "python",
             "requirements": ["seedenv-fixture==1.0"], "imports": ["seedenv_fixture"]},
            {"id": "fixture-missing", "title": "Unavailable wheel", "kind": "python",
             "requirements": ["seedenv-missing-fixture"], "imports": ["seedenv_missing_fixture"]},
            {"id": "fixture-native", "title": "Native tool", "kind": "command",
             "commands": ["seedenv-fixture-unavailable-command"]},
        ], "modules": [
            {"id": "fixture", "title": "Fixture", "components": ["fixture-python"], "guide": "guide.md"},
            {"id": "fixture-composed", "title": "Composed", "includes": ["fixture"],
             "components": ["fixture-python", "fixture-native"], "guide": "guide.md"},
        ]}
        (self.root / "guide.md").write_text("Use the complete API to calculate.\n", encoding="utf-8")
        self.save_catalog()
        self.manager = Manager(self.home, Catalog(self.extra))

    def make_wheel(self):
        files = {
            "seedenv_fixture/__init__.py": "def square(x): return x*x\n",
            "seedenv_fixture-1.0.dist-info/METADATA": "Metadata-Version: 2.1\nName: seedenv-fixture\nVersion: 1.0\n",
            "seedenv_fixture-1.0.dist-info/WHEEL": "Wheel-Version: 1.0\nGenerator: seedenv-tests\nRoot-Is-Purelib: true\nTag: py3-none-any\n",
        }
        files["seedenv_fixture-1.0.dist-info/RECORD"] = "".join(f"{name},,\n" for name in [*files, "seedenv_fixture-1.0.dist-info/RECORD"])
        with zipfile.ZipFile(self.wheels / "seedenv_fixture-1.0-py3-none-any.whl", "w") as archive:
            for name, content in files.items():
                archive.writestr(name, content)

    def save_catalog(self):
        self.extra.write_text(json.dumps(self.definition), encoding="utf-8")

    def cli(self, *args, input=None):
        env = {**os.environ, "PYTHONPATH": str(ROOT / "src")}
        return subprocess.run([sys.executable, "-m", "seedenv", "--home", str(self.home),
                               "--catalog", str(self.extra), *args], text=True,
                              input=input, capture_output=True, env=env, timeout=90)

    def prepare(self):
        result = self.manager.prepare(["fixture"], offline=True, find_links=[self.wheels])
        self.assertFalse(result["failed"], result)
        return result["ready"][0]

    def test_composition_and_software_search(self):
        modules, components = self.manager.catalog.select(["fixture", "fixture-composed"])
        self.assertEqual(components, ["fixture-python", "fixture-native"])
        self.assertEqual(len(modules), 2)
        self.assertIn("quantum", [x["id"] for x in self.manager.catalog.search("qutip")["items"]])
        self.assertEqual(self.manager.catalog.search("fixture", limit=1)["next_offset"], 1)

    def test_catalog_rejects_cycle_and_resource_escape(self):
        self.definition["modules"][0]["includes"] = ["fixture-composed"]
        self.save_catalog()
        with self.assertRaisesRegex(ValueError, "Circular"):
            Catalog(self.extra)
        self.definition["modules"][0].pop("includes")
        self.definition["modules"][0]["guide"] = "../outside.md"
        self.save_catalog()
        with self.assertRaisesRegex(ValueError, "resource"):
            Catalog(self.extra)

    def test_install_calculate_and_reuse_in_another_process(self):
        first = self.prepare()
        result = self.cli("run", "fixture-python", "--", "-c", "from seedenv_fixture import square; print(square(12))")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "144")
        second = self.cli("prepare", "fixture", "--offline")
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertEqual(json.loads(second.stdout)["ready"][0]["command"], first["command"])
        self.assertEqual(len(list((self.home / "environments").iterdir())), 1)
        # Rebinding must preserve a venv symlink's invocation path.
        other = Manager(self.root / "other", self.manager.catalog)
        bound = other.bind("fixture-python", first["command"])
        self.assertEqual(bound["command"], first["command"])
        self.assertFalse(bound["managed"])

    def test_failed_addition_preserves_ready_environment(self):
        original = self.prepare()
        result = self.manager.prepare(["fixture-python", "fixture-missing", "fixture-native"], offline=True, find_links=[self.wheels])
        self.assertEqual([x["component"] for x in result["ready"]], ["fixture-python"])
        self.assertEqual(result["failed"][0]["component"], "fixture-missing")
        self.assertEqual(result["pending"][0]["action"], "setup")
        self.assertEqual(self.manager.entry("fixture-python")["command"], original["command"])
        self.assertEqual(len(list((self.home / "environments").iterdir())), 1)

    def test_background_job_survives_request_process_exit(self):
        started = self.cli("prepare", "fixture", "--background", "--offline", "--find-links", str(self.wheels))
        self.assertEqual(started.returncode, 0, started.stderr)
        job = json.loads(started.stdout)["job"]
        deadline = time.monotonic() + 60
        while time.monotonic() < deadline:
            result = self.manager.status(job)
            if result["state"] not in {"queued", "running"}:
                break
            time.sleep(0.1)
        self.assertEqual(result["state"], "ready", result)
        self.assertEqual(self.cli("entry", "fixture-python").returncode, 0)

    def test_cancellation_and_concurrent_preparation(self):
        cancel = self.root / "cancel"
        cancel.touch()
        with self.assertRaises(Cancelled):
            self.manager.prepare(["fixture"], cancel=cancel)
        self.assertEqual(self.manager.state.list(), [])
        lock = self.home / "locks" / "fixture-python.lock"
        with installation_lock(lock):
            result = self.cli("prepare", "fixture", "--offline", "--find-links", str(self.wheels))
            self.assertEqual(result.returncode, 2)
            self.assertIn("another process", result.stdout)

    def test_real_installer_process_is_cancelled(self):
        # A short child creates its own cancellation signal, then stays alive.
        cancel = self.root / "cancel"
        start = time.monotonic()
        with self.assertRaises(Cancelled):
            run([sys.executable, "-c", "import pathlib,sys,time; pathlib.Path(sys.argv[1]).touch(); time.sleep(30)", str(cancel)], cancel=cancel)
        self.assertLess(time.monotonic() - start, 10)

    def test_mcp_stream_and_native_host_request(self):
        requests = [
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-11-25"}},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "seedenv_plan", "arguments": {"selections": ["fixture"]}}},
            {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "seedenv_prepare", "arguments": {"selections": []}}},
            {"jsonrpc": "2.0", "id": 4, "method": "resources/read", "params": {"uri": "seedenv://guides/fixture"}},
        ]
        result = self.cli("mcp", input="".join(json.dumps(x) + "\n" for x in requests))
        self.assertEqual(result.returncode, 0, result.stderr)
        responses = [json.loads(line) for line in result.stdout.splitlines()]
        self.assertEqual([x["id"] for x in responses], [1, 2, 3, 4])
        self.assertEqual(responses[0]["result"]["protocolVersion"], "2025-11-25")
        self.assertTrue(responses[2]["result"]["isError"])
        self.assertIn("complete API", responses[3]["result"]["contents"][0]["text"])
        request = origo_requests(self.manager, ["fixture"])["preparations"][0]["request"]
        self.assertEqual(request["requirements"], ["seedenv-fixture==1.0"])
        self.assertIn("execution_id", request)

    def test_service_connections_remain_host_owned(self):
        plan = self.manager.plan(["references", "databases"])
        services = [x for x in plan["actions"] if x["kind"] == "connector"]
        self.assertEqual(len(services), 2)
        self.assertTrue(all(x["action"] == "configure-connector" for x in services))
        self.assertEqual(services[1]["connection"]["credentials"], "host-managed")
        with self.assertRaisesRegex(ValueError, "integration manager"):
            self.manager.bind("connector-postgresql", [sys.executable])

    def test_multilingual_output_and_mcp_under_non_utf8_host_defaults(self):
        env = {**os.environ, "PYTHONPATH": str(ROOT / "src"), "PYTHONIOENCODING": "ascii"}
        command = [sys.executable, "-m", "seedenv", "--home", str(self.home)]
        result = subprocess.run([*command, "search", "光学"], capture_output=True, env=env, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertGreater(json.loads(result.stdout.decode("utf-8"))["total"], 0)
        request = {"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                   "params": {"name": "seedenv_search", "arguments": {"query": "光学"}}}
        result = subprocess.run([*command, "mcp"], input=(json.dumps(request, ensure_ascii=False) + "\n").encode("utf-8"),
                                capture_output=True, env=env, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        text = json.loads(result.stdout.decode("utf-8"))["result"]["content"][0]["text"]
        self.assertGreater(json.loads(text)["total"], 0)

    def test_generic_mcp_export_uses_selected_home_and_embedded_code(self):
        exported = self.root / "mcp"
        export_plugin(exported, "mcp", home=self.home, catalog=self.extra)
        config = json.loads((exported / "mcp.json").read_text())["mcpServers"]["seedenv"]
        env = {**os.environ, **config["env"]}
        env.pop("PYTHONPATH", None)
        request = {"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                   "params": {"name": "seedenv_show", "arguments": {"name": "fixture"}}}
        result = subprocess.run([config["command"], *config["args"]], input=json.dumps(request) + "\n",
                                text=True, capture_output=True, env=env, cwd=self.root, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("fixture-python", result.stdout)
        self.assertEqual(config["env"]["SEEDENV_HOME"], str(self.home))

    def test_exported_origo_plugin_runs_after_moving(self):
        exported = self.root / "plugin"
        export_plugin(exported)
        moved = self.root / "moved plugin"
        shutil.move(exported, moved)
        request = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/list"}) + "\n"
        env = {**os.environ, "SEEDENV_HOME": str(self.home)}
        env.pop("PYTHONPATH", None)
        result = subprocess.run([sys.executable, "-B", str(moved / "server.py")], input=request,
                                text=True, capture_output=True, env=env, cwd=self.root, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("seedenv_prepare", result.stdout)
        self.assertEqual(json.loads((moved / "plugin.json").read_text())["skills"], ["skills/seedenv"])


if __name__ == "__main__":
    unittest.main()
