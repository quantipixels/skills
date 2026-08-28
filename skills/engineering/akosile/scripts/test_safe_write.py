import hashlib
import json
import subprocess
import sys
import tempfile
import threading
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("safe-write.py")


def invoke(*arguments: object) -> tuple[int, dict]:
    result = subprocess.run(
        [sys.executable, str(SCRIPT), *map(str, arguments)],
        check=False,
        capture_output=True,
        text=True,
    )
    return result.returncode, json.loads(result.stdout)


class SafeWriteTests(unittest.TestCase):
    def test_snapshot_and_create_use_exact_matching_bytes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root = base / ".qp"
            root.mkdir()
            target = root / "record.md"
            snapshot = base / "snapshot.md"
            candidate = base / "candidate.md"

            snapshot.write_text("stale\n", encoding="utf-8")
            code, payload = invoke(
                "snapshot",
                "--root",
                root,
                "--target",
                target,
                "--output",
                snapshot,
            )
            self.assertEqual(code, 0)
            self.assertEqual(payload["result"]["digest"], "absent")
            self.assertFalse(snapshot.exists())

            candidate.write_text("first\n", encoding="utf-8")
            code, payload = invoke(
                "write",
                "--root",
                root,
                "--target",
                target,
                "--candidate",
                candidate,
                "--expected",
                "absent",
            )
            self.assertEqual(code, 0)

            code, payload = invoke(
                "snapshot",
                "--root",
                root,
                "--target",
                target,
                "--output",
                snapshot,
            )
            self.assertEqual(code, 0)
            self.assertEqual(snapshot.read_bytes(), target.read_bytes())
            self.assertEqual(
                payload["result"]["digest"], hashlib.sha256(snapshot.read_bytes()).hexdigest()
            )

            code, payload = invoke(
                "snapshot",
                "--root",
                root,
                "--target",
                target,
                "--output",
                root / "inside.md",
            )
            self.assertEqual(code, 2)
            self.assertEqual(payload["error"]["code"], "SNAPSHOT_INSIDE_ROOT")

    def test_candidate_based_on_snapshot_cannot_overwrite_later_change(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root = base / ".qp"
            root.mkdir()
            target = root / "settings.json"
            snapshot = base / "settings.snapshot.json"
            candidate = base / "candidate.json"
            target.write_text('{"base": true}\n', encoding="utf-8")

            code, payload = invoke(
                "snapshot",
                "--root",
                root,
                "--target",
                target,
                "--output",
                snapshot,
            )
            self.assertEqual(code, 0)
            expected = payload["result"]["digest"]
            self.assertEqual(snapshot.read_text(encoding="utf-8"), '{"base": true}\n')

            target.write_text('{"concurrent": true}\n', encoding="utf-8")
            candidate.write_text(
                snapshot.read_text(encoding="utf-8").replace("true", '"edited"'),
                encoding="utf-8",
            )

            code, payload = invoke(
                "write",
                "--root",
                root,
                "--target",
                target,
                "--candidate",
                candidate,
                "--expected",
                expected,
            )
            self.assertEqual(code, 2)
            self.assertEqual(payload["error"]["code"], "STALE_TARGET")
            self.assertEqual(target.read_text(encoding="utf-8"), '{"concurrent": true}\n')

    def test_concurrent_writers_accept_only_one_shared_digest(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "record.md"
            target.write_text("base\n", encoding="utf-8")
            expected = hashlib.sha256(target.read_bytes()).hexdigest()
            candidates = []
            for name in ("one", "two"):
                candidate = root / f"{name}.md"
                candidate.write_text(f"{name}\n", encoding="utf-8")
                candidates.append(candidate)

            barrier = threading.Barrier(3)
            outcomes: list[str] = []

            def writer(candidate: Path) -> None:
                barrier.wait()
                code, payload = invoke(
                    "write",
                    "--root",
                    root,
                    "--target",
                    target,
                    "--candidate",
                    candidate,
                    "--expected",
                    expected,
                )
                outcomes.append("OK" if code == 0 else payload["error"]["code"])

            threads = [threading.Thread(target=writer, args=(candidate,)) for candidate in candidates]
            for thread in threads:
                thread.start()
            barrier.wait()
            for thread in threads:
                thread.join(timeout=10)

            self.assertCountEqual(outcomes, ["OK", "STALE_TARGET"])
            self.assertIn(target.read_text(encoding="utf-8"), {"one\n", "two\n"})

    def test_rejects_outside_target_and_does_not_create_parent(self) -> None:
        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as outside:
            root = Path(directory)
            candidate = root / "candidate.md"
            candidate.write_text("candidate\n", encoding="utf-8")

            code, payload = invoke(
                "write",
                "--root",
                root,
                "--target",
                Path(outside) / "record.md",
                "--candidate",
                candidate,
                "--expected",
                "absent",
            )
            self.assertEqual(code, 2)
            self.assertEqual(payload["error"]["code"], "TARGET_OUTSIDE_ROOT")

            missing_target = root / "missing" / "record.md"
            code, payload = invoke(
                "write",
                "--root",
                root,
                "--target",
                missing_target,
                "--candidate",
                candidate,
                "--expected",
                "absent",
            )
            self.assertEqual(code, 2)
            self.assertEqual(payload["error"]["code"], "PARENT_MISSING")
            self.assertFalse(missing_target.parent.exists())

    def test_rejects_symlink_target_path(self) -> None:
        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as outside:
            root = Path(directory)
            link = root / "linked"
            try:
                link.symlink_to(Path(outside), target_is_directory=True)
            except OSError:
                self.skipTest("symlinks unavailable")
            candidate = root / "candidate.md"
            candidate.write_text("candidate\n", encoding="utf-8")

            code, payload = invoke(
                "write",
                "--root",
                root,
                "--target",
                link / "record.md",
                "--candidate",
                candidate,
                "--expected",
                "absent",
            )
            self.assertEqual(code, 2)
            self.assertEqual(payload["error"]["code"], "SYMLINK_PATH")

    def test_rejects_symlink_candidate(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "record.md"
            real_candidate = root / "real.md"
            real_candidate.write_text("candidate\n", encoding="utf-8")
            linked_candidate = root / "linked.md"
            try:
                linked_candidate.symlink_to(real_candidate)
            except OSError:
                self.skipTest("symlinks unavailable")

            code, payload = invoke(
                "write",
                "--root",
                root,
                "--target",
                target,
                "--candidate",
                linked_candidate,
                "--expected",
                "absent",
            )
            self.assertEqual(code, 2)
            self.assertEqual(payload["error"]["code"], "INVALID_CANDIDATE")
            self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()
