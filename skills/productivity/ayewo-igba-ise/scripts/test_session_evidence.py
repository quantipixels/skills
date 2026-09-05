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
    def build_codex(self, records, extra=None):
        tmp = tempfile.TemporaryDirectory(); self.addCleanup(tmp.cleanup)
        root = Path(tmp.name) / ".codex"; sessions = root / "sessions"; sessions.mkdir(parents=True)
        for name, lines in records.items():
            (sessions / f"{name}.jsonl").write_text("\n".join(json.dumps(x) for x in lines) + "\n")
        argv = ["--host", "codex", "--codex-root", str(root)]
        if extra: argv += extra
        return session_evidence.build(session_evidence.args(argv))

    def test_explicit_slash_invocation_is_high_confidence_without_raw_text(self):
        secret = "DO-NOT-EMIT-SECRET"
        report = self.build_codex({"root": [
            {"timestamp": "2026-09-01T10:00:00Z", "type": "session_meta", "payload": {"id": "root", "cwd": "/work/repo", "cli_version": "1.2.3"}},
            {"timestamp": "2026-09-01T10:01:00Z", "type": "response_item", "payload": {"type": "message", "role": "user", "content": [{"type": "input_text", "text": f"/root-cause {secret}"}]}}
        ]}, ["--skill", "root-cause"])
        item = report["sessions"][0]
        self.assertEqual(item["skill_signals"], [{"skill": "root-cause", "strength": "EXPLICIT_INVOKE", "lines": [2]}])
        self.assertNotIn(secret, json.dumps(report))

    def test_natural_user_mention_is_reference_not_invocation(self):
        report = self.build_codex({"root": [
            {"type": "session_meta", "payload": {"id": "root"}},
            {"type": "response_item", "payload": {"type": "message", "role": "user", "content": [{"type": "input_text", "text": "Use the root-cause skill."}]}}
        ]}, ["--skill", "root-cause"])
        self.assertEqual(report["sessions"][0]["skill_signals"], [{"skill": "root-cause", "strength": "USER_SKILL_REFERENCE", "lines": [2]}])

    def test_negated_user_mention_is_not_invocation(self):
        report = self.build_codex({"root": [
            {"type": "session_meta", "payload": {"id": "root"}},
            {"type": "response_item", "payload": {"type": "message", "role": "user", "content": [{"type": "input_text", "text": "Do not use root-cause for this task."}]}}
        ]}, ["--skill", "root-cause"])
        self.assertEqual(report["sessions"][0]["skill_signals"], [{"skill": "root-cause", "strength": "USER_SKILL_REFERENCE", "lines": [2]}])

    def test_system_skill_path_is_reference_not_loaded(self):
        report = self.build_codex({"root": [
            {"type": "session_meta", "payload": {"id": "root"}},
            {"type": "response_item", "payload": {"type": "message", "role": "system", "content": [{"type": "input_text", "text": "/repo/skills/experimental/root-cause/SKILL.md"}]}}
        ]}, ["--skill", "root-cause"])
        self.assertEqual(report["sessions"][0]["skill_signals"], [{"skill": "root-cause", "strength": "SKILL_PATH_REFERENCE", "lines": [2]}])

    def test_nested_tool_payload_skill_key_does_not_prove_routing(self):
        report = self.build_codex({"root": [
            {"type": "session_meta", "payload": {"id": "root"}},
            {"type": "response_item", "payload": {"type": "function_call_output", "output": {"example": {"selected_skill": "root-cause"}}}}
        ]}, ["--skill", "root-cause"])
        self.assertEqual(report["sessions"][0]["skill_signals"], [])

    def test_top_level_structured_skill_is_reference_not_routing(self):
        report = self.build_codex({"root": [
            {"type": "session_meta", "payload": {"id": "root"}},
            {"type": "selection", "selected_skill": "root-cause"}
        ]}, ["--skill", "root-cause"])
        self.assertEqual(report["sessions"][0]["skill_signals"], [{"skill": "root-cause", "strength": "STRUCTURED_SKILL_REFERENCE", "lines": [2]}])

    def test_parent_threads_normalize_to_one_root(self):
        report = self.build_codex({
            "root": [{"type": "session_meta", "payload": {"id": "root", "cwd": "/work/repo"}}],
            "child": [{"type": "session_meta", "payload": {"id": "child", "parent_thread_id": "root", "cwd": "/work/repo"}}]
        })
        items = {x["session_id"]: x for x in report["sessions"]}
        self.assertEqual(items["child"]["root_session_id"], "root")
        self.assertEqual(items["child"]["ancestor_session_ids"], ["root"])
        self.assertEqual(report["summary"]["resolved_root_sessions"], 1)

    def test_missing_parent_remains_unresolved_and_filterable(self):
        records = {
            "child-a": [{"type": "session_meta", "payload": {"id": "child-a", "parent_thread_id": "missing-root"}}],
            "child-b": [{"type": "session_meta", "payload": {"id": "child-b", "parent_thread_id": "missing-root"}}],
        }
        report = self.build_codex(records)
        self.assertEqual(report["summary"]["resolved_root_sessions"], 0)
        self.assertEqual(report["summary"]["unresolved_root_members"], 2)
        for item in report["sessions"]:
            self.assertIsNone(item["root_session_id"])
            self.assertEqual(item["root_resolution"], "UNRESOLVED_PARENT")
            self.assertEqual(item["ancestor_session_ids"], ["missing-root"])
        filtered = self.build_codex(records, ["--session", "missing-root"])
        self.assertEqual({x["session_id"] for x in filtered["sessions"]}, {"child-a", "child-b"})

    def test_skill_focus_does_not_drop_sessions_without_signal(self):
        report = self.build_codex({
            "a": [{"type": "session_meta", "payload": {"id": "a"}}, {"type": "response_item", "payload": {"type": "message", "role": "user", "content": [{"type": "input_text", "text": "/root-cause"}]}}],
            "b": [{"type": "session_meta", "payload": {"id": "b"}}, {"type": "response_item", "payload": {"type": "message", "role": "user", "content": [{"type": "input_text", "text": "hello"}]}}],
        }, ["--skill", "root-cause"])
        self.assertEqual(report["summary"]["sessions"], 2)
        by = {x["session_id"]: x for x in report["sessions"]}
        self.assertEqual(by["b"]["skill_signals"], [])

    def test_no_default_cutoff_and_unknown_time_is_uncertain(self):
        report = self.build_codex({
            "old": [{"timestamp": "2020-01-01T00:00:00Z", "type": "session_meta", "payload": {"id": "old"}}],
            "unknown": [{"type": "session_meta", "payload": {"id": "unknown"}}],
            "new": [{"timestamp": "2030-01-01T00:00:00Z", "type": "session_meta", "payload": {"id": "new"}}],
        }, ["--since", "2025-01-01T00:00:00Z"])
        self.assertEqual({x["session_id"] for x in report["sessions"]}, {"new", "unknown"})
        unknown = next(x for x in report["sessions"] if x["session_id"] == "unknown")
        self.assertEqual(unknown["filter_state"], "UNCERTAIN")

    def test_claude_subagent_path_groups_under_root_session(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / ".claude"; project = root / "projects" / "-work-repo"
            main = project / "root-session.jsonl"; sub = project / "root-session" / "subagents" / "agent-a.jsonl"
            sub.parent.mkdir(parents=True); main.parent.mkdir(parents=True, exist_ok=True)
            main.write_text(json.dumps({"type": "user", "sessionId": "root-session", "timestamp": "2026-09-02T10:00:00Z", "cwd": "/work/repo", "message": {"role": "user", "content": "hello"}}) + "\n")
            sub.write_text(json.dumps({"type": "assistant", "timestamp": "2026-09-02T10:01:00Z", "cwd": "/work/repo", "message": {"role": "assistant", "content": []}}) + "\n")
            report = session_evidence.build(session_evidence.args(["--host", "claude", "--claude-root", str(root)]))
            by = {x["relation"]: x for x in report["sessions"]}
            self.assertEqual(by["subagent"]["root_session_id"], "root-session")

    def test_invalid_json_is_counted_not_fatal(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / ".claude"; project = root / "projects" / "-work"; project.mkdir(parents=True)
            (project / "s1.jsonl").write_text("{not json}\n" + json.dumps({"type": "user", "sessionId": "s1", "message": {"role": "user", "content": "ok"}}) + "\n")
            report = session_evidence.build(session_evidence.args(["--host", "claude", "--claude-root", str(root)]))
            self.assertEqual(report["summary"]["invalid_json_lines"], 1)


if __name__ == "__main__":
    unittest.main()
