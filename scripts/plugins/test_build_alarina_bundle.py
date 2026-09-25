#!/usr/bin/env python3
"""Focused structural and failure checks for the Alárinà compiler."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

import yaml


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("build_alarina_bundle", HERE / "build_alarina_bundle.py")
COMPILER = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(COMPILER)
REPOSITORY = HERE.parents[1]


class BundleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="qp-alarina-bundle-")
        self.root = Path(self.temporary.name)
        self.repository = self.root / "source"
        (self.repository / "skills").mkdir(parents=True)
        for name in ("alarina",):
            shutil.copytree(REPOSITORY / "skills" / name, self.repository / "skills" / name)
        (self.repository / "agents").mkdir()
        shutil.copy2(REPOSITORY / "agents" / "alarina.md", self.repository / "agents" / "alarina.md")
        shutil.copy2(REPOSITORY / "package.json", self.repository / "package.json")
        shutil.copy2(REPOSITORY / "LICENSE", self.repository / "LICENSE")
        self.providers = self.root / "providers.yaml"
        shutil.copy2(HERE / "providers.yaml", self.providers)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def build(self, name: str, provider: str = "codex") -> tuple[Path, dict]:
        output = self.root / name
        return output, COMPILER.build(output, provider, self.repository, self.providers)

    def change_routes(self, change) -> None:
        path = self.repository / "skills" / "alarina" / "routes.yaml"
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        change(data)
        path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")

    def test_provider_specimens_have_one_entry_and_complete_commands(self) -> None:
        for provider in ("codex", "claude"):
            output, manifest = self.build(provider, provider)
            skill = output / "skills" / "alarina"
            self.assertEqual([skill / "SKILL.md"], list(output.rglob("SKILL.md")))
            routes = yaml.safe_load((self.repository / "skills/alarina/routes.yaml").read_text(encoding="utf-8"))
            self.assertEqual([item["id"] for item in routes["commands"]], manifest["commands"])
            self.assertEqual([], list(output.rglob("OWNER.md")))
            for command in routes["commands"]:
                source = self.repository / "skills/alarina" / command["reference"]
                target = skill / command["reference"]
                self.assertEqual(source.read_bytes(), target.read_bytes())
                self.assertEqual(0o755 if source.stat().st_mode & 0o111 else 0o644, target.stat().st_mode & 0o777)
            for path in (self.repository / "skills/alarina/references").rglob("*"):
                if not path.is_file() or "__pycache__" in path.parts or ".pytest_cache" in path.parts or path.suffix == ".pyc" or path.name == ".DS_Store":
                    continue
                relative = path.relative_to(self.repository / "skills/alarina")
                copied = skill / relative
                self.assertEqual(path.read_bytes(), copied.read_bytes())
                self.assertEqual(0o755 if path.stat().st_mode & 0o111 else 0o644, copied.stat().st_mode & 0o777)
            self.assertFalse(any("__pycache__" in path.parts or path.suffix == ".pyc" for path in output.rglob("*")))
            self.assertEqual((self.repository / "LICENSE").read_bytes(), (output / "LICENSE").read_bytes())
            self.assertTrue(all(row["sha256"] == COMPILER.digest((output / row["path"]).read_bytes()) for row in manifest["files"]))
            self.assertTrue(all(row["source"] is None or row["source_sha256"] == COMPILER.digest((self.repository / row["source"]).read_bytes()) for row in manifest["files"]))
            COMPILER.check_links(skill)
            text = (skill / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn(manifest["qualified_invocation"], text)
            self.assertNotIn("dirty", manifest["source"])
            self.assertEqual(64, len(manifest["source"]["sha256"]))
            other = "/qp-skills:alarina" if provider == "codex" else "$qp-skills:alarina"
            self.assertNotIn(other, text)
            self.assertEqual(manifest, json.loads((output / "bundle-manifest.json").read_text(encoding="utf-8")))
        self.assertTrue((self.root / "codex/skills/alarina/agents/openai.yaml").is_file())
        claude_agent = (self.root / "claude/agents/alarina.md").read_text(encoding="utf-8")
        self.assertIn("skills:\n  - qp-skills:alarina", claude_agent)
        self.assertIn("${CLAUDE_PLUGIN_ROOT}/skills/alarina/SKILL.md", claude_agent)
        self.assertNotIn("skills:\n  - alarina", claude_agent)

    def test_fixed_input_is_deterministic(self) -> None:
        first, manifest1 = self.build("first")
        second, manifest2 = self.build("second")
        self.assertEqual(manifest1, manifest2)
        files1 = {p.relative_to(first): p.read_bytes() for p in first.rglob("*") if p.is_file()}
        files2 = {p.relative_to(second): p.read_bytes() for p in second.rglob("*") if p.is_file()}
        self.assertEqual(files1, files2)

    def test_source_group_write_bit_does_not_change_bundle(self) -> None:
        first, manifest1 = self.build("first")
        license_path = self.repository / "LICENSE"
        license_path.chmod(0o664)
        second, manifest2 = self.build("second")
        self.assertEqual(manifest1, manifest2)
        self.assertEqual(0o644, (first / "LICENSE").stat().st_mode & 0o777)
        self.assertEqual(0o644, (second / "LICENSE").stat().st_mode & 0o777)

    def test_existing_output_and_failed_build_preserve_previous_artifact(self) -> None:
        output, _ = self.build("candidate")
        original = {p.relative_to(output): p.read_bytes() for p in output.rglob("*") if p.is_file()}
        with self.assertRaisesRegex(COMPILER.BuildError, "already exists"):
            COMPILER.build(output, "codex", self.repository, self.providers)
        entry = self.repository / "skills/alarina/SKILL.md"
        entry.write_text(entry.read_text(encoding="utf-8") + "\n[broken](../outside.md)\n", encoding="utf-8")
        with self.assertRaisesRegex(COMPILER.BuildError, "link escapes"):
            COMPILER.build(self.root / "failed", "codex", self.repository, self.providers)
        self.assertFalse((self.root / "failed").exists())
        self.assertEqual(original, {p.relative_to(output): p.read_bytes() for p in output.rglob("*") if p.is_file()})

    def test_replace_publishes_complete_candidate(self) -> None:
        output, first = self.build("candidate")
        marker = output / "stale-file"
        marker.write_text("old\n", encoding="utf-8")
        second = COMPILER.build(output, "codex", self.repository, self.providers, replace=True)
        self.assertFalse(marker.exists())
        self.assertEqual(first, second)
        self.assertEqual(second, json.loads((output / "bundle-manifest.json").read_text(encoding="utf-8")))
        self.assertFalse(output.with_name(".candidate.previous").exists())

    def test_verify_output_rejects_stale_or_extra_files(self) -> None:
        output, expected = self.build("candidate")
        self.assertEqual(expected, COMPILER.verify_output(output, "codex", self.repository, self.providers))
        (output / "skills/alarina/SKILL.md").write_text("changed\n", encoding="utf-8")
        with self.assertRaisesRegex(COMPILER.BuildError, "stale bundle"):
            COMPILER.verify_output(output, "codex", self.repository, self.providers)

    def test_route_command_and_path_failures(self) -> None:
        self.change_routes(lambda data: data["routes"][0]["owners"].append({"command": "qp-update", "required": True}))
        with self.assertRaisesRegex(COMPILER.BuildError, "explicit-only"):
            self.build("excluded")
        self.change_routes(lambda data: data["routes"][0].update(playbook="../../outside.md"))
        with self.assertRaisesRegex(COMPILER.BuildError, "escaping playbook"):
            self.build("escape")

    def test_missing_command_and_malformed_route_fail(self) -> None:
        reference = self.repository / "skills/alarina/commands/alaga-deliver.md"
        reference.unlink()
        with self.assertRaisesRegex(COMPILER.BuildError, "missing command"):
            self.build("missing")
        shutil.copy2(REPOSITORY / "skills/alarina/commands/alaga-deliver.md", reference)
        self.change_routes(lambda data: data["routes"][0].update(implicit="yes"))
        with self.assertRaisesRegex(COMPILER.BuildError, "implicit"):
            self.build("malformed")

    def test_retired_discovery_metadata_fails(self) -> None:
        retired = self.repository / "skills" / "alaga" / "SKILL.md"
        retired.parent.mkdir()
        retired.write_text("---\nname: alaga\ndescription: Retired\n---\n", encoding="utf-8")
        with self.assertRaisesRegex(COMPILER.BuildError, "one SKILL"):
            self.build("retired")
        shutil.rmtree(retired.parent)
        nested = self.repository / "skills" / "alarina" / "references" / "alaga" / "agents" / "openai.yaml"
        nested.parent.mkdir()
        nested.write_text("interface: {}\n", encoding="utf-8")
        with self.assertRaisesRegex(COMPILER.BuildError, "nested discovery"):
            self.build("nested")

    def test_output_overlapping_source_is_rejected(self) -> None:
        for output in (self.repository, self.repository / "skills", self.repository / "skills/alarina", self.repository / "skills/alarina/child", self.repository / "plugins/../skills"):
            with self.subTest(output=output), self.assertRaisesRegex(COMPILER.BuildError, "overlaps canonical source"):
                COMPILER.build(output, "codex", self.repository, self.providers, replace=True)

    def test_provider_and_placeholder_failures(self) -> None:
        config = yaml.safe_load(self.providers.read_text(encoding="utf-8"))
        config["providers"]["codex"]["frontmatter"].append("unknown")
        self.providers.write_text(yaml.safe_dump(config, sort_keys=False), encoding="utf-8")
        with self.assertRaisesRegex(COMPILER.BuildError, "frontmatter"):
            self.build("bad-provider")
        shutil.copy2(HERE / "providers.yaml", self.providers)
        config = yaml.safe_load(self.providers.read_text(encoding="utf-8"))
        config["candidate_providers"][0]["release_inclusion"] = True
        self.providers.write_text(yaml.safe_dump(config, sort_keys=False), encoding="utf-8")
        with self.assertRaisesRegex(COMPILER.BuildError, "cannot be released"):
            self.build("released-candidate")
        shutil.copy2(HERE / "providers.yaml", self.providers)
        entry = self.repository / "skills/alarina/SKILL.md"
        entry.write_text(entry.read_text(encoding="utf-8") + "\n{{missing_provider_value}}\n", encoding="utf-8")
        with self.assertRaisesRegex(COMPILER.BuildError, "placeholder"):
            self.build("placeholder")


if __name__ == "__main__":
    unittest.main()
