import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("snapshot.py")


class SnapshotTests(unittest.TestCase):
    def run_fixture(self, payload):
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
            json.dump(payload, handle)
            path = Path(handle.name)
        try:
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--fixture", str(path)],
                check=True,
                capture_output=True,
                text=True,
            )
            return json.loads(result.stdout)
        finally:
            path.unlink(missing_ok=True)

    def test_github_normalizes_facts_without_readiness(self):
        result = self.run_fixture(
            {
                "provider": "github",
                "host": "github.com",
                "repository": "qp/example",
                "core": {
                    "number": 7,
                    "url": "https://github.com/qp/example/pull/7",
                    "state": "OPEN",
                    "isDraft": False,
                    "baseRefName": "main",
                    "headRefName": "feature",
                    "headRefOid": "abc",
                    "mergeable": "MERGEABLE",
                    "reviewDecision": None,
                },
                "checks": [{"name": "test", "state": "SUCCESS", "required": True}],
                "checks_complete": True,
                "threads": {
                    "nodes": [
                        {
                            "id": "T1",
                            "isResolved": False,
                            "isOutdated": False,
                            "path": "app.py",
                            "line": 4,
                            "comments": {"nodes": [{"id": "C1", "body": "claim", "author": {"login": "reviewer"}}]},
                        }
                    ],
                    "pageInfo": {"hasNextPage": False},
                },
            }
        )
        self.assertEqual(result["head"]["sha"], "abc")
        self.assertEqual(result["feedback"][0]["id"], "T1")
        self.assertTrue(result["capabilities"]["feedback_complete"])
        self.assertNotIn("handoff_ready", result)
        self.assertNotIn("recommended_action", result)

    def test_github_marks_incomplete_feedback_pagination(self):
        result = self.run_fixture(
            {
                "provider": "github",
                "core": {
                    "number": 8,
                    "url": "https://github.com/qp/example/pull/8",
                    "state": "OPEN",
                    "isDraft": False,
                    "baseRefName": "main",
                    "headRefName": "feature",
                    "headRefOid": "def",
                    "mergeable": "UNKNOWN",
                },
                "checks": [],
                "threads": {"nodes": [], "pageInfo": {"hasNextPage": True}},
            }
        )
        self.assertFalse(result["capabilities"]["feedback_complete"])

    def test_gitlab_normalizes_pipeline_and_discussion(self):
        result = self.run_fixture(
            {
                "provider": "gitlab",
                "host": "gitlab.com",
                "repository": "qp/example",
                "core": {
                    "iid": 9,
                    "web_url": "https://gitlab.com/qp/example/-/merge_requests/9",
                    "state": "opened",
                    "draft": False,
                    "target_branch": "main",
                    "source_branch": "feature",
                    "sha": "123",
                    "detailed_merge_status": "mergeable",
                },
                "jobs": [{"id": 10, "name": "test", "status": "success", "web_url": "https://gitlab/jobs/10"}],
                "discussions": [
                    {
                        "id": "D1",
                        "notes": [
                            {"id": 11, "resolvable": True, "resolved": False, "body": "claim", "author": {"username": "reviewer"}}
                        ],
                    }
                ],
                "approvals": {"approved": False, "approvals_left": 1},
            }
        )
        self.assertEqual(result["number"], 9)
        self.assertEqual(result["checks"][0]["name"], "test")
        self.assertEqual(result["feedback"][0]["id"], "D1")


if __name__ == "__main__":
    unittest.main()
