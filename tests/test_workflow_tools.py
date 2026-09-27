"""Behavioral checks for bounded workflow discovery and privacy preflight."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills/alarina/scripts"))

from workflow_tools import (
    inventory_workflows,
    inspect_contribution,
    validate_workflow,
)


def recipe(**changes: object) -> str:
    data: dict[str, object] = {
        "version": 1,
        "id": "check-cli",
        "title": "Check CLI behavior",
        "scope": "project",
        "status": "verified",
        "assumptions": ["The project supplies a runnable CLI"],
        "steps": [{"method": "alaga-verify-project", "requires": ["CLI build"], "produces": ["output proof"]}],
        "evidence": [{"result": "passed", "locator": "local-proof.txt", "candidate": "commit abc123"}],
        "retirement": "Recheck when the CLI entrypoint changes",
    }
    data.update(changes)
    return "```alarina-workflow+json\n" + json.dumps(data) + "\n```\n\n# Reader guidance\n"


def proposal(**changes: object) -> str:
    data: dict[str, object] = {
        "version": 1,
        "purpose": "Help agents verify a CLI after changing its output",
        "generic_change": "Record the start command and observed output",
        "synthetic_example": "A demo CLI prints READY",
        "challenges": ["A stale build can look healthy"],
        "benefits": ["The next engineer can repeat the check"],
        "evidence_limits": "One synthetic journey does not prove all commands",
        "sanitized_test_result": "Synthetic example passed locally",
    }
    data.update(changes)
    return "```alarina-contribution+json\n" + json.dumps(data, indent=2) + "\n```\n"


class WorkflowToolsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, name: str, content: str) -> Path:
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_unstructured_markdown_is_not_a_workflow_recipe(self) -> None:
        result = validate_workflow(self.write("plain.md", "# Working path\nUse the existing test command.\n"))
        self.assertEqual(result["classification"], "invalid")
        self.assertFalse(result["usable_as_guidance"])
        self.assertEqual(result["errors"][0]["code"], "unstructured")
        self.assertEqual(result["semantic_verification"], "not-assessed")

    def test_structured_verified_requires_proof_and_assumptions(self) -> None:
        path = self.write("empty-proof.md", recipe(evidence=[]))
        result = validate_workflow(path)
        self.assertEqual(result["classification"], "invalid")
        self.assertIn("verified-proof", {error["code"] for error in result["errors"]})
        path.write_text(recipe(assumptions=[]), encoding="utf-8")
        result = validate_workflow(path)
        self.assertIn("assumptions", {error["code"] for error in result["errors"]})

    def test_retired_recipe_is_indexed_but_not_active(self) -> None:
        result = validate_workflow(self.write("retired.md", recipe(status="retired")))
        self.assertEqual(result["classification"], "structured")
        self.assertFalse(result["usable_as_guidance"])
        self.assertEqual(result["metadata"]["status"], "retired")

    def test_malformed_json_is_actionable(self) -> None:
        result = validate_workflow(self.write("broken.md", "```alarina-workflow+json\n{invalid\n```\n"))
        self.assertEqual(result["classification"], "invalid")
        self.assertEqual(result["errors"][0]["code"], "malformed-json")

    def test_duplicate_workflow_key_fails_closed(self) -> None:
        content = recipe().replace('"id": "check-cli",', '"id": "check-cli", "id": "other-id",')
        result = validate_workflow(self.write("duplicate.md", content))
        self.assertEqual(result["classification"], "invalid")
        self.assertEqual(result["errors"][0]["code"], "duplicate-key")
        self.assertFalse(result["usable_as_guidance"])

    def test_inventory_sorts_and_surfaces_duplicate_ids(self) -> None:
        self.write("z.md", recipe())
        self.write("nested/a.md", recipe(title="Other title"))
        result = inventory_workflows([self.root])
        self.assertEqual([Path(item["path"]).name for item in result["workflows"]], ["a.md", "z.md"])
        self.assertEqual(len(result["duplicates"]["check-cli"]), 2)
        self.assertIn("duplicate-id", {error["code"] for error in result["errors"]})

    def test_inventory_does_not_follow_directory_or_file_symlinks(self) -> None:
        other = tempfile.TemporaryDirectory()
        self.addCleanup(other.cleanup)
        external = Path(other.name)
        (external / "private.md").write_text(recipe(id="private-recipe"), encoding="utf-8")
        (self.root / "linked").symlink_to(external, target_is_directory=True)
        (self.root / "linked-file.md").symlink_to(external / "private.md")
        result = inventory_workflows([self.root])
        self.assertEqual(len(result["workflows"]), 1)
        self.assertEqual(result["workflows"][0]["classification"], "invalid")
        self.assertEqual(result["workflows"][0]["errors"][0]["code"], "symlink")
        self.assertIn("directory-symlink", {error["code"] for error in result["errors"]})
        self.assertNotIn("private-recipe", result["duplicates"])

    def test_missing_root_is_reported(self) -> None:
        result = inventory_workflows([self.root / "missing"])
        self.assertEqual(result["workflows"], [])
        self.assertEqual(result["errors"][0]["code"], "root-unavailable")

    def test_contribution_flags_secrets_without_echoing_them(self) -> None:
        secret = "ghp_ABCDEF1234567890"
        email = "person@company.internal"
        content = proposal(generic_change=f"Use token={secret} for {email} at /Users/alice/private")
        result = inspect_contribution(self.write("candidate.md", content))
        self.assertEqual(result["status"], "needs-human-review")
        categories = {finding["category"] for finding in result["findings"]}
        self.assertTrue({"secret-value", "email", "home-path"}.issubset(categories))
        serialized = json.dumps(result)
        self.assertNotIn(secret, serialized)
        self.assertNotIn(email, serialized)
        self.assertNotIn("alice", serialized)

    def test_contribution_flags_private_url_key_and_transcript(self) -> None:
        content = proposal(synthetic_example="https://intranet.corp/private\n-----BEGIN PRIVATE KEY-----\nagent-transcripts/run.jsonl")
        result = inspect_contribution(self.write("candidate.md", content))
        categories = {finding["category"] for finding in result["findings"]}
        self.assertTrue({"private-url", "private-key", "transcript-dump"}.issubset(categories))

    def test_decoded_json_values_cannot_hide_escaped_private_data(self) -> None:
        value = r'\u002fUsers\u002falice\u002fwork'
        content = proposal(generic_change="/Users/alice/work").replace("/Users/alice/work", value)
        result = inspect_contribution(self.write("encoded.md", content))
        self.assertTrue(any(
            finding["category"] == "home-path" and finding["source"] == "decoded-field"
            and finding["field"] == "generic_change"
            for finding in result["findings"]
        ))
        self.assertNotIn("alice", json.dumps(result))

    def test_decoded_windows_path_json_token_and_private_addresses(self) -> None:
        text = r'C:\Users\alice\private; {"token":"value123"}; {"role":"user"}; 10.2.3.4 192.168.1.2 fd00::1 ::1; Bearer value123'
        result = inspect_contribution(self.write("candidate.md", proposal(generic_change=text)))
        decoded = {finding["category"] for finding in result["findings"] if finding["source"] == "decoded-field"}
        self.assertTrue({"home-path", "secret-value", "private-address", "transcript-dump"}.issubset(decoded))
        self.assertNotIn("value123", json.dumps(result))
        self.assertNotIn("alice", json.dumps(result))

    def test_duplicate_contribution_key_and_malformed_block_fail_closed(self) -> None:
        content = proposal().replace('"purpose": "Help agents', '"purpose": "Hidden", "purpose": "Help agents')
        result = inspect_contribution(self.write("duplicate.md", content))
        self.assertEqual(result["status"], "needs-human-review")
        self.assertIn("duplicate-key", {error["code"] for error in result["errors"]})
        self.assertNotIn("Hidden", json.dumps(result))
        malformed = inspect_contribution(self.write("malformed.md", "```alarina-contribution+json\n{bad\n```\n"))
        self.assertIn("malformed-json", {error["code"] for error in malformed["errors"]})

    def test_clean_synthetic_proposal_is_only_no_patterns_found(self) -> None:
        result = inspect_contribution(self.write("candidate.md", proposal()))
        self.assertEqual(result["status"], "no-patterns-found")
        self.assertIn("Human review is required", result["notice"])
        self.assertEqual(result["findings"], [])

    def test_contribution_rejects_unlisted_content_and_fields(self) -> None:
        hidden_key = "secret_api_key_ABCDEF123456"
        content = proposal(**{hidden_key: "not for export"}) + "Additional unreviewed body\n"
        result = inspect_contribution(self.write("candidate.md", content))
        codes = {error["code"] for error in result["errors"]}
        self.assertIn("unknown-fields", codes)
        self.assertIn("outside-content", codes)
        self.assertEqual(result["status"], "needs-human-review")
        self.assertNotIn(hidden_key, json.dumps(result))


if __name__ == "__main__":
    unittest.main()
