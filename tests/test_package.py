"""Mechanical positive/negative controls, not assertions about instruction wording."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check_package.py"
SPEC = importlib.util.spec_from_file_location("check_package", SCRIPT)
package = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(package)


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write("skills/example/SKILL.md", "---\nname: example\ndescription: A useful result\n---\n# Example\n")
        self.write(".codex-plugin/plugin.json", json.dumps({"name": "qp-skills", "skills": "./skills/"}))
        self.write(".claude-plugin/plugin.json", json.dumps({"name": "qp-skills"}))

    def write(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        return target

    def rejected(self, fragment):
        errors = package.check(self.root)
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_valid_package_and_external_links(self):
        self.write("skills/example/references/detail.md", "[root](../SKILL.md) [web](https://example.com/x)\n")
        self.assertEqual([], package.check(self.root))

    def test_name_mismatch(self):
        self.write("skills/example/SKILL.md", "---\nname: different\ndescription: Result\n---\n")
        self.rejected("does not match")

    def test_invalid_yaml_and_description(self):
        for text, message in (("---\nname: [\n---\n", "expected"),
                              ("---\nname: example\n---\n", "description"),
                              ("# No frontmatter", "missing YAML")):
            with self.subTest(text=text):
                self.write("skills/example/SKILL.md", text)
                self.rejected(message)

    def test_duplicate_key_is_not_silently_overridden(self):
        self.write("skills/example/SKILL.md", "---\nname: example\nname: another\ndescription: Result\n---\n")
        self.rejected("duplicate mapping key")

    def test_nested_broken_reference(self):
        self.write("skills/example/references/detail.md", "[old owner](../../missing/SKILL.md)\n")
        self.rejected("missing link target")

    def test_missing_skill_entrypoint(self):
        self.write("skills/orphan/agents/openai.yaml", "interface: {}\n")
        self.rejected("missing SKILL.md")

    def test_code_examples_do_not_become_links(self):
        self.write("skills/example/references/detail.md", "```md\n[not a link](missing.md)\n```\n")
        self.assertEqual([], package.check(self.root))

    def test_links_cannot_escape_package(self):
        self.write("README.md", "[outside](../outside.md)\n")
        self.rejected("escapes package")

    def test_both_manual_only_controls_agree(self):
        self.write("skills/example/SKILL.md", "---\nname: example\ndescription: Result\ndisable-model-invocation: true\n---\n")
        self.rejected("policies disagree")
        self.write("skills/example/agents/openai.yaml", "policy:\n  allow_implicit_invocation: false\n")
        self.assertEqual([], package.check(self.root))

    def test_strings_are_not_boolean_policy(self):
        self.write("skills/example/agents/openai.yaml", 'policy:\n  allow_implicit_invocation: "false"\n')
        self.rejected("must be boolean")

    def test_invalid_plugin_path_and_json(self):
        self.write(".codex-plugin/plugin.json", '{"name":"qp-skills","skills":"./missing/"}')
        self.rejected("Codex skills path")
        self.write(".claude-plugin/plugin.json", "{")
        self.rejected(".claude-plugin/plugin.json")

    def test_empty_installation_cannot_pass(self):
        (self.root / "skills/example/SKILL.md").unlink()
        self.rejected("no skill entrypoints")

    def test_cli_propagates_failure(self):
        command = [sys.executable, str(SCRIPT), "--root", str(self.root)]
        self.assertEqual(0, subprocess.run(command, capture_output=True, timeout=10).returncode)
        self.write("README.md", "[missing](does-not-exist.md)\n")
        result = subprocess.run(command, capture_output=True, text=True, timeout=10)
        self.assertEqual(1, result.returncode)
        self.assertIn("missing link target", result.stderr)


if __name__ == "__main__":
    unittest.main()
