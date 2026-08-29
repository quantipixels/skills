import hashlib
import json
import subprocess
import sys
import tempfile
import threading
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("safe-write.py")


def run(*args):
    result = subprocess.run([sys.executable, str(SCRIPT), *map(str, args)], capture_output=True, text=True)
    return result.returncode, json.loads(result.stdout)


def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


class SafeWriteTests(unittest.TestCase):
    def test_publish_exact_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root, target, candidate = base / ".qp", base / ".qp/record.md", base / "candidate"
            root.mkdir()
            target.write_bytes(b"old\n")
            candidate.write_bytes(b"new\n")

            code, payload = run(
                "--root", root,
                "--target", target,
                "--candidate", candidate,
                "--expected-target", digest(b"old\n"),
                "--expected-candidate", digest(b"new\n"),
            )

            self.assertEqual(code, 0)
            self.assertEqual(payload["result"]["previous_digest"], digest(b"old\n"))
            self.assertEqual(payload["result"]["digest"], digest(b"new\n"))
            self.assertEqual(target.read_bytes(), b"new\n")

    def test_absent_target_can_be_created(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root, target, candidate = base / ".qp", base / ".qp/record.md", base / "candidate"
            root.mkdir()
            candidate.write_bytes(b"new\n")

            code, payload = run(
                "--root", root,
                "--target", target,
                "--candidate", candidate,
                "--expected-target", "absent",
                "--expected-candidate", digest(b"new\n"),
            )

            self.assertEqual(code, 0)
            self.assertEqual(payload["result"]["previous_digest"], "absent")
            self.assertEqual(target.read_bytes(), b"new\n")

    def test_candidate_changed_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root, target, candidate = base / ".qp", base / ".qp/record.md", base / "candidate"
            root.mkdir()
            candidate.write_bytes(b"B")

            code, payload = run(
                "--root", root,
                "--target", target,
                "--candidate", candidate,
                "--expected-target", "absent",
                "--expected-candidate", digest(b"A"),
            )

            self.assertEqual((code, payload["error"]["code"]), (2, "CANDIDATE_CHANGED"))
            self.assertFalse(target.exists())

    def test_candidate_inside_root_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            candidate, target = root / "candidate", root / "record"
            candidate.write_text("x")

            code, payload = run(
                "--root", root,
                "--target", target,
                "--candidate", candidate,
                "--expected-target", "absent",
                "--expected-candidate", digest(b"x"),
            )

            self.assertEqual((code, payload["error"]["code"]), (2, "CANDIDATE_INSIDE_ROOT"))

    def test_stale_target_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root, target, candidate = base / ".qp", base / ".qp/record", base / "candidate"
            root.mkdir()
            target.write_bytes(b"changed")
            candidate.write_bytes(b"candidate")

            code, payload = run(
                "--root", root,
                "--target", target,
                "--candidate", candidate,
                "--expected-target", digest(b"old"),
                "--expected-candidate", digest(b"candidate"),
            )

            self.assertEqual((code, payload["error"]["code"]), (2, "STALE_TARGET"))
            self.assertEqual(target.read_bytes(), b"changed")

    def test_two_writers_cannot_accept_one_target_digest(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root, target = base / ".qp", base / ".qp/record"
            root.mkdir()
            target.write_bytes(b"base")
            expected = digest(b"base")
            candidates = []
            for value in (b"one", b"two"):
                path = base / value.decode()
                path.write_bytes(value)
                candidates.append((path, digest(value)))

            barrier, outcomes = threading.Barrier(3), []

            def writer(item):
                path, candidate_digest = item
                barrier.wait()
                code, payload = run(
                    "--root", root,
                    "--target", target,
                    "--candidate", path,
                    "--expected-target", expected,
                    "--expected-candidate", candidate_digest,
                )
                outcomes.append("OK" if code == 0 else payload["error"]["code"])

            threads = [threading.Thread(target=writer, args=(item,)) for item in candidates]
            for thread in threads:
                thread.start()
            barrier.wait()
            for thread in threads:
                thread.join(10)

            self.assertCountEqual(outcomes, ["OK", "STALE_TARGET"])


if __name__ == "__main__":
    unittest.main()
