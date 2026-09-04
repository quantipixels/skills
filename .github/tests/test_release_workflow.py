from pathlib import Path
import unittest

import yaml


REPO_ROOT = Path(__file__).resolve().parents[2]
WORKFLOW = REPO_ROOT / ".github" / "workflows" / "release.yml"


class ReleaseWorkflowContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = yaml.load(WORKFLOW.read_text(), Loader=yaml.BaseLoader)
        cls.triggers = cls.workflow["on"]
        cls.jobs = cls.workflow["jobs"]

    def test_release_is_driven_from_ori(self):
        self.assertEqual(self.triggers["push"]["branches"], ["ori"])

    def test_changesets_remains_version_and_tag_owner(self):
        release = self.jobs["release"]
        changesets = next(
            step for step in release["steps"] if step.get("uses") == "changesets/action@v1"
        )
        self.assertEqual(changesets["with"]["version"], "npm run version")
        self.assertEqual(changesets["with"]["publish"], "npx changeset tag")
        self.assertEqual(changesets["with"]["commit"], "chore: version skills")
        self.assertEqual(changesets["with"]["title"], "chore: version skills")


if __name__ == "__main__":
    unittest.main()
