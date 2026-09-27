"""Behavioral tests for local verification and candidate freshness."""

from __future__ import annotations

import json
import os
from pathlib import Path
import signal
import stat
import subprocess
import sys
import tempfile
import time
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills/alarina/scripts"))
import local_checks

from local_checks import candidate_snapshot, check_freshness, run_checks


def git(project: Path, *args: str) -> str:
    proc = subprocess.run(["git", "-C", str(project), *args], text=True,
                          capture_output=True, check=True)
    return proc.stdout.strip()


class LocalChecksTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.project = self.root / "project"
        self.project.mkdir()
        git(self.project, "init", "-q")
        git(self.project, "config", "user.email", "test@example.invalid")
        git(self.project, "config", "user.name", "Test")
        (self.project / "tracked.txt").write_text("initial\n")
        git(self.project, "add", ".")
        git(self.project, "commit", "-qm", "initial")
        self.base = git(self.project, "rev-parse", "HEAD")

    def output(self, name: str = "run") -> Path:
        return self.root / name

    @staticmethod
    def check(code: str, proof: str = "unittest", *, name: str = "check") -> dict:
        return {"id": name, "argv": [sys.executable, "-c", code],
                "proof": {"type": proof}}

    def test_snapshot_tracks_head_base_index_untracked_content_and_mode(self) -> None:
        first = candidate_snapshot(self.project, "HEAD")
        (self.project / "tracked.txt").write_text("edited\n")
        edited = candidate_snapshot(self.project, "HEAD")
        self.assertNotEqual(first["candidate_digest"], edited["candidate_digest"])
        git(self.project, "add", "tracked.txt")
        staged = candidate_snapshot(self.project, "HEAD")
        self.assertNotEqual(edited["candidate_digest"], staged["candidate_digest"])
        untracked = self.project / "new.txt"
        untracked.write_text("one")
        one = candidate_snapshot(self.project, "HEAD")
        untracked.write_text("two")
        two = candidate_snapshot(self.project, "HEAD")
        self.assertNotEqual(one["candidate_digest"], two["candidate_digest"])
        mode = untracked.stat().st_mode
        untracked.chmod(mode | stat.S_IXUSR)
        changed_mode = candidate_snapshot(self.project, "HEAD")
        self.assertNotEqual(two["candidate_digest"], changed_mode["candidate_digest"])
        git(self.project, "add", ".")
        git(self.project, "commit", "-qm", "change")
        changed_head = candidate_snapshot(self.project, "HEAD")
        self.assertNotEqual(changed_mode["candidate_digest"], changed_head["candidate_digest"])
        self.assertEqual(changed_head["base_oid"], changed_head["head"])
        from_old_base = candidate_snapshot(self.project, self.base)
        self.assertNotEqual(changed_head["candidate_digest"], from_old_base["candidate_digest"])

    def test_tracked_deletion_is_a_complete_candidate_change(self) -> None:
        first = candidate_snapshot(self.project)
        (self.project / "tracked.txt").unlink()
        deleted = candidate_snapshot(self.project)
        self.assertTrue(deleted["complete"])
        self.assertNotEqual(first["candidate_digest"], deleted["candidate_digest"])
        self.assertIn({"path": "tracked.txt", "kind": "deleted"}, deleted["files"])

    def test_tracked_file_below_replaced_symlink_is_incomplete(self) -> None:
        nested = self.project / "nested"
        nested.mkdir()
        (nested / "file.txt").write_text("tracked")
        git(self.project, "add", "nested/file.txt")
        git(self.project, "commit", "-qm", "nested")
        (nested / "file.txt").unlink()
        nested.rmdir()
        outside = self.root / "outside"
        outside.mkdir()
        (outside / "file.txt").write_text("outside content")
        nested.symlink_to(outside, target_is_directory=True)
        snapshot = candidate_snapshot(self.project)
        state = next(item for item in snapshot["files"] if item["path"] == "nested/file.txt")
        self.assertEqual(state["kind"], "unreadable")
        self.assertNotIn("sha256", state)
        self.assertFalse(snapshot["complete"])

    def test_submodule_and_missing_common_identity_are_explicitly_incomplete(self) -> None:
        git(self.project, "update-index", "--add", "--cacheinfo",
            f"160000,{self.base},submod")
        (self.project / "submod").mkdir()
        submodule = candidate_snapshot(self.project)
        self.assertFalse(submodule["complete"])
        self.assertIn("submodule interior is not included", submodule["limitations"])
        original = local_checks._git

        def failed_common(project: Path, *args: str):
            if "--git-common-dir" in args:
                return subprocess.CompletedProcess(["git"], 1, b"", b"error")
            return original(project, *args)

        with mock.patch.object(local_checks, "_git", side_effect=failed_common):
            missing_common = candidate_snapshot(self.project)
        self.assertFalse(missing_common["complete"])
        self.assertIn("common Git directory could not be resolved",
                      missing_common["limitations"])

    def test_receipt_freshness_and_config_digest(self) -> None:
        code = 'print("Ran 1 test in 0.001s\\n\\nOK")'
        receipt = run_checks(self.project, [self.check(code)], self.output(), base=self.base,
                             config_digest="alpha")
        self.assertEqual("passed", receipt["gate_status"])
        self.assertEqual("current", check_freshness(self.project, receipt, "alpha", self.base)["status"])
        self.assertEqual("stale", check_freshness(self.project, receipt, "beta", self.base)["status"])
        (self.project / "new.txt").write_text("new")
        self.assertEqual("stale", check_freshness(self.project, receipt, "alpha", self.base)["status"])
        with self.assertRaises(FileExistsError):
            run_checks(self.project, [], self.output())

    def test_zero_all_skipped_and_failed_test_proof(self) -> None:
        cases = [
            ('print("Ran 0 tests in 0.000s\\n\\nOK")', "unittest"),
            ('print("Ran 1 test in 0.000s\\n\\nOK (skipped=1)")', "unittest"),
            ('print("Ran 2 tests in 0.000s\\n\\nFAILED (failures=1)")', "unittest"),
            ('print("=== 1 skipped in 0.01s ===")', "pytest"),
            ('print("1..1\\nok 1 # SKIP unavailable")', "tap"),
            ('print("1..2\\nok 1\\nnot ok 2")', "tap"),
        ]
        for index, (code, proof) in enumerate(cases):
            with self.subTest(index=index):
                receipt = run_checks(self.project, [self.check(code, proof)],
                                     self.output(f"case-{index}"))
                self.assertEqual("failed", receipt["gate_status"])
                self.assertEqual("failed", receipt["checks"][0]["result"])

    def test_missing_tool_empty_checks_and_exit_only(self) -> None:
        missing = {"id": "missing", "argv": ["nonexistent-alarina-check-tool"],
                   "proof": {"type": "unittest"}}
        self.assertEqual("blocked", run_checks(self.project, [missing],
                                                self.output("missing"))["gate_status"])
        self.assertEqual("incomplete", run_checks(self.project, [],
                                                   self.output("empty"))["gate_status"])
        command = self.check("print('ok')", "exit")
        receipt = run_checks(self.project, [command], self.output("exit"))
        self.assertEqual("passed", receipt["gate_status"])
        self.assertFalse(receipt["test_proof_observed"])
        self.assertIsNone(receipt["checks"][0]["observed_counts"])

    def test_argv_is_literal_and_log_private_bounded(self) -> None:
        marker = self.root / "should-not-exist"
        value = f"$(touch {marker})"
        check = {"id": "literal", "argv": [sys.executable, "-c",
                 "import sys; print('Ran 1 test in 0.1s\\n\\nOK'); print(sys.argv[1])",
                 value], "proof": {"type": "unittest"}}
        receipt = run_checks(self.project, [check], self.output("literal"))
        self.assertEqual("passed", receipt["gate_status"])
        self.assertFalse(marker.exists())
        log = Path(receipt["checks"][0]["log"])
        self.assertIn(value, log.read_text())
        self.assertLess(log.stat().st_size, 132000)
        self.assertFalse(receipt["checks"][0]["log_truncated"])
        huge = self.check("print('Ran 1 test in 0.1s\\n\\nOK'); print('x'*200000)")
        truncated = run_checks(self.project, [huge], self.output("truncated"))
        self.assertEqual("failed", truncated["gate_status"])
        self.assertTrue(truncated["checks"][0]["log_truncated"])
        self.assertLess(Path(truncated["checks"][0]["log"]).stat().st_size, 132000)

    def test_junit_freshness_and_nested_suite_counts(self) -> None:
        report = self.project / "junit.xml"
        report.write_text('<testsuite tests="1"><testcase name="old"/></testsuite>')
        # Existing report, no write during check: stale despite exit 0.
        stale = {"id": "stale", "argv": [sys.executable, "-c", "pass"],
                 "proof": {"type": "junit", "path": "junit.xml"}}
        receipt = run_checks(self.project, [stale], self.output("junit-stale"))
        self.assertEqual("failed", receipt["checks"][0]["result"])
        report.unlink()
        (self.project / ".gitignore").write_text("junit.xml\n")
        git(self.project, "add", ".gitignore")
        git(self.project, "commit", "-qm", "ignore reports")
        xml = '<testsuites tests="2"><testsuite tests="2"><testcase name="a"/><testcase name="b"><skipped/></testcase></testsuite></testsuites>'
        code = "from pathlib import Path; Path('junit.xml').write_text(" + repr(xml) + ")"
        fresh = {"id": "fresh", "argv": [sys.executable, "-c", code],
                 "proof": {"type": "junit", "path": "junit.xml"}}
        receipt = run_checks(self.project, [fresh], self.output("junit-fresh"))
        self.assertEqual("passed", receipt["gate_status"])
        self.assertEqual({"total": 2, "passed": 1, "failed": 0, "skipped": 1},
                         receipt["checks"][0]["observed_counts"])
        report.unlink()
        bad_xml = '<testsuite tests="2"><testcase name="only-one"/></testsuite>'
        bad_code = "from pathlib import Path; Path('junit.xml').write_text(" + repr(bad_xml) + ")"
        bad = {"id": "bad-xml", "argv": [sys.executable, "-c", bad_code],
               "proof": {"type": "junit", "path": "junit.xml"}}
        bad_receipt = run_checks(self.project, [bad], self.output("junit-bad"))
        self.assertEqual("failed", bad_receipt["gate_status"])
        report.unlink()
        inconsistent = '<testsuite tests="1" failures="1"><testcase name="green"/></testsuite>'
        inconsistent_code = "from pathlib import Path; Path('junit.xml').write_text(" + repr(inconsistent) + ")"
        bad_summary = {"id": "bad-summary", "argv": [sys.executable, "-c", inconsistent_code],
                       "proof": {"type": "junit", "path": "junit.xml"}}
        self.assertEqual("failed", run_checks(self.project, [bad_summary],
                                               self.output("junit-summary"))["gate_status"])

    def test_paths_and_output_guard(self) -> None:
        outside = self.root / "outside"
        outside.mkdir()
        (self.project / "escape").symlink_to(outside, target_is_directory=True)
        bad = [
            {"id": "cwd", "argv": [sys.executable, "-c", "pass"],
             "cwd": "escape", "proof": {"type": "exit"}},
            {"id": "proof", "argv": [sys.executable, "-c", "pass"],
             "proof": {"type": "junit", "path": "escape/report.xml"}},
            {"id": "traversal", "argv": [sys.executable, "-c", "pass"],
             "cwd": "../outside", "proof": {"type": "exit"}},
        ]
        receipt = run_checks(self.project, bad, self.output("bad-paths"))
        self.assertEqual(["blocked"] * 3, [r["result"] for r in receipt["checks"]])
        with self.assertRaises(ValueError):
            run_checks(self.project, [], self.project / "nonignored-output")
        (self.project / ".gitignore").write_text("private-runs/\n")
        git(self.project, "add", ".gitignore")
        git(self.project, "commit", "-qm", "ignore private runs")
        run_checks(self.project, [], self.project / "private-runs" / "one")

    def test_candidate_change_during_check_marks_stale(self) -> None:
        code = ("from pathlib import Path; Path('tracked.txt').write_text('changed'); "
                "print('Ran 1 test in 0.001s\\n\\nOK')")
        receipt = run_checks(self.project, [self.check(code)], self.output("changed"))
        self.assertEqual("stale", receipt["gate_status"])
        fresh = check_freshness(self.project, receipt)
        self.assertEqual("stale", fresh["status"])
        self.assertFalse(fresh["fresh"])

    def test_quiet_pytest_and_multiple_summary_failures(self) -> None:
        quiet = run_checks(self.project, [self.check(
            "print('1 passed in 0.02s')", "pytest")], self.output("quiet-pytest"))
        self.assertEqual("passed", quiet["gate_status"])
        mixed_pytest = run_checks(self.project, [self.check(
            "print('1 failed in 0.01s\\n1 passed in 0.02s')", "pytest")],
            self.output("mixed-pytest"))
        self.assertEqual("failed", mixed_pytest["gate_status"])
        mixed_unittest = run_checks(self.project, [self.check(
            "print('Ran 1 test in 0.1s\\n\\nFAILED (failures=1)\\nRan 1 test in 0.1s\\n\\nOK')")],
            self.output("mixed-unittest"))
        self.assertEqual("failed", mixed_unittest["gate_status"])

    def test_freshness_preserves_receipt_base_and_needs_before_snapshot(self) -> None:
        receipt = run_checks(self.project, [self.check("print('ok')", "exit")],
                             self.output("base-receipt"), base="HEAD")
        self.assertTrue(check_freshness(self.project, receipt)["fresh"])
        missing = dict(receipt)
        del missing["snapshot_before"]
        self.assertFalse(check_freshness(self.project, missing)["fresh"])
        git(self.project, "branch", "old-base", self.base)
        (self.project / "tracked.txt").write_text("new")
        git(self.project, "add", "tracked.txt")
        git(self.project, "commit", "-qm", "new head")
        self.assertFalse(check_freshness(self.project, receipt)["fresh"])

    def test_unknown_fields_git_path_and_junit_symlink_swap(self) -> None:
        outside = self.root / "outside.xml"
        outside.write_text('<testsuite tests="1"><testcase name="secret"/></testsuite>')
        cases = [
            {"id": "unknown", "argv": [sys.executable, "-c", "pass"],
             "surprise": 1, "proof": {"type": "exit"}},
            {"id": "proof-field", "argv": [sys.executable, "-c", "pass"],
             "proof": {"type": "exit", "surprise": 1}},
            {"id": "git", "argv": [sys.executable, "-c", "pass"],
             "cwd": ".git", "proof": {"type": "exit"}},
            {"id": "git-proof", "argv": [sys.executable, "-c", "pass"],
             "proof": {"type": "junit", "path": ".git/report.xml"}},
        ]
        receipt = run_checks(self.project, cases, self.output("invalid-fields"))
        self.assertEqual(["blocked"] * 4, [item["result"] for item in receipt["checks"]])
        swap_code = ("from pathlib import Path; "
                     f"Path('report.xml').symlink_to({str(outside)!r})")
        swap = {"id": "swap", "argv": [sys.executable, "-c", swap_code],
                "proof": {"type": "junit", "path": "report.xml"}}
        swapped = run_checks(self.project, [swap], self.output("swapped"))
        self.assertEqual("stale", swapped["gate_status"])
        self.assertEqual("failed", swapped["checks"][0]["result"])
        self.assertIn("outside", swapped["checks"][0]["reason"])

    def test_non_git_candidate_is_limited_even_with_passing_tests(self) -> None:
        plain = self.root / "plain"
        plain.mkdir()
        (plain / "value.txt").write_text("one")
        first = candidate_snapshot(plain)
        (plain / "value.txt").write_text("two")
        second = candidate_snapshot(plain)
        self.assertNotEqual(first["candidate_digest"], second["candidate_digest"])
        self.assertEqual("non-git", second["kind"])
        check = self.check('print("Ran 1 test in 0.001s\\n\\nOK")')
        receipt = run_checks(plain, [check], self.output("plain-run"))
        self.assertEqual("incomplete", receipt["gate_status"])
        self.assertEqual("unknown", check_freshness(plain, receipt)["status"])

    def test_timeout_kills_owned_process_group(self) -> None:
        pid_path = self.root / "child.pid"
        heartbeat = self.root / "heartbeat"
        child_code = ("from pathlib import Path; import time; "
                      f"p=Path({str(heartbeat)!r}); "
                      "exec('while True:\\n p.write_text(str(time.time_ns()))\\n time.sleep(0.05)')")
        code = ("import subprocess,sys,time; "
                f"p=subprocess.Popen([sys.executable,'-c',{child_code!r}]); "
                f"open({str(pid_path)!r},'w').write(str(p.pid)); "
                "time.sleep(60)")
        check = {"id": "timeout", "argv": [sys.executable, "-c", code],
                 "timeout_seconds": 1, "proof": {"type": "unittest"}}
        receipt = run_checks(self.project, [check], self.output("timeout"))
        self.assertEqual("failed", receipt["gate_status"])
        self.assertTrue(receipt["checks"][0]["timed_out"])
        self.assertTrue(pid_path.exists())
        self.assertTrue(heartbeat.exists())
        first = heartbeat.read_text()
        time.sleep(0.2)
        self.assertEqual(first, heartbeat.read_text())

    def test_timeout_kills_term_ignoring_group(self) -> None:
        pid_path = self.root / "ignoring.pid"
        code = ("import os,signal,time; signal.signal(signal.SIGTERM, signal.SIG_IGN); "
                f"open({str(pid_path)!r},'w').write(str(os.getpid())); time.sleep(60)")
        check = {"id": "ignore-term", "argv": [sys.executable, "-c", code],
                 "timeout_seconds": 1, "proof": {"type": "unittest"}}
        receipt = run_checks(self.project, [check], self.output("ignore-term"))
        self.assertEqual("failed", receipt["gate_status"])
        self.assertTrue(receipt["checks"][0]["timed_out"])
        pid = int(pid_path.read_text())
        with self.assertRaises(ProcessLookupError):
            os.kill(pid, 0)

    def test_successful_check_cleans_background_descendants(self) -> None:
        heartbeat = self.root / "background-heartbeat"
        pid_path = self.root / "background.pid"
        child = ("from pathlib import Path; import time; "
                 f"p=Path({str(heartbeat)!r}); "
                 "exec('while True:\\n p.write_text(str(time.time_ns()))\\n time.sleep(0.02)')")
        parent = ("import subprocess,sys,time\nfrom pathlib import Path\n"
                  f"p=subprocess.Popen([sys.executable,'-c',{child!r}],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)\n"
                  f"Path({str(pid_path)!r}).write_text(str(p.pid))\n"
                  f"for _ in range(100):\n if Path({str(heartbeat)!r}).exists(): break\n time.sleep(0.02)\n")
        try:
            result = run_checks(self.project, [self.check(parent, "exit")], self.output("background"))
            self.assertEqual(result["gate_status"], "passed")
            self.assertTrue(heartbeat.exists())
            last = heartbeat.read_text()
            time.sleep(0.1)
            self.assertEqual(heartbeat.read_text(), last, "owned background child survived check completion")
        finally:
            if pid_path.exists():
                try:
                    os.kill(int(pid_path.read_text()), signal.SIGKILL)
                except ProcessLookupError:
                    pass

    def test_interrupted_verifier_reaps_check_process(self) -> None:
        module_root = str(Path(local_checks.__file__).parent)
        for interrupt in (signal.SIGINT, signal.SIGTERM):
            with self.subTest(interrupt=interrupt):
                pid_path = self.root / f"interrupt-{interrupt}.pid"
                output = self.output(f"interrupt-{interrupt}")
                child_code = ("from pathlib import Path; import os,time; "
                              f"Path({str(pid_path)!r}).write_text(str(os.getpid())); time.sleep(60)")
                wrapper = ("import sys; from pathlib import Path; "
                           "sys.path.insert(0,sys.argv[1]); from local_checks import run_checks; "
                           "run_checks(Path(sys.argv[2]),[{'id':'sleep','argv':[sys.executable,'-c',sys.argv[4]],"
                           "'timeout_seconds':30,'proof':{'type':'exit'}}],Path(sys.argv[3]))")
                verifier = subprocess.Popen(
                    [sys.executable, "-c", wrapper, module_root, str(self.project), str(output), child_code],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                child_pid = None
                try:
                    for _ in range(100):
                        if pid_path.exists():
                            child_pid = int(pid_path.read_text())
                            break
                        time.sleep(0.03)
                    self.assertIsNotNone(child_pid, "configured check never started")
                    verifier.send_signal(interrupt)
                    verifier.wait(timeout=5)
                    with self.assertRaises(ProcessLookupError):
                        os.kill(child_pid, 0)
                finally:
                    if child_pid is not None:
                        try:
                            os.killpg(child_pid, signal.SIGKILL)
                        except ProcessLookupError:
                            pass
                    if verifier.poll() is None:
                        verifier.kill()
                        verifier.wait(timeout=5)

    def test_collection_error_reaps_started_check(self) -> None:
        pid_path = self.root / "collection-error.pid"
        child_code = ("from pathlib import Path; import os,time; "
                      f"Path({str(pid_path)!r}).write_text(str(os.getpid())); time.sleep(60)")

        def fail_selector():
            for _ in range(100):
                if pid_path.exists():
                    break
                time.sleep(0.03)
            raise OSError("selector unavailable")

        child_pid = None
        try:
            with mock.patch.object(local_checks.selectors, "DefaultSelector", side_effect=fail_selector):
                with self.assertRaisesRegex(OSError, "selector unavailable"):
                    local_checks._run_command([sys.executable, "-c", child_code],
                                              self.project, 30, self.output("error.log"))
            self.assertTrue(pid_path.exists())
            child_pid = int(pid_path.read_text())
            with self.assertRaises(ProcessLookupError):
                os.kill(child_pid, 0)
        finally:
            if child_pid is not None:
                try:
                    os.killpg(child_pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass


if __name__ == "__main__":
    unittest.main()
