"""Falsifiable tests for the structural checker, not prompt wording."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/html-artifact/scripts/verify_artifact.py'
spec = importlib.util.spec_from_file_location('verify_artifact', SCRIPT)
verifier = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verifier)


def document(body='', profile='portable'):
    return f'<!doctype html><html lang="en" data-artifact-delivery="{profile}"><head><meta name="viewport" content="width=device-width"><title>Review</title></head><body>{body}</body></html>'


def manifest(**overrides):
    value = dict(schemaVersion=1, artifactId='test', revision='1', sourceCut=[], delivery='portable', interactionState='transient', dependencies=[])
    value.update(overrides)
    return '<script type="application/json" id="qp-artifact-manifest">' + json.dumps(value).replace('<', r'\u003c') + '</script>'


class StructuralTests(unittest.TestCase):
    def codes(self, html):
        return {item['code'] for item in verifier.inspect_html(html)['diagnostics']}

    def test_small_document_needs_no_manifest(self):
        self.assertTrue(verifier.inspect_html(document('<h1>Small</h1>'))['ok'])

    def test_duplicate_id_rejected(self):
        self.assertIn('duplicate-id', self.codes(document('<p id="x"></p><p id="x"></p>')))

    def test_fragment_missing_and_encoded_target(self):
        self.assertIn('missing-target', self.codes(document('<a href="#missing">Go</a>')))
        self.assertNotIn('missing-target', self.codes(document('<a href="#caf%C3%A9">Go</a><p id="café"></p>')))

    def test_aria_and_view_targets(self):
        self.assertIn('missing-target', self.codes(document('<button data-view-target="gone" aria-controls="gone">Go</button>')))

    def test_citation_not_runtime_dependency(self):
        self.assertTrue(verifier.inspect_html(document('<a href="https://example.org/paper">Source</a>'))['ok'])

    def test_portable_active_resources_rejected(self):
        self.assertIn('portable-remote', self.codes(document('<script src="https://example.org/code.js"></script>')))
        self.assertIn('portable-remote', self.codes(document('<link rel="stylesheet" href="//example.org/a.css">')))

    def test_data_image_is_embedded(self):
        self.assertTrue(verifier.inspect_html(document('<img alt="dot" src="data:image/png;base64,AA==">'))['ok'])

    def test_code_examples_not_active_resource_paths(self):
        self.assertNotIn('machine-path', self.codes(document('<pre>/home/demo/output.html</pre>')))
        self.assertIn('machine-path', self.codes(document('<img alt="x" src="file:///home/demo/x.png">')))

    def test_host_root_relative_resource_is_legitimate(self):
        self.assertTrue(verifier.inspect_html(document('<img alt="x" src="/assets/x.png">', 'host'))['ok'])
        self.assertIn('portable-root-path', self.codes(document('<img alt="x" src="/assets/x.png">')))

    def test_manifest_roundtrips_hostile_text(self):
        html = document(manifest(purpose='Quotes " and </script><script>bad()</script>'))
        self.assertTrue(verifier.inspect_html(html, require_manifest=True)['ok'])

    def test_html_escaped_json_rejected(self):
        self.assertIn('manifest-invalid', self.codes(document(manifest().replace('"schemaVersion"', '&quot;schemaVersion&quot;'))))

    def test_manifest_profile_mismatch(self):
        self.assertIn('manifest-invalid', self.codes(document(manifest(delivery='connected'))))

    def test_bad_manifest_types(self):
        for value in [manifest(schemaVersion=True), manifest(schemaVersion=2), manifest(sourceCut=['wrong']), manifest(dependencies='wrong')]:
            with self.subTest(value=value):
                self.assertIn('manifest-invalid', self.codes(document(value)))

    def test_duplicate_json_key_rejected(self):
        value = manifest().replace('"schemaVersion": 1', '"schemaVersion": 1, "schemaVersion": 1')
        self.assertIn('manifest-invalid', self.codes(document(value)))

    def test_state_api_review_is_not_claimed_execution(self):
        self.assertIn('state-api', self.codes(document('<script>const example = "localStorage";</script>')))
        self.assertNotIn('state-api', self.codes(document('<p>localStorage is not used.</p>')))

    def test_required_metadata(self):
        self.assertFalse(verifier.inspect_html('<html><body>Missing</body></html>')['ok'])

    def test_require_manifest_opt_in(self):
        self.assertFalse(verifier.inspect_html(document(), require_manifest=True)['ok'])

    def test_cli_exit_status(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'test.html'
            path.write_text(document())
            result = subprocess.run([sys.executable, str(SCRIPT), str(path), '--json'], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0)
            self.assertTrue(json.loads(result.stdout)['ok'])
            path.write_text(document('<a href="#absent">Missing</a>'))
            self.assertEqual(subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True).returncode, 1)
            path.unlink()
            self.assertEqual(subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True).returncode, 2)


if __name__ == '__main__':
    unittest.main()
