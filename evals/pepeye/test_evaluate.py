"""Mechanical tests only: these do not establish model behavior."""

import copy
from pathlib import Path
import tempfile
import unittest

import evaluate


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.run = Path(self.temp.name) / "run"
        evaluate.prepare("P1", "control", self.run)

    def judgments(self):
        result = evaluate.read_json(self.run / "judgments.template.json")
        result["record_kind"] = "synthetic-test"
        for item in result["checks"].values():
            item.update(verdict="pass", evidence="synthetic fixture assertion")
        return result

    def fix_fixture(self):
        case = evaluate.read_json(self.run / "oracle.json")
        for name, contents in case["expected_files"].items():
            (self.run / "actor" / "workspace" / name).write_text(contents)

    def test_private_rubric_is_not_in_actor_inputs(self):
        actor = self.run / "actor"
        self.assertFalse((actor / "oracle.json").exists())
        self.assertFalse((actor / "skill").exists())
        self.assertNotIn("p1-exact-edit", (actor / "prompt.md").read_text())
        treatment = Path(self.temp.name) / "treatment"
        evaluate.prepare("P1", "pepeye", treatment)
        self.assertTrue((treatment / "actor" / "skill" / "SKILL.md").is_file())
        self.assertEqual(evaluate.read_json(treatment / "manifest.json")["treatment_sha256"],
                         evaluate.fingerprint(treatment / "actor" / "skill"))

    def test_existing_run_cannot_be_overwritten(self):
        with self.assertRaises(ValueError):
            evaluate.prepare("P1", "control", self.run)

    def test_unfixed_or_extra_file_fails_even_with_positive_judgments(self):
        self.assertEqual(evaluate.grade(self.run, self.judgments())["status"], "fail")
        self.fix_fixture()
        self.assertEqual(evaluate.grade(self.run, self.judgments())["status"], "pass")
        (self.run / "actor" / "workspace" / "extra.txt").write_text("unrequested")
        self.assertEqual(evaluate.grade(self.run, self.judgments())["status"], "fail")

    def test_missing_or_unverified_check_never_passes(self):
        self.fix_fixture()
        judgments = self.judgments()
        key = next(iter(judgments["checks"]))
        judgments["checks"][key]["verdict"] = "unverified"
        self.assertEqual(evaluate.grade(self.run, judgments)["status"], "unverified")
        del judgments["checks"][key]
        with self.assertRaises(ValueError):
            evaluate.grade(self.run, judgments)

    def test_template_and_unsupported_pass_are_rejected(self):
        with self.assertRaises(ValueError):
            evaluate.grade(self.run, evaluate.read_json(self.run / "judgments.template.json"))
        judgments = self.judgments()
        next(iter(judgments["checks"].values()))["evidence"] = ""
        with self.assertRaises(ValueError):
            evaluate.grade(self.run, judgments)

    def test_unknown_cost_preserved_and_invalid_cost_rejected(self):
        result = evaluate.grade(self.run, self.judgments())
        self.assertIsNone(result["judgments"]["metrics"]["cost_usd"])
        for value in (-1, float("nan"), True):
            judgments = copy.deepcopy(self.judgments())
            judgments["metrics"]["cost_usd"] = value
            with self.assertRaises(ValueError):
                evaluate.grade(self.run, judgments)


if __name__ == "__main__":
    unittest.main()
