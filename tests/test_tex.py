import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from zipfile import ZipFile

from seedenv import tex


class TexPreparationTests(unittest.TestCase):
    def test_font_failure_resumes_installed_dependencies_and_keeps_completed_install(self):
        with tempfile.TemporaryDirectory(prefix="seedenv tex ") as temporary:
            home = Path(temporary)
            spec = tex.recipe()
            asset = "TinyTeX-1-linux-x86_64-v2026.11.tar.xz"
            root = home / "software" / asset.removesuffix(".tar.xz")
            (root / "bin/x86_64-linux").mkdir(parents=True)
            installed = root / "installed-packages"
            installed.write_text("completed dependencies")
            modified = installed.stat().st_mtime_ns
            font = spec["fonts"][0]

            def download(url, path, cancel=None):
                if path.name.endswith(".zip") and not path.exists():
                    raise OSError("font download interrupted")

            with patch.object(tex, "asset_name", return_value=asset), \
                    patch.object(tex, "_download", side_effect=download), \
                    patch.object(tex, "run") as run, patch.object(tex, "describe"):
                with self.assertRaisesRegex(OSError, "font download interrupted"):
                    tex.prepare(home)
                self.assertFalse((root / "seedenv-prepared.json").exists())
                self.assertEqual(installed.stat().st_mtime_ns, modified)
                archive = home / "cache" / f"{font['id']}-{font['version']}.zip"
                archive.parent.mkdir()
                with ZipFile(archive, "w") as bundle:
                    for source in font["files"]:
                        bundle.writestr(source, source.encode())
                command, prepared = tex.prepare(home)
                self.assertEqual(prepared, root)
                self.assertEqual(installed.stat().st_mtime_ns, modified)
                for source, relative in font["files"].items():
                    self.assertEqual((root / "texmf-local" / relative).read_bytes(), source.encode())
                commands = [call.args[0] for call in run.call_args_list]
                self.assertNotIn("fandol", next(command for command in commands if "ctex" in command))
                self.assertTrue(any(Path(command[0]).stem == "mktexlsr" for command in commands))
                self.assertEqual(json.loads((root / "seedenv-prepared.json").read_text())["fonts"], spec["fonts"])
                run.reset_mock()
                self.assertEqual(tex.prepare(home, offline=True), (command, root))
                run.assert_not_called()

    def test_incomplete_font_archive_does_not_publish_a_ready_environment(self):
        with tempfile.TemporaryDirectory(prefix="seedenv fonts ") as temporary:
            home = Path(temporary)
            font = tex.recipe()["fonts"][0]
            archive = home / f"{font['id']}-{font['version']}.zip"
            with ZipFile(archive, "w") as bundle:
                bundle.writestr("fandol/README", "font package")
            with patch.object(tex, "run") as run:
                with self.assertRaisesRegex(RuntimeError, "Cannot install fandol fonts"):
                    tex._install_fonts(home / "tex", home, [font], home / "bin", {}, None)
                run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
