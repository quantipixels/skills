import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

SCRIPT = Path(__file__).with_name("render-index.py")


def invoke(workspace: Path, output: Path) -> tuple[int, dict]:
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--workspace", str(workspace), "--output", str(output)],
        check=False,
        capture_output=True,
        text=True,
    )
    return result.returncode, json.loads(result.stdout)


def write_record(
    workspace: Path,
    *,
    owner: str,
    record_id: str,
    title: str,
    updated_at: str,
    record_type: str = "initiative-plan",
    status: str = "Draft",
    revision: int = 1,
) -> Path:
    bundle = workspace / "records" / owner / record_id
    bundle.mkdir(parents=True)
    metadata = {
        "owner": owner,
        "record_type": record_type,
        "title": title,
        "updated_at": updated_at,
        "revision": revision,
        "status": status,
    }
    record = bundle / "record.md"
    record.write_text(
        "---\n" + yaml.safe_dump(metadata, sort_keys=False) + "---\n\n# Body\n",
        encoding="utf-8",
    )
    return record


class RenderIndexTests(unittest.TestCase):
    def test_sorts_by_instant_and_links_real_collision_slug(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory) / ".qp"
            workspace.mkdir()
            output = Path(directory) / "INDEX.candidate.md"
            write_record(
                workspace,
                owner="atona",
                record_id="20260828-first",
                title="First",
                updated_at="2026-08-28T10:00:00+02:00",
            )
            second = write_record(
                workspace,
                owner="atona",
                record_id="20260828-second-2",
                title="Second",
                updated_at="2026-08-28T09:30:00+00:00",
                record_type="initiative/plan-v2",
            )
            (second.parent / "second-2.html").write_text("<html></html>", encoding="utf-8")
            (second.parent / "index.html").write_text("<html></html>", encoding="utf-8")

            code, payload = invoke(workspace, output)
            self.assertEqual(code, 0)
            index = output.read_text(encoding="utf-8")
            self.assertLess(index.index("Second"), index.index("First"))
            self.assertIn("records/atona/20260828-second-2/second-2.html", index)
            self.assertIn("initiative/plan-v2", index)
            self.assertIn("## Legacy HTML entrypoints", index)
            self.assertEqual(len(payload["result"]["legacy_html"]), 1)
            self.assertFalse((workspace / "INDEX.md").exists())

    def test_valid_yaml_comments_quotes_and_folded_title(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory) / ".qp"
            bundle = workspace / "records" / "atona" / "20260828-yaml"
            bundle.mkdir(parents=True)
            output = Path(directory) / "candidate.md"
            (bundle / "record.md").write_text(
                "---\n"
                "owner: atona\n"
                "record_type: initiative-plan\n"
                "title: >-\n  Checkout # recovery\n"
                "updated_at: 2026-08-28T05:00:00+01:00 # current instant\n"
                "revision: 1\n"
                "status: 'Draft # one'\n"
                "---\n\n# Body\n",
                encoding="utf-8",
            )

            code, payload = invoke(workspace, output)
            self.assertEqual(code, 0)
            self.assertEqual(payload["result"]["invalid"], [])
            index = output.read_text(encoding="utf-8")
            self.assertIn("Checkout # recovery", index)
            self.assertIn("Draft # one", index)

    def test_invalid_records_remain_visible_diagnostics(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory) / ".qp"
            output = Path(directory) / "candidate.md"
            duplicate = workspace / "records" / "atona" / "20260828-duplicate"
            duplicate.mkdir(parents=True)
            (duplicate / "record.md").write_text(
                "---\nowner: atona\nowner: alaga\n---\n\nBody\n",
                encoding="utf-8",
            )
            write_record(
                workspace,
                owner="atona",
                record_id="20260828-bad-time",
                title="Bad time",
                updated_at="not-a-time",
            )
            mismatch = write_record(
                workspace,
                owner="atona",
                record_id="20260828-mismatch",
                title="Mismatch",
                updated_at="2026-08-28T05:00:00+01:00",
            )
            mismatch.write_text(
                mismatch.read_text(encoding="utf-8").replace("owner: atona", "owner: alaga"),
                encoding="utf-8",
            )

            code, payload = invoke(workspace, output)
            self.assertEqual(code, 0)
            self.assertEqual(
                {item["code"] for item in payload["result"]["invalid"]},
                {"INVALID_FRONTMATTER", "INVALID_UPDATED_AT", "OWNER_PATH_MISMATCH"},
            )
            index = output.read_text(encoding="utf-8")
            self.assertIn("## Invalid records", index)
            self.assertIn("20260828-duplicate", index)
            self.assertIn("20260828-bad-time", index)
            self.assertIn("20260828-mismatch", index)

    def test_rejects_symlinked_record_path(self) -> None:
        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as outside:
            workspace = Path(directory) / ".qp"
            output = Path(directory) / "candidate.md"
            bundle = workspace / "records" / "atona" / "20260828-linked"
            bundle.mkdir(parents=True)
            outside_record = Path(outside) / "record.md"
            outside_record.write_text("outside\n", encoding="utf-8")
            try:
                (bundle / "record.md").symlink_to(outside_record)
            except OSError:
                self.skipTest("symlinks unavailable")

            code, payload = invoke(workspace, output)
            self.assertEqual(code, 0)
            self.assertEqual(payload["result"]["invalid"][0]["code"], "SYMLINK_PATH")

    def test_missing_workspace_and_symlink_output_fail_without_initializing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / ".qp"
            output = Path(directory) / "candidate.md"
            code, payload = invoke(missing, output)
            self.assertEqual(code, 2)
            self.assertEqual(payload["error"]["code"], "WORKSPACE_MISSING")
            self.assertFalse(missing.exists())

            workspace = Path(directory) / "present"
            workspace.mkdir()
            outside = Path(directory) / "outside.md"
            outside.write_text("outside\n", encoding="utf-8")
            linked_output = Path(directory) / "linked.md"
            try:
                linked_output.symlink_to(outside)
            except OSError:
                self.skipTest("symlinks unavailable")
            code, payload = invoke(workspace, linked_output)
            self.assertEqual(code, 2)
            self.assertEqual(payload["error"]["code"], "SYMLINK_OUTPUT")
            self.assertEqual(outside.read_text(encoding="utf-8"), "outside\n")

            code, payload = invoke(workspace, workspace / "INDEX.md")
            self.assertEqual(code, 2)
            self.assertEqual(payload["error"]["code"], "OUTPUT_INSIDE_WORKSPACE")
            self.assertFalse((workspace / "INDEX.md").exists())


if __name__ == "__main__":
    unittest.main()
