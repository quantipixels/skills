"""Exercise the shipped Codex manifest boundary, not authenticated host behaviour."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / 'skills/ko-skill/scripts/validate-package.py'


class CodexManifestTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.repo = Path(temporary.name)
        (self.repo / '.claude-plugin').mkdir()
        (self.repo / '.claude-plugin/plugin.json').write_text('{"name":"qp-skills"}')
        (self.repo / '.codex-plugin').mkdir()
        self.manifest = self.repo / '.codex-plugin/plugin.json'
        self.manifest.write_bytes((ROOT / '.codex-plugin/plugin.json').read_bytes())
        self.skill('example')

    def skill(self, name):
        path = self.repo / 'skills' / name / 'SKILL.md'
        path.parent.mkdir(parents=True)
        path.write_text(f'---\nname: {name}\ndescription: Example capability.\n---\n')

    def validate(self):
        result = subprocess.run(
            [sys.executable, str(VALIDATOR), '--repo', str(self.repo), '--format', 'json'],
            capture_output=True, text=True, timeout=10,
        )
        self.assertNotIn('Traceback', result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(result.returncode, 0 if payload['valid'] else 1)
        return payload

    def assert_rejected(self, code):
        payload = self.validate()
        self.assertFalse(payload['valid'])
        self.assertIn(code, {finding['code'] for finding in payload['findings']})

    def test_shipped_manifest_uses_native_discovery_without_a_second_inventory(self):
        self.assertTrue(self.validate()['valid'])
        self.skill('another')
        payload = self.validate()
        self.assertTrue(payload['valid'])
        self.assertEqual(payload['skills_checked'], 2)

    def test_missing_manifest_is_not_silently_accepted(self):
        self.manifest.unlink()
        self.assert_rejected('codex_manifest.invalid')

    def test_malformed_or_non_object_manifest_fails_cleanly(self):
        for text in ('{', 'null', '[]', '"qp-skills"'):
            with self.subTest(text=text):
                self.manifest.write_text(text)
                self.assert_rejected('codex_manifest.invalid')

    def test_wrong_or_missing_identity_is_rejected(self):
        for name in ('other', None, ['qp-skills']):
            with self.subTest(name=name):
                self.manifest.write_text(json.dumps({'name': name, 'skills': './skills/'}))
                self.assert_rejected('codex_manifest.name')

    def test_alternate_escaping_and_per_skill_paths_are_rejected(self):
        for skills in ('../skills/', '/skills/', './skills/example/', ['./skills/'], None):
            with self.subTest(skills=skills):
                self.manifest.write_text(json.dumps({'name': 'qp-skills', 'skills': skills}))
                self.assert_rejected('codex_manifest.inventory')

    def test_declared_directory_must_exist(self):
        (self.repo / 'skills/example/SKILL.md').unlink()
        (self.repo / 'skills/example').rmdir()
        (self.repo / 'skills').rmdir()
        self.assert_rejected('codex_manifest.target')

    def test_skills_directory_cannot_escape_the_package_through_a_symlink(self):
        with tempfile.TemporaryDirectory() as outside:
            source = self.repo / 'skills'
            source.rename(Path(outside) / 'skills')
            try:
                source.symlink_to(Path(outside) / 'skills', target_is_directory=True)
            except OSError as error:
                self.skipTest(f'symlinks unavailable: {error}')
            self.assert_rejected('codex_manifest.target')

    def test_shipped_adapter_adds_no_implicit_execution_or_startup_settings(self):
        manifest = json.loads((ROOT / '.codex-plugin/plugin.json').read_text())
        self.assertEqual(manifest['name'], 'qp-skills')
        self.assertEqual(manifest['skills'], './skills/')
        for key in ('hooks', 'mcpServers', 'apps', 'agents'):
            self.assertNotIn(key, manifest)
        for path in ('.mcp.json', '.app.json', 'hooks/hooks.json'):
            self.assertFalse((ROOT / path).exists(), path)
        self.assertNotIn('defaultPrompt', manifest.get('interface', {}))


if __name__ == '__main__':
    unittest.main()
