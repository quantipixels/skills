import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).with_name("session-evidence.py")
SPEC = importlib.util.spec_from_file_location("session_evidence", SCRIPT)
session_evidence = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(session_evidence)


class SessionEvidenceTest(unittest.TestCase):
    def test_codex_extracts_metadata_tools_and_explicit_skill_without_raw_text(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / ".codex"
            session = root / "sessions" / "rollout.jsonl"
            session.parent.mkdir(parents=True)
            secret = "DO-NOT-EMIT-SECRET"
            lines = [
                {"timestamp": "2026-09-01T10:00:00Z", "type": "session_meta", "payload": {"id": "codex-root", "cwd": "/work/repo", "cli_version": "1.2.3", "originator": "codex_cli_rs"}},
                {"timestamp": "2026-09-01T10:01:00Z", "type": "response_item", "payload": {"type": "message", "role": "user", "content": [{"type": "input_text", "text": f"Use the `root-cause` skill. {secret}"}]}},
                {"timestamp": "2026-09-01T10:02:00Z", "type": "response_item", "payload": {"type": "function_call", "name": "shell"}},
            ]
            session.write_text("\n".join(json.dumps(line) for line in lines) + "\n")
            report = session_evidence.build(session_evidence.args(["--host", "codex", "--codex-root", str(root), "--skill", "root-cause"]))
            item = report["sessions"][0]
            self.assertEqual(report["summary"]["sessions"], 1)
            self.assertEqual(item["session_id"], "codex-root")
            self.assertEqual(item["cwd"], "/work/repo")
            self.assertEqual(item["host_version"], "1.2.3")
            self.assertEqual(item["skill_signals"], [{"skill": "root-cause", "strength": "EXPLICIT_INVOKE", "lines": [2]}])
            self.assertNotIn(secret, json.dumps(report))

    def test_codex_parent_threads_normalize_to_one_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / ".codex"; sessions = root / "sessions"; sessions.mkdir(parents=True)
            (sessions / "root.jsonl").write_text(json.dumps({"timestamp": "2026-09-01T10:00:00Z", "type": "session_meta", "payload": {"id": "root", "cwd": "/work/repo"}}) + "\n")
            (sessions / "child.jsonl").write_text(json.dumps({"timestamp": "2026-09-01T10:01:00Z", "type": "session_meta", "payload": {"id": "child", "parent_thread_id": "root", "cwd": "/work/repo"}}) + "\n")
            report = session_evidence.build(session_evidence.args(["--host", "codex", "--codex-root", str(root)]))
            items = {item["session_id"]: item for item in report["sessions"]}
            self.assertEqual(items["child"]["root_session_id"], "root")
            self.assertEqual(items["child"]["relation"], "subagent")
            self.assertEqual(report["summary"]["root_sessions"], 1)

    def test_claude_subagent_path_groups_under_root_session(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / ".claude"; project = root / "projects" / "-work-repo"
            main = project / "root-session.jsonl"; subagent = project / "root-session" / "subagents" / "agent-a.jsonl"
            subagent.parent.mkdir(parents=True); main.parent.mkdir(parents=True, exist_ok=True)
            main.write_text(json.dumps({"type": "user", "sessionId": "root-session", "timestamp": "2026-09-02T10:00:00Z", "cwd": "/work/repo", "version": "2.1.250", "message": {"role": "user", "content": "hello"}}) + "\n")
            subagent.write_text(json.dumps({"type": "assistant", "timestamp": "2026-09-02T10:01:00Z", "cwd": "/work/repo", "version": "2.1.250", "message": {"role": "assistant", "content": []}}) + "\n")
            report = session_evidence.build(session_evidence.args(["--host", "claude", "--claude-root", str(root)]))
            by_relation = {item["relation"]: item for item in report["sessions"]}
            self.assertEqual(by_relation["root"]["session_id"], "root-session")
            self.assertEqual(by_relation["subagent"]["root_session_id"], "root-session")
            self.assertEqual(report["summary"]["root_sessions"], 1)

    def test_optional_time_filter_keeps_unknown_time_as_uncertain(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / ".codex"; sessions = root / "sessions"; sessions.mkdir(parents=True)
            (sessions / "unknown.jsonl").write_text(json.dumps({"type": "session_meta", "payload": {"id": "unknown", "cwd": "/work/repo"}}) + "\n")
            report = session_evidence.build(session_evidence.args(["--host", "codex", "--codex-root", str(root), "--since", "2030-01-01T00:00:00Z"]))
            self.assertEqual(report["summary"]["sessions"], 1)
            self.assertEqual(report["sessions"][0]["filter_state"], "UNCERTAIN")
            self.assertEqual(report["sessions"][0]["filter_uncertainty"], ["time"])

    def test_no_default_cutoff_and_explicit_time_filter(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / ".codex"; sessions = root / "sessions"; sessions.mkdir(parents=True)
            for name, stamp in (("old", "2020-01-01T00:00:00Z"), ("new", "2030-01-01T00:00:00Z")):
                (sessions / f"{name}.jsonl").write_text(json.dumps({"timestamp": stamp, "type": "session_meta", "payload": {"id": name, "cwd": "/work/repo"}}) + "\n")
            all_report = session_evidence.build(session_evidence.args(["--host", "codex", "--codex-root", str(root)]))
            self.assertEqual(all_report["summary"]["sessions"], 2)
            filtered = session_evidence.build(session_evidence.args(["--host", "codex", "--codex-root", str(root), "--since", "2025-01-01T00:00:00Z"]))
            self.assertEqual([item["session_id"] for item in filtered["sessions"]], ["new"])

    def test_invalid_json_is_counted_not_fatal(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / ".claude"; project = root / "projects" / "-work"; project.mkdir(parents=True)
            path = project / "s1.jsonl"
            path.write_text("{not json}\n" + json.dumps({"type": "user", "sessionId": "s1", "cwd": "/work", "message": {"role": "user", "content": "ok"}}) + "\n")
            report = session_evidence.build(session_evidence.args(["--host", "claude", "--claude-root", str(root)]))
            self.assertEqual(report["summary"]["invalid_json_lines"], 1)
            self.assertEqual(report["sessions"][0]["event_count"], 1)

    def test_assistant_instruction_text_is_not_explicit_invocation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / ".claude"; project = root / "projects" / "-work"; project.mkdir(parents=True)
            (project / "s1.jsonl").write_text(json.dumps({"type": "assistant", "sessionId": "s1", "cwd": "/work", "message": {"role": "assistant", "content": "Use the `root-cause` skill next."}}) + "\n")
            report = session_evidence.build(session_evidence.args(["--host", "claude", "--claude-root", str(root), "--skill", "root-cause"]))
            self.assertEqual(report["sessions"][0]["skill_signals"], [])


if __name__ == "__main__":
    unittest.main()
