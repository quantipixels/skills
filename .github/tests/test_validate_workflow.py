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
        self.assertEqual(self.triggers["push"]["branches"], ["ori"])

    def test_merge_queue_candidates_are_validated(self):
        self.assertIn("merge_group", self.triggers)

    def test_compatibility_smoke_proves_claimed_native_paths(self):
        compatibility = self.jobs["compatibility-smoke"]
        runs = "\n".join(step.get("run", "") for step in compatibility["steps"])
        self.assertIn("skills@${SKILLS_CLI_VERSION}", runs)
        self.assertIn("@anthropic-ai/claude-code@${CLAUDE_CODE_VERSION} plugin validate .", runs)
        self.assertIn('plugin marketplace add "$GITHUB_WORKSPACE" --scope user', runs)
        self.assertIn("plugin install qp-skills@qp-skills --scope user", runs)
        self.assertIn("plugin list --json", runs)

    def test_linux_proof_is_not_duplicated_in_portable_matrix(self):
        portable = self.jobs["portable-mechanics"]
        self.assertEqual(set(portable["strategy"]["matrix"]["os"]), {"macos-latest", "windows-latest"})
        skill_runs = "\n".join(step.get("run", "") for step in self.jobs["skill-package"]["steps"])
        self.assertIn("scripts/test_uninstall.py", skill_runs)

    def test_native_validators_are_separate_steps(self):
        commands = [step.get("run", "") for step in self.jobs["portable-mechanics"]["steps"]]
        self.assertTrue(any("validate-package.py" in command for command in commands))
        self.assertTrue(any("validate-plugin-agents.py" in command for command in commands))
        self.assertFalse(any("validate-package.py" in command and "validate-plugin-agents.py" in command for command in commands))

    def test_exposes_one_stable_aggregate_check(self):
        validate = self.jobs["validate"]
        self.assertEqual(validate["name"], "Validate")
        self.assertEqual(set(validate["needs"]), {"package-state", "skill-package", "akosile-tests", "compatibility-smoke", "portable-mechanics"})


if __name__ == "__main__":
    unittest.main()
