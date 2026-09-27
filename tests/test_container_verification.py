import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "skills/alarina/scripts/container_verification.py"
spec = importlib.util.spec_from_file_location("container_verification", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ContainerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name) / "checkout"
        self.project.mkdir()
        (self.project / ".qp").mkdir()
        (self.project / ".devcontainer").mkdir()
        (self.project / ".devcontainer/devcontainer.json").write_text("// existing config\n{}", encoding="utf-8")
        runner = self.project / "skills/alarina/scripts/alarina.py"
        runner.parent.mkdir(parents=True)
        runner.write_text("# runner", encoding="utf-8")
        self.output = ".qp/container-verification/test"

    def snapshot(self, project):
        return {"kind": "git", "complete": True, "head": "head", "base_oid": None, "index": [],
                "files": [{"path": "file.txt", "kind": "file", "sha256": "f" * 64, "size": 1,
                           "mode": 0o644}],
                "candidate_digest": "a" * 64}

    def transport(self, *, source=None, running=True, gate="passed", fresh=True):
        source = source or str(self.project)

        def run(argv, timeout):
            if argv[1] == "inspect":
                info = {"Id": "abc123def4567890", "Image": "image-sha", "State": {"Running": running},
                        "Mounts": [{"Type": "bind", "Source": source,
                                    "Destination": "/work", "RW": True}]}
                return 0, json.dumps([info])
            if "-c" in argv:
                import hashlib
                runner = self.project / "skills/alarina/scripts/alarina.py"
                return 0, json.dumps({"python": "3.12.0", "runner_sha256": hashlib.sha256(runner.read_bytes()).hexdigest()})
            if "verify" in argv:
                path = self.project / self.output / "receipt.json"
                path.parent.mkdir(parents=True)
                digest = "a" * 64
                receipt = {"schema_version": 1, "gate_status": gate, "project": "/work",
                           "snapshot_before": self.snapshot(self.project),
                           "snapshot_after": self.snapshot(self.project),
                           "selection": {"not_selected": []}, "checks": [{"id": "test", "result": "passed"}]}
                path.write_text(json.dumps(receipt), encoding="utf-8")
                return (0 if gate == "passed" else 1), "{}"
            return (0 if fresh else 1), json.dumps({"fresh": fresh})

        return run

    def verify(self, run):
        return module.verify_existing("abc123def456", self.project, "/work", "/work/skills/alarina/scripts/alarina.py",
                                      run=run, snapshot=self.snapshot, output_relative=self.output)

    def test_passed_gate_binds_mount_and_receipt(self):
        result = self.verify(self.transport())
        self.assertEqual(result["status"], "passed")
        self.assertEqual(result["environment"]["host_project"], str(self.project.resolve()))

    def test_wrong_checkout_rejected_before_execution(self):
        with self.assertRaisesRegex(module.ContainerVerificationError, "real checkout"):
            self.verify(self.transport(source=str(self.project.parent)))

    def test_stopped_container_rejected(self):
        with self.assertRaisesRegex(module.ContainerVerificationError, "not running"):
            self.verify(self.transport(running=False))

    def test_failed_gate_and_stale_receipt_rejected(self):
        with self.assertRaisesRegex(module.ContainerVerificationError, "gate failed"):
            self.verify(self.transport(gate="failed"))
        self.output = ".qp/container-verification/stale"
        with self.assertRaisesRegex(module.ContainerVerificationError, "stale"):
            self.verify(self.transport(fresh=False))

    def test_no_gate_receipt_rejected(self):
        def run(argv, timeout):
            if argv[1] == "inspect" or "-c" in argv:
                return self.transport()(argv, timeout)
            return 1, ""
        with self.assertRaisesRegex(module.ContainerVerificationError, "receipt"):
            self.verify(run)

    def test_candidate_drift_rejected(self):
        transport = self.transport()

        def run(argv, timeout):
            code, output = transport(argv, timeout)
            if "verify" in argv:
                path = self.project / self.output / "receipt.json"
                receipt = json.loads(path.read_text(encoding="utf-8"))
                receipt["snapshot_after"]["candidate_digest"] = "b" * 64
                path.write_text(json.dumps(receipt), encoding="utf-8")
            return code, output

        with self.assertRaisesRegex(module.ContainerVerificationError, "changed candidate"):
            self.verify(run)

    def test_nested_mount_masking_is_rejected_by_file_inventory(self):
        transport = self.transport()

        def run(argv, timeout):
            code, output = transport(argv, timeout)
            if "verify" in argv:
                path = self.project / self.output / "receipt.json"
                receipt = json.loads(path.read_text(encoding="utf-8"))
                receipt["snapshot_after"]["files"][0]["sha256"] = "0" * 64
                receipt["snapshot_before"]["files"][0]["sha256"] = "0" * 64
                path.write_text(json.dumps(receipt), encoding="utf-8")
            return code, output

        with self.assertRaisesRegex(module.ContainerVerificationError, "inventories differ"):
            self.verify(run)

    def test_executable_bit_mismatch_is_rejected(self):
        transport = self.transport()

        def run(argv, timeout):
            code, output = transport(argv, timeout)
            if "verify" in argv:
                path = self.project / self.output / "receipt.json"
                receipt = json.loads(path.read_text(encoding="utf-8"))
                for key in ("snapshot_before", "snapshot_after"):
                    receipt[key]["files"][0]["mode"] = 0o755
                path.write_text(json.dumps(receipt), encoding="utf-8")
            return code, output

        with self.assertRaisesRegex(module.ContainerVerificationError, "inventories differ"):
            self.verify(run)

    def test_read_write_mode_difference_is_tolerated(self):
        transport = self.transport()

        def run(argv, timeout):
            code, output = transport(argv, timeout)
            if "verify" in argv:
                path = self.project / self.output / "receipt.json"
                receipt = json.loads(path.read_text(encoding="utf-8"))
                for key in ("snapshot_before", "snapshot_after"):
                    receipt[key]["files"][0]["mode"] = 0o600
                path.write_text(json.dumps(receipt), encoding="utf-8")
            return code, output

        self.assertEqual(self.verify(run)["status"], "passed")

    def test_receipt_limit_is_separate_from_metadata_limit(self):
        path = self.project / "receipt.json"
        path.write_text(json.dumps({"padding": "x" * (module.MAX_JSON + 1024)}), encoding="utf-8")
        self.assertIn("padding", module._read_receipt(path))

    def test_missing_devcontainer_config_rejected(self):
        (self.project / ".devcontainer/devcontainer.json").unlink()
        with self.assertRaisesRegex(module.ContainerVerificationError, "devcontainer config"):
            self.verify(self.transport())

    def test_runner_hash_mismatch_rejected(self):
        transport = self.transport()

        def run(argv, timeout):
            if "-c" in argv:
                return 0, json.dumps({"python": "3.12.0", "runner_sha256": "0" * 64})
            return transport(argv, timeout)

        with self.assertRaisesRegex(module.ContainerVerificationError, "runner does not match"):
            self.verify(run)

    def test_failed_check_record_rejected(self):
        transport = self.transport()

        def run(argv, timeout):
            code, output = transport(argv, timeout)
            if "verify" in argv:
                path = self.project / self.output / "receipt.json"
                receipt = json.loads(path.read_text(encoding="utf-8"))
                receipt["checks"][0]["result"] = "failed"
                path.write_text(json.dumps(receipt), encoding="utf-8")
            return code, output

        with self.assertRaisesRegex(module.ContainerVerificationError, "gate failed"):
            self.verify(run)

    def test_timeout_identifies_run_for_recovery(self):
        transport = self.transport()

        def run(argv, timeout):
            if "verify" in argv:
                raise module.ContainerVerificationError("Docker client timed out")
            return transport(argv, timeout)

        with self.assertRaisesRegex(module.ContainerVerificationError,
                                    "container=abc123def456; output=.*container-verification/test"):
            self.verify(run)


if __name__ == "__main__":
    unittest.main()
