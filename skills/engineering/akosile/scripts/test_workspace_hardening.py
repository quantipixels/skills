import shutil
import subprocess
import tempfile
import threading
import unittest
from pathlib import Path
from unittest.mock import patch

import akosile_workspace as workspace
import akosile_workspace.workspace_state as workspace_state


class WorkspaceHardeningTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        subprocess.run(["git", "init", "-q", str(self.repo)], check=True)
        workspace.initialize(self.repo)

    def tearDown(self):
        self.tmp.cleanup()

    @staticmethod
    def frontmatter(subject="checkout-recovery", **changes):
        value = {
            "owner": "atona",
            "record_type": "initiative-plan",
            "subject": subject,
            "title": "Checkout recovery",
            "candidate": "repo@abc",
            "status": "Draft",
        }
        value.update(changes)
        return value

    def create_record(self, subject, slug):
        resolved = workspace.resolve_record(
            self.repo, owner="atona", subject=subject, slug=slug, create=True
        )
        workspace.write_record(
            self.repo,
            resolved["record_ref"],
            self.frontmatter(subject),
            f"# {subject}\n",
            "absent",
        )
        return resolved

    def test_read_only_resolution_does_not_initialize_workspace(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            self.assertFalse(
                workspace.resolve_record(
                    repo,
                    owner="atona",
                    subject="absent-plan",
                    slug="absent-plan",
                    create=False,
                )["existing"]
            )
            self.assertFalse(
                workspace.resolve_record(
                    repo, record_ref="atona/20260827-absent-plan", create=False
                )["existing"]
            )
            artifact = workspace.resolve_artifact(
                repo, slug="absent-report", create=False
            )
            exact = workspace.resolve_artifact(
                repo, artifact_id="20260827-absent-report", create=False
            )
            self.assertEqual(artifact["expected_html_name"], "absent-report.html")
            self.assertTrue(exact["html"].endswith("/absent-report.html"))
            self.assertFalse((repo / ".qp").exists())

    def test_record_type_remains_owner_native(self):
        resolved = workspace.resolve_record(
            self.repo,
            owner="atona",
            subject="custom-type",
            slug="custom-type",
            create=True,
        )
        workspace.write_record(
            self.repo,
            resolved["record_ref"],
            self.frontmatter("custom-type", record_type="architecture/v1"),
            "# Custom type\n",
            "absent",
        )
        self.assertEqual(
            workspace.read_record(self.repo, resolved["record_ref"])["metadata"]["record_type"],
            "architecture/v1",
        )

    def test_exact_write_cannot_duplicate_owner_subject_identity(self):
        self.create_record("shared-subject", "first-shared")
        second_ref = "atona/20260827-second-shared"
        with self.assertRaises(workspace.WorkspaceError) as raised:
            workspace.write_record(
                self.repo,
                second_ref,
                self.frontmatter("shared-subject", title="Second shared"),
                "# Second shared\n",
                "absent",
            )
        self.assertEqual(raised.exception.code, "DUPLICATE_SUBJECT")
        self.assertFalse((self.repo / ".qp/records/atona/20260827-second-shared").exists())

    def test_concurrent_exact_writes_enforce_unique_subject(self):
        barrier = threading.Barrier(3)
        outcomes = []

        def writer(record_ref, title):
            barrier.wait()
            try:
                workspace.write_record(
                    self.repo,
                    record_ref,
                    self.frontmatter("concurrent-subject", title=title),
                    f"# {title}\n",
                    "absent",
                )
                outcomes.append("ok")
            except workspace.WorkspaceError as error:
                outcomes.append(error.code)

        threads = [
            threading.Thread(
                target=writer,
                args=("atona/20260827-concurrent-one", "Concurrent one"),
            ),
            threading.Thread(
                target=writer,
                args=("atona/20260827-concurrent-two", "Concurrent two"),
            ),
        ]
        for thread in threads:
            thread.start()
        barrier.wait()
        for thread in threads:
            thread.join(timeout=5)
        self.assertCountEqual(outcomes, ["ok", "DUPLICATE_SUBJECT"])

    def test_exact_artifact_allocation_is_serialized(self):
        barrier = threading.Barrier(3)
        results = []

        def allocate():
            barrier.wait()
            results.append(
                workspace.resolve_artifact(
                    self.repo,
                    artifact_id="20260827-fixed-artifact",
                    create=True,
                )["existing"]
            )

        threads = [threading.Thread(target=allocate) for _ in range(2)]
        for thread in threads:
            thread.start()
        barrier.wait()
        for thread in threads:
            thread.join(timeout=5)
        self.assertCountEqual(results, [False, True])

    def test_verified_record_survives_real_index_io_failure(self):
        resolved = workspace.resolve_record(
            self.repo,
            owner="atona",
            subject="index-failure",
            slug="index-failure",
            create=True,
        )
        with patch.object(
            workspace_state, "rebuild_index", side_effect=OSError("disk unavailable")
        ):
            written = workspace.write_record(
                self.repo,
                resolved["record_ref"],
                self.frontmatter("index-failure"),
                "# Index failure\n",
                "absent",
            )
        self.assertEqual(written["index"]["error"]["code"], "INDEX_WRITE_FAILED")
        self.assertEqual(
            workspace.read_record(self.repo, resolved["record_ref"])["metadata"]["revision"],
            1,
        )

    def test_doctor_reports_missing_subject_and_record_legacy_index(self):
        bundle = self.repo / ".qp/records/atona/20260827-legacy-plan"
        bundle.mkdir(parents=True)
        (bundle / "record.md").write_text(
            "---\n"
            "owner: atona\n"
            "record_type: initiative-plan\n"
            "title: Legacy plan\n"
            "updated_at: 2026-08-27T20:00:00+01:00\n"
            "revision: 1\n"
            "status: Draft\n"
            "---\n\n# Legacy plan\n",
            encoding="utf-8",
        )
        (bundle / "index.html").write_text("<html></html>", encoding="utf-8")
        issues = workspace.doctor(self.repo)["issues"]
        self.assertIn("MISSING_SUBJECT", [item["code"] for item in issues])
        legacy = [item for item in issues if item["code"] == "LEGACY_INDEX_HTML"]
        self.assertEqual(len(legacy), 1)
        self.assertTrue(legacy[0]["expected"].endswith("/legacy-plan.html"))

    def test_doctor_reports_workspace_root_symlink_and_repair_stops(self):
        shutil.rmtree(self.repo / ".qp")
        outside = self.repo / "outside-workspace"
        outside.mkdir()
        try:
            (self.repo / ".qp").symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest("symlinks unavailable")
        diagnosed = workspace.doctor(self.repo)
        self.assertEqual(diagnosed["issues"][0]["code"], "SYMLINK_ESCAPE")
        repaired = workspace.repair(self.repo)
        self.assertEqual(repaired["changed"]["state"], "BLOCKED")
        self.assertEqual(list(outside.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
