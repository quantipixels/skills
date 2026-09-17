import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest


MODULE = Path(__file__).with_name("verify_native_install.py")
SPEC = importlib.util.spec_from_file_location("verify_native_install", MODULE)
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class NativeInstallVerifierTest(unittest.TestCase):
    def test_bad_command_and_timeout_are_truthful(self):
        with self.assertRaisesRegex(verify.NativeVerificationError, "could not start"):
            verify.run(["qp-command-that-does-not-exist"], {})
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
        with tempfile.TemporaryDirectory() as temporary:
            installed = Path(temporary)
            for relative in (".codex-plugin/plugin.json", "skills/alarina/SKILL.md"):
                target = installed / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(verify.ROOT / relative, target)
            (installed / "skills/alarina/SKILL.md").write_text("tampered\n")
            with self.assertRaisesRegex(verify.NativeVerificationError, "differs from source"):
                verify.sample_files(installed, ".codex-plugin/plugin.json")


if __name__ == "__main__":
    unittest.main()
