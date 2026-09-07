"""Installer boundaries with real filesystem state and controlled network/CLI calls."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SHA = 'a' * 40
SOURCE = 'quantipixels/skills'


class InstallTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='qp install ')
        self.addCleanup(temporary.cleanup)
        self.work = Path(temporary.name)
        self.home = self.work / 'home with spaces'
        self.home.mkdir()
        self.bin = self.work / 'bin'
        self.bin.mkdir()
        self.lock = self.home / '.agents/.skill-lock.json'
        self.manifest = self.work / 'manifest.json'
        self.tree = self.work / 'tree.json'
        self.log = self.work / 'calls.jsonl'
        self.content = self.work / 'content.json'
        self.manifest.write_text(json.dumps({'name': 'qp-skills', 'skills': [
            './skills/engineering/alaga', './skills/productivity/arojinle']}))
        content = {'skills/engineering/alaga/SKILL.md': '---\nname: alaga\n---\n',
                   'skills/engineering/alaga/references/guide.md': 'Use the project tool.\n',
                   'skills/productivity/arojinle/SKILL.md': '---\nname: arojinle\n---\nUse amose.\n'}
        self.content.write_text(json.dumps(content))
        entries = [];
        for name, text in content.items():
            data = text.encode()
            digest = hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()
            entries.append({'path': name, 'type': 'blob', 'mode': '100644', 'sha': digest})
        self.tree.write_text(json.dumps({'truncated': False, 'tree': entries}))
        self.env = {k: v for k, v in os.environ.items() if k not in ('XDG_STATE_HOME', 'CLAUDE_CONFIG_DIR', 'CODEX_HOME')}
        self.env.update(HOME=str(self.home), PATH=str(self.bin) + os.pathsep + os.environ['PATH'],
                        QP_TEST_ROOT=str(self.work), QP_TEST_MODE='ok', QP_TEST_SHA=SHA)
        self.stub('curl', '''
import json, os, shutil, sys
from pathlib import Path
root = Path(os.environ['QP_TEST_ROOT'])
args = sys.argv[1:]
url = next(a for a in args if a.startswith('https://'))
output = Path(args[args.index('-o') + 1])
with (root / 'calls.jsonl').open('a') as f: f.write(json.dumps(['curl', *args]) + '\\n')
if os.environ['QP_TEST_MODE'] == 'fetch-fail': sys.exit(22)
if '/commits/' in url: output.write_text(json.dumps({'sha': os.environ['QP_TEST_SHA']}))
elif '/git/trees/' in url: shutil.copyfile(root / 'tree.json', output)
else: shutil.copyfile(root / 'manifest.json', output)
''')
        self.stub('npx', '''
import json, os, shutil, sys
from pathlib import Path
from urllib.parse import unquote
root = Path(os.environ['QP_TEST_ROOT'])
args = sys.argv[1:]
mode = os.environ['QP_TEST_MODE']
with (root / 'calls.jsonl').open('a') as f: f.write(json.dumps(['npx', *args]) + '\\n')
assert args[:2] == ['--yes', 'skills@1.5.23'] and '--global' in args, args
assert Path.cwd() != root, 'native global removal must not see caller project'
assert sys.stdin.read() == '', 'native CLI must not consume piped script'
if mode == 'native-fail': sys.exit(17)
if mode == 'noop': sys.exit(0)
home = Path.home()
lock = Path(os.environ['XDG_STATE_HOME']) / 'skills/.skill-lock.json' if os.environ.get('XDG_STATE_HOME') else home / '.agents/.skill-lock.json'
lock.parent.mkdir(parents=True, exist_ok=True)
state = json.loads(lock.read_text()) if lock.exists() else {'version': 3, 'skills': {}}
canonical = home / '.agents/skills'
claude = Path(os.environ.get('CLAUDE_CONFIG_DIR', str(home / '.claude'))) / 'skills'
if args[2] == 'add':
    assert args[3].startswith('https://github.com/quantipixels/skills#')
    ref = unquote(args[3].split('#')[1])
    names = args[args.index('--skill') + 1:args.index('--yes', 2)]
    assert set(names) == {'alaga', 'arojinle'}
    for name in names:
        state['skills'][name] = {'source': 'quantipixels/skills', 'ref': ref}
    if mode != 'lock-only':
        for key, text in json.loads((root / 'content.json').read_text()).items():
            relative = '/'.join(key.split('/')[2:])
            if mode == 'missing-reference' and 'references/' in relative: continue
            target = canonical / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text + ('drift' if mode == 'wrong-content' else ''))
        if 'claude-code' in args and mode != 'missing-alias':
            claude.mkdir(parents=True, exist_ok=True)
            for name in names:
                alias = claude / name
                if not alias.is_symlink(): alias.symlink_to(canonical / name, target_is_directory=True)
    if mode == 'changed-owner': state['skills']['retired'] = {'source': 'someone/else'}
    if mode == 'lost-owner': state['skills'].pop('retired', None)
elif args[2] == 'remove':
    if mode == 'prune-noop': sys.exit(0)
    # Model the upstream legacy cleanup to test caller-project isolation.
    shutil.rmtree(Path.cwd() / 'agent/skills/alaga', ignore_errors=True)
    for name in args[args.index('--yes', 2) + 1:]:
        state['skills'].pop(name, None)
        shutil.rmtree(canonical / name, ignore_errors=True)
        alias = claude / name
        if alias.is_symlink(): alias.unlink()
else: raise AssertionError(args)
lock.write_text(json.dumps(state))
''')

    def stub(self, name, code):
        target = self.bin / name
        target.write_text('#!' + sys.executable + '\n' + code)
        target.chmod(0o755)

    def state(self, entries, version=3):
        self.lock.parent.mkdir(parents=True, exist_ok=True)
        self.lock.write_text(json.dumps({'version': version, 'skills': entries}))

    def run_script(self, *args, mode='ok', uninstall=False, pipe=False):
        self.env['QP_TEST_MODE'] = mode
        script = ROOT / 'scripts' / ('uninstall.sh' if uninstall else 'install.sh')
        command = ['bash', '-s', '--', *args] if pipe else ['bash', str(script), *args]
        return subprocess.run(command, input=script.read_text() if pipe else None, cwd=self.work,
                              env=self.env, text=True, capture_output=True, timeout=20)

    def calls(self):
        return [v for l in self.log.read_text().splitlines() if (v := json.loads(l))[0] == 'npx'] if self.log.exists() else []

    def test_pipe_install_reinstall_and_uninstall_preserve_other_work(self):
        self.env['CLAUDE_CONFIG_DIR'] = str(self.home / 'custom claude')
        self.state({'retired': {'source': 'git@github.com:quantipixels/skills.git'}, 'other': {'source': 'someone/else'}})
        project = self.work / 'agent/skills/alaga'
        project.mkdir(parents=True)
        (project / 'mine').write_text('project skill')
        for _ in range(2):
            result = self.run_script('--ref', 'feature/use-skills', '--codex', '--claude', '--prune', pipe=True)
            self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('#feature%2Fuse-skills', self.calls()[0][4])
        self.assertEqual(set(json.loads(self.lock.read_text())['skills']), {'alaga', 'arojinle', 'other'})
        self.assertTrue((self.home / 'custom claude/skills/alaga').is_symlink())
        for _ in range(2):
            result = self.run_script(uninstall=True, pipe=True)
            self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(set(json.loads(self.lock.read_text())['skills']), {'other'})
        self.assertFalse((self.home / '.agents/skills/alaga').exists())
        self.assertFalse((self.home / 'custom claude/skills/alaga').is_symlink())
        self.assertEqual((project / 'mine').read_text(), 'project skill')

    def test_preview_and_default_keep_retired_names(self):
        self.state({'retired': {'source': SOURCE}})
        before = self.lock.read_bytes()
        for uninstall in (False, True):
            self.assertEqual(self.run_script('--dry-run', uninstall=uninstall).returncode, 0)
        self.assertEqual(self.lock.read_bytes(), before)
        self.assertEqual(self.calls(), [])
        self.assertEqual(self.run_script().returncode, 0)
        self.assertIn('retired', json.loads(self.lock.read_text())['skills'])

    def test_bad_arguments_never_contact_network(self):
        for args in [('--unknown',), ('--ref',), ('--ref', SHA), ('--ref', '../bad')]:
            self.assertNotEqual(self.run_script(*args).returncode, 0)
        self.assertEqual(self.run_script('--help').returncode, 0)
        self.assertFalse(self.log.exists())

    def test_foreign_or_untracked_collision_is_not_replaced(self):
        for source in ('someone/else', 'https://github.com.evil/quantipixels/skills'):
            self.state({'alaga': {'source': source}})
            self.assertNotEqual(self.run_script().returncode, 0)
        self.state({})
        target = self.home / '.agents/skills/alaga'
        target.mkdir(parents=True)
        (target / 'mine').write_text('untracked')
        self.assertNotEqual(self.run_script().returncode, 0)
        self.assertEqual((target / 'mine').read_text(), 'untracked')
        self.assertEqual(self.calls(), [])

    def test_dangling_and_canonical_links_are_not_replaced(self):
        self.state({'alaga': {'source': SOURCE}})
        target = self.home / '.agents/skills/alaga'
        target.parent.mkdir(parents=True)
        target.symlink_to(self.work / 'not-present')
        self.assertNotEqual(self.run_script().returncode, 0)
        target.unlink()
        alias = self.home / '.claude/skills/alaga'
        alias.parent.mkdir(parents=True)
        alias.symlink_to(self.work / 'foreign')
        self.assertNotEqual(self.run_script('--claude').returncode, 0)
        self.assertEqual(alias.readlink(), self.work / 'foreign')
        self.assertEqual(self.calls(), [])

    def test_corrupt_unsafe_and_old_locks_fail_closed(self):
        self.lock.parent.mkdir(parents=True)
        for text in ('not-json', '[]', '{"skills":null}', '{"skills":{"alaga":null}}',
                     json.dumps({'version': 2, 'skills': {'alaga': {'source': SOURCE}}}),
                     json.dumps({'version': 3, 'skills': {'--all': {'source': SOURCE}}})):
            self.lock.write_text(text)
            for uninstall in (False, True):
                self.assertNotEqual(self.run_script(uninstall=uninstall).returncode, 0)
            self.assertEqual(self.lock.read_text(), text)
        self.assertEqual(self.calls(), [])

    def test_incomplete_metadata_and_fetch_errors_do_not_install(self):
        for value in (None, {'name': 'qp-skills', 'skills': []}, {'name': 'qp-skills', 'skills': ['../escape']}):
            self.manifest.write_text(json.dumps(value))
            self.assertNotEqual(self.run_script().returncode, 0)
        self.assertNotEqual(self.run_script(mode='fetch-fail').returncode, 0)
        self.assertEqual(self.calls(), [])

    def test_wrong_or_partial_install_does_not_prune(self):
        for mode in ('native-fail', 'noop', 'lock-only', 'wrong-content', 'missing-reference', 'missing-alias'):
            with self.subTest(mode=mode):
                self.state({'retired': {'source': SOURCE}})
                # Isolate each partial failure so a prior run cannot fill its missing file.
                import shutil
                shutil.rmtree(self.home / '.agents/skills', ignore_errors=True)
                shutil.rmtree(self.home / '.claude', ignore_errors=True)
                result = self.run_script('--claude', '--prune', mode=mode)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('retired', json.loads(self.lock.read_text())['skills'])
        self.assertTrue(all(c[3] == 'add' for c in self.calls()))

    def test_lost_or_changed_ownership_cannot_authorize_pruning(self):
        for mode in ('lost-owner', 'changed-owner', 'prune-noop'):
            self.state({name: {'source': SOURCE, 'ref': 'ori'} for name in ('retired', 'alaga', 'arojinle')})
            self.log.unlink(missing_ok=True)
            result = self.run_script('--prune', mode=mode)
            self.assertEqual(result.returncode == 0, mode == 'lost-owner', result.stderr)
            if mode != 'prune-noop': self.assertEqual(len(self.calls()), 1)

    def test_current_ref_with_stale_bytes_does_not_pass_verification(self):
        self.assertEqual(self.run_script().returncode, 0)
        target = self.home / '.agents/skills/alaga/references/guide.md'
        target.write_text('obsolete')
        self.assertNotEqual(self.run_script(mode='noop').returncode, 0)

    def test_xdg_state_and_relative_config_boundaries(self):
        self.env['XDG_STATE_HOME'] = str(self.work / 'state with spaces')
        self.lock = Path(self.env['XDG_STATE_HOME']) / 'skills/.skill-lock.json'
        self.state({'other': {'source': 'someone/else'}})
        for uninstall in (False, True):
            result = self.run_script(uninstall=uninstall)
            self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(set(json.loads(self.lock.read_text())['skills']), {'other'})
        self.env['XDG_STATE_HOME'] = 'relative'
        for uninstall in (False, True): self.assertNotEqual(self.run_script(uninstall=uninstall).returncode, 0)


if __name__ == '__main__':
    unittest.main()
