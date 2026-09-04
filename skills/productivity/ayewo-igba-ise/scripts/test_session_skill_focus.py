import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).with_name("session-evidence.py")
SPEC = importlib.util.spec_from_file_location("session_evidence_focus", SCRIPT)
session_evidence = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(session_evidence)


class SessionEvidenceSkillFocusTest(unittest.TestCase):
    def test_explicit_skill_focus_does_not_expand_to_all_repo_skills(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            root = tmp / ".codex"
            sessions = root / "sessions"
            sessions.mkdir(parents=True)
            skills = tmp / "skills"
            for group, name in (("experimental", "root-cause"), ("engineering", "alaga")):
                path = skills / group / name / "SKILL.md"
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(f"---\nname: {name}\n---\n")

            line = {
                "timestamp": "2026-09-01T10:00:00Z",
                "type": "response_item",
                "payload": {
                    "type": "message",
                    "role": "user",
                    "content": [{"type": "input_text", "text": "Use root-cause, then use alaga."}],
                },
            }
            (sessions / "s1.jsonl").write_text(json.dumps(line) + "\n")

            report = session_evidence.build(
                session_evidence.args([
                    "--host", "codex",
                    "--codex-root", str(root),
                    "--skills-root", str(skills),
                    "--skill", "root-cause",
                ])
            )

            self.assertEqual(report["filters"]["skills"], ["root-cause"])
            self.assertEqual(
                report["sessions"][0]["skill_signals"],
                [{"skill": "root-cause", "strength": "EXPLICIT_INVOKE", "lines": [1]}],
            )

    def test_skill_focus_preserves_sessions_without_a_signal(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / ".codex"
            sessions = root / "sessions"
            sessions.mkdir(parents=True)
            (sessions / "s1.jsonl").write_text(
                json.dumps({
                    "timestamp": "2026-09-01T10:00:00Z",
                    "type": "session_meta",
                    "payload": {"id": "s1", "cwd": "/work/repo"},
                }) + "\n"
            )

            report = session_evidence.build(
                session_evidence.args([
                    "--host", "codex",
                    "--codex-root", str(root),
                    "--skill", "root-cause",
                ])
            )

            self.assertEqual(report["summary"]["sessions"], 1)
            self.assertEqual(report["filters"]["skills"], ["root-cause"])
            self.assertEqual(report["sessions"][0]["skill_signals"], [])


if __name__ == "__main__":
    unittest.main()
