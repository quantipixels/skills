"""Reject broken packages and test independently loaded package validators."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / 'scripts/skills'


class PackageIntegrityTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.repo = Path(temporary.name)
        (self.repo / '.claude-plugin').mkdir()
        (self.repo / 'agents').mkdir()
        self.agent()
        self.skill('example')
        self.manifest()
        (self.repo / '.codex-plugin').mkdir()
        (self.repo / '.codex-plugin/plugin.json').write_bytes(
            (ROOT / '.codex-plugin/plugin.json').read_bytes())

    def skill(self, name, text=None):
        path = self.repo / 'skills' / name / 'SKILL.md'
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text or f'---\nname: {name}\ndescription: Perform the example task.\n---\n\n# Example\n', encoding='utf-8')
        return path

    def agent(self, preload='example'):
        (self.repo / 'agents/main.md').write_text(f'---\nname: main\ndescription: Main agent.\nskills: [qp-skills:{preload}]\n---\n')

    def manifest(self, **updates):
        value = {'name': 'qp-skills', **updates}
        (self.repo / '.claude-plugin/plugin.json').write_text(json.dumps(value))

    def run_validator(self, name='validate-package.py'):
        return subprocess.run([sys.executable, str(SCRIPTS / name), '--repo', str(self.repo)],
                              text=True, capture_output=True, timeout=10)

    def assert_invalid(self, name='validate-package.py'):
        result = self.run_validator(name)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertNotIn('Traceback', result.stderr)
        return result

    def test_native_directory_discovery_and_agent_preload(self):
        for name in ('validate-package.py', 'validate-plugin-agents.py'):
            result = self.run_validator(name)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_or_invalid_codex_manifest_is_rejected(self):
        path = self.repo / '.codex-plugin/plugin.json'
        for text in (None, '{', '[]'):
            with self.subTest(text=text):
                if text is None:
                    path.unlink()
                else:
                    path.write_text(text)
                self.assertIn('[codex_manifest.invalid]', self.assert_invalid().stdout)
                path.write_bytes((ROOT / '.codex-plugin/plugin.json').read_bytes())

    def test_codex_manifest_keeps_package_identity_and_shared_inventory(self):
        path = self.repo / '.codex-plugin/plugin.json'
        original = json.loads(path.read_text())
        for key, value, code in (('name', 'other', 'name'),
                                 ('skills', '../skills/', 'inventory')):
            with self.subTest(key=key):
                path.write_text(json.dumps({**original, key: value}))
                self.assertIn(f'[codex_manifest.{code}]', self.assert_invalid().stdout)
                path.write_text(json.dumps(original))

    def test_codex_skill_target_exists_and_stays_inside_package(self):
        source = self.repo / 'skills'
        with tempfile.TemporaryDirectory() as outside:
            target = Path(outside) / 'skills'
            source.rename(target)
            self.assertIn('[codex_manifest.target]', self.assert_invalid().stdout)
            try:
                source.symlink_to(target, target_is_directory=True)
            except OSError as error:
                self.skipTest(f'symlinks unavailable: {error}')
            self.assertIn('[codex_manifest.target]', self.assert_invalid().stdout)

    def test_duplicate_frontmatter_identity_is_rejected(self):
        self.skill('other', '---\nname: example\ndescription: Conflicting identity.\n---\n')
        self.assert_invalid()
        self.assert_invalid('validate-plugin-agents.py')

    def test_duplicate_yaml_keys_are_rejected(self):
        self.skill('example', '---\nname: wrong\nname: example\ndescription: Example.\n---\n')
        self.assert_invalid()
        self.assert_invalid('validate-plugin-agents.py')

    def test_grouped_or_nested_entrypoint_is_rejected(self):
        self.skill('engineering/orphan')
        self.assert_invalid()

    def test_missing_entrypoint_is_not_silently_omitted(self):
        (self.repo / 'skills/incomplete/references').mkdir(parents=True)
        self.assert_invalid()

    def test_non_object_manifest_is_a_clean_failure(self):
        for value in ([], None, 'not a manifest'):
            with self.subTest(value=value):
                (self.repo / '.claude-plugin/plugin.json').write_text(json.dumps(value))
                self.assert_invalid()
                self.assert_invalid('validate-plugin-agents.py')

    def test_competing_manifest_inventory_is_rejected(self):
        self.manifest(skills=['./skills/example'])
        self.assert_invalid()

    def test_noncanonical_name_is_rejected(self):
        self.skill('UpperCase')
        self.assert_invalid()

    def test_missing_and_escaping_local_resources_are_rejected(self):
        for reference in ('references/absent.md', '../../outside.md'):
            with self.subTest(reference=reference):
                self.skill('example', f'---\nname: example\ndescription: Example.\n---\n[More]({reference})\n')
                self.assert_invalid()

    def test_missing_preloaded_skill_is_rejected(self):
        self.agent('missing')
        self.assert_invalid('validate-plugin-agents.py')

    def test_user_only_preload_is_rejected(self):
        self.skill('example', '---\nname: example\ndescription: Example.\ndisable-model-invocation: true\n---\n')
        self.assert_invalid('validate-plugin-agents.py')

    def test_forbidden_default_prompt_is_rejected(self):
        target = self.repo / 'skills/example/agents/openai.yaml'
        target.parent.mkdir()
        target.write_text('interface:\n  default_prompt: hello\n')
        self.assert_invalid()


if __name__ == '__main__':
    unittest.main()
