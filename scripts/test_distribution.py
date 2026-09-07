"""Exercise owned-path updates/removal and interruption recovery on real files."""
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).with_name('distribution.py')
spec = importlib.util.spec_from_file_location('distribution', SCRIPT)
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)


class DistributionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='qp distribution ')
        self.addCleanup(self.temp.cleanup)
        self.work = Path(self.temp.name)
        self.home = self.work / 'home with spaces'
        self.home.mkdir()
        env = {key: value for key, value in os.environ.items()
               if key not in ('XDG_DATA_HOME', 'XDG_STATE_HOME', 'CLAUDE_CONFIG_DIR', 'CODEX_HOME')}
        env.update(HOME=str(self.home))
        self.env = patch.dict(os.environ, env, clear=True)
        self.env.start()
        self.addCleanup(self.env.stop)
        self.output = contextlib.redirect_stdout(io.StringIO())
        self.output.__enter__()
        self.addCleanup(lambda: self.output.__exit__(None, None, None))
        self.source = self.work / 'source'
        (self.source / 'scripts').mkdir(parents=True)
        shutil.copy2(SCRIPT, self.source / 'scripts/distribution.py')
        self.skill('alpha')
        self.skill('beta')
        self.root = d.location()

    def skill(self, name, text='First version'):
        folder = self.source / 'skills' / name
        folder.mkdir(parents=True, exist_ok=True)
        (folder / 'SKILL.md').write_text(f'---\nname: {name}\ndescription: Test skill.\n---\n{text}\n')

    def install(self, *hosts):
        d.install(self.source, list(hosts))

    def test_install_update_retire_and_repeated_uninstall(self):
        self.install('codex', 'claude')
        alpha = self.home / '.agents/skills/alpha'
        claude = self.home / '.claude/skills/alpha'
        self.assertTrue(alpha.is_symlink())
        self.assertTrue(claude.is_symlink())
        first = d.current(self.root)
        self.skill('alpha', 'Updated')
        shutil.rmtree(self.source / 'skills/beta')
        self.skill('gamma')
        self.install()
        self.assertNotEqual(d.current(self.root), first)
        self.assertIn('Updated', (alpha / 'SKILL.md').read_text())
        for host in ('.agents', '.claude'):
            self.assertFalse(os.path.lexists(self.home / host / 'skills/beta'))
            self.assertTrue((self.home / host / 'skills/gamma/SKILL.md').is_file())
        self.assertEqual(len(list((self.root / 'generations').iterdir())), 1)
        d.uninstall()
        d.uninstall()
        self.assertFalse(os.path.lexists(alpha))
        self.assertFalse(os.path.lexists(claude))
        self.assertIsNone(d.current(self.root))

    def test_preview_changes_nothing(self):
        d.install(self.source, ['codex'], True)
        self.assertFalse(self.root.exists())
        self.install()
        before = sorted(str(p.relative_to(self.home)) for p in self.home.rglob('*'))
        d.install(self.source, ['claude'], True)
        d.uninstall(True)
        self.assertEqual(before, sorted(str(p.relative_to(self.home)) for p in self.home.rglob('*')))

    def test_foreign_file_directory_and_link_are_not_adopted(self):
        target = self.home / '.agents/skills/alpha'
        target.parent.mkdir(parents=True)
        for shape in ('file', 'directory', 'link'):
            with self.subTest(shape=shape):
                if shape == 'file': target.write_text('Mine')
                elif shape == 'directory': target.mkdir(); (target / 'mine').write_text('Mine')
                else: target.symlink_to(self.work / 'absent')
                with self.assertRaises(d.InstallError): self.install()
                self.assertTrue(os.path.lexists(target))
                if shape == 'directory': shutil.rmtree(target)
                else: target.unlink()
        self.assertIsNone(d.current(self.root))

    def test_external_manager_lock_is_never_modified(self):
        lock = self.home / '.agents/.skill-lock.json'
        lock.parent.mkdir(parents=True)
        original = json.dumps({'version': 999, 'skills': {'alpha': {'source': 'someone/else'}}})
        lock.write_text(original)
        with self.assertRaises(d.InstallError): self.install()
        d.uninstall()
        self.assertEqual(lock.read_text(), original)

    def test_modified_owned_content_blocks_update_and_removal(self):
        self.install()
        target = self.home / '.agents/skills/alpha/SKILL.md'
        target.write_text('My local change')
        for action in (self.install, d.uninstall):
            with self.assertRaises(d.InstallError): action()
            self.assertEqual(target.read_text(), 'My local change')

    def test_replaced_host_link_and_unrelated_hosts_survive(self):
        self.install('codex', 'claude')
        foreign = self.home / '.cursor/skills/alpha'
        foreign.mkdir(parents=True)
        (foreign / 'mine').write_text('Foreign')
        managed = self.home / '.claude/skills/alpha'
        managed.unlink(); managed.mkdir(); (managed / 'mine').write_text('Replacement')
        with self.assertRaises(d.InstallError): d.uninstall()
        self.assertEqual((managed / 'mine').read_text(), 'Replacement')
        shutil.rmtree(managed)
        d.uninstall()
        self.assertEqual((foreign / 'mine').read_text(), 'Foreign')

    def test_symlink_package_content_is_rejected(self):
        (self.source / 'skills/alpha/escape').symlink_to(self.home)
        with self.assertRaises(d.InstallError): self.install()
        self.assertFalse(self.root.exists())

    def test_source_copy_failure_keeps_previous_snapshot(self):
        self.install()
        old = d.current(self.root)
        with patch.object(d.shutil, 'copytree', side_effect=OSError('disk full')):
            with self.assertRaises(OSError): self.install()
        self.assertEqual(d.current(self.root), old)
        self.assertTrue((self.home / '.agents/skills/alpha/SKILL.md').is_file())
        self.assertFalse((self.root / 'transaction.json').exists())

    def test_interrupted_before_pointer_switch_rolls_back_new_links(self):
        self.install()
        old = d.current(self.root)
        self.skill('gamma')
        real_replace = os.replace
        def interrupted(source, destination):
            if Path(destination) == self.root / 'current': raise SystemExit(93)
            return real_replace(source, destination)
        with patch.object(d.os, 'replace', side_effect=interrupted):
            with self.assertRaises(SystemExit): self.install('claude')
        self.assertTrue((self.root / 'transaction.json').exists())
        self.assertEqual(d.current(self.root), old)
        with d.locked(self.root): d.recover(self.root)
        self.assertFalse(os.path.lexists(self.home / '.claude/skills/gamma'))
        self.assertTrue((self.home / '.agents/skills/alpha/SKILL.md').is_file())
        self.install('claude')
        self.assertTrue((self.home / '.claude/skills/gamma/SKILL.md').is_file())

    def test_interrupted_after_switch_finishes_retired_link_cleanup(self):
        self.install()
        shutil.rmtree(self.source / 'skills/beta')
        real_recover = d.recover
        calls = 0
        def interrupted(root):
            nonlocal calls
            calls += 1
            if calls == 2: raise SystemExit(93)
            return real_recover(root)
        with patch.object(d, 'recover', side_effect=interrupted):
            with self.assertRaises(SystemExit): self.install()
        self.assertTrue(os.path.lexists(self.home / '.agents/skills/beta'))
        self.install()
        self.assertFalse(os.path.lexists(self.home / '.agents/skills/beta'))
        self.assertFalse((self.root / 'transaction.json').exists())

    def test_interrupted_removal_can_resume_without_current_pointer(self):
        self.install()
        real_recover = d.recover
        calls = 0
        def interrupted(root):
            nonlocal calls
            calls += 1
            if calls == 2: raise SystemExit(93)
            return real_recover(root)
        with patch.object(d, 'recover', side_effect=interrupted):
            with self.assertRaises(SystemExit): d.uninstall()
        self.assertIsNone(d.current(self.root))
        d.uninstall()
        self.assertFalse(os.path.lexists(self.home / '.agents/skills/alpha'))

    def test_custom_locations_and_relocation_preserve_old_unrelated_files(self):
        os.environ['XDG_DATA_HOME'] = str(self.work / 'custom data')
        os.environ['CLAUDE_CONFIG_DIR'] = str(self.work / 'claude one')
        self.root = d.location()
        self.install('claude')
        old = self.work / 'claude one/skills'
        (old / 'unrelated').write_text('Mine')
        os.environ['CLAUDE_CONFIG_DIR'] = str(self.work / 'claude two')
        self.install('claude')
        self.assertFalse(os.path.lexists(old / 'alpha'))
        self.assertEqual((old / 'unrelated').read_text(), 'Mine')
        self.assertTrue((self.work / 'claude two/skills/alpha/SKILL.md').is_file())
        d.uninstall()

    def test_simultaneous_operation_is_rejected(self):
        self.install()
        with d.locked(self.root):
            with self.assertRaises(d.InstallError): self.install()
        self.assertTrue((self.home / '.agents/skills/alpha/SKILL.md').is_file())

    def test_corrupt_or_escaping_current_state_fails_closed(self):
        self.install()
        pointer = self.root / 'current'
        pointer.unlink(); pointer.symlink_to(self.source)
        for action in (self.install, d.uninstall):
            with self.assertRaises(d.InstallError): action()
        self.assertTrue((self.source / 'skills/alpha/SKILL.md').is_file())

    def test_substituted_generation_parent_is_rejected_before_any_removal(self):
        self.install('codex', 'claude')
        old = d.current(self.root)
        outside = self.work / 'outside-generations'
        (self.root / 'generations').rename(outside)
        (self.root / 'generations').symlink_to(outside, target_is_directory=True)
        for action in (self.install, d.uninstall):
            with self.assertRaises(d.InstallError): action()
            self.assertTrue((outside / old / 'skills/alpha/SKILL.md').is_file())
            self.assertTrue((self.home / '.agents/skills/alpha').is_symlink())
            self.assertTrue((self.root / 'current').is_symlink())
            self.assertFalse((self.root / 'transaction.json').exists())

    def test_real_shell_entrypoints_work_with_spaces(self):
        for name in ('install.sh', 'uninstall.sh'):
            shutil.copy2(SCRIPT.with_name(name), self.source / 'scripts' / name)
        for name, args in [('install.sh', ['--source', str(self.source), '--codex']),
                           ('install.sh', ['--source', str(self.source), '--claude']),
                           ('uninstall.sh', ['--dry-run']), ('uninstall.sh', []), ('uninstall.sh', [])]:
            result = subprocess.run(['bash', str(self.source / 'scripts' / name), *args],
                                    capture_output=True, text=True, timeout=20)
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_empty_nested_and_missing_sources_fail_without_installation(self):
        shutil.rmtree(self.source / 'skills')
        for shape in ('missing', 'empty', 'nested'):
            if shape == 'empty': (self.source / 'skills').mkdir()
            elif shape == 'nested': (self.source / 'skills/engineering').mkdir()
            with self.assertRaises(d.InstallError): self.install()
        self.assertFalse(self.root.exists())


if __name__ == '__main__':
    unittest.main()
