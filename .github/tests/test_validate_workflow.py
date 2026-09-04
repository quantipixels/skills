from pathlib import Path
import unittest

import yaml


REPO_ROOT = Path(__file__).resolve().parents[2]
WORKFLOW = REPO_ROOT / ".github" / "workflows" / "validate.yml"


class ValidateWorkflowContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = yaml.load(WORKFLOW.read_text(), Loader=yaml.BaseLoader)
        cls.triggers = cls.workflow["on"]
        cls.jobs = cls.workflow["jobs"]

    def test_pull_requests_include_intermediate_stack_bases(self):
        self.assertIn("pull_request", self.triggers)
        pull_request = self.triggers["pull_request"]
        if isinstance(pull_request, dict):
            self.assertNotIn("branches", pull_request)
            self.assertNotIn("branches-ignore", pull_request)

    def test_ori_pushes_are_validated(self):
        push = self.triggers["push"]
        self.assertEqual(push["branches"], ["ori"])

    def test_merge_queue_candidates_are_validated(self):
        self.assertIn("merge_group", self.triggers)

    def test_compatibility_smoke_is_part_of_validation(self):
        compatibility = self.jobs["compatibility-smoke"]
        self.assertEqual(compatibility["name"], "Compatibility smoke")
        self.assertEqual(compatibility["env"]["SKILLS_CLI_VERSION"], "1.5.23")
        self.assertEqual(compatibility["env"]["CLAUDE_CODE_VERSION"], "2.1.260")
        runs = "\n".join(step.get("run", "") for step in compatibility["steps"])
        self.assertIn(
            "@anthropic-ai/claude-code@${CLAUDE_CODE_VERSION} plugin validate .",
            runs,
        )

    def test_portable_mechanics_cover_supported_os_families(self):
        portable = self.jobs["portable-mechanics"]
        self.assertEqual(portable["name"], "Portable mechanics (${{ matrix.os }})")
        self.assertEqual(
            set(portable["strategy"]["matrix"]["os"]),
            {"ubuntu-latest", "macos-latest", "windows-latest"},
        )
        runs = "\n".join(step.get("run", "") for step in portable["steps"])
        self.assertIn("scripts/test_uninstall.py", runs)
        self.assertIn("skills/engineering/akosile/scripts", runs)
        self.assertIn("skills/productivity/ayewo-igba-ise/scripts", runs)

    def test_exposes_one_stable_aggregate_check(self):
        validate = self.jobs["validate"]
        self.assertEqual(validate["name"], "Validate")
        self.assertEqual(
            set(validate["needs"]),
            {
                "package-state",
                "skill-package",
                "akosile-tests",
                "compatibility-smoke",
                "portable-mechanics",
            },
        )


if __name__ == "__main__":
    unittest.main()
