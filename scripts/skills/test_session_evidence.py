"""Regression checks for the session adapter's skill discovery and emitted signals.

Run with: python3 -m unittest discover -s scripts/skills -p 'test_*.py'
"""

import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ADAPTER = Path(__file__).resolve().parents[2] / "skills/ironu/scripts/session-evidence.py"


class SkillDiscoveryTests(unittest.TestCase):
    def test_discovered_and_explicit_skills_reach_session_signals(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skills = root / "repo/skills"
            script = skills / "ironu/scripts/session-evidence.py"
            script.parent.mkdir(parents=True)
            shutil.copyfile(ADAPTER, script)
            for name in ("example", "ironu"):
                package = skills / name
                package.mkdir(exist_ok=True)
                (package / "SKILL.md").write_text(f"---\nname: {name}\n---\n", encoding="utf-8")
            sessions = root / "codex/sessions"
            sessions.mkdir(parents=True)
            transcript = sessions / "rollout.jsonl"
            events = [
                {"type": "session_meta", "payload": {"id": "test-session"}},
                {"type": "response_item", "payload": {"role": "user", "content": "Use $example and $external."}},
            ]
            original = "\n".join(json.dumps(event) for event in events) + "\n"
            transcript.write_text(original, encoding="utf-8")
            cases = (
                ("checkout discovery", [], ["example", "ironu"], "example"),
                ("explicit skills root", ["--skills-root", str(skills)], ["example", "ironu"], "example"),
                ("explicit skill override", ["--skill", "external"], ["external"], "external"),
            )
            for label, options, names, signal in cases:
                with self.subTest(label=label):
                    result = subprocess.run(
                        [sys.executable, str(script), "--host", "codex", "--codex-root", str(root / "codex"), *options],
                        cwd=root, check=True, capture_output=True, text=True, timeout=10,
                    )
                    report = json.loads(result.stdout)
                    self.assertEqual(names, report["filters"]["skills"])
                    self.assertEqual(1, report["summary"]["sessions"])
                    self.assertEqual(
                        [{"skill": signal, "strength": "EXPLICIT_INVOKE", "lines": [2]}],
                        report["sessions"][0]["skill_signals"],
                    )
                    self.assertEqual(original, transcript.read_text(encoding="utf-8"))


class MiningLedgerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="qp-mining-")
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name).resolve()
        self.codex = self.base / "codex/sessions"
        self.claude = self.base / "claude/projects/project"
        self.codex.mkdir(parents=True)
        self.claude.mkdir(parents=True)
        self.ledger = self.base / "reflection/mined.jsonl"
        self.reader = self.base / "reader.jsonl"
        self.env = {**os.environ, "HOME": str(self.base / "home")}
        self.env.pop("CODEX_HOME", None)
        self.env.pop("CLAUDE_CONFIG_DIR", None)
        self.before = self.session("before", "codex", "2020-01-01T00:00:00Z")
        self.first = self.session("first", "codex", "2020-01-10T00:00:00Z")
        self.gap = self.session("gap", "codex", "2020-01-20T00:00:00Z")
        self.second = self.session("second", "codex", "2020-01-30T00:00:00Z")
        self.other = self.session("claude-session", "claude", "2020-01-10T00:00:00Z")

    def session(self, name, host, date):
        path = (self.codex if host == "codex" else self.claude) / f"{name}.jsonl"
        event = {"type": "session_meta", "timestamp": date, "payload": {"id": name}} if host == "codex" else {"type": "user", "timestamp": date, "sessionId": name, "message": {"role": "user", "content": "fixture"}}
        path.write_text(json.dumps(event) + "\n")
        modified = datetime.fromisoformat(date.replace("Z", "+00:00")).timestamp()
        os.utime(path, (modified, modified))
        return path

    def entry(self, path, host="codex", covered="full", **fields):
        return {"path": str(path), "host": host, "session": path.stem,
                "bytes": path.stat().st_size, "mtime": path.stat().st_mtime, "covered": covered, **fields}

    def run_tool(self, *options, ledger=True, status=0):
        command = [sys.executable, str(ADAPTER), "--codex-root", str(self.base / "codex"),
                   "--claude-root", str(self.base / "claude"), *options]
        if ledger: command.extend(["--ledger", str(self.ledger)])
        result = subprocess.run(command, cwd=self.base, env=self.env, capture_output=True, text=True, timeout=10)
        self.assertEqual(status, result.returncode, result.stdout + result.stderr)
        return json.loads(result.stdout) if status == 0 else result.stderr

    def record(self, entries, ledger=True):
        self.reader.write_text("\n".join(json.dumps(entry) for entry in entries) + "\n")
        return self.run_tool("--record-mined", str(self.reader), ledger=ledger)

    def test_full_and_all_user_message_reads_append_without_changing_transcripts(self):
        original = {path: path.read_bytes() for path in (self.first, self.gap, self.other)}
        result = self.record([self.entry(self.first), self.entry(self.gap, covered="skim"),
                              self.entry(self.other, "claude", "skim", all_user_messages_read=True)])
        self.assertEqual(2, result["appended"])
        self.assertEqual(1, result["skipped"])
        report = self.run_tool("--coverage")
        self.assertEqual(1, report["hosts"]["codex"]["mined"]["count"])
        self.assertEqual(1, report["hosts"]["claude"]["mined"]["count"])
        self.assertEqual(3, report["hosts"]["codex"]["unmined"]["count"])
        for path, content in original.items(): self.assertEqual(content, path.read_bytes())
        self.assertEqual(2, len(self.ledger.read_text().splitlines()))

    def test_ranges_gaps_and_history_before_first_run_have_counts_and_bytes(self):
        self.record([self.entry(self.first)])
        self.record([self.entry(self.second)])
        host = self.run_tool("--coverage")["hosts"]["codex"]
        self.assertEqual(2, len(host["mined_ranges"]))
        self.assertEqual("2020-01-10T00:00:00Z", host["mined_ranges"][0]["started_at"])
        self.assertEqual(1, host["never_mined_before_first_run"]["count"])
        self.assertEqual(self.before.stat().st_size, host["never_mined_before_first_run"]["bytes"])
        self.assertEqual(1, len(host["gaps_between_runs"]))
        self.assertEqual(1, host["gaps_between_runs"][0]["count"])
        self.assertEqual(self.gap.stat().st_size, host["gaps_between_runs"][0]["bytes"])

    def test_changed_size_or_mtime_is_unmined_and_remining_restores_coverage(self):
        self.record([self.entry(self.first), self.entry(self.second)])
        modified = self.first.stat().st_mtime
        self.first.write_text(self.first.read_text() + "{}\n")
        os.utime(self.first, (modified, modified))
        os.utime(self.second, (modified + 1, modified + 1))
        host = self.run_tool("--coverage")["hosts"]["codex"]
        self.assertEqual(0, host["mined"]["count"])
        self.assertEqual(2, host["changed_since_mining"]["count"])
        self.assertEqual(0, self.run_tool("--removal-candidates")["candidates"]["count"])
        self.record([self.entry(self.first), self.entry(self.second)])
        self.assertEqual(2, self.run_tool("--coverage")["hosts"]["codex"]["mined"]["count"])

    def test_candidates_are_old_unchanged_ledger_sessions_and_never_delete(self):
        fresh = self.session("fresh", "codex", "2020-01-01T00:00:00Z")
        now = datetime.now(timezone.utc).timestamp()
        os.utime(fresh, (now, now))
        recent = self.session("recent", "codex", "2020-01-01T00:00:00Z")
        thirty_days_ago = now - timedelta(days=30).total_seconds()
        os.utime(recent, (thirty_days_ago, thirty_days_ago))
        self.record([self.entry(self.first), self.entry(fresh), self.entry(recent)])
        old = self.run_tool("--removal-candidates")
        self.assertEqual(90, old["older_than_days"])
        self.assertEqual(["first"], [s["session_id"] for s in old["candidates"]["sessions"]])
        self.assertEqual(2, self.run_tool("--removal-candidates", "--older-than-days", "14")["candidates"]["count"])
        self.assertEqual(0, self.run_tool("--removal-candidates", "--older-than-days", "36500")["candidates"]["count"])
        self.assertEqual(3, self.run_tool("--removal-candidates", "--older-than-days", "0")["candidates"]["count"])
        for path in (self.before, self.first, self.gap, self.second, fresh, recent): self.assertTrue(path.exists())
        self.assertIn("zero or more", self.run_tool("--removal-candidates", "--older-than-days", "-1", status=2))

    def test_missing_unreadable_and_malformed_ledgers_supply_no_coverage(self):
        for mode in ("missing", "directory", "malformed"):
            with self.subTest(mode=mode):
                if mode == "directory": self.ledger.mkdir(parents=True)
                elif mode == "malformed":
                    self.ledger.rmdir()
                    self.ledger.write_text('{broken\n{"path":"missing"}\n')
                report = self.run_tool("--coverage")
                self.assertEqual(0, report["hosts"]["codex"]["mined"]["count"])
                self.assertEqual(4, report["hosts"]["codex"]["never_mined_before_first_run"]["count"])
                self.assertEqual(0, self.run_tool("--removal-candidates")["candidates"]["count"])

    def test_stale_reader_fingerprint_does_not_become_current(self):
        entry = self.entry(self.first)
        self.first.write_text(self.first.read_text() + "{}\n")
        self.record([entry])
        host = self.run_tool("--coverage")["hosts"]["codex"]
        self.assertEqual(1, host["changed_since_mining"]["count"])
        self.assertEqual(0, host["mined"]["count"])
        saved = json.loads(self.ledger.read_text())
        self.assertEqual(entry["bytes"], saved["bytes"])

    def test_history_indexes_and_incomplete_records_cannot_be_mined(self):
        indexes = []
        for host, folder in (("codex", self.codex), ("claude", self.claude)):
            for name in ("history.jsonl", "index.jsonl", "sessions-index.jsonl"):
                path = folder / name
                path.write_text(self.first.read_text())
                indexes.append(self.entry(path, host))
        alias = self.codex / "aliased-history.jsonl"
        alias.symlink_to(self.codex / "history.jsonl")
        indexes.append(self.entry(alias))
        bad = [self.entry(self.first, covered="partial"), self.entry(self.first, mtime=None), self.entry(self.first, bytes=-1)]
        result = self.record([*indexes, *bad])
        self.assertEqual(0, result["appended"])
        self.assertFalse(self.ledger.exists())
        report = self.run_tool()
        self.assertEqual(5, report["summary"]["sessions"])

    def test_default_user_ledger_and_transcript_ledger_rejection(self):
        result = self.record([self.entry(self.first)], ledger=False)
        user_ledger = self.base / "home/.qp/reflection/mined.jsonl"
        self.assertEqual(1, result["appended"])
        self.assertTrue(user_ledger.is_file())
        self.ledger = self.first
        original = self.first.read_bytes()
        self.assertIn("session stores", self.run_tool("--record-mined", str(self.reader), status=2))
        self.assertEqual(original, self.first.read_bytes())


if __name__ == "__main__":
    unittest.main()
