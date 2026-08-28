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
    def test_create_and_digest_exact_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "record.md"
            candidate = root / "candidate.md"
            candidate.write_text("first\n", encoding="utf-8")

            code, payload = invoke("digest", "--target", target)
            self.assertEqual(code, 0)
            self.assertEqual(payload["result"]["digest"], "absent")

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
            self.assertEqual(target.read_text(encoding="utf-8"), "first\n")
            self.assertEqual(
                payload["result"]["digest"], hashlib.sha256(b"first\n").hexdigest()
            )

    def test_stale_write_is_rejected_without_changing_target(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "settings.json"
            target.write_text("{}\n", encoding="utf-8")
            stale = hashlib.sha256(target.read_bytes()).hexdigest()
            target.write_text('{"current": true}\n', encoding="utf-8")
            candidate = root / "candidate.json"
            candidate.write_text('{"stale": true}\n', encoding="utf-8")

            code, payload = invoke(
                "write",
                "--root",
                root,
                "--target",
                target,
                "--candidate",
                candidate,
                "--expected",
                stale,
            )
            self.assertEqual(code, 2)
            self.assertEqual(payload["error"]["code"], "STALE_TARGET")
            self.assertEqual(target.read_text(encoding="utf-8"), '{"current": true}\n')

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

            threads = [
                threading.Thread(target=writer, args=(candidate,)) for candidate in candidates
            ]
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
