"""Protect delivery-profile enforcement through the actual artifact CLI."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[2] / "skills/alarina/scripts/verify_artifact.py"
REMOTE = '<link rel="stylesheet" href="https://example.invalid/style.css">'


class DeliveryProfileTest(unittest.TestCase):
    def check_document(self, attributes, content, status, profile, diagnostic=None):
        document = (
            f'<!doctype html><html lang="en" {attributes}><head><title>Report</title>'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'{content}</head><body><h1>Report</h1></body></html>'
        )
        with tempfile.TemporaryDirectory(prefix="qp-artifact-test-") as temporary:
            artifact = Path(temporary) / "report.html"
            artifact.write_text(document, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(artifact), "--json"],
                capture_output=True, text=True, timeout=10,
            )
        self.assertEqual(result.returncode, status, result.stdout + result.stderr)
        evidence = json.loads(result.stdout)
        self.assertEqual(evidence["deliveryProfile"], profile)
        if diagnostic:
            self.assertIn(diagnostic, [item["code"] for item in evidence["diagnostics"]])

    def test_missing_or_misspelled_marker_cannot_pass_as_connected(self):
        for attributes in ("", 'data-delivery="portable"'):
            with self.subTest(attributes=attributes):
                self.check_document(attributes, REMOTE, 1, None, "delivery-missing")

    def test_declared_profile_controls_remote_resource_check(self):
        for profile, content, status in (
            ("portable", "", 0), ("portable", REMOTE, 1),
            ("connected", REMOTE, 0), ("host", REMOTE, 0),
        ):
            with self.subTest(profile=profile, remote=bool(content)):
                self.check_document(
                    f'data-artifact-delivery="{profile}"', content, status, profile,
                    "portable-remote" if status else None,
                )

    def test_existing_manifest_only_delivery_is_enforced_and_conflicts_fail(self):
        manifest = {
            "schemaVersion": 1, "artifactId": "example", "revision": "1",
            "sourceCut": [], "delivery": "portable", "interactionState": "transient",
            "dependencies": [],
        }
        content = '<script type="application/json" id="qp-artifact-manifest">' + json.dumps(manifest) + '</script>'
        self.check_document("", content, 0, "portable")
        self.check_document("", content + REMOTE, 1, "portable", "portable-remote")
        self.check_document('data-artifact-delivery="connected"', content, 1, "connected", "manifest-invalid")


if __name__ == "__main__":
    unittest.main()
