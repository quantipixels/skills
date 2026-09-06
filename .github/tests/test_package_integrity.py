"""Exercise package rejection paths and shipped host-adapter wiring."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import tomllib

import yaml

SCRIPTS = Path(__file__).resolve().parents[2] / 'skills/engineering/ko-skill/scripts'


class PackageIntegrityTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.repo = Path(temporary.name)
        (self.repo / '.claude-plugin').mkdir()
        (self.repo / 'agents').mkdir()
        (self.repo / 'agents/qp.md').write_text('---\nname: qp\ndescription: Main agent.\nskills: [qp-skills:example]\n---\n')
        self.skill('engineering', 'example')
        self.manifest()

    def skill(self, group, name, text=None):
        path = self.repo / 'skills' / group / name / 'SKILL.md'
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text or f'---\nname: {name}\ndescription: Perform the example task.\n---\n\n# Example\n', encoding='utf-8')
        return path

    def manifest(self, entries=None):
        value = {'name': 'qp-skills', 'skills': entries or ['./skills/engineering/example']}
        (self.repo / '.claude-plugin/plugin.json').write_text(json.dumps(value))

    def run_validator(self, name='validate-package.py'):
        return subprocess.run([sys.executable, str(SCRIPTS / name), '--repo', str(self.repo)],
                              text=True, capture_output=True, timeout=10)

    def assert_invalid(self, name='validate-package.py'):
        result = self.run_validator(name)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertNotIn('Traceback', result.stderr)
        return result

    def test_valid_package_and_agents(self):
        for name in ('validate-package.py', 'validate-plugin-agents.py'):
            result = self.run_validator(name)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_duplicate_public_name_across_groups_is_rejected(self):
        self.skill('productivity', 'example')
        self.manifest(['./skills/engineering/example', './skills/productivity/example'])
        self.assert_invalid()
        self.assert_invalid('validate-plugin-agents.py')

    def test_duplicate_yaml_keys_are_rejected(self):
        self.skill('engineering', 'example', '---\nname: wrong\nname: example\ndescription: Example.\n---\n')
        self.assert_invalid()
        self.assert_invalid('validate-plugin-agents.py')

    def test_misplaced_skill_is_not_silently_omitted(self):
        self.skill('unexpected', 'orphan')
        self.assert_invalid()

    def test_missing_entrypoint_is_not_silently_omitted(self):
        (self.repo / 'skills/productivity/incomplete/references').mkdir(parents=True)
        self.assert_invalid()

    def test_nested_skill_entrypoint_is_rejected(self):
        path = self.repo / 'skills/engineering/example/extra/SKILL.md'
        path.parent.mkdir()
        path.write_text('---\nname: nested\ndescription: Nested.\n---\n')
        self.assert_invalid()

    def test_non_object_manifest_is_a_clean_failure(self):
        for value in ([], None, 'not a manifest'):
            with self.subTest(value=value):
                (self.repo / '.claude-plugin/plugin.json').write_text(json.dumps(value))
                self.assert_invalid()
                self.assert_invalid('validate-plugin-agents.py')

    def test_noncanonical_name_is_rejected(self):
        self.skill('engineering', 'UpperCase')
        self.manifest(['./skills/engineering/example', './skills/engineering/UpperCase'])
        self.assert_invalid()

    def test_missing_and_escaping_local_resources_are_rejected(self):
        path = self.repo / 'skills/engineering/example/SKILL.md'
        for reference in ('references/absent.md', '../../../outside.md'):
            with self.subTest(reference=reference):
                path.write_text(f'---\nname: example\ndescription: Example.\n---\n[More]({reference})\n')
                self.assert_invalid()

    def test_missing_preloaded_skill_is_rejected(self):
        (self.repo / 'agents/qp.md').write_text('---\nname: qp\ndescription: Main agent.\nskills: [qp-skills:missing]\n---\n')
        self.assert_invalid('validate-plugin-agents.py')

    def test_user_only_preload_is_rejected(self):
        self.skill('engineering', 'example', '---\nname: example\ndescription: Example.\ndisable-model-invocation: true\n---\n')
        (self.repo / 'agents/qp.md').write_text('---\nname: qp\ndescription: Main agent.\nskills: [qp-skills:example]\n---\n')
        self.assert_invalid('validate-plugin-agents.py')

    def test_forbidden_default_prompt_is_rejected(self):
        target = self.repo / 'skills/engineering/example/agents/openai.yaml'
        target.parent.mkdir()
        target.write_text('interface:\n  default_prompt: hello\n')
        self.assert_invalid()


class PepeyeAdapterTests(unittest.TestCase):
    """Check loadable wiring; these tests do not prove model behavior."""

    def test_single_main_agent_with_lazy_skill_loading(self):
        repo = Path(__file__).resolve().parents[2]
        manifest = json.loads((repo / '.claude-plugin/plugin.json').read_text())
        self.assertEqual(manifest['agents'], ['./agents/pepeye.md'])
        self.assertEqual(sorted(p.name for p in (repo / 'agents').glob('*.md')), ['pepeye.md'])
        agent = yaml.safe_load((repo / 'agents/pepeye.md').read_text().split('---', 2)[1])
        self.assertEqual(agent['name'], 'pepeye')
        self.assertEqual(agent['model'], 'inherit')
        self.assertEqual(agent.get('skills', []), [])
        skill_path = './skills/experimental/pepeye'
        self.assertIn(skill_path, manifest['skills'])
        skill = yaml.safe_load((repo / skill_path / 'SKILL.md').read_text().split('---', 2)[1])
        self.assertEqual(skill['name'], 'pepeye')
        self.assertNotEqual(skill.get('context'), 'fork')
        self.assertIsNot(skill.get('disable-model-invocation'), True)

    def test_codex_profile_only_sets_developer_instructions(self):
        repo = Path(__file__).resolve().parents[2]
        path = repo / 'agents/codex/pepeye.config.toml'
        profile = tomllib.loads(path.read_text(encoding='utf-8'))
        # Prevent a profile from quietly replacing native prompts, permissions, or models.
        self.assertEqual(set(profile), {'developer_instructions'})
        self.assertIsInstance(profile['developer_instructions'], str)
        self.assertTrue(profile['developer_instructions'].strip())
        # The two native formats must not drift into competing main-agent roles.
        body = (repo / 'agents/pepeye.md').read_text(encoding='utf-8').split('---', 2)[2]
        self.assertEqual(profile['developer_instructions'].strip(), body.strip())


if __name__ == '__main__':
    unittest.main()
