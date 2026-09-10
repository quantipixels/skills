import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).with_name("skill-doctor.py")
SPEC = importlib.util.spec_from_file_location("skill_doctor", SCRIPT)
skill_doctor = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(skill_doctor)


class SkillDoctorTest(unittest.TestCase):
    def make_repo(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        repo = Path(tmp.name)
        alpha = repo / "skills" / "alpha"
        beta = repo / "skills" / "beta"
        (alpha / "references").mkdir(parents=True)
        (alpha / "scripts").mkdir()
        beta.mkdir(parents=True)
        (alpha / "SKILL.md").write_text(
            "---\nname: alpha\ndescription: Route alpha work.\nmetadata:\n  maturity: experimental\n---\n\n"
            "# Alpha\n\nRead [focused guidance](references/focused.md). Use `beta` as needed.\n"
        )
        (alpha / "references" / "focused.md").write_text("Read [detail](detail.md).\n")
        (alpha / "references" / "detail.md").write_text("# Detail\n")
        (alpha / "references" / "orphan.md").write_text("# Orphan\n")
        (alpha / "scripts" / "mechanic.py").write_text("print('ok')\n")
        (alpha / "scripts" / "test_mechanic.py").write_text("# test placeholder\n")
        (beta / "SKILL.md").write_text("---\nname: beta\ndescription: Do beta work.\n---\n\n# Beta\n")
        return repo

    def test_reports_context_resources_and_reference_graph_without_verdict(self):
        repo = self.make_repo()
        report = skill_doctor.build(skill_doctor.parse_args(["--repo", str(repo), "--skill", "alpha", "--format", "json"]))
        alpha = report["skills"][0]
        self.assertEqual(alpha["name"], "alpha")
        self.assertEqual(alpha["maturity"], "experimental")
        self.assertEqual(alpha["related_skill_mentions"], ["beta"])
        self.assertEqual(alpha["supporting_markdown"]["entrypoint_links"], ["references/focused.md"])
        self.assertEqual(alpha["supporting_markdown"]["unreferenced_candidates"], ["references/orphan.md"])
        self.assertEqual(alpha["scripts"]["non_test_files"], ["scripts/mechanic.py"])
        self.assertEqual(alpha["scripts"]["tests"], ["scripts/test_mechanic.py"])
        self.assertIn("not quality, focus, or behavior verdicts", report["interpretation"])

    def test_repo_inventory_uses_native_skills_directory(self):
        repo = self.make_repo()
        report = skill_doctor.build(skill_doctor.parse_args(["--repo", str(repo)]))
        self.assertEqual([item["name"] for item in report["skills"]], ["alpha", "beta"])


if __name__ == "__main__":
    unittest.main()
