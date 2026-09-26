"""Snapshot comparison and safe staging checks for native installs."""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import tempfile
import time
import unittest
from unittest.mock import patch


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("verifier", HERE / "verify_native_install.py")
verifier = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(verifier)


def write(root: Path, relative: str, content: str) -> None:
    target = root / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content)


class NativeInstallVerifierTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.before = self.root / "before"
        self.installed = self.root / "installed"
        write(self.source, ".codex-plugin/plugin.json", '{"name":"qp-skills","version":"2.0.0"}')
        write(self.source, "skills/alarina/SKILL.md", "New skill.\n")
        write(self.source, "skills/alarina/commands/alaga-deliver.md", "New method.\n")
        write(self.before, ".codex-plugin/plugin.json", '{"name":"qp-skills","version":"1.0.0"}')
        write(self.before, "skills/alarina/SKILL.md", "Old skill.\n")
        write(self.before, "skills/qp-update/SKILL.md", "Retired skill.\n")
        shutil.copytree(self.source, self.installed)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_snapshot_records_migration_without_claiming_activation(self) -> None:
        result = verifier.verify_upgrade_snapshot(self.before, self.installed, "codex", self.source)
        self.assertEqual({"source": "2.0.0", "before": "1.0.0", "installed": "2.0.0"}, result["versions"])
        self.assertIn("skills/alarina/SKILL.md", result["changed_paths"])
        self.assertIn("skills/qp-update/SKILL.md", result["removed_paths"])
        self.assertEqual("not_observed", result["manager_transition"])
        self.assertEqual("not_observed", result["session_activation"])

    def test_snapshot_rejects_foreign_or_tampered_install(self) -> None:
        write(self.before, ".codex-plugin/plugin.json", '{"name":"foreign","version":"1.0.0"}')
        with self.assertRaisesRegex(verifier.NativeVerificationError, "foreign"):
            verifier.verify_upgrade_snapshot(self.before, self.installed, "codex", self.source)
        write(self.before, ".codex-plugin/plugin.json", '{"name":"qp-skills","version":"1.0.0"}')
        write(self.installed, "skills/alarina/commands/alaga-deliver.md", "Tampered.\n")
        with self.assertRaisesRegex(verifier.NativeVerificationError, "content differs"):
            verifier.verify_upgrade_snapshot(self.before, self.installed, "codex", self.source)

    def test_inventory_rejects_second_discoverable_skill(self) -> None:
        write(self.installed, "skills/other/SKILL.md", "Unexpected.\n")
        with self.assertRaisesRegex(verifier.NativeVerificationError, "inventory"):
            verifier.compare_installed_files(self.installed, self.source)

    def test_stage_exports_only_runtime_surface(self) -> None:
        for relative in verifier.DECLARATIONS:
            write(self.root, relative, "Declaration.\n")
        write(self.root, "skills/alarina/SKILL.md", "Current skill.\n")
        write(self.root, "LICENSE", "Licence.\n")
        write(self.root, "tracked-dev.txt", "Development file.\n")
        write(self.root, ".qp/private.txt", "Private state.\n")
        write(self.root, "node_modules/marker.txt", "Dependency state.\n")
        destination = self.root / "staged"
        with patch.object(verifier, "ROOT", self.root):
            verifier.stage_package(destination)
        self.assertEqual("Current skill.\n", (destination / "skills/alarina/SKILL.md").read_text())
        self.assertFalse((destination / "tracked-dev.txt").exists())
        self.assertFalse((destination / ".qp").exists())
        self.assertFalse((destination / "node_modules").exists())

    def test_run_reports_errors_and_timeout(self) -> None:
        with self.assertRaisesRegex(verifier.NativeVerificationError, "could not start"):
            verifier.run(["qp-command-that-does-not-exist"], {})
        with self.assertRaisesRegex(verifier.NativeVerificationError, "command failed"):
            verifier.run(["python3", "-c", "import sys; sys.exit(3)"], {})
        with self.assertRaisesRegex(verifier.NativeVerificationError, "timed out"):
            verifier.run(["python3", "-c", "import time; time.sleep(30)"], {}, timeout=0.05)

    def test_run_cleans_child_that_keeps_pipes_open(self) -> None:
        command = ["python3", "-c", "import subprocess; subprocess.Popen(['python3','-c','import time;time.sleep(30)'])"]
        started = time.monotonic()
        with self.assertRaisesRegex(verifier.NativeVerificationError, "timed out"):
            verifier.run(command, {}, timeout=0.1)
        self.assertLess(time.monotonic() - started, 3)

    def test_export_cli_writes_new_runtime_package_only(self) -> None:
        for relative in verifier.DECLARATIONS:
            write(self.root, relative, "Declaration.\n")
        write(self.root, "skills/alarina/SKILL.md", "Canonical skill.\n")
        destination = self.root.parent / f"{self.root.name}-export"
        try:
            with patch.object(verifier, "ROOT", self.root), contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(0, verifier.main(["--export", str(destination)]))
            self.assertTrue(json.loads(output.getvalue())["success"])
            self.assertTrue((destination / "skills/alarina/SKILL.md").is_file())
            self.assertFalse((destination / "node_modules").exists())
            with patch.object(verifier, "ROOT", self.root), contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit):
                    verifier.main(["--export", str(destination)])
        finally:
            shutil.rmtree(destination, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
