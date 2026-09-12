import importlib.util
import json
from pathlib import Path
import tempfile
import tomllib
import unittest

ROOT = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "render_agent_definitions", ROOT / "render-agent-definitions.py"
)
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MOD)


class AgentDefinitionRendererTests(unittest.TestCase):
    def setUp(self):
        self.postures = MOD.load_postures(
            ROOT.parent / "assets" / "agent-experience" / "postures.json"
        )
        self.ids = [item["id"] for item in self.postures]

    def settings_file(self, directory: Path, definitions: dict) -> Path:
        path = directory / "settings.json"
        path.write_text(json.dumps({"definitions": definitions}), encoding="utf-8")
        return path

    def test_catalogue_is_provider_neutral_and_uses_yoruba_agent_ids(self):
        self.assertEqual(
            self.ids,
            [
                "asawari",
                "olutupale",
                "akowe",
                "oluse",
                "oludaniloju",
                "oluwadi",
                "oluyewo",
            ],
        )
        raw = (
            ROOT.parent / "assets" / "agent-experience" / "postures.json"
        ).read_text(encoding="utf-8")
        self.assertNotIn("gpt-", raw.lower())
        self.assertNotIn("claude-", raw.lower())
        self.assertNotIn('"skills"', raw)
        self.assertNotIn("baseline_model", raw)
        self.assertNotIn("baseline_effort", raw)
        self.assertNotIn('"sandbox"', raw)

    def test_only_selected_definitions_are_rendered_and_unpinned_by_default(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            settings = MOD.load_settings(
                self.settings_file(
                    folder,
                    {
                        "oluyewo": {},
                        "akowe": {"model": "test-model", "effort": "medium"},
                    },
                ),
                self.postures,
            )
            output = folder / "codex"
            written = MOD.render("codex", self.postures, settings, output)
            self.assertEqual([path.name for path in written], ["akowe.toml", "oluyewo.toml"])
            reviewer = tomllib.loads((output / "oluyewo.toml").read_text(encoding="utf-8"))
            writer = tomllib.loads((output / "akowe.toml").read_text(encoding="utf-8"))
            self.assertNotIn("model", reviewer)
            self.assertNotIn("model_reasoning_effort", reviewer)
            self.assertEqual(reviewer["sandbox_mode"], "read-only")
            self.assertEqual(writer["model"], "test-model")
            self.assertEqual(writer["model_reasoning_effort"], "medium")
            self.assertEqual(writer["sandbox_mode"], "workspace-write")
            self.assertIn("qp-skills-agent-definition: v1", (output / "oluyewo.toml").read_text())

    def test_claude_definition_uses_boundary_without_preloading_skills(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            settings = MOD.load_settings(
                self.settings_file(folder, {"oluyewo": {}, "akowe": {}}),
                self.postures,
            )
            output = folder / "claude"
            MOD.render("claude", self.postures, settings, output)
            reviewer = (output / "oluyewo.md").read_text(encoding="utf-8")
            writer = (output / "akowe.md").read_text(encoding="utf-8")
            self.assertIn("disallowedTools:", reviewer)
            self.assertNotIn("disallowedTools:", writer)
            self.assertNotIn("skills:", reviewer)
            self.assertIn("qp-skills-agent-definition: v1", reviewer)

    def test_unknown_definition_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            path = self.settings_file(folder, {"ghost": {"model": "x"}})
            with self.assertRaisesRegex(ValueError, "unknown definitions"):
                MOD.load_settings(path, self.postures)


if __name__ == "__main__":
    unittest.main()
