"""Contract tests for configuration, isolated records and read-only readiness."""
from pathlib import Path
import json
import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills/alarina/scripts"))
from project_context import ContextError, doctor, load_context, resolve_destination


class ProjectContextTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.home = self.base / "home"
        self.root = self.base / "first/service"
        self.root.mkdir(parents=True)
        self.home.mkdir()

    def config(self, value, path=None):
        path = path or self.root / ".alarina.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value))

    def context(self, task="feature"):
        return load_context(self.root, task, home=self.home)

    def git(self, *args, root=None):
        return subprocess.run(["git", "-C", str(root or self.root), *args],
                              check=True, text=True, capture_output=True).stdout.strip()

    def init_repo(self, root=None):
        root = root or self.root
        self.git("init", "-q", root=root)
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                 "commit", "--allow-empty", "-qm", "fixture", root=root)

    def test_no_configuration_writes_and_default_artifact_is_task_scoped(self):
        ctx = self.context()
        self.assertIn("/projects/", ctx["locations"]["task_root"])
        self.assertIn("/worktrees/", ctx["locations"]["task_root"])
        self.assertEqual(Path(ctx["locations"]["doc_root"]).parent, Path(ctx["locations"]["task_root"]))
        self.assertEqual(ctx, self.context())
        self.assertFalse((self.home / ".qp").exists())
        self.assertEqual(list(self.root.iterdir()), [])

    def test_different_projects_with_same_basename_do_not_collide(self):
        other = self.base / "second/service"
        other.mkdir(parents=True)
        first = self.context()
        second = load_context(other, "feature", home=self.home)
        self.assertNotEqual(first["project"]["id"], second["project"]["id"])
        self.assertNotEqual(first["locations"]["doc_root"], second["locations"]["doc_root"])

    def test_worktrees_share_project_namespace_but_not_task_state(self):
        self.init_repo()
        other = self.base / "linked"
        self.git("worktree", "add", "--detach", str(other))
        one, two = self.context(), load_context(other, "feature", home=self.home)
        self.assertEqual(one["project"]["id"], two["project"]["id"])
        self.assertEqual(one["locations"]["project_workflows"], two["locations"]["project_workflows"])
        self.assertNotEqual(one["locations"]["task_root"], two["locations"]["task_root"])

    def test_distinct_task_identity_and_safe_components(self):
        one, two = self.context("first/../../case"), self.context("first-case")
        self.assertNotEqual(one["locations"]["task_root"], two["locations"]["task_root"])
        self.assertTrue(Path(one["locations"]["task_root"]).is_relative_to(self.home))

    def test_explicit_and_established_destinations_override_fallback(self):
        self.config({"version": 1, "doc_root": "docs/reports"})
        ctx = self.context()
        explicit = self.base / "requested/report.html"
        chosen = resolve_destination(ctx, kind="artifact", name="ignored.html", destination=str(explicit))
        self.assertEqual(chosen["path"], str(explicit))
        owner = resolve_destination(ctx, kind="artifact", name="new.html", established_root="existing/reports")
        self.assertEqual(owner["path"], str(self.root / "existing/reports/new.html"))
        configured = resolve_destination(ctx, kind="artifact", name="report.html")
        self.assertEqual(configured["path"], str(self.root / "docs/reports/report.html"))
        self.assertFalse(explicit.exists())

    def test_personal_and_local_settings_never_override_team_gates(self):
        global_path = self.home / ".qp/alarina/config.json"
        self.config({"version": 1, "state_root": "~/custom", "contribution_suggestions": False}, global_path)
        self.config({"version": 1, "doc_root": "docs"})
        self.config({"version": 1, "state_root": str(self.base / "private")}, self.root / ".alarina.local.json")
        ctx = self.context()
        self.assertEqual(ctx["locations"]["state_root"], str(self.base / "private"))
        self.assertFalse(ctx["config"]["contribution_suggestions"])
        self.assertEqual(ctx["config_sources"]["doc_root"], str(self.root / ".alarina.json"))
        self.config({"version": 1, "checks": []}, self.root / ".alarina.local.json")
        with self.assertRaisesRegex(ContextError, "unsupported"):
            self.context()

    def test_invalid_config_never_silently_falls_back(self):
        for value in ("../outside", ".", "/tmp/reports", ".git/notes"):
            with self.subTest(value=value):
                self.config({"version": 1, "doc_root": value})
                with self.assertRaises(ContextError):
                    self.context()
        self.config({"version": 1, "models": {"worker": "example"}})
        with self.assertRaisesRegex(ContextError, "unsupported"):
            self.context()

    def test_duplicate_keys_and_bad_versions_rejected(self):
        (self.root / ".alarina.json").write_text('{"version":1,"doc_root":"docs","doc_root":"other"}')
        with self.assertRaisesRegex(ContextError, "duplicate"):
            self.context()
        for version in (True, 2, "1"):
            self.config({"version": version})
            with self.assertRaisesRegex(ContextError, "version"):
                self.context()

    def test_symlink_cannot_escape_configured_root_or_merge_private_projects(self):
        outside = self.base / "outside"
        outside.mkdir()
        (self.root / "docs").symlink_to(outside, target_is_directory=True)
        self.config({"version": 1, "doc_root": "docs/reports"})
        with self.assertRaises(ContextError):
            self.context()
        (self.root / ".alarina.json").unlink()
        ctx = self.context()
        project_state = Path(ctx["locations"]["project_state"])
        project_state.parent.mkdir(parents=True)
        project_state.symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ContextError, "symlink"):
            self.context()

    def test_task_required_for_default_records_but_not_explicit_owner(self):
        ctx = self.context(None)
        with self.assertRaisesRegex(ContextError, "--task"):
            resolve_destination(ctx, kind="record", name="plan.md")
        self.assertEqual(resolve_destination(ctx, kind="record", destination="existing/plan.md")["path"],
                         str(self.root / "existing/plan.md"))

    def test_doctor_reports_gaps_without_running_discovered_scripts(self):
        marker = self.root / "ran"
        check = {"id": "check", "argv": [sys.executable, "-c", f"open({str(marker)!r},'w').close()"], "proof": {"type": "exit"}}
        self.config({"version": 1, "checks": [check], "required_tools": ["alarina-fixture-missing-executable"]})
        result = doctor(self.context())
        self.assertEqual(result["status"], "gaps")
        self.assertFalse(result["executed"])
        self.assertFalse(marker.exists())
        self.assertIn("required_tool", [gap["kind"] for gap in result["gaps"]])

    def test_missing_local_gate_advisory_is_explicit(self):
        result = doctor(self.context())
        self.assertEqual(result["status"], "gaps")
        self.assertIn("advise the user", result["gaps"][0]["message"])
        self.assertIn("CI", result["gaps"][0]["message"])

    def test_doctor_does_not_inspect_package_symlink_outside_project(self):
        outside = self.base / "outside-package.json"
        outside.write_text(json.dumps({"scripts": {"test:outside": "echo outside"}}))
        (self.root / "package.json").symlink_to(outside)
        result = doctor(self.context())
        self.assertEqual(result["unverified_suggestions"], [])
        self.assertTrue(any(gap["kind"] == "discovery" for gap in result["gaps"]))

    def test_command_needs_explicit_proof_contract(self):
        self.config({"version": 1, "checks": [{"id": "test", "argv": ["python3", "-m", "unittest"]}]})
        with self.assertRaisesRegex(ContextError, "proof"):
            self.context()

    def test_empty_explicit_destination_does_not_redirect(self):
        for argument in ("destination", "established_root", "name"):
            with self.subTest(argument=argument), self.assertRaises(ContextError):
                resolve_destination(self.context(), kind="artifact", **{argument: ""})

    def test_loaded_mutable_values_cannot_change_other_project_defaults(self):
        one = self.context()
        one["config"]["required_tools"].append("not-a-real-required-tool")
        one["config"]["checks"].append({"id": "unexpected"})
        self.assertEqual(self.context()["config"]["required_tools"], [])
        self.assertEqual(self.context()["config"]["checks"], [])
        self.assertFalse(self.context()["config"]["contribution_suggestions"])


if __name__ == "__main__":
    unittest.main()
