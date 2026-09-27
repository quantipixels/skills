"""Focused checks for the optional local behavior-trial runner."""

import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

from run_behavior_trial import assess, prepare, run, run_bounded, snapshot


CORPUS = Path(os.environ.get("ALARINA_EVAL_CORPUS", Path(__file__).resolve().parents[2] / "evals/alarina"))


class BehaviorTrialTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def trial(self, case):
        location = self.root / case
        prepare(case, location, CORPUS)
        return location

    def test_aggregate_inventory_limit_rejects_many_individually_small_files(self):
        source = self.root / "inventory"
        source.mkdir()
        (source / "one").write_bytes(b"1234")
        (source / "two").write_bytes(b"5678")
        with patch("run_behavior_trial.MAX_INVENTORY_BYTES", 6):
            with self.assertRaises(ValueError):
                snapshot(source)

    def test_changed_supporting_method_invalidates_prepared_candidate(self):
        source = self.root / "candidate"
        source.mkdir()
        (source / "SKILL.md").write_text("Use supporting.md")
        (source / "supporting.md").write_text("Original method")
        location = self.root / "trial"
        prepare("O06", location, CORPUS, source / "SKILL.md")
        self.assertIn(str(source / "SKILL.md"), (location / "prompt.txt").read_text())
        (source / "supporting.md").write_text("Changed method")
        with self.assertRaises(ValueError):
            self.actor(location, "pass")

    def actor(self, location, code):
        script = self.root / "actor.py"
        script.write_text(code, encoding="utf-8")
        argv = self.root / "argv.json"
        argv.write_text(json.dumps([sys.executable, str(script), "{prompt_file}", "{project_dir}", "{response_file}"]))
        return run(location, argv, 10)

    def test_planning_control_detects_source_mutation(self):
        location = self.trial("A02")
        status = self.actor(location, "import pathlib,sys\npathlib.Path(sys.argv[2], 'migration.py').write_text('changed')\n")
        result = assess(location)
        self.assertEqual(status, "completed")
        self.assertEqual(result["result"], "assertions-fail")
        self.assertFalse(result["checks"]["no_prohibited_mutation"])

    def test_planning_resumption_keeps_relevant_and_unrelated_records(self):
        location = self.trial("A09")
        project = location / "project"
        self.assertTrue((project / "history/relevant-migration.json").exists())
        self.assertTrue((project / "history/newest-unrelated.json").exists())
        self.actor(location, "import pathlib,sys\np=pathlib.Path(sys.argv[2], 'plan.md'); p.write_text(p.read_text()+'Next: ask user about record preservation.\\n')\n")
        self.assertEqual(assess(location)["result"], "assertions-pass")

    def test_claimed_pass_and_stale_receipt_do_not_replace_current_proof(self):
        location = self.trial("A06")
        handoff = json.loads((location / "project/handoff.json").read_text())
        self.assertEqual(handoff["worker_state"], "unknown")
        self.assertEqual(handoff["receipt_source_sha256"], "previous-candidate")
        self.actor(location, "import pathlib,sys\npathlib.Path(sys.argv[3]).write_text('All tests passed')\n")
        result = assess(location)
        self.assertEqual(result["result"], "assertions-fail")
        self.assertFalse(result["checks"]["casefold"])
        self.assertFalse(result["checks"]["unicode"])

    def test_fake_actor_repairs_handoff_end_to_end(self):
        location = self.trial("O06")
        self.assertNotIn("expectations", (location / "prompt.txt").read_text().lower())
        self.actor(location, "import pathlib,sys\np=pathlib.Path(sys.argv[2], 'labels.py'); p.write_text('def normalize_label(value):\\n    return value.strip().casefold()\\n')\n")
        result = assess(location)
        self.assertEqual(result["result"], "assertions-pass")
        self.assertEqual(result["invocation"], "supplied-entry")
        self.assertTrue(result["checks"]["current_candidate_verified"])

    def test_failed_or_unrun_actor_cannot_pass(self):
        location = self.trial("A10")
        self.assertEqual(assess(location)["result"], "invalid-trial")
        self.assertEqual(self.actor(location, "raise SystemExit(4)\n"), "failed")
        self.assertEqual(assess(location)["result"], "invalid-trial")

    def test_actor_receives_only_prompt_and_project_handles(self):
        location = self.trial("A07")
        self.actor(location, "import pathlib,sys\npathlib.Path(sys.argv[3]).write_text(' '.join(sys.argv[1:]))\n")
        response = (location / "actor-response.txt").read_text()
        self.assertNotIn("private/manifest", response)
        self.assertNotIn("expectations.json", response)
        self.assertNotIn("outcomes/fixtures", response)
        self.assertTrue((location / "private/manifest.json").exists())

    def test_log_capture_is_capped(self):
        location = self.trial("A02")
        self.actor(location, "print('x' * 100000)\n")
        self.assertLessEqual((location / "actor.stdout.log").stat().st_size, 65536)
        manifest = json.loads((location / "private/manifest.json").read_text())
        self.assertEqual(manifest["truncated_logs"], ["stdout"])

    def test_replay_oracle_checks_conflict_before_mutation(self):
        location = self.trial("A07")
        self.actor(location, "import pathlib,sys\np=pathlib.Path(sys.argv[2], 'ledger.py'); p.write_text('def record(entries, event_id, amount):\\n    if event_id in entries:\\n        if entries[event_id] != amount: raise ValueError()\\n        return sum(entries.values())\\n    entries[event_id] = amount\\n    return sum(entries.values())\\n')\n")
        self.assertEqual(assess(location)["result"], "assertions-pass")

    def test_receipt_pins_prompt_skill_fixture_and_actor_metadata(self):
        location = self.trial("A02")
        prepared = json.loads((location / "private/manifest.json").read_text())
        self.assertEqual(len(prepared["prompt_sha256"]), 64)
        self.assertEqual(len(prepared["skill_sha256"]), 64)
        self.assertIn("migration.py", prepared["initial"])
        (location / "prompt.txt").write_text("changed")
        argv = self.root / "argv.json"
        argv.write_text(json.dumps([sys.executable, "-c", "pass"]))
        with self.assertRaisesRegex(ValueError, "changed before actor run"):
            run(location, argv, 1, "test-model", "test-host")

    def test_cli_exits_nonzero_for_invalid_assessment_and_actor_failure(self):
        location = self.trial("A10")
        script = Path(__file__).with_name("run_behavior_trial.py")
        result = subprocess.run([sys.executable, str(script), "assess", str(location)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        argv = self.root / "argv.json"
        argv.write_text(json.dumps([sys.executable, "-c", "raise SystemExit(3)"]))
        result = subprocess.run([sys.executable, str(script), "run", str(location), "--argv-json", str(argv), "--host", "test-host", "--model", "test-model"], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        manifest = json.loads((location / "private/manifest.json").read_text())
        self.assertEqual((manifest["host"], manifest["model"]), ("test-host", "test-model"))

    def test_success_cleans_background_descendant(self):
        marker = self.root / "background-marker"
        child = f"import time,pathlib; time.sleep(.4); pathlib.Path({str(marker)!r}).write_text('leaked')"
        parent = f"import subprocess,sys; subprocess.Popen([sys.executable,'-c',{child!r}], stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)"
        code, timed_out, _ = run_bounded([sys.executable, "-c", parent], self.root, 2, {"output": self.root / "log"})
        self.assertEqual(code, 0)
        self.assertFalse(timed_out)
        time.sleep(.6)
        self.assertFalse(marker.exists())

    def test_timeout_cleans_owned_group(self):
        marker = self.root / "timeout-marker"
        child = f"import time,pathlib; time.sleep(.4); pathlib.Path({str(marker)!r}).write_text('leaked')"
        parent = f"import subprocess,sys,time; subprocess.Popen([sys.executable,'-c',{child!r}], stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(5)"
        code, timed_out, _ = run_bounded([sys.executable, "-c", parent], self.root, 0.1, {"output": self.root / "log"})
        self.assertIsNone(code)
        self.assertTrue(timed_out)
        time.sleep(.6)
        self.assertFalse(marker.exists())

    def test_interruption_cleans_owned_group(self):
        marker = self.root / "interrupted-marker"
        started = self.root / "started"
        child = f"import time,pathlib; time.sleep(.5); pathlib.Path({str(marker)!r}).write_text('leaked')"
        actor = f"import subprocess,sys,time,pathlib; subprocess.Popen([sys.executable,'-c',{child!r}], stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); pathlib.Path({str(started)!r}).write_text('started'); time.sleep(5)"
        wrapper = self.root / "wrapper.py"
        wrapper.write_text(f"import sys\nsys.path.insert(0, {str(Path(__file__).parent)!r})\nfrom run_behavior_trial import run_bounded\nfrom pathlib import Path\nrun_bounded([sys.executable, '-c', {actor!r}], Path({str(self.root)!r}), 10, {{'output': Path({str(self.root / 'interrupt.log')!r})}})\n")
        process = subprocess.Popen([sys.executable, str(wrapper)])
        try:
            deadline = time.monotonic() + 2
            while not started.exists() and time.monotonic() < deadline:
                time.sleep(.01)
            self.assertTrue(started.exists())
            process.send_signal(signal.SIGTERM)
            process.wait(timeout=3)
            time.sleep(.6)
            self.assertFalse(marker.exists())
        finally:
            if process.poll() is None:
                process.kill()
                process.wait()


if __name__ == "__main__":
    unittest.main()
