"""Regression checks for the session adapter's skill discovery and emitted signals.

Run with: python3 -m unittest discover -s scripts/skills -p 'test_*.py'
"""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ADAPTER = Path(__file__).resolve().parents[2] / "skills/alarina/references/ayewo-igba-ise/scripts/session-evidence.py"


class SkillDiscoveryTests(unittest.TestCase):
    def test_command_reference_signal_and_discovery_from_consolidated_layout(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / "repo/skills/alarina"
            script = skill / "references/ayewo-igba-ise/scripts/session-evidence.py"
            script.parent.mkdir(parents=True)
            shutil.copyfile(ADAPTER, script)
            (skill / "SKILL.md").write_text("---\nname: alarina\n---\n", encoding="utf-8")
            sessions = root / "codex/sessions"
            sessions.mkdir(parents=True)
            event = {"type": "response_item", "payload": {"role": "assistant", "content": "Read /tmp/plugin/skills/alarina/commands/alaga-diagnose.md"}}
            (sessions / "reference.jsonl").write_text(json.dumps(event) + "\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(script), "--host", "codex", "--codex-root", str(root / "codex")],
                cwd=root, check=True, capture_output=True, text=True, timeout=10,
            )
            report = json.loads(result.stdout)
            self.assertEqual(["alarina"], report["filters"]["skills"])
            self.assertEqual(
                [{"skill": "alarina", "strength": "COMMAND_PATH_REFERENCE", "lines": [1]}],
                report["sessions"][0]["skill_signals"],
            )

    def test_discovered_and_explicit_skills_reach_session_signals(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skills = root / "repo/skills"
            script = skills / "ayewo-igba-ise/scripts/session-evidence.py"
            script.parent.mkdir(parents=True)
            shutil.copyfile(ADAPTER, script)
            for name in ("ayewo-igba-ise", "example"):
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
                ("checkout discovery", [], ["ayewo-igba-ise", "example"], "example"),
                ("explicit skills root", ["--skills-root", str(skills)], ["ayewo-igba-ise", "example"], "example"),
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

    def test_plugin_qualified_invocation_and_bundled_owner_path_are_visible(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skills = root / "repo/skills"
            script = skills / "ayewo-igba-ise/scripts/session-evidence.py"
            script.parent.mkdir(parents=True)
            shutil.copyfile(ADAPTER, script)
            for name in ("alarina", "alaga"):
                package = skills / name
                package.mkdir(exist_ok=True)
                (package / "SKILL.md").write_text(f"---\nname: {name}\n---\n", encoding="utf-8")
            sessions = root / "codex/sessions"
            sessions.mkdir(parents=True)
            transcript = sessions / "bundle.jsonl"
            events = [
                {"type": "session_meta", "payload": {"id": "bundle-session"}},
                {
                    "type": "response_item",
                    "payload": {"role": "user", "content": "Use $qp-skills:alarina to diagnose this failure."},
                },
                {
                    "type": "response_item",
                    "payload": {
                        "role": "assistant",
                        "content": "Read /tmp/plugin/skills/alarina/owners/alaga/OWNER.md",
                    },
                },
            ]
            transcript.write_text("\n".join(json.dumps(event) for event in events) + "\n", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    str(script),
                    "--host",
                    "codex",
                    "--codex-root",
                    str(root / "codex"),
                    "--skills-root",
                    str(skills),
                ],
                cwd=root,
                check=True,
                capture_output=True,
                text=True,
                timeout=10,
            )
            report = json.loads(result.stdout)
            self.assertEqual(
                [
                    {"skill": "alaga", "strength": "OWNER_PATH_REFERENCE", "lines": [3]},
                    {"skill": "alarina", "strength": "EXPLICIT_INVOKE", "lines": [2]},
                ],
                report["sessions"][0]["skill_signals"],
            )


if __name__ == "__main__":
    unittest.main()
