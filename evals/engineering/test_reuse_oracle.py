"""Check that the standalone reuse oracle distinguishes plausible integrations."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent


class ReuseOracleTest(unittest.TestCase):
    def run_candidate(self, actions):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            shutil.copytree(HERE / "fixtures" / "reuse", root, dirs_exist_ok=True)
            api = root / "api.py"
            api.write_text(api.read_text().replace('    if action == "show":', actions + '    if action == "show":'))
            result = subprocess.run([sys.executable, str(HERE / "oracle.py"), str(root), "reuse"], capture_output=True, text=True, timeout=15)
            return result.returncode, json.loads(result.stdout)

    def test_existing_owner_integration_passes(self):
        code, outcomes = self.run_candidate('    if action == "pause": return service.hold(key)\n    if action == "resume": return service.release(key)\n')
        self.assertEqual(0, code, outcomes)
        self.assertEqual(4, len(outcomes))

    def test_missing_actions_are_errors_not_assertion_failures(self):
        code, outcomes = self.run_candidate("")
        self.assertNotEqual(0, code)
        self.assertTrue(all(item["status"] == "error" for item in outcomes))

    def test_noop_pause_cannot_pass(self):
        code, outcomes = self.run_candidate('    if action == "pause": return None\n    if action == "resume": return service.release(key)\n')
        self.assertNotEqual(0, code)
        self.assertEqual("fail", outcomes[0]["status"])

    def test_bypassed_domain_guard_cannot_pass(self):
        code, outcomes = self.run_candidate('    if action == "pause": return service.store.suspend(key, True)\n    if action == "resume": return service.store.suspend(key, False)\n')
        self.assertNotEqual(0, code)
        self.assertEqual("fail", outcomes[-1]["status"])


if __name__ == "__main__":
    unittest.main()
