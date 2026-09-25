"""Mechanical consistency checks for Alárinà actor and expectation files."""

from __future__ import annotations

import json
from pathlib import Path
import unittest

import yaml


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ALARINA = ROOT / "skills/alarina"


def load_json(relative: str):
    return json.loads((HERE / relative).read_text(encoding="utf-8"))


class AlarinaCaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.routes = yaml.safe_load((ALARINA / "routes.yaml").read_text(encoding="utf-8"))
        cls.families = set(cls.routes["families"])
        cls.commands = {command["id"] for command in cls.routes["commands"]}
        for command in cls.routes["commands"]:
            if not (ALARINA / command["reference"]).is_file():
                raise AssertionError(f"missing command: {command['id']}")

    def assert_matched_ids(self, actor_path: str, expectation_path: str):
        actors = load_json(actor_path)
        expectations = load_json(expectation_path)
        actor_ids = [actor["id"] for actor in actors]
        self.assertEqual(len(actor_ids), len(set(actor_ids)))
        self.assertEqual(set(actor_ids), set(expectations))
        return actors, expectations

    def test_trigger_cases_and_private_expectations_match(self):
        actors, expectations = self.assert_matched_ids(
            "triggers/cases.json", "triggers/expectations.json"
        )
        for actor in actors:
            self.assertTrue(actor.get("prompt", "").strip())
            expected = expectations[actor["id"]]
            self.assertIs(type(expected["selected"]), bool)
            if expected["selected"]:
                self.assertIn(expected["family"], self.families)
            else:
                self.assertTrue(expected.get("class"))

    def test_dispatch_cases_reference_real_bundle_paths(self):
        actors, expectations = self.assert_matched_ids(
            "dispatch/cases.json", "dispatch/expectations.json"
        )
        for actor in actors:
            self.assertTrue(actor.get("prompt", "").strip() or actor.get("condition") == "bare-invocation")
            expected = expectations[actor["id"]]
            self.assertIn(expected["family"], self.families)
            playbook = expected.get("playbook")
            if playbook is not None:
                self.assertTrue((ALARINA / playbook).is_file(), playbook)
                matches = [route for route in self.routes["routes"] if route["playbook"] == playbook]
                self.assertEqual(1, len(matches), playbook)
                self.assertIn(expected["family"], matches[0]["families"])
            self.assertFalse(set(expected.get("commands", [])) - self.commands)
            self.assertIsInstance(expected.get("forbid", []), list)
        covered = {command for expected in expectations.values() for command in expected.get("commands", [])}
        self.assertEqual(self.commands, covered)


if __name__ == "__main__":
    unittest.main()
