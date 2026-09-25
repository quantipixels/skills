import contextlib
import hashlib
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


def bundle(root, host="codex", version="2.0.0", extra=None):
    files = {
        f".{host}-plugin/plugin.json": json.dumps({"name": "qp-skills", "version": version}),
        "LICENSE": "Fixture license\n",
        "skills/alarina/SKILL.md": "---\nname: alarina\n---\nRoute work.\n",
        "skills/alarina/commands/alaga-deliver.md": "Delivery method.\n",
    }
    if host == "claude":
        files["agents/alarina.md"] = "Conductor agent.\n"
    files.update(extra or {})
    for relative, content in files.items():
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)
    manifest = {"provider": host, "plugin_version": version, "files": [
        {"path": name, "sha256": hashlib.sha256(content.encode()).hexdigest()}
        for name, content in sorted(files.items())
    ]}
    (root / "bundle-manifest.json").write_text(json.dumps(manifest))
    return root


def fixtures(temp, host="codex"):
    repository = temp / "repository"
    source = bundle(repository / "plugins" / host / "qp-skills", host, extra={
        "skills/alarina/commands/alaga-deliver.md": "New delivery method.\n",
        "skills/alarina/references/new.md": "Added reference.\n",
    })
    before = temp / "before"
    legacy = {
        f".{host}-plugin/plugin.json": json.dumps({"name": "qp-skills", "version": "1.0.0"}),
        "skills/alarina/SKILL.md": "Old conductor.\n",
        "skills/qp-update/SKILL.md": "Old updater.\n",
        "skills/qp-update/references/old.md": "Retired reference.\n",
    }
    for relative, content in legacy.items():
        target = before / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)
    installed = temp / "installed"
    shutil.copytree(source, installed)
    return repository, source, before, installed


class NativeInstallVerifierTest(unittest.TestCase):
    def test_bad_command_and_timeout_are_truthful(self):
        with self.assertRaisesRegex(verify.NativeVerificationError, "could not start"):
            verify.run(["qp-command-that-does-not-exist"], {})
        with self.assertRaisesRegex(verify.NativeVerificationError, r"command failed \(3\)"):
            verify.run(["python3", "-c", "import sys; sys.exit(3)"], {})
        with self.assertRaisesRegex(verify.NativeVerificationError, "timed out"):
            verify.run(["python3", "-c", "import time; time.sleep(30)"], {}, timeout=0.05)

    def test_manager_response_validation(self):
        with self.assertRaisesRegex(verify.NativeVerificationError, "did not return JSON"):
            verify.load_json("not-json", "command")
        with self.assertRaisesRegex(verify.NativeVerificationError, "expected an object"):
            verify.require_mapping([], "command")
        with self.assertRaisesRegex(verify.NativeVerificationError, "manifest object"):
            verify.validate_claude_validation({"success": True, "manifest": None})
        with self.assertRaisesRegex(verify.NativeVerificationError, "disabled"):
            verify.require_enabled_plugin([{"pluginId": verify.PACKAGE_SELECTOR, "enabled": False}], "listing")
        with self.assertRaisesRegex(verify.NativeVerificationError, "exactly one"):
            verify.require_enabled_plugin([], "listing")

    def test_process_membership_requires_parseable_observation(self):
        for output in ("", "bad records\n", "17 42 extra\n"):
            result = verify.subprocess.CompletedProcess([], 0, output, "")
            with self.subTest(output=output), patch.object(verify.subprocess, "run", return_value=result):
                with self.assertRaises(verify.NativeVerificationError):
                    verify._process_group_members(42)

    def test_permission_probe_does_not_treat_unreadable_group_as_gone(self):
        class ExitedProcess:
            pid = 512

        with patch.object(verify.os, "killpg", side_effect=PermissionError("probe")), \
                patch.object(verify, "_process_group_members", return_value={903}):
            self.assertTrue(verify._group_exists(ExitedProcess()))

    def test_snapshot_accepts_legacy_baseline_and_reports_file_changes(self):
        with tempfile.TemporaryDirectory() as temporary:
            repository, source, before, installed = fixtures(Path(temporary), "claude")
            before_digest = verify._tree_digest(before)
            with patch.object(verify, "ROOT", repository):
                result = verify.verify_upgrade_snapshot(before, installed, "claude")
            self.assertEqual({"source": "2.0.0", "before": "1.0.0", "installed": "2.0.0"}, result["versions"])
            self.assertIn("skills/alarina/SKILL.md", result["changed_paths"])
            self.assertIn("skills/alarina/references/new.md", result["added_paths"])
            self.assertIn("skills/qp-update/SKILL.md", result["removed_paths"])
            self.assertEqual("snapshot-comparison", result["evidence"])
            self.assertEqual("not_observed", result["manager_transition"])
            self.assertEqual("not_observed", result["session_activation"])
            self.assertEqual(before_digest, verify._tree_digest(before))
            self.assertEqual(len(verify._files(source)), result["verified_file_count"])

    def test_snapshot_rejects_foreign_stale_or_tampered_content(self):
        for mutation in ("foreign", "stale", "tampered", "extra", "missing", "bad_hash"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as temporary:
                repository, source, before, installed = fixtures(Path(temporary))
                if mutation == "foreign":
                    (before / ".codex-plugin/plugin.json").write_text('{"name":"other-plugin","version":"1.0.0"}')
                elif mutation == "stale":
                    shutil.rmtree(installed)
                    shutil.copytree(before, installed)
                elif mutation == "tampered":
                    (installed / "skills/alarina/commands/alaga-deliver.md").write_text("Tampered.\n")
                elif mutation == "extra":
                    (installed / "extra.txt").write_text("Extra.\n")
                elif mutation == "missing":
                    (installed / "skills/alarina/commands/alaga-deliver.md").unlink()
                elif mutation == "bad_hash":
                    (source / "skills/alarina/commands/alaga-deliver.md").write_text("Changed after compilation.\n")
                with patch.object(verify, "ROOT", repository):
                    with self.assertRaises(verify.NativeVerificationError):
                        verify.verify_upgrade_snapshot(before, installed, "codex")

    def test_only_alarina_and_host_agent_are_accepted(self):
        for host in ("codex", "claude"):
            with self.subTest(host=host), tempfile.TemporaryDirectory() as temporary:
                repository, source, before, installed = fixtures(Path(temporary), host)
                with patch.object(verify, "ROOT", repository):
                    verify.validate_installed_inventory(installed, host)
                    unwanted = installed / "skills/other/SKILL.md"
                    unwanted.parent.mkdir(parents=True)
                    unwanted.write_text("---\nname: other\n---\n")
                    with self.assertRaisesRegex(verify.NativeVerificationError, "skill inventory"):
                        verify.validate_installed_inventory(installed, host)
                    unwanted.unlink()
                    agent = installed / "agents/alarina.md"
                    if host == "claude":
                        agent.unlink()
                    else:
                        agent.parent.mkdir(exist_ok=True)
                        agent.write_text("Unexpected native agent.\n")
                    with self.assertRaisesRegex(verify.NativeVerificationError, "agent inventory"):
                        verify.validate_installed_inventory(installed, host)

    def test_snapshot_cli_is_read_only_and_reports_failure(self):
        with tempfile.TemporaryDirectory() as temporary:
            repository, source, before, installed = fixtures(Path(temporary), "claude")
            arguments = ["--host", "claude", "--before-root", str(before), "--installed-root", str(installed)]
            with patch.object(verify, "ROOT", repository):
                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    self.assertEqual(0, verify.main(arguments))
                result, _ = json.JSONDecoder().raw_decode(output.getvalue())
                self.assertTrue(result["success"])
                (installed / "agents/alarina.md").unlink()
                with contextlib.redirect_stdout(io.StringIO()) as output:
                    self.assertEqual(1, verify.main(arguments))
                self.assertFalse(json.loads(output.getvalue())["success"])

    def test_snapshot_cli_requires_both_roots_and_one_host(self):
        for arguments in (["--before-root", "/unused"], ["--installed-root", "/unused"],
                          ["--before-root", "/unused", "--installed-root", "/unused"]):
            with self.subTest(arguments=arguments), contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as error:
                    verify.main(arguments)
                self.assertEqual(2, error.exception.code)


if __name__ == "__main__":
    unittest.main()
