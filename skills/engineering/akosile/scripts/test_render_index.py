import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

SCRIPT = Path(__file__).with_name("render-index.py")


def run(workspace, output):
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--workspace", str(workspace), "--output", str(output)],
        capture_output=True,
        text=True,
    )
    return result.returncode, json.loads(result.stdout)


def record(workspace, record_id, *, owner="atona", updated="2026-08-28T05:00:00+01:00", **values):
    bundle = workspace / "records" / owner / record_id
    bundle.mkdir(parents=True)
    data = {
        "owner": owner,
        "record_type": "initiative-plan",
        "title": record_id,
        "updated_at": updated,
        "revision": 1,
        "status": "Draft",
        **values,
    }
    path = bundle / "record.md"
    path.write_text("---\n" + yaml.safe_dump(data, sort_keys=False) + "---\n\nBody\n")
    return path


class RenderIndexTests(unittest.TestCase):
    def test_orders_instants_and_uses_real_collision_slug(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            workspace, output = base / ".qp", base / "candidate.md"
            workspace.mkdir()
            record(workspace, "20260828-first", updated="2026-08-28T10:00:00+02:00")
            second = record(
                workspace,
                "20260828-second-2",
                updated="2026-08-28T09:30:00+00:00",
                record_type="initiative/plan-v2",
            )
            (second.parent / "second-2.html").write_text("<html></html>")
            (second.parent / "index.html").write_text("<html></html>")
            code, payload = run(workspace, output)
            text = output.read_text()
            self.assertEqual(code, 0)
            self.assertLess(text.index("second-2"), text.index("first"))
            self.assertIn("second-2.html", text)
            self.assertIn("initiative/plan-v2", text)
            self.assertEqual(len(payload["result"]["legacy_html"]), 1)
            self.assertFalse((workspace / "INDEX.md").exists())

    def test_parses_yaml_and_surfaces_invalid_records(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            workspace, output = base / ".qp", base / "candidate.md"
            bundle = workspace / "records/atona/20260828-valid"
            bundle.mkdir(parents=True)
            (bundle / "record.md").write_text(
                "---\nowner: atona\nrecord_type: initiative-plan\n"
                "title: >-\n  Checkout # recovery\n"
                "updated_at: 2026-08-28T05:00:00+01:00 # now\n"
                "revision: 1\nstatus: 'Draft # one'\n---\n\nBody\n"
            )
            bad = workspace / "records/atona/20260828-duplicate"
            bad.mkdir(parents=True)
            (bad / "record.md").write_text("---\nowner: atona\nowner: alaga\n---\n")
            record(workspace, "20260828-bad-time", updated="not-a-time")
            code, payload = run(workspace, output)
            self.assertEqual(code, 0)
            self.assertEqual(
                {item["code"] for item in payload["result"]["invalid"]},
                {"INVALID_FRONTMATTER", "INVALID_UPDATED_AT"},
            )
            text = output.read_text()
            self.assertIn("Checkout # recovery", text)
            self.assertIn("Draft # one", text)
            self.assertIn("## Invalid records", text)

    def test_rejects_authoritative_or_symlinked_output(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            workspace = base / ".qp"
            workspace.mkdir()
            code, payload = run(workspace, workspace / "INDEX.md")
            self.assertEqual((code, payload["error"]["code"]), (2, "OUTPUT_INSIDE_WORKSPACE"))
            linked = base / "linked"
            try:
                linked.symlink_to(workspace, target_is_directory=True)
            except OSError:
                return
            code, payload = run(workspace, linked / "candidate.md")
            self.assertEqual((code, payload["error"]["code"]), (2, "OUTPUT_INSIDE_WORKSPACE"))
            self.assertFalse((workspace / "candidate.md").exists())

    def test_missing_or_malformed_workspace_does_not_initialize(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory) / ".qp"
            output = Path(directory) / "candidate.md"
            code, payload = run(workspace, output)
            self.assertEqual((code, payload["error"]["code"]), (2, "WORKSPACE_MISSING"))
            self.assertFalse(workspace.exists())

            workspace.mkdir()
            (workspace / "records").write_text("not a directory")
            code, payload = run(workspace, output)
            self.assertEqual((code, payload["error"]["code"]), (2, "INVALID_RECORDS"))
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
