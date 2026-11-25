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

    def test_template_only_flow_and_relocated_writing_export(self):
        from seedenv.writing import templates, create_manuscript
        self.assertEqual(len(templates()["items"]), 22)
        self.assertEqual(len(templates(language="zh", form="article")["items"]), 3)
        self.assertEqual(self.manager.start(["writing-templates"])["job"], None)
        paper = self.root / "manuscript 中文"
        create_manuscript("compact-article-zh", paper)
        self.assertTrue((paper / "main.tex").is_file())
        self.assertTrue((paper / "sn-nature.bst").is_file())
        self.assertEqual((paper / "WRITING.md").read_bytes(),
                         (ROOT / "src/seedenv/data/guides/writing-methods.md").read_bytes())
        self.assertFalse(self.home.exists())
        with self.assertRaises(FileExistsError):
            create_manuscript("standard-article-en", paper)
        exported = self.root / "writing export"
        export_plugin(exported, "mcp", selections=["writing-templates"])
        moved = self.root / "moved writing"
        exported.rename(moved)
        env = {**os.environ, "SEEDENV_HOME": str(self.home)}
        env.pop("PYTHONPATH", None)
        request = {"jsonrpc":"2.0", "id":1, "method":"tools/call", "params":{
            "name":"seedenv_manuscript", "arguments":{"template":"standard-book-en", "output":str(self.root/"book")}}}
        result = subprocess.run([sys.executable, str(moved/"server.py")], input=json.dumps(request)+"\n",
                                capture_output=True, text=True, cwd=self.root, env=env, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn('"isError": true', result.stdout)
        self.assertTrue((self.root/"book/main.tex").is_file())
        self.assertEqual((self.root/"book/WRITING.md").read_bytes(), (paper/"WRITING.md").read_bytes())
        self.assertFalse(self.home.exists())
        export_plugin(self.root/"numeric export", "mcp", selections=["numerical-computing"])
        self.assertFalse((self.root/"numeric export/seedenv/data/writing").exists())

    def test_host_request_reuses_an_external_interpreter_without_a_second_install(self):
        original = self.prepare()
        other = self.root / "host owned space"
        request = {"selections":["fixture"], "existing":[{"command":original["command"]}], "options":{"offline":True}}
        result = subprocess.run([sys.executable,"-m","seedenv","--home",str(other),"--catalog",str(self.extra),"prepare-request"],
                                input=json.dumps(request), capture_output=True, text=True,
                                env={**os.environ,"PYTHONPATH":str(ROOT/"src")}, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        value = json.loads(result.stdout)
        self.assertEqual(value["ready"][0]["command"], original["command"])
        self.assertFalse(value["ready"][0]["managed"])
        self.assertFalse((other/"environments").exists())
        self.assertFalse((other/"jobs").exists())
        repeat = Manager(other, Catalog(self.extra)).prepare_request({"selections":["fixture"],"options":{"offline":True}})
        self.assertEqual(repeat["ready"][0]["command"], original["command"])
        roundtrip = self.manager.prepare_request(request)["ready"][0]
        self.assertTrue(roundtrip["managed"])
        self.assertEqual(roundtrip["location"], original["location"])

    def test_interrupted_python_destination_is_reused_on_retry(self):
        failed = self.manager.prepare(["fixture"], offline=True)
        self.assertEqual(len(failed["failed"]), 1)
        record = self.home/"preparing/fixture-python.json"
        prefix = Path(json.loads(record.read_text())["location"])
        self.assertEqual(self.manager.state.list(), [])
        result = self.prepare()
        self.assertEqual(Path(result["location"]), prefix)
        self.assertFalse(record.exists())
        self.assertEqual(len(list((self.home/"environments").iterdir())), 1)
        self.assertEqual(self.cli("run","fixture-python","--","-c","from seedenv_fixture import square; print(square(7))").stdout.strip(), "49")

    def test_existing_legacy_location_is_preserved_and_new_spaces_use_system(self):
        space = self.root/"research"
        self.assertEqual(Manager(research_space=space).home, space/"System/env/seedenv")
        legacy = space/"system/seedenv"
        legacy.mkdir(parents=True)
        self.assertEqual(Manager(research_space=space).home, legacy)
        self.assertEqual(Manager(home=self.home, research_space=space).home, self.home)

    def test_tex_archive_continues_an_interrupted_http_transfer(self):
        import http.server
        import threading
        from seedenv.tex import _download
        payload = b"TeX archive bytes" * 1000
        ranges = []
        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                requested = self.headers.get("Range")
                ranges.append(requested)
                if requested:
                    start = int(requested.removeprefix("bytes=").removesuffix("-"))
                    if start == len(payload):
                        self.send_response(416)
                        self.send_header("Content-Range", f"bytes */{len(payload)}")
                        self.end_headers()
                        return
                    self.send_response(206)
                    self.send_header("Content-Range", f"bytes {start}-{len(payload)-1}/{len(payload)}")
                    self.send_header("Content-Length", str(len(payload)-start))
                    self.end_headers()
                    self.wfile.write(payload[start:])
                else:
                    self.send_response(200)
                    self.send_header("Content-Length", str(len(payload)))
                    self.end_headers()
                    self.wfile.write(payload[:1000])
            def log_message(self, *args): pass
        server = http.server.ThreadingHTTPServer(("127.0.0.1",0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        archive = self.root/"archive.tar.xz"
        try:
            url = f"http://127.0.0.1:{server.server_port}/tex"
            with self.assertRaises((RuntimeError, OSError)):
                _download(url, archive)
            self.assertFalse(archive.exists())
            _download(url, archive)
            self.assertEqual(archive.read_bytes(), payload)
            self.assertEqual(ranges, [None, "bytes=1000-"])
            archive.replace(archive.with_suffix(".xz.partial"))
            _download(url, archive)
            self.assertEqual(archive.read_bytes(), payload)
            self.assertEqual(ranges[-1], f"bytes={len(payload)}-")
        finally:
            server.shutdown(); server.server_close(); thread.join()

    def test_shared_foundation_selections_do_not_install_a_group(self):
        basics = self.manager.catalog.browse("scientific-basics")
        self.assertEqual(self.manager.catalog.browse("research-essentials"), basics)
        with self.assertRaisesRegex(ValueError, "is a field"):
            self.manager.prepare(["scientific-writing"])
        plan = self.manager.plan(["scientific-python", "numerical-computing", "symbolic-mathematics", "scientific-plotting"])
        self.assertEqual([a["action"] for a in plan["actions"]], ["install","share","share","share"])
        self.assertEqual(self.manager.prepare(["writing-methods","writing-templates"])["ready"], [])
        self.assertFalse(self.home.exists())

    def test_composition_and_software_search(self):
        modules, components = self.manager.catalog.select(["fixture", "fixture-composed"])
        self.assertEqual(components, ["fixture-python", "fixture-native"])
        self.assertEqual(len(modules), 2)
        self.assertIn("quantum", [x["id"] for x in self.manager.catalog.search("qutip")["items"]])
        self.assertEqual(self.manager.catalog.search("fixture", limit=1)["next_offset"], 1)

    def test_empty_selection_and_browsing_do_not_create_user_files(self):
        self.manager.catalog.browse('optics')
        self.assertEqual(self.manager.state.list(), [])
        self.assertEqual(self.manager.plan([])['actions'], [])
        self.assertEqual(self.manager.plan([])['storage']['download_bytes'], 0)
        self.assertEqual(self.manager.start([])['job'], None)
        self.assertTrue(self.manager.context([])['ready'])
        self.assertEqual(self.cli('prepare', '--background').returncode, 0)
        self.assertFalse(self.home.exists())

    def test_selected_larger_environment_is_shared_regardless_of_order(self):
        self.definition['components'].append({**self.definition['components'][0],
            'id': 'fixture-small', 'reuse_from': ['fixture-python']})
        self.save_catalog()
        manager = Manager(self.home, Catalog(self.extra))
        plan = manager.plan(['fixture-small', 'fixture'])
        self.assertEqual([(a['component'], a['action']) for a in plan['actions']],
                         [('fixture-python', 'install'), ('fixture-small', 'share')])
        result = manager.prepare(['fixture-small', 'fixture'], offline=True, find_links=[self.wheels])
        self.assertEqual(result['failed'], [])
        self.assertEqual(len(list((self.home / 'environments').iterdir())), 1)
        self.assertEqual(manager.entry('fixture-small')['command'], manager.entry('fixture-python')['command'])

    def test_context_contains_only_selected_guidance_and_real_entries(self):
        pending = self.manager.context(['fixture'])
        self.assertFalse(pending['ready'])
        self.assertEqual([m['id'] for m in pending['modules']], ['fixture'])
        original = self.prepare()
        ready = self.manager.context(['fixture'])
        self.assertTrue(ready['ready'])
        self.assertEqual(ready['software'][0]['command'], original['command'])
        self.assertIn('complete API', ready['modules'][0]['guide'])
        # An existing Python executable is insufficient when its software was removed.
        package = next(Path(original['location']).rglob('seedenv_fixture/__init__.py')).parent
        shutil.rmtree(package)
        self.assertFalse(self.manager.context(['fixture'])['ready'])

    def test_related_resources_are_not_research_directions(self):
        catalog = self.manager.catalog
        optics = catalog.browse('optics')
        self.assertIn('optical-lab', [r['id'] for r in optics['resources']])
        self.assertTrue(all('optical-lab' not in d['modules'] for d in catalog.fields['optics']['directions']))
        self.assertEqual(next(f for f in optics['fields'] if f['id'] == 'scientific-basics')['kind'], 'shared')

    def test_prepared_software_keeps_laboratory_connection_with_host(self):
        self.definition['modules'].append({'id': 'fixture-experiment', 'title': 'Experiment',
            'components': ['fixture-python', 'connector-laboratory'], 'guide': 'guide.md'})
        self.save_catalog()
        manager = Manager(self.home, Catalog(self.extra))
        result = manager.prepare(['fixture-experiment'], offline=True, find_links=[self.wheels])
        self.assertEqual(len(result['ready']), 1)
        self.assertEqual(result['failed'], [])
        self.assertEqual(result['pending'][0]['connection']['type'], 'laboratory')
        self.assertEqual(result['pending'][0]['modules'], ['fixture-experiment'])
        context = manager.context(['fixture-experiment'])
        self.assertFalse(context['ready'])
        self.assertEqual(context['software'][0]['action'], 'reuse')
        self.assertEqual(context['software'][1]['action'], 'configure-connector')
        repeated = manager.prepare(['fixture-experiment'], offline=True, find_links=[self.wheels])
        self.assertEqual(repeated['ready'][0]['command'], result['ready'][0]['command'])
        self.assertEqual(len(list((self.home / 'environments').iterdir())), 1)

    def test_fields_navigate_without_selecting_a_whole_discipline(self):
        catalog = self.manager.catalog
        self.assertIn("optics", [f["id"] for f in catalog.browse()["fields"]])
        directions = catalog.browse("optics")["directions"]
        self.assertIn("optoelectronic-devices", [d["id"] for d in directions])
        devices = catalog.search(field="optics", direction="optoelectronic-devices")["items"]
        self.assertIn("semiconductor-transport", [m["id"] for m in devices])
        self.assertNotIn("fiber-pulses", [m["id"] for m in devices])
        with self.assertRaisesRegex(ValueError, "is a field"):
            self.manager.plan(["optics"])
        with self.assertRaisesRegex(ValueError, "within its field"):
            catalog.search(direction="optoelectronic-devices")
        self.assertFalse((self.home / "environments").exists())

    def test_extension_adds_a_task_to_an_existing_direction(self):
        original = self.manager.catalog.fields["optics"]
        first = original["directions"][0]
        self.definition["fields"] = [{"id":"optics", "title":original["title"],
            "directions":[{"id":first["id"], "title":first["title"], "modules":["fixture"]}]}]
        self.save_catalog()
        catalog = Catalog(self.extra)
        ids = [m["id"] for m in catalog.search(field="optics", direction=first["id"])["items"]]
        self.assertIn("fixture", ids)
        self.assertIn("lens-design", ids)
        self.assertEqual(catalog.show("fixture")["paths"][0]["field"], "optics")

    def test_specific_tasks_prepare_only_their_shared_software(self):
        thin = self.manager.plan(["thin-films"])
        self.assertEqual([a["component"] for a in thin["actions"]], ["python-tmm"])
        self.assertNotIn("miepython", thin["actions"][0]["requirements"])
        quantum = self.manager.plan(["quantum", "quantum-trajectories", "photon-correlations"])
        self.assertEqual([a["component"] for a in quantum["actions"]], ["python-quantum"])
        self.assertEqual(quantum["storage"]["new_environments"], 1)
        # The same module is reachable from physics and optics, not copied.
        for field in ["optics", "physics"]:
            self.assertIn("photon-correlations", [m["id"] for m in self.manager.catalog.search("correlations", field=field)["items"]])

    def test_smaller_component_reuses_previously_prepared_environment(self):
        original = self.prepare()
        self.definition["components"].append({**self.definition["components"][0],
            "id": "fixture-small", "reuse_from": ["fixture-python"]})
        self.save_catalog()
        manager = Manager(self.home, Catalog(self.extra))
        plan = manager.plan(["fixture-python", "fixture-small"])
        self.assertEqual([a["action"] for a in plan["actions"]], ["reuse", "reuse"])
        self.assertEqual(plan["storage"]["reused_environments"], 1)
        self.assertEqual(manager.entry("fixture-small")["command"], original["command"])
        result = self.cli("prepare", "fixture-small", "--offline")
        self.assertEqual(result.returncode, 0, result.stderr)
        saved = json.loads(result.stdout)["ready"][0]
        self.assertEqual(saved["component"], "fixture-small")
        self.assertEqual(saved["command"], original["command"])
        self.assertEqual(len(list((self.home / "environments").iterdir())), 1)

    def test_user_research_space_and_external_solver_binding(self):
        user_space = self.root / "user research space"
        manager = Manager(catalog=self.manager.catalog, research_space=user_space)
        expected = user_space / "System" / "env" / "seedenv"
        self.assertEqual(manager.home, expected)
        plan = manager.plan(["thin-films"])
        self.assertEqual(plan["storage"]["root"], str(expected))
        self.assertIsNone(plan["storage"]["download_bytes"])
        host = origo_requests(manager, ["thin-films"])
        self.assertEqual(host["installation_root"], str(expected))
        self.assertTrue(host["preparations"][0]["request"]["destination"].startswith("environments/"))
        original = self.prepare()
        self.definition["components"].append({"id":"fixture-external", "title":"Existing solver", "kind":"environment",
            "imports":["seedenv_fixture"], "instructions":"Connect an existing interpreter"})
        self.save_catalog()
        external = Manager(self.home, Catalog(self.extra))
        self.assertEqual(external.prepare(["fixture-external"])["pending"][0]["action"], "setup")
        external.bind("fixture-external", original["command"])
        self.assertEqual(external.prepare(["fixture-external"])["ready"][0]["command"], original["command"])
        self.assertEqual(self.manager.plan(["fdtd"], target="windows")["actions"][0]["action"], "choose-host")

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
        self.assertEqual(len(list((self.home / "environments").iterdir())), 2)
        self.assertTrue((self.home / "preparing" / "fixture-missing.json").is_file())

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
            {"jsonrpc": "2.0", "id": 5, "method": "resources/read", "params": {"uri": "seedenv://examples/thin-films"}},
            {"jsonrpc": "2.0", "id": 6, "method": "resources/templates/list"},
            {"jsonrpc": "2.0", "id": 7, "method": "unknown/method"},
            {"jsonrpc": "2.0", "id": 8, "method": "prompts/get", "params": {"name": "missing"}},
        ]
        result = self.cli("mcp", input="".join(json.dumps(x) + "\n" for x in requests))
        self.assertEqual(result.returncode, 0, result.stderr)
        responses = [json.loads(line) for line in result.stdout.splitlines()]
        self.assertEqual([x["id"] for x in responses], [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(responses[0]["result"]["protocolVersion"], "2025-11-25")
        empty = json.loads(responses[2]['result']['content'][0]['text'])
        self.assertEqual((empty['state'], empty['job']), ('ready', None))
        self.assertIn("complete API", responses[3]["result"]["contents"][0]["text"])
        self.assertIn("coh_tmm", responses[4]["result"]["contents"][0]["text"])
        self.assertEqual(responses[5]["result"], {"resourceTemplates": []})
        self.assertEqual(responses[6]["error"]["code"], -32601)
        self.assertEqual(responses[7]["error"]["code"], -32600)
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

    def test_selected_plugin_exposes_only_its_packaged_resources(self):
        exported = self.root / 'numeric plugin'
        export_plugin(exported, selections=['numerical-computing'])
        metadata = json.loads((exported / 'plugin.json').read_text())['environment']
        self.assertIn('zh-CN', metadata['presentation'])
        self.assertFalse(any(item['kind'] == 'writing' for item in metadata['resources']))
        for resource in metadata['resources']:
            self.assertTrue((exported / resource['package_path']).exists(), resource)

    def test_selected_export_contains_local_catalogue_resources_after_moving(self):
        self.definition['modules'][0]['example'] = {'component': 'fixture-python', 'file': 'example.py'}
        (self.root / 'example.py').write_text('from seedenv_fixture import square\nprint(square(3))\n')
        self.save_catalog()
        exported = self.root / 'selected'
        export_plugin(exported, 'mcp', catalog=self.extra, selections=['fixture'])
        packed = json.loads((exported / 'seedenv/data/catalog.json').read_text())
        self.assertEqual([m['id'] for m in packed['modules']], ['fixture'])
        self.assertEqual([c['id'] for c in packed['components']], ['fixture-python'])
        self.assertTrue((exported / 'skills/seedenv/SKILL.md').is_file())
        self.assertNotIn('SEEDENV_CATALOG', json.loads((exported / 'mcp.json').read_text())['mcpServers']['seedenv']['env'])
        moved = self.root / 'portable'
        shutil.move(exported, moved)
        self.extra.unlink()
        (self.root / 'guide.md').unlink()
        (self.root / 'example.py').unlink()
        requests = [{'jsonrpc':'2.0','id':1,'method':'tools/call',
                     'params':{'name':'seedenv_context','arguments':{'selections':['fixture']}}},
                    {'jsonrpc':'2.0','id':2,'method':'tools/call',
                     'params':{'name':'seedenv_example','arguments':{'name':'fixture'}}}]
        env = {**os.environ, 'SEEDENV_HOME': str(self.home)}
        env.pop('PYTHONPATH', None)
        space = self.root / 'receiving research space'
        configured = subprocess.run([sys.executable, str(moved / 'configure.py'), '--research-space', str(space)],
                                    capture_output=True, text=True, cwd=self.root, env=env, timeout=30)
        self.assertEqual(configured.returncode, 0, configured.stderr)
        config = json.loads((moved / 'mcp.json').read_text())['mcpServers']['seedenv']
        self.assertEqual(config['env']['SEEDENV_HOME'], str(space / 'System' / 'env' / 'seedenv'))
        result = subprocess.run([config['command'], *config['args']], input=''.join(json.dumps(r)+'\n' for r in requests),
                                capture_output=True, text=True, cwd=self.root, env={**env, **config['env']}, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        responses = [json.loads(line) for line in result.stdout.splitlines()]
        context = json.loads(responses[0]['result']['content'][0]['text'])
        self.assertEqual([m['id'] for m in context['modules']], ['fixture'])
        self.assertIn('complete API', context['modules'][0]['guide'])
        example = json.loads(responses[1]['result']['content'][0]['text'])
        self.assertEqual(context['modules'][0]['example']['uri'], example['uri'])
        self.assertIn('print(square(3))', example['content'])


if __name__ == "__main__":
    unittest.main()
