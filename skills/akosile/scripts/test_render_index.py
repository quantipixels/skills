import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("render-index.py")


def run(workspace):
    return subprocess.run([sys.executable, str(SCRIPT), str(workspace)], capture_output=True, text=True)


def record(workspace, record_subject, **values):
    owner = values.pop("owner", "atona")
    bundle = workspace / "records" / owner / record_subject
    bundle.mkdir(parents=True)
    data = {
        "owner": owner,
        "record_type": "initiative-plan",
        "title": record_subject,
        "updated_at": "2026-08-28T05:00:00+01:00",
        "revision": 1,
        "status": "Draft",
        **values,
    }
    lines = []
    for key, value in data.items():
        encoded = json.dumps(value, ensure_ascii=False) if isinstance(value, str) else str(value)
        lines.append(f"{key}: {encoded}")
    (bundle / "record.md").write_text("---\n" + "\n".join(lines) + "\n---\n\nBody\n")
    return bundle


class RenderIndexTests(unittest.TestCase):
    def test_new_and_legacy_subjects_order_and_link(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory) / ".qp"
            workspace.mkdir()
            record(workspace, "payment-migration", updated_at="2026-08-28T10:00:00+02:00")
            legacy = record(workspace, "20260828-legacy", updated_at="2026-08-28T09:30:00+00:00")
            (legacy / "index.html").write_text("x")
            result = run(workspace)
            self.assertEqual(result.returncode, 0)
            self.assertLess(result.stdout.index("20260828-legacy"), result.stdout.index("payment-migration"))
            self.assertIn("20260828-legacy/index.html", result.stdout)

    def test_metadata_is_literal_not_markup(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory) / ".qp"
            workspace.mkdir()
            record(
                workspace, "hostile", title="<img src=x onerror=alert(1)>",
                status="[click](https://example.com)", record_type="foo|bar",
            )
            result = run(workspace)
            self.assertEqual(result.returncode, 0)
            self.assertNotIn("<img", result.stdout)
            self.assertNotIn("[click](", result.stdout)
            self.assertIn("foo\\|bar", result.stdout)

    def test_subject_mismatch_and_duplicate_yaml_surface_invalid(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory) / ".qp"
            workspace.mkdir()
            record(workspace, "right", subject="wrong")
            duplicate = workspace / "records/atona/dup"
            duplicate.mkdir(parents=True)
            (duplicate / "record.md").write_text("---\nowner: atona\nowner: alaga\n---\n")
            result = run(workspace)
            self.assertEqual(result.returncode, 0)
            self.assertIn("SUBJECT\\_PATH\\_MISMATCH", result.stdout)
            self.assertIn("INVALID\\_FRONTMATTER", result.stdout)

    def test_common_envelope_rejects_unsupported_yaml_forms(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory) / ".qp"
            workspace.mkdir()
            block = record(workspace, "block")
            block_record = block / "record.md"
            block_record.write_text(block_record.read_text().replace('title: "block"', "title: >\n  block"))
            sequence = record(workspace, "sequence")
            sequence_record = sequence / "record.md"
            sequence_record.write_text(sequence_record.read_text().replace('title: "sequence"', "title: [sequence]"))

            result = run(workspace)

            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.count("INVALID\\_FRONTMATTER"), 2)
            self.assertNotIn("| block |", result.stdout)
            self.assertNotIn("| sequence |", result.stdout)

    def test_supported_quotes_comments_and_nested_owner_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory) / ".qp"
            workspace.mkdir()
            bundle = record(workspace, "quoted")
            path = bundle / "record.md"
            text = path.read_text()
            text = text.replace('title: "quoted"', 'title: "Quoted # title" # visible title')
            text = text.replace('status: "Draft"', "status: 'Owner''s Draft' # current state")
            text = text.replace("---\n\nBody", "details:\n  tags: [one, two]\n---\n\nBody")
            path.write_text(text)

            result = run(workspace)

            self.assertEqual(result.returncode, 0)
            self.assertIn("Quoted # title", result.stdout)
            self.assertIn("Owner's Draft", result.stdout)
            self.assertNotIn("Invalid records", result.stdout)

    def test_missing_workspace_fails_without_creation(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory) / ".qp"
            result = run(workspace)
            self.assertEqual(result.returncode, 2)
            self.assertFalse(workspace.exists())


if __name__ == "__main__":
    unittest.main()
