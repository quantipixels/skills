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
        (alpha / "workflows").mkdir()
        beta.mkdir(parents=True)
        (alpha / "SKILL.md").write_text(
            "---\nname: alpha\ndescription: Review payment changes for security and correctness.\nmetadata:\n  maturity: experimental\n---\n\n"
            "# Alpha\n\nRead [focused guidance](references/focused.md) and [lane](workflows/lane.md). Use `beta` as needed.\n"
        )
        (alpha / "references" / "focused.md").write_text("Read [detail](detail.md).\n")
        (alpha / "references" / "detail.md").write_text("# Detail\n")
        (alpha / "references" / "orphan.md").write_text("# Orphan\n")
        (alpha / "workflows" / "lane.md").write_text("# Lane\n")
        (alpha / "scripts" / "mechanic.py").write_text("print('ok')\n")
        (alpha / "scripts" / "test_mechanic.py").write_text("# test placeholder\n")
        (beta / "SKILL.md").write_text(
            "---\nname: beta\ndescription: Review API changes for security and correctness.\n---\n\n# Beta\n"
        )
        return repo

    def test_reports_context_resources_and_reference_graph_without_verdict(self):
        repo = self.make_repo()
        report = skill_doctor.build(skill_doctor.parse_args(["--repo", str(repo), "--skill", "alpha", "--format", "json"]))
        alpha = report["skills"][0]
        self.assertEqual(alpha["name"], "alpha")
        self.assertEqual(alpha["maturity"], "experimental")
        self.assertEqual(alpha["related_skill_mentions"], ["beta"])
        self.assertEqual(
            alpha["supporting_markdown"]["entrypoint_links"],
            ["references/focused.md", "workflows/lane.md"],
        )
        self.assertEqual(alpha["supporting_markdown"]["unreferenced_candidates"], ["references/orphan.md"])
        self.assertEqual(alpha["scripts"]["non_test_files"], ["scripts/mechanic.py"])
        self.assertEqual(alpha["scripts"]["tests"], ["scripts/test_mechanic.py"])
        self.assertEqual(alpha["resources"]["workflows"], 1)
        self.assertIn("not quality", report["interpretation"])
        self.assertIn("not prove", report["portfolio"]["interpretation"])

    def test_repo_inventory_reports_routing_footprint_and_overlap_leads(self):
        repo = self.make_repo()
        report = skill_doctor.build(skill_doctor.parse_args(["--repo", str(repo)]))
        self.assertEqual([item["name"] for item in report["skills"]], ["alpha", "beta"])
        self.assertEqual(
            report["portfolio"]["routing_pointer_total"]["words"],
            sum(item["routing_pointer"]["words"] for item in report["skills"]),
        )
        lead = report["portfolio"]["description_overlap_leads"][0]
        self.assertEqual(lead["skills"], ["alpha", "beta"])
        self.assertEqual(lead["shared_terms"], ["changes", "correctness", "review", "security"])


if __name__ == "__main__":
    unittest.main()
