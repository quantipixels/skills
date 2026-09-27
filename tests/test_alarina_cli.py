"""Exercise the assembled CLI against real disposable projects and commands."""
from contextlib import redirect_stdout, redirect_stderr
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills/alarina/scripts"))
import alarina
from project_context import load_context


class AlarinaCLITests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.project = self.base / "project"
        self.project.mkdir()
        self.home = self.base / "user"
        self.home.mkdir()
        (self.project / ".gitignore").write_text("__pycache__/\n")
        (self.project / "test_behavior.py").write_text(
            "import unittest\nclass Behavior(unittest.TestCase):\n"
            "    def test_real_boundary(self):\n        self.assertEqual('sample'.upper(), 'SAMPLE')\n")
        self.configure([{"id": "unit", "argv": [sys.executable, "-B", "-m", "unittest", "discover"],
                         "proof": {"type": "unittest"}}])
        self.git("init", "-q")
        self.git("add", ".")
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                 "commit", "-qm", "fixture")

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.project), *args], check=True,
                              capture_output=True, text=True).stdout.strip()

    def configure(self, checks, **settings):
        (self.project / ".alarina.json").write_text(json.dumps({"version": 1, "checks": checks, **settings}))

    def invoke(self, operation, *args):
        stdout, stderr = io.StringIO(), io.StringIO()
        context = lambda project, task=None: load_context(project, task, home=self.home)
        with patch.object(alarina, "load_context", side_effect=context), redirect_stdout(stdout), redirect_stderr(stderr):
            code = alarina.main([operation, "--project", str(self.project), *map(str, args)])
        return code, json.loads(stdout.getvalue() or stderr.getvalue())

    def test_real_run_then_freshness_then_changed_candidate(self):
        output = self.base / "run"
        code, result = self.invoke("verify", "--output", output, "--base", "HEAD")
        self.assertEqual(code, 0, result)
        self.assertEqual(result["gate_status"], "passed")
        self.assertEqual(result["checks"][0]["observed_counts"]["passed"], 1)
        self.assertNotIn("files", result["snapshot_after"])
        receipt = json.loads((output / "receipt.json").read_text())
        self.assertIn("files", receipt["snapshot_after"])
        self.assertEqual(receipt["selection"]["executed_ids"], ["unit"])
        self.assertEqual(self.invoke("freshness", output / "receipt.json")[0], 0)
        (self.project / "changed.txt").write_text("new candidate")
        code, stale = self.invoke("freshness", output / "receipt.json")
        self.assertEqual(code, 1)
        self.assertFalse(stale["fresh"])

    def test_subset_receipt_keeps_omitted_checks_visible(self):
        checks = json.loads((self.project / ".alarina.json").read_text())["checks"]
        checks.append({"id": "build", "argv": [sys.executable, "-c", "raise SystemExit(1)"], "proof": {"type": "exit"}})
        self.configure(checks, remote_checks=["Preview smoke check"])
        output = self.base / "subset"
        code, result = self.invoke("verify", "--output", output, "--check", "unit")
        self.assertEqual(code, 0, result)
        self.assertEqual(result["gate_status"], "partial")
        self.assertEqual(result["selected_status"], "passed")
        receipt = json.loads((output / "receipt.json").read_text())
        self.assertEqual(receipt["selection"]["not_selected"], ["build"])
        self.assertEqual(receipt["remote_checks"], ["Preview smoke check"])
        code, freshness = self.invoke("freshness", output / "receipt.json")
        self.assertEqual(code, 0)
        self.assertEqual(freshness["gate_status"], "partial")
        failed_code, failed = self.invoke("verify", "--output", self.base / "failed-subset", "--check", "build")
        self.assertEqual(failed_code, 1)
        self.assertEqual(failed["gate_status"], "failed")

    def test_changed_personal_configuration_invalidates_run(self):
        personal = self.home / ".qp/alarina/config.json"
        personal.parent.mkdir(parents=True)
        personal.write_text('{"version":1,"contribution_suggestions":false}')
        script = f"from pathlib import Path; Path({str(personal)!r}).write_text('{{\"version\":1,\"contribution_suggestions\":true}}')"
        self.configure([{"id": "change-config", "argv": [sys.executable, "-c", script], "proof": {"type": "exit"}}])
        output = self.base / "changed-config"
        code, result = self.invoke("verify", "--output", output)
        self.assertEqual(code, 1)
        self.assertEqual(result["gate_status"], "stale")
        self.assertIn("configuration changed", result["config_error"])
        self.assertEqual(json.loads((output / "receipt.json").read_text())["gate_status"], "stale")

    def test_doctor_is_read_only_and_never_claims_test_execution(self):
        before = list(self.home.rglob("*"))
        code, result = self.invoke("doctor")
        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "configured")
        self.assertFalse(result["executed"])
        self.assertEqual(list(self.home.rglob("*")), before)

    def test_invalid_selection_does_not_create_output(self):
        output = self.base / "unknown"
        code, result = self.invoke("verify", "--output", output, "--check", "not-registered")
        self.assertEqual(code, 2)
        self.assertFalse(output.exists())

    def test_default_verify_uses_task_records_and_does_not_overwrite(self):
        code, result = self.invoke("verify", "--task", "same-task")
        self.assertEqual(code, 0, result)
        first = Path(result["receipt_path"])
        self.assertTrue(first.is_relative_to(self.home / ".qp/alarina/projects"))
        code, again = self.invoke("verify", "--task", "same-task")
        self.assertEqual(code, 0, again)
        self.assertNotEqual(result["receipt_path"], again["receipt_path"])
        self.assertTrue(first.is_file())

    def test_default_verify_rejects_symlinked_checks_parent(self):
        context = load_context(self.project, "same-task", home=self.home)
        task_root = Path(context["locations"]["task_root"])
        task_root.mkdir(parents=True)
        outside = self.base / "outside"
        outside.mkdir()
        (task_root / "checks").symlink_to(outside, target_is_directory=True)
        code, result = self.invoke("verify", "--task", "same-task")
        self.assertEqual(code, 2)
        self.assertIn("symlink parent", result["error"])
        self.assertEqual(list(outside.iterdir()), [])

    def test_unavailable_optional_workflow_roots_are_not_an_error(self):
        code, result = self.invoke("workflows")
        self.assertEqual(code, 0)
        self.assertEqual(result["workflows"], [])
        self.assertEqual(len(result["absent_optional_roots"]), 2)

    def test_default_workflow_inventory_rejects_misfiled_scope(self):
        context = load_context(self.project, home=self.home)
        recipe = {"version": 1, "id": "fixture", "title": "Fixture", "status": "draft",
                  "assumptions": ["fixture only"], "steps": [{"method": "alaga-deliver"}],
                  "evidence": [], "retirement": ""}
        for key, wrong_scope, correct_scope in (
            ("portable_workflows", "project", "portable"),
            ("project_workflows", "portable", "project"),
        ):
            with self.subTest(library=key):
                root = Path(context["locations"][key])
                root.mkdir(parents=True)
                path = root / "fixture.md"
                def write(scope):
                    path.write_text("```alarina-workflow+json\n" + json.dumps({**recipe, "scope": scope}) + "\n```\n")
                write(wrong_scope)
                code, result = self.invoke("workflows")
                self.assertEqual(code, 1, result)
                self.assertFalse(result["workflows"][0]["usable_as_guidance"])
                self.assertIsNone(result["workflows"][0]["metadata"])
                self.assertEqual(result["workflows"][0]["errors"][0]["code"], "library-scope")
                write(correct_scope)
                self.assertEqual(self.invoke("workflows")[0], 0)
                path.unlink()


if __name__ == "__main__":
    unittest.main()
