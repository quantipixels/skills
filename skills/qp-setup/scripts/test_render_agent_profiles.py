import importlib.util
import json
from pathlib import Path
import tempfile
import tomllib
import unittest

ROOT = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("render_agent_profiles", ROOT / "render-agent-profiles.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MOD)


class AgentProfileRendererTests(unittest.TestCase):
    def setUp(self):
        self.roles = MOD.load_roles(ROOT.parent / "assets" / "agent-experience" / "roles.json")
        self.role_names = [role["name"] for role in self.roles]

    def settings_file(self, directory: Path) -> Path:
        path = directory / "settings.json"
        path.write_text(
            json.dumps(
                {
                    "roles": {
                        name: {"model": "test-model", "effort": "medium"}
                        for name in self.role_names
                    }
                }
            ),
            encoding="utf-8",
        )
        return path

    def test_catalogue_is_provider_neutral_and_has_expected_work_postures(self):
        self.assertEqual(
            self.role_names,
            [
                "explorer",
                "analyst",
                "writer",
                "implementer",
                "verifier",
                "researcher",
                "reviewer",
            ],
        )
        raw = (ROOT.parent / "assets" / "agent-experience" / "roles.json").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("gpt-", raw.lower())
        self.assertNotIn("claude-", raw.lower())
        self.assertNotIn('"skills"', raw)

    def test_codex_profiles_render_runtime_defaults_and_sandbox(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            settings = MOD.load_settings(self.settings_file(root), self.roles)
            output = root / "codex"
            written = MOD.render("codex", self.roles, settings, output)
            self.assertEqual(len(written), 7)
            reviewer = tomllib.loads(
                (output / "reviewer.toml").read_text(encoding="utf-8")
            )
            implementer = tomllib.loads(
                (output / "implementer.toml").read_text(encoding="utf-8")
            )
            self.assertEqual(reviewer["model"], "test-model")
            self.assertEqual(reviewer["model_reasoning_effort"], "medium")
            self.assertEqual(reviewer["sandbox_mode"], "read-only")
            self.assertEqual(implementer["sandbox_mode"], "workspace-write")

    def test_claude_profiles_render_without_preloaded_skills(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            settings = MOD.load_settings(self.settings_file(root), self.roles)
            output = root / "claude"
            written = MOD.render("claude", self.roles, settings, output)
            self.assertEqual(len(written), 7)
            reviewer = (output / "reviewer.md").read_text(encoding="utf-8")
            writer = (output / "writer.md").read_text(encoding="utf-8")
            self.assertIn('model: "test-model"', reviewer)
            self.assertIn('effort: "medium"', reviewer)
            self.assertIn("disallowedTools:", reviewer)
            self.assertNotIn("disallowedTools:", writer)
            self.assertNotIn("skills:", reviewer)
            self.assertNotIn("skills:", writer)

    def test_unknown_settings_role_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            path = root / "settings.json"
            path.write_text(
                json.dumps({"roles": {"ghost": {"model": "x"}}}),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "unknown roles"):
                MOD.load_settings(path, self.roles)


if __name__ == "__main__":
    unittest.main()
