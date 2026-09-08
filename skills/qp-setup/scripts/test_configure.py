"""Regression tests for settings resolution and native setup, not prompt quality."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import tomllib
import unittest
from unittest.mock import patch

import configure as c
import settings as s


def header(data):
    # Emitted frontmatter uses the JSON scalar/array subset of YAML.
    return {key: json.loads(value) for key, value in
            (line.split(": ", 1) for line in data.decode().split("---", 2)[1].strip().splitlines())}


class ConfigurationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.home, self.repo = self.root / "home", self.root / "project"
        self.home.mkdir()
        self.repo.mkdir()
        env = patch.dict(os.environ, {"CLAUDE_CONFIG_DIR": str(self.home / ".claude"),
                                     "CODEX_HOME": str(self.home / ".codex")})
        env.start()
        self.addCleanup(env.stop)

    def setting(self, root, value):
        path = root / ".qp/setting.json"
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps(value), encoding="utf-8")
        return path

    def sync(self, **kwargs):
        return c.sync(("claude", "codex"), "user", self.repo, home=self.home, **kwargs)

    def test_missing_settings_leave_communication_and_native_models_unset(self):
        result = s.resolve(self.home, self.repo)
        self.assertEqual(result["communication_instruction"], "")
        self.assertEqual(result["sources"], [])
        self.assertFalse((self.home / ".qp").exists())
        for name, data in c.render("codex", result).items():
            value = tomllib.loads(data.decode())
            self.assertEqual(value["name"] + ".toml", name)
            self.assertNotIn("model", value)
            self.assertNotIn("model_reasoning_effort", value)
        for name, data in c.render("claude", result).items():
            value = header(data)
            self.assertNotIn("effort", value)
            if name != "qp-pepeye.md":
                self.assertNotIn("model", value)

    def test_scope_precedes_specificity_and_fields_merge_independently(self):
        self.setting(self.home, {"communication": "yoruba", "codex": {
            "model": "global-model", "reasoning": "low", "agents": {
                "atona": {"model": "global-planner", "reasoning": "high"}}}})
        self.setting(self.repo, {"communication": "default", "codex": {
            "model": "adaptive", "agents": {"alaga": {"model": "repo-author"}}}})
        result = s.resolve(self.home, self.repo)
        self.assertEqual(result["hosts"]["codex"]["atona"], {"model": "adaptive", "reasoning": "high"})
        self.assertEqual(result["hosts"]["codex"]["alaga"], {"model": "repo-author", "reasoning": "low"})
        self.assertEqual(result["hosts"]["claude"]["atona"]["model"], "adaptive")
        self.assertEqual(result["communication_instruction"], "")
        self.assertEqual(result["origins"]["communication"], str(self.repo / ".qp/setting.json"))
        self.assertEqual(len(result["sources"]), 2)

    def test_communication_is_resolved_not_baked_into_agents(self):
        baseline = c.render("claude", s.resolve(self.home))
        for mode in ("yoruba", "adaptive", "default"):
            self.setting(self.home, {"communication": mode})
            effective = s.resolve(self.home)
            self.assertEqual(effective["communication"], mode)
            self.assertEqual(bool(effective["communication_instruction"]), mode != "default")
            self.assertEqual(c.render("claude", effective), baseline)

    def test_malformed_and_unknown_preferences_are_rejected_with_source(self):
        path = self.setting(self.home, {})
        invalid = ['{', '[]', '{"communication":"default","communication":"yoruba"}',
                   '{"codex":{"agents":{"atona":{"model":"x","model":"y"}}}}']
        invalid += [json.dumps(v) for v in (
            {"version": True}, {"version": 2}, {"communication": None}, {"communication": []},
            {"communication": "english"}, {"hooks": "sh bad.sh"}, {"codex": None},
            {"codex": {"model": "x\npermission=unsafe"}}, {"claude": {"reasoning": "ultra"}},
            {"codex": {"agents": {"ro-wo": {}}}}, {"codex": {"agents": {"atona": {"tools": []}}}},
            {"codex": {"agents": {"pepeye": {"model": "x"}}}},
        )]
        for text in invalid:
            with self.subTest(text=text):
                path.write_text(text)
                with self.assertRaisesRegex(s.ConfigError, "setting.json"):
                    s.resolve(self.home, self.repo)

    def git(self, path, *args):
        result = subprocess.run(["git", "-C", str(path), *args], capture_output=True, text=True, timeout=15)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_checkout_discovery_handles_subdirectories_nested_repos_and_worktrees(self):
        self.git(self.repo, "init", "-q")
        self.git(self.repo, "-c", "user.email=test@example.invalid", "-c", "user.name=Test", "commit", "--allow-empty", "-qm", "fixture")
        child = self.repo / "nested/deep"
        child.mkdir(parents=True)
        self.assertEqual(s.repo_root(child), self.repo)
        self.git(child.parent, "init", "-q")
        self.assertEqual(s.repo_root(child), child.parent)
        worktree = self.root / "worktree"
        self.git(self.repo, "worktree", "add", "--detach", str(worktree))
        self.assertTrue((worktree / ".git").is_file())
        self.assertEqual(s.repo_root(worktree), worktree)
        self.setting(self.root, {"communication": "yoruba"})
        self.assertEqual(s.resolve(self.home, worktree)["communication"], "default")

    def test_native_pins_and_read_only_boundaries_are_host_specific(self):
        self.setting(self.home, {"claude": {"agents": {"atunwo": {"model": "opus", "reasoning": "high"}}},
                                 "codex": {"agents": {"atunwo": {"model": "review-model", "reasoning": "xhigh"}}}})
        result = s.resolve(self.home)
        claude = header(c.render("claude", result)["qp-atunwo.md"])
        codex = tomllib.loads(c.render("codex", result)["qp-atunwo.toml"].decode())
        self.assertEqual((claude["model"], claude["effort"]), ("opus", "high"))
        self.assertEqual((codex["model"], codex["model_reasoning_effort"]), ("review-model", "xhigh"))
        self.assertEqual(codex["sandbox_mode"], "read-only")
        self.assertEqual(set(claude["tools"].split(", ")), {"Read", "Glob", "Grep", "WebSearch", "WebFetch"})
        self.assertNotIn("permissionMode", claude)
        self.assertNotIn("sandbox_mode", tomllib.loads(c.render("codex", result)["qp-alaga.toml"].decode()))
        self.assertEqual(header(c.render("claude", result)["qp-alaga.md"])["disallowedTools"], "Agent")

    def test_preview_is_read_only_and_user_sync_cannot_capture_repo_preferences(self):
        self.setting(self.repo, {"codex": {"model": "repo-model"}})
        self.sync(dry_run=True)
        self.assertEqual(list(self.home.iterdir()), [])
        self.sync()
        native = self.home / ".codex/agents/qp-atona.toml"
        self.assertNotIn("model", tomllib.loads(native.read_text(encoding="utf-8")))
        c.sync(("codex",), "repo", self.repo, home=self.home)
        local = self.repo / ".codex/agents/qp-atona.toml"
        self.assertEqual(tomllib.loads(local.read_text(encoding="utf-8"))["model"], "repo-model")

    def test_sync_updates_owned_files_clears_pins_and_preserves_host_configuration(self):
        originals = {self.home / ".claude/settings.json": b'{"permissions":{"deny":["Bash"]}}',
                     self.home / ".codex/config.toml": b'developer_instructions = "preserve me"\n'}
        for path, data in originals.items():
            path.parent.mkdir()
            path.write_bytes(data)
        self.setting(self.home, {"codex": {"model": "fixed", "reasoning": "high"}})
        self.sync()
        self.sync()
        native = self.home / ".codex/agents/qp-atona.toml"
        self.assertEqual(tomllib.loads(native.read_text(encoding="utf-8"))["model"], "fixed")
        self.setting(self.home, {"codex": {"model": "inherit", "reasoning": "adaptive"}})
        self.sync()
        self.assertNotIn("model", tomllib.loads(native.read_text(encoding="utf-8")))
        self.assertNotIn("model_reasoning_effort", tomllib.loads(native.read_text(encoding="utf-8")))
        for path, data in originals.items():
            self.assertEqual(path.read_bytes(), data)
        self.assertTrue((self.home / ".qp/setting.json").is_file())

    def test_plugin_skill_preloads_do_not_change_direct_agent_identity(self):
        self.sync(plugin_skills=True)
        value = header((self.home / ".claude/agents/qp-atona.md").read_bytes())
        self.assertEqual(value["name"], "qp-atona")
        self.assertEqual(value["skills"], ["qp-skills:atona"])

    def test_collision_preflight_does_not_partially_install_the_other_host(self):
        foreign = self.home / ".codex/agents/qp-atona.toml"
        foreign.parent.mkdir(parents=True)
        foreign.write_text("personal file")
        with self.assertRaises(s.ConfigError):
            self.sync()
        self.assertEqual(foreign.read_text(encoding="utf-8"), "personal file")
        self.assertFalse((self.home / ".claude").exists())
        self.assertFalse((foreign.parent / c.STATE).exists())

    def test_edited_agents_are_preserved_on_update_and_remove(self):
        self.sync()
        path = self.home / ".claude/agents/qp-atona.md"
        path.write_bytes(path.read_bytes() + b"\nUser changes\n")
        before = {p: p.read_bytes() for p in self.home.rglob("*") if p.is_file()}
        for remove in (False, True):
            with self.assertRaises(s.ConfigError):
                self.sync(remove=remove)
            self.assertEqual({p: p.read_bytes() for p in before}, before)

    def test_symlink_destinations_are_not_followed(self):
        folder = self.home / ".codex/agents"
        folder.parent.mkdir()
        outside = self.root / "outside"
        outside.mkdir()
        try:
            folder.symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest("Symlinks unavailable")
        with self.assertRaises(s.ConfigError):
            self.sync()
        self.assertEqual(list(outside.iterdir()), [])
        folder.unlink()
        folder.mkdir()
        (folder / "qp-atona.toml").symlink_to(outside / "missing")
        with self.assertRaises(s.ConfigError):
            self.sync()
        self.assertFalse((outside / "missing").exists())

    def test_repository_host_symlink_cannot_redirect_local_settings_into_global_config(self):
        outside = self.home / ".codex"
        outside.mkdir()
        try:
            (self.repo / ".codex").symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest("Symlinks unavailable")
        self.setting(self.repo, {"codex": {"model": "repo-only"}})
        with self.assertRaisesRegex(s.ConfigError, "Repository host directory"):
            c.sync(("codex",), "repo", self.repo, home=self.home)
        self.assertEqual(list(outside.iterdir()), [])

    def test_interrupted_update_recovers_only_known_generated_bytes(self):
        self.sync()
        self.setting(self.home, {"claude": {"model": "new-model"}, "codex": {"reasoning": "high"}})
        write = c.atomic_write
        count = 0
        def interrupted(path, data, expected):
            nonlocal count
            count += 1
            if count == 3:
                raise OSError("simulated interruption")
            return write(path, data, expected)
        with patch.object(c, "atomic_write", side_effect=interrupted):
            with self.assertRaises(OSError):
                self.sync()
        modified = self.home / ".claude/agents/qp-alaga.md"
        previous = modified.read_bytes()
        modified.write_bytes(previous + b"\nnot generated\n")
        with self.assertRaises(s.ConfigError):
            self.sync()
        modified.write_bytes(previous)
        self.sync()
        self.assertEqual(header((self.home / ".claude/agents/qp-atona.md").read_bytes())["model"], "new-model")
        self.assertEqual(tomllib.loads((self.home / ".codex/agents/qp-atona.toml").read_text(encoding="utf-8"))["model_reasoning_effort"], "high")

    def test_stale_lock_requires_inspection_and_cannot_be_overwritten(self):
        folder = self.home / ".claude/agents"
        folder.mkdir(parents=True)
        lock = folder / c.LOCK
        lock.write_text("prior process")
        with self.assertRaisesRegex(s.ConfigError, "Setup lock"):
            self.sync()
        self.assertEqual(lock.read_text(encoding="utf-8"), "prior process")
        self.assertFalse((folder / c.STATE).exists())

    def test_invalid_ownership_paths_cannot_escape_the_agent_directory(self):
        self.sync()
        manifest = self.home / ".codex/agents" / c.STATE
        data = json.loads(manifest.read_text(encoding="utf-8"))
        victim = self.home / "victim"
        victim.write_text("preserve")
        data["files"]["../../victim"] = [c.digest(victim.read_bytes())]
        manifest.write_text(json.dumps(data))
        with self.assertRaises(s.ConfigError):
            self.sync(remove=True)
        self.assertEqual(victim.read_text(encoding="utf-8"), "preserve")

    def test_remove_is_idempotent_ignores_invalid_preferences_and_preserves_other_agents(self):
        self.sync()
        setting = self.setting(self.home, {})
        setting.write_text("invalid now")
        foreign = self.home / ".codex/agents/personal.toml"
        foreign.write_text("keep")
        self.sync(remove=True)
        self.sync(remove=True)
        self.assertEqual(setting.read_text(encoding="utf-8"), "invalid now")
        self.assertEqual(foreign.read_text(encoding="utf-8"), "keep")
        self.assertFalse((foreign.parent / c.STATE).exists())
        self.assertEqual(list(foreign.parent.glob("qp-*.toml")), [])

    def test_relative_or_overlapping_host_paths_are_rejected(self):
        for env in ({"CODEX_HOME": "relative"}, {"CODEX_HOME": str(self.home / ".claude")}):
            with patch.dict(os.environ, env):
                with self.assertRaises(s.ConfigError):
                    self.sync()

    def test_cli_inspection_accepts_explicit_non_git_project_and_reports_conflicting_scope(self):
        self.setting(self.repo, {"communication": "adaptive"})
        script = Path(c.__file__)
        env = {**os.environ, "HOME": str(self.home), "USERPROFILE": str(self.home)}
        result = subprocess.run([sys.executable, str(script), "inspect", "--repo", str(self.repo)],
                                capture_output=True, text=True, env=env, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["communication"], "adaptive")
        result = subprocess.run([sys.executable, str(script), "sync", "--scope", "user", "--host", "all", "--repo", str(self.repo)],
                                capture_output=True, text=True, env=env, timeout=10)
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("Traceback", result.stderr)
        self.assertFalse((self.home / ".claude").exists())


class PackagedAdapterTests(unittest.TestCase):
    def test_generated_adapters_and_schema_match_source_without_maintainer_preferences(self):
        root = Path(__file__).resolve().parents[3]
        for relative, data in c.package_outputs().items():
            with self.subTest(path=relative):
                self.assertEqual((root / relative).read_bytes(), data)
        source_roles = set(s.roles())
        manifest = json.loads((root / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(set(manifest["agents"]), {f"./agents/{name}.md" for name in source_roles})
        self.assertEqual(set(p.stem for p in (root / "agents").glob("*.md")), source_roles)
        # The shared schema must not grow another source of role/effort defaults.
        self.assertEqual(json.loads((s.ASSETS / "setting.schema.json").read_text(encoding="utf-8")), s.schema())


if __name__ == "__main__":
    unittest.main()
