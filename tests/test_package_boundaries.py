"""Regression controls for active documents and packaged host metadata."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/skills/check_package.py"
SPEC = importlib.util.spec_from_file_location("package_boundaries", SCRIPT)
package = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(package)


class PackageBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "package"
        self.write("skills/example/SKILL.md", "---\nname: example\ndescription: A usable skill\n---\n")
        self.write(".codex-plugin/plugin.json", json.dumps({"name": "qp-skills", "skills": "./skills/"}))
        self.write(".claude-plugin/plugin.json", json.dumps({"name": "qp-skills"}))

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_active_observations_directories_are_not_archives(self):
        for folder in ("skills/example/observations", "docs/observations", "evals/new/observations"):
            with self.subTest(folder=folder):
                path = self.write(f"{folder}/detail.md", "[missing](missing.md)\n")
                errors = package.check(self.root)
                self.assertTrue(any(f"{folder}/detail.md: missing link target" in error for error in errors), errors)
                path.unlink()

    def test_only_known_historical_records_skip_current_link_validation(self):
        for group in ("coordination", "engineering"):
            self.write(f"evals/{group}/observations/past.md", "[old](retired.md)\n")
        self.assertEqual([], package.check(self.root))
        self.write("evals/engineering/README.md", "[current](missing.md)\n")
        self.assertTrue(any("evals/engineering/README.md: missing link target" in error
                            for error in package.check(self.root)))

    def metadata_link(self, target):
        path = self.root / "skills/example/agents/openai.yaml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.symlink_to(target)
        return path

    def test_missing_metadata_and_internal_metadata_symlink_are_valid(self):
        self.assertEqual([], package.check(self.root))
        self.write("skills/example/agents/shared.yaml", "interface: {}\n")
        self.metadata_link("shared.yaml")
        self.assertEqual([], package.check(self.root))

    def test_dangling_metadata_is_not_treated_as_absent(self):
        self.metadata_link("missing.yaml")
        errors = package.check(self.root)
        self.assertTrue(any("metadata" in error for error in errors), errors)

    def test_metadata_outside_the_package_is_rejected(self):
        target = self.root.parent / "unpackaged.yaml"
        target.write_text("interface: {}\n", encoding="utf-8")
        self.metadata_link(target)
        errors = package.check(self.root)
        self.assertTrue(any("metadata escapes package" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
