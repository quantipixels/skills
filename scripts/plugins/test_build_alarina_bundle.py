"""Behavioral checks for shared-root declaration generation."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("builder", HERE / "build_alarina_bundle.py")
builder = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(builder)
SOURCE = HERE.parents[1]


class NativeDeclarationsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        shutil.copytree(SOURCE / "skills", self.root / "skills")
        shutil.copytree(SOURCE / "agents", self.root / "agents")
        (self.root / "scripts/plugins").mkdir(parents=True)
        shutil.copy2(SOURCE / "scripts/plugins/providers.yaml", self.root / "scripts/plugins/providers.yaml")
        shutil.copy2(SOURCE / "package.json", self.root / "package.json")
        shutil.copy2(SOURCE / "opencode.json", self.root / "opencode.json")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_build_uses_one_shared_skill_and_native_agent_formats(self) -> None:
        builder.run(self.root, check=False)
        builder.run(self.root, check=True)
        self.assertEqual([self.root / "skills/alarina/SKILL.md"], list(self.root.rglob("SKILL.md")))
        codex = json.loads((self.root / ".codex-plugin/plugin.json").read_text())
        claude = json.loads((self.root / ".claude-plugin/plugin.json").read_text())
        self.assertEqual("./skills/", codex["skills"])
        self.assertEqual("./skills/", claude["skills"])
        self.assertEqual(["./agents/alarina.claude.md"], claude["agents"])
        self.assertIn("$qp-skills:alarina", (self.root / "agents/alarina.codex.toml").read_text())
        self.assertIn("qp-skills:alarina", (self.root / "agents/alarina.claude.md").read_text())
        self.assertEqual((self.root / "agents/alarina.md").read_bytes(), (self.root / ".opencode/agents/alarina.md").read_bytes())

    def test_check_rejects_stale_declaration(self) -> None:
        builder.run(self.root, check=False)
        (self.root / "agents/alarina.md").write_text((self.root / "agents/alarina.md").read_text() + "\nNew rule.\n")
        with self.assertRaisesRegex(builder.BuildError, "stale"):
            builder.run(self.root, check=True)

    def test_menu_drift_and_explicit_only_routes_fail(self) -> None:
        skill = self.root / "skills/alarina/SKILL.md"
        skill.write_text(skill.read_text().replace("Assess a reported issue", "Change a reported issue"))
        with self.assertRaisesRegex(builder.BuildError, "table differs"):
            builder.run(self.root, check=False)
        shutil.copy2(SOURCE / "skills/alarina/SKILL.md", skill)
        routes = self.root / "skills/alarina/routes.yaml"
        routes.write_text(routes.read_text().replace("command: alaga-intake", "command: qp-update", 1))
        with self.assertRaisesRegex(builder.BuildError, "explicit-only"):
            builder.run(self.root, check=False)

    def test_links_and_discovery_containment_fail(self) -> None:
        skill = self.root / "skills/alarina/SKILL.md"
        skill.write_text(skill.read_text() + "\n[escape](../../other.md)\n")
        with self.assertRaisesRegex(builder.BuildError, "link escapes"):
            builder.run(self.root, check=False)
        shutil.copy2(SOURCE / "skills/alarina/SKILL.md", skill)
        extra = self.root / "skills/other/SKILL.md"
        extra.parent.mkdir()
        extra.write_text("---\nname: other\n---\n")
        with self.assertRaisesRegex(builder.BuildError, "one SKILL"):
            builder.run(self.root, check=False)

    def test_native_skill_paths_reject_drift(self) -> None:
        for relative, field, diagnostic in (
            ("opencode.json", "skills", "OpenCode skills.paths"),
            ("package.json", "pi", "Pi pi.skills"),
        ):
            with self.subTest(host=relative):
                path = self.root / relative
                original = path.read_text()
                try:
                    data = json.loads(original)
                    data[field] = {"paths": ["./missing"]} if field == "skills" else {"skills": ["./missing"]}
                    path.write_text(json.dumps(data))
                    with self.assertRaisesRegex(builder.BuildError, diagnostic):
                        builder.run(self.root, check=False)
                finally:
                    path.write_text(original)

    def test_skill_description_limit(self) -> None:
        path = self.root / "skills/alarina/SKILL.md"
        text = path.read_text()
        description = builder.frontmatter(path)[0]["description"]
        path.write_text(text.replace(description, "x" * 1025, 1))
        with self.assertRaisesRegex(builder.BuildError, "description exceeds 1024"):
            builder.run(self.root, check=False)


if __name__ == "__main__":
    unittest.main()
