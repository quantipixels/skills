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


class SessionActivityTest(unittest.TestCase):
    def test_codex_tool_activity_is_structural_and_redacts_output(self):
        secret = "DO-NOT-EMIT-TOOL-OUTPUT"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / ".codex"
            sessions = root / "sessions"
            sessions.mkdir(parents=True)
            records = [
                {"type": "session_meta", "payload": {"id": "root", "cwd": "/work/repo"}},
                {"type": "response_item", "payload": {"type": "function_call", "name": "shell", "call_id": "c1", "arguments": "private args"}},
                {"type": "response_item", "payload": {"type": "function_call_output", "call_id": "c1", "output": secret}},
                {"type": "response_item", "payload": {"type": "function_call", "name": "shell", "call_id": "c2", "arguments": "more private args"}},
                {"type": "response_item", "payload": {"type": "function_call_output", "call_id": "c2", "is_error": True, "output": secret}},
            ]
            (sessions / "root.jsonl").write_text("\n".join(json.dumps(x) for x in records) + "\n")
            report = session_evidence.build(session_evidence.args(["--host", "codex", "--codex-root", str(root)]))

        activity = report["sessions"][0]["activity"]
        self.assertEqual(activity["tool_calls"], 2)
        self.assertEqual(activity["tool_results"], 2)
        self.assertEqual(activity["tool_failures"], 1)
        self.assertEqual(activity["repeated_same_tool_calls"], 1)
        self.assertEqual(activity["tool_calls_by_name"], {"shell": 2})
        self.assertGreater(activity["tool_result_bytes"], 0)
        self.assertNotIn(secret, json.dumps(report))
        self.assertNotIn("private args", json.dumps(report))

    def test_claude_tool_activity_uses_structured_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / ".claude"
            project = root / "projects" / "-work-repo"
            project.mkdir(parents=True)
            records = [
                {
                    "type": "assistant",
                    "sessionId": "root",
                    "message": {
                        "role": "assistant",
                        "content": [
                            {"type": "tool_use", "id": "t1", "name": "Read", "input": {"file": "private"}},
                            {"type": "tool_use", "id": "t2", "name": "Read", "input": {"file": "private-2"}},
                        ],
                    },
                },
                {
                    "type": "user",
                    "sessionId": "root",
                    "message": {
                        "role": "user",
                        "content": [
                            {"type": "tool_result", "tool_use_id": "t1", "content": "secret"},
                            {"type": "tool_result", "tool_use_id": "t2", "is_error": True, "content": "secret failure"},
                        ],
                    },
                },
            ]
            (project / "root.jsonl").write_text("\n".join(json.dumps(x) for x in records) + "\n")
            report = session_evidence.build(session_evidence.args(["--host", "claude", "--claude-root", str(root)]))

        activity = report["sessions"][0]["activity"]
        self.assertEqual(activity["tool_calls"], 2)
        self.assertEqual(activity["tool_results"], 2)
        self.assertEqual(activity["tool_failures"], 1)
        self.assertEqual(activity["repeated_same_tool_calls"], 1)
        self.assertEqual(activity["tool_calls_by_name"], {"Read": 2})
        self.assertNotIn("secret failure", json.dumps(report))


if __name__ == "__main__":
    unittest.main()
