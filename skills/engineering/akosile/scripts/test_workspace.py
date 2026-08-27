import json
import subprocess
import tempfile
import threading
import time
import unittest
from pathlib import Path
from unittest.mock import patch

import akosile_workspace as workspace
import akosile_workspace.workspace_state as workspace_state



class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        subprocess.run(["git", "init", "-q", str(self.repo)], check=True)
        workspace.initialize(self.repo)

    def tearDown(self):
        self.tmp.cleanup()

    def frontmatter(self, **changes):
        value = {
            "owner": "atona",
            "record_type": "initiative-plan",
            "subject": "checkout-recovery",
            "title": "Checkout recovery",
            "candidate": "repo@abc",
            "status": "Draft",
        }
        value.update(changes)
        return value

    def allocate(self, subject="checkout-recovery", slug="checkout-recovery"):
        return workspace.resolve_record(
            self.repo,
            owner="atona",
            subject=subject,
            slug=slug,
            create=True,
        )

    def create_record(self, **changes):
        resolved = self.allocate(
            subject=changes.get("subject", "checkout-recovery"),
            slug=changes.get("slug", "checkout-recovery"),
        )
        frontmatter = self.frontmatter(**{key: value for key, value in changes.items() if key != "slug"})
        written = workspace.write_record(
            self.repo,
            resolved["record_ref"],
            frontmatter,
            "# Checkout recovery\n",
            "absent",
        )
        return resolved, written

    def test_init_uses_git_worktree_root_and_preserves_settings(self):
        settings = self.repo / ".qp/settings.json"
        settings.write_text('{"x": 1}\n', encoding="utf-8")
        nested = self.repo / "a/b"
        nested.mkdir(parents=True)
        result = workspace.initialize(nested)
        self.assertEqual(result["workspace"], str(self.repo / ".qp"))
        self.assertEqual(json.loads(settings.read_text()), {"x": 1})
        self.assertTrue((self.repo / ".qp/INDEX.md").exists())
        exclude = Path(
            subprocess.run(
                ["git", "-C", str(self.repo), "rev-parse", "--git-path", "info/exclude"],
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()
        )
        if not exclude.is_absolute():
            exclude = self.repo / exclude
        self.assertIn(".qp/", exclude.read_text())

    def test_malformed_settings_are_never_overwritten_by_init_or_repair(self):
        settings = self.repo / ".qp/settings.json"
        settings.write_text("{broken", encoding="utf-8")
        self.assertEqual(workspace.initialize(self.repo)["settings_state"], "INVALID_PRESERVED")
        workspace.repair(self.repo)
        self.assertEqual(settings.read_text(), "{broken")

    def test_record_and_artifact_html_use_real_slugs(self):
        record = self.allocate()
        self.assertEqual(record["projection_name"], "checkout-recovery.html")
        self.assertNotEqual(record["projection_name"], "index.html")
        artifact = workspace.resolve_artifact(
            self.repo, slug="architecture-review", create=True
        )
        self.assertEqual(artifact["html_name"], "architecture-review.html")
        self.assertTrue(
            artifact["html_workspace_path"].endswith("/architecture-review.html")
        )

    def test_record_identity_is_subject_not_title_or_candidate(self):
        created, _ = self.create_record()
        resolved = workspace.resolve_record(
            self.repo,
            owner="atona",
            subject="checkout-recovery",
            slug="different-title",
            create=True,
        )
        self.assertEqual(resolved["record_ref"], created["record_ref"])

    def test_legacy_record_without_subject_remains_readable_and_can_be_upgraded_exactly(self):
        bundle = self.repo / ".qp/records/atona/20260827-legacy-plan"
        bundle.mkdir(parents=True)
        record = bundle / "record.md"
        record.write_text(
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
        exact = workspace.read_record(self.repo, "atona/20260827-legacy-plan")
        self.assertNotIn("subject", exact["metadata"])
        with self.assertRaisesRegex(workspace.WorkspaceError, "exact record_ref update"):
            workspace.resolve_record(
                self.repo,
                owner="atona",
                subject="legacy-plan",
                slug="legacy-plan",
                create=True,
            )
        upgraded = workspace.write_record(
            self.repo,
            "atona/20260827-legacy-plan",
            self.frontmatter(subject="legacy-plan", title="Legacy plan"),
            "# Legacy plan\n",
            exact["digest"],
        )
        self.assertEqual(upgraded["revision"], 2)
        self.assertEqual(
            workspace.read_record(self.repo, "atona/20260827-legacy-plan")["metadata"]["subject"],
            "legacy-plan",
        )

    def test_yaml_frontmatter_supports_comments_quotes_and_folded_values(self):
        resolved = self.allocate()
        path = Path(resolved["record"])
        path.write_text(
            "---\n"
            "owner: atona\n"
            "record_type: initiative-plan\n"
            "subject: checkout-recovery\n"
            "title: >-\n  Checkout # recovery\n"
            "updated_at: 2026-08-27T20:00:00+01:00 # current instant\n"
            "revision: 1\n"
            "status: 'Draft # one'\n"
            "---\n\n# Body\n",
            encoding="utf-8",
        )
        data = workspace.read_record_data(self.repo, path)
        self.assertEqual(data["metadata"]["title"], "Checkout # recovery")
        self.assertEqual(data["metadata"]["status"], "Draft # one")
        self.assertIsInstance(data["metadata"]["updated_at"], str)

    def test_duplicate_yaml_keys_are_rejected(self):
        with self.assertRaises(workspace.WorkspaceError):
            workspace.split_record(
                "---\nowner: atona\nowner: alaga\n---\n\nBody\n"
            )

    def test_write_record_assigns_revision_timestamp_and_requires_cas(self):
        resolved, first = self.create_record()
        self.assertEqual(first["revision"], 1)
        current = workspace.read_record(self.repo, resolved["record_ref"])
        updated = workspace.write_record(
            self.repo,
            resolved["record_ref"],
            self.frontmatter(status="Planned"),
            "# Checkout recovery\n",
            current["digest"],
        )
        self.assertEqual(updated["revision"], 2)
        self.assertIn("+00:00", updated["updated_at"])
        with self.assertRaisesRegex(workspace.WorkspaceError, "changed since"):
            workspace.write_record(
                self.repo,
                resolved["record_ref"],
                self.frontmatter(status="Closed"),
                "# Checkout recovery\n",
                current["digest"],
            )

    def test_record_identity_fields_are_immutable(self):
        resolved, _ = self.create_record()
        current = workspace.read_record(self.repo, resolved["record_ref"])
        with self.assertRaisesRegex(workspace.WorkspaceError, "cannot change"):
            workspace.write_record(
                self.repo,
                resolved["record_ref"],
                self.frontmatter(subject="another-subject"),
                "# Changed\n",
                current["digest"],
            )

    def test_concurrent_writers_serialize_and_only_one_accepts_same_digest(self):
        resolved, _ = self.create_record()
        current = workspace.read_record(self.repo, resolved["record_ref"])
        barrier = threading.Barrier(3)
        outcomes = []

        def writer(status):
            barrier.wait()
            try:
                workspace.write_record(
                    self.repo,
                    resolved["record_ref"],
                    self.frontmatter(status=status),
                    f"# {status}\n",
                    current["digest"],
                )
                outcomes.append("ok")
            except workspace.WorkspaceError as error:
                outcomes.append(error.code)

        threads = [
            threading.Thread(target=writer, args=(status,))
            for status in ("Planned", "Closed")
        ]
        for thread in threads:
            thread.start()
        barrier.wait()
        for thread in threads:
            thread.join(timeout=5)
        self.assertCountEqual(outcomes, ["ok", "STALE_WRITE"])
        self.assertEqual(
            workspace.read_record(self.repo, resolved["record_ref"])["metadata"]["revision"],
            2,
        )

    def test_exact_record_allocation_is_serialized(self):
        ref = "atona/20260827-fixed-record"
        barrier = threading.Barrier(3)
        results = []

        def allocate_exact():
            barrier.wait()
            results.append(
                workspace.resolve_record(self.repo, record_ref=ref, create=True)["existing"]
            )

        threads = [threading.Thread(target=allocate_exact) for _ in range(2)]
        for thread in threads:
            thread.start()
        barrier.wait()
        for thread in threads:
            thread.join(timeout=5)
        self.assertCountEqual(results, [False, True])

    def test_verified_record_write_survives_index_rebuild_failure(self):
        resolved = self.allocate()
        with patch.object(workspace_state, "rebuild_index", side_effect=workspace.WorkspaceError("INDEX_FAILED", "index unavailable")):
            written = workspace.write_record(
                self.repo,
                resolved["record_ref"],
                self.frontmatter(),
                "# Checkout recovery\n",
                "absent",
            )
        self.assertEqual(written["index"]["state"], "FAILED")
        self.assertEqual(
            workspace.read_record(self.repo, resolved["record_ref"])["metadata"]["revision"],
            1,
        )

    def test_settings_compare_and_swap_preserves_unknown_sections(self):
        current = workspace.read_settings(self.repo)
        candidate = {
            "unknown": {"value": 1},
            "se-triage": {"labels": {"confirmed": "Confirmed"}},
        }
        written = workspace.write_settings(
            self.repo, json.dumps(candidate), current["digest"]
        )
        self.assertEqual(written["value"], candidate)
        with self.assertRaises(workspace.WorkspaceError):
            workspace.write_settings(self.repo, "{}", current["digest"])

    def test_index_sorts_by_instant_and_links_slug_projection(self):
        first, _ = self.create_record(subject="first", slug="first")
        second, _ = self.create_record(subject="second", slug="second")
        first_path, second_path = Path(first["record"]), Path(second["record"])
        first_path.write_text(
            first_path.read_text().replace(
                workspace.read_record_data(self.repo, first_path)["metadata"]["updated_at"],
                "2026-08-27T10:00:00+02:00",
            ),
            encoding="utf-8",
        )
        second_path.write_text(
            second_path.read_text().replace(
                workspace.read_record_data(self.repo, second_path)["metadata"]["updated_at"],
                "2026-08-27T09:30:00+00:00",
            ),
            encoding="utf-8",
        )
        Path(second["projection"]).write_text("<html></html>", encoding="utf-8")
        workspace.rebuild_index(self.repo)
        index = (self.repo / ".qp/INDEX.md").read_text()
        self.assertLess(index.index("second"), index.index("first"))
        self.assertIn("second.html", index)
        self.assertNotIn("index.html", index)

    def test_symlink_escape_is_rejected(self):
        outside = self.repo / "outside"
        outside.mkdir()
        owner = self.repo / ".qp/records/atona"
        if owner.exists():
            owner.rmdir()
        try:
            owner.symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest("symlinks unavailable")
        with self.assertRaises(workspace.WorkspaceError):
            workspace.resolve_record(
                self.repo,
                owner="atona",
                subject="escape",
                slug="escape",
                create=True,
            )

    def test_doctor_reports_symlinked_workspace_component_without_following_it(self):
        records = self.repo / ".qp/records"
        outside = self.repo / "outside-records"
        outside.mkdir()
        records.rmdir()
        try:
            records.symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest("symlinks unavailable")
        result = workspace.doctor(self.repo)
        self.assertEqual(result["status"], "ISSUES_FOUND")
        self.assertIn("SYMLINK_ESCAPE", [item["code"] for item in result["issues"]])

    def test_doctor_reports_legacy_index_html_and_repair_does_not_migrate_it(self):
        artifact = workspace.resolve_artifact(
            self.repo, slug="legacy-report", create=True
        )
        legacy = Path(artifact["bundle"]) / "index.html"
        legacy.write_text("<html></html>", encoding="utf-8")
        issues = workspace.doctor(self.repo)["issues"]
        self.assertIn("LEGACY_INDEX_HTML", [item["code"] for item in issues])
        workspace.repair(self.repo)
        self.assertTrue(legacy.exists())
        self.assertFalse(Path(artifact["html"]).exists())


if __name__ == "__main__":
    unittest.main()
