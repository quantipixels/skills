import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("qp_update", ROOT / "update.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MOD)


class UpdateTests(unittest.TestCase):
    def test_direct_installation_is_detected_from_owned_manifest(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "owner.json").write_text(
                json.dumps({"format": 1, "source": MOD.SOURCE}), encoding="utf-8"
            )
            current = root / "current"
            current.mkdir()
            (current / "installation.json").write_text(
                json.dumps(
                    {
                        "format": 1,
                        "source": MOD.SOURCE,
                        "skills": ["pepeye", "alaga"],
                        "hosts": {"codex": "/tmp/skills"},
                    }
                ),
                encoding="utf-8",
            )
            found = MOD.direct_installation(root)
            self.assertEqual(found["manager"], "direct")
            self.assertEqual(found["skills"], ["alaga", "pepeye"])

    def test_skills_cli_detection_uses_source_not_name_guessing(self):
        with tempfile.TemporaryDirectory() as temp:
            lock = Path(temp) / ".skill-lock.json"
            lock.write_text(
                json.dumps(
                    {
                        "version": 3,
                        "skills": {
                            "pepeye": {
                                "source": MOD.SOURCE,
                                "sourceUrl": "https://github.com/quantipixels/skills.git",
                            },
                            "foreign": {
                                "source": "elsewhere/skills",
                                "sourceUrl": "https://github.com/elsewhere/skills.git",
                            },
                        },
                    }
                ),
                encoding="utf-8",
            )
            found = MOD.skills_cli_installation(lock)
            self.assertEqual(found["skills"], ["pepeye"])

    def test_catalogue_delta_separates_new_and_deprecated(self):
        additions, deprecated = MOD.catalogue_delta(
            ["alaga", "old-skill"], ["alaga", "new-skill"]
        )
        self.assertEqual(additions, ["new-skill"])
        self.assertEqual(deprecated, ["old-skill"])

    def test_claude_plugin_detection_is_tolerant_of_nested_json(self):
        payload = {
            "installed": [
                {"name": "other", "scope": "user"},
                {
                    "plugin": {
                        "name": "qp-skills",
                        "marketplace": "qp-skills",
                        "scope": "project",
                    }
                },
            ]
        }
        found = MOD.claude_plugin_from_payload(payload)
        self.assertEqual(found["manager"], "claude-plugin")


if __name__ == "__main__":
    unittest.main()
