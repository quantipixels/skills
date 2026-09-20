import contextlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
from unittest.mock import patch
import tempfile
import unittest


MODULE = Path(__file__).with_name("verify_native_install.py")
SPEC = importlib.util.spec_from_file_location("verify_native_install", MODULE)
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


def bundle(root, extra=None):
    """Small real files; these fixtures do not simulate a native manager."""
    files = {
        ".codex-plugin/plugin.json": '{"name": "qp-skills"}\n',
        ".claude-plugin/plugin.json": '{"name": "qp-skills"}\n',
        "skills/alarina/SKILL.md": "---\nname: alarina\n---\nConductor.\n",
        "skills/qp-update/SKILL.md": "---\nname: qp-update\n---\nUpdater B.\n",
        "skills/qp-update/references/lifecycle.md": "Lifecycle B.\n",
        "agents/alarina.md": "Conductor agent.\n",
    }
    if extra:
        files[f"skills/{extra}/SKILL.md"] = f"---\nname: {extra}\n---\nFixture.\n"
    for relative, content in files.items():
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)
    return root


class NativeInstallVerifierTest(unittest.TestCase):
    def test_bad_command_and_timeout_are_truthful(self):
        with self.assertRaisesRegex(verify.NativeVerificationError, "could not start"):
            verify.run(["qp-command-that-does-not-exist"], {})
        with self.assertRaisesRegex(verify.NativeVerificationError, r"command failed \(3\)"):
            verify.run(["python3", "-c", "import sys; sys.exit(3)"], {})
        with self.assertRaisesRegex(verify.NativeVerificationError, "timed out"):
            verify.run(["python3", "-c", "import time; time.sleep(30)"], {}, timeout=0.05)

    def test_bad_json_and_shape_fail_before_install_claim(self):
        with self.assertRaisesRegex(verify.NativeVerificationError, "did not return JSON"):
            verify.load_json("not-json", "fake command")
        with self.assertRaisesRegex(verify.NativeVerificationError, "expected an object"):
            verify.require_mapping([], "fake command")
        with self.assertRaisesRegex(verify.NativeVerificationError, "manifest object"):
            verify.validate_claude_validation({"success": True, "manifest": None})

    def test_missing_disabled_and_mismatch_are_rejected(self):
        with self.assertRaisesRegex(verify.NativeVerificationError, "installation path is missing"):
            verify._path_value("/path/that/is/not/installed", "fake install")
        with self.assertRaisesRegex(verify.NativeVerificationError, "disabled"):
            verify.require_enabled_plugin(
                [{"pluginId": verify.PACKAGE_SELECTOR, "enabled": False}], "fake listing"
            )
        with self.assertRaisesRegex(verify.NativeVerificationError, "exactly one"):
            verify.require_enabled_plugin([], "missing listing")
        with self.assertRaisesRegex(verify.NativeVerificationError, "exactly one"):
            verify.require_enabled_plugin(
                [
                    {"pluginId": verify.PACKAGE_SELECTOR, "enabled": True},
                    {"pluginId": verify.PACKAGE_SELECTOR, "enabled": True},
                ],
                "duplicate listing",
            )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = bundle(root / "source")
            installed = root / "installed"
            shutil.copytree(source, installed)
            (installed / "skills/alarina/SKILL.md").write_text("tampered\n")
            with patch.object(verify, "ROOT", source):
                with self.assertRaisesRegex(verify.NativeVerificationError, "differs from source"):
                    verify.sample_files(installed, ".codex-plugin/plugin.json")
                shutil.rmtree(installed / "skills/alarina")
                with self.assertRaisesRegex(verify.NativeVerificationError, "skill inventory differs"):
                    verify.validate_installed_inventory(installed, "codex")

    def test_process_membership_requires_parseable_observation(self):
        for output in ("", "bad records\n", "17 42 extra\n"):
            result = verify.subprocess.CompletedProcess([], 0, output, "")
            with self.subTest(output=output), patch.object(verify.subprocess, "run", return_value=result):
                with self.assertRaises(verify.NativeVerificationError):
                    verify._process_group_members(42)
        result = verify.subprocess.CompletedProcess([], 0, "17 42\n18 43\n", "")
        with patch.object(verify.subprocess, "run", return_value=result):
            self.assertEqual({17}, verify._process_group_members(42))
            self.assertEqual(set(), verify._process_group_members(99))

    def test_permission_probe_does_not_treat_unreadable_group_as_gone(self):
        class ExitedProcess:
            pid = 512

            @staticmethod
            def poll():
                return 0

        with patch.object(verify.os, "killpg", side_effect=PermissionError("probe")), \
                patch.object(verify, "_process_group_members", return_value={903}):
            self.assertTrue(verify._group_exists(ExitedProcess()))
        with patch.object(verify.os, "killpg", side_effect=PermissionError("probe")), \
                patch.object(verify, "_process_group_members", side_effect=verify.NativeVerificationError("unreadable")):
            with self.assertRaises(verify.NativeVerificationError):
                verify._group_exists(ExitedProcess())

    def test_upgrade_snapshot_checks_names_and_updater_without_running_manager(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = bundle(root / "source", "new-skill")
            before = bundle(root / "before", "retired-skill")
            (before / "skills/qp-update/SKILL.md").write_text("Updater A.\n")
            (before / "skills/qp-update/references/lifecycle.md").write_text("Lifecycle A.\n")
            installed = root / "installed"
            shutil.copytree(source, installed)
            before_digest = verify._tree_digest(before)
            with patch.object(verify, "ROOT", source), \
                    patch.object(verify, "run", side_effect=AssertionError("must not run a manager")):
                result = verify.verify_upgrade_snapshot(before, installed, "codex")
            self.assertEqual(["new-skill"], result["added_skills"])
            self.assertEqual(["retired-skill"], result["retired_skills"])
            self.assertEqual(before_digest, verify._tree_digest(before))
            self.assertEqual("snapshot-comparison", result["evidence"])
            self.assertEqual("not_observed", result["manager_transition"])
            self.assertEqual("not_observed", result["session_activation"])
            samples = {item["path"] for item in result["sampled_files"]}
            self.assertIn("skills/qp-update/references/lifecycle.md", samples)
            self.assertEqual(result["source_scope"]["skills"], result["before_scope"]["skills"])

    def test_upgrade_snapshot_rejects_same_count_stale_install(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = bundle(root / "source", "new-skill")
            before = bundle(root / "before", "retired-skill")
            installed = root / "installed"
            shutil.copytree(before, installed)
            with patch.object(verify, "ROOT", source):
                with self.assertRaisesRegex(verify.NativeVerificationError, "skill inventory differs"):
                    verify.verify_upgrade_snapshot(before, installed, "codex")

    def test_upgrade_snapshot_rejects_wrong_content_outside_updater(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = bundle(root / "source", "new-skill")
            before = bundle(root / "before", "retired-skill")
            installed = root / "installed"
            shutil.copytree(source, installed)
            (installed / "skills/new-skill/SKILL.md").write_text("Wrong package content.\n")
            with patch.object(verify, "ROOT", source):
                with self.assertRaisesRegex(verify.NativeVerificationError, "package content differs"):
                    verify.verify_upgrade_snapshot(before, installed, "codex")

    def test_updater_reference_is_checked_when_skill_body_matches(self):
        for mutation in ("stale", "missing", "obsolete"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                source = bundle(root / "source")
                installed = root / "installed"
                shutil.copytree(source, installed)
                reference = installed / "skills/qp-update/references/lifecycle.md"
                if mutation == "stale":
                    reference.write_text("Lifecycle A.\n")
                elif mutation == "missing":
                    reference.unlink()
                else:
                    reference.with_name("obsolete.md").write_text("Old instructions.\n")
                with patch.object(verify, "ROOT", source):
                    with self.assertRaises(verify.NativeVerificationError):
                        verify.sample_files(installed, ".codex-plugin/plugin.json")

    def test_upgrade_snapshot_rejects_missing_or_foreign_baseline(self):
        for mutation in ("missing", "foreign"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                source = bundle(root / "source")
                before = bundle(root / "before")
                installed = root / "installed"
                shutil.copytree(source, installed)
                if mutation == "missing":
                    shutil.rmtree(before / "skills")
                else:
                    (before / ".codex-plugin/plugin.json").write_text('{"name":"other-plugin"}')
                with patch.object(verify, "ROOT", source):
                    with self.assertRaises(verify.NativeVerificationError):
                        verify.verify_upgrade_snapshot(before, installed, "codex")

    def test_upgrade_snapshot_rejects_baseline_alias_and_empty_source(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = bundle(root / "source")
            installed = bundle(root / "installed")
            with patch.object(verify, "ROOT", source):
                with self.assertRaisesRegex(verify.NativeVerificationError, "separate"):
                    verify.verify_upgrade_snapshot(installed, installed, "codex")
            empty = root / "empty"
            empty.mkdir()
            with patch.object(verify, "ROOT", empty):
                with self.assertRaisesRegex(verify.NativeVerificationError, "source inventory"):
                    verify.validate_installed_inventory(empty, "codex")

    def test_snapshot_cli_is_read_only_and_reports_failure(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = bundle(root / "source", "new-skill")
            before = bundle(root / "before", "retired-skill")
            installed = root / "installed"
            shutil.copytree(source, installed)
            arguments = ["--host", "claude", "--before-root", str(before), "--installed-root", str(installed)]
            with patch.object(verify, "ROOT", source), \
                    patch.object(verify, "run", side_effect=AssertionError("must not run a manager")):
                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    self.assertEqual(0, verify.main(arguments))
                result, _ = json.JSONDecoder().raw_decode(output.getvalue())
                self.assertTrue(result["success"])
                self.assertEqual("snapshot-comparison", result["results"][0]["evidence"])
                (installed / "agents/alarina.md").unlink()
                with contextlib.redirect_stdout(io.StringIO()) as output:
                    self.assertEqual(1, verify.main(arguments))
                self.assertFalse(json.loads(output.getvalue())["success"])

    def test_snapshot_cli_requires_both_roots_and_one_host(self):
        for arguments in (
                ["--before-root", "/unused"],
                ["--installed-root", "/unused"],
                ["--before-root", "/unused", "--installed-root", "/unused"],
        ):
            with self.subTest(arguments=arguments), \
                    patch.object(verify, "verify_codex") as codex, \
                    patch.object(verify, "verify_claude") as claude, \
                    contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as error:
                    verify.main(arguments)
                self.assertEqual(2, error.exception.code)
                codex.assert_not_called()
                claude.assert_not_called()


if __name__ == "__main__":
    unittest.main()
