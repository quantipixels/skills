import importlib.util
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "skills/alarina/scripts/installation_diagnostics.py"
spec = importlib.util.spec_from_file_location("installation_diagnostics", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.installed = self.root / "installed"
        for root in (self.source, self.installed):
            skill = root / "skills/alarina"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text("same", encoding="utf-8")
            (root / "package.json").write_text('{"name":"qp-skills","version":"1.0.0"}', encoding="utf-8")

    def test_equal_files_do_not_claim_activation(self):
        result = module.diagnose(self.source, self.installed)
        self.assertEqual(result["files"]["status"], "match")
        self.assertEqual(result["activation"], "unknown")
        self.assertEqual(result["session"]["status"], "unknown")

    def test_drift_and_stale_success_record(self):
        path = self.installed / "skills/alarina/SKILL.md"
        data = {"reads": [{"path": str(path), "sha256": "0" * 64, "version": "1.0.0", "success": True}]}
        result = module.diagnose(self.source, self.installed, session=data)
        self.assertEqual(result["session"]["status"], "stale")
        path.write_text("changed", encoding="utf-8")
        result = module.diagnose(self.source, self.installed)
        self.assertEqual(result["files"]["changed"], ["skills/alarina/SKILL.md"])

    def test_supplied_manager_and_read_record_stay_labeled(self):
        path = self.installed / "skills/alarina/SKILL.md"
        digest = module._inventory(self.installed)["skills/alarina/SKILL.md"]
        manager = {"host": "codex", "plugins": [{"id": "qp-skills", "installedPath": str(self.installed), "enabled": True}]}
        session = {"reads": [{"path": str(path), "sha256": digest, "version": "1.0.0", "success": True}]}
        result = module.diagnose(self.source, self.installed, manager=manager, session=session)
        self.assertEqual(result["manager"]["status"], "reported-enabled")
        self.assertEqual(result["session"]["status"], "supplied-current-read-records")
        self.assertEqual(result["activation"], "unknown")

    def test_symlink_escape_is_rejected(self):
        (self.installed / "skills/alarina/SKILL.md").unlink()
        (self.installed / "skills/alarina/SKILL.md").symlink_to(self.source / "skills/alarina/SKILL.md")
        with self.assertRaises(module.DiagnosticError):
            module.diagnose(self.source, self.installed)

    def test_oversized_input_is_rejected(self):
        path = self.root / "evidence.json"
        path.write_bytes(b"x" * (module.MAX_JSON + 1))
        with self.assertRaises(module.DiagnosticError):
            module._json_file(path)

    def test_version_mismatch_marks_read_record_stale(self):
        path = self.installed / "skills/alarina/SKILL.md"
        digest = module._inventory(self.installed)["skills/alarina/SKILL.md"]
        result = module.diagnose(self.source, self.installed, session={"reads": [
            {"path": str(path), "sha256": digest, "version": "0.9.0", "success": True}]})
        self.assertEqual(result["session"]["status"], "stale")

    def test_package_cache_noise_is_excluded(self):
        cache = self.installed / "skills/alarina/scripts/__pycache__"
        cache.mkdir(parents=True)
        (cache / "module.pyc").write_bytes(b"cache")
        self.assertEqual(module.diagnose(self.source, self.installed)["files"]["status"], "match")

    def test_linked_root_is_rejected(self):
        alias = self.root / "alias"
        alias.symlink_to(self.installed, target_is_directory=True)
        with self.assertRaises(module.DiagnosticError):
            module.diagnose(self.source, alias)

    def test_cli_flags_stale_session_even_when_files_match(self):
        path = self.root / "session.json"
        path.write_text(json.dumps({"reads": [{"path": str(self.installed / "skills/alarina/SKILL.md"),
                                               "sha256": "0" * 64, "version": "1.0.0", "success": True}]}),
                        encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()):
            code = module.main(["--source-root", str(self.source), "--installed-root", str(self.installed),
                                "--session-json", str(path)])
        self.assertEqual(code, 1)


if __name__ == "__main__":
    unittest.main()
