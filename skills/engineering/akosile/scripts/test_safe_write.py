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


class SafeWriteTests(unittest.TestCase):
    def test_snapshot_and_publish_exact_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root, target = base / ".qp", base / ".qp/record.md"
            snapshot, candidate = base / "snapshot", base / "candidate"
            root.mkdir()
            target.write_bytes(b"old\n")
            code, payload = run("snapshot", "--root", root, "--target", target, "--output", snapshot)
            self.assertEqual(code, 0)
            candidate.write_bytes(b"new\n")
            candidate_digest = hashlib.sha256(candidate.read_bytes()).hexdigest()
            code, _ = run(
                "write", "--root", root, "--target", target, "--candidate", candidate,
                "--expected-target", payload["result"]["digest"], "--expected-candidate", candidate_digest,
            )
            self.assertEqual(code, 0)
            self.assertEqual(target.read_bytes(), b"new\n")

    def test_candidate_changed_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root, target, candidate = base / ".qp", base / ".qp/record.md", base / "candidate"
            root.mkdir()
            candidate.write_bytes(b"A")
            expected = hashlib.sha256(b"A").hexdigest()
            candidate.write_bytes(b"B")
            code, payload = run(
                "write", "--root", root, "--target", target, "--candidate", candidate,
                "--expected-target", "absent", "--expected-candidate", expected,
            )
            self.assertEqual((code, payload["error"]["code"]), (2, "CANDIDATE_CHANGED"))
            self.assertFalse(target.exists())

    def test_candidate_inside_root_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            candidate, target = root / "candidate", root / "record"
            candidate.write_text("x")
            digest = hashlib.sha256(b"x").hexdigest()
            code, payload = run(
                "write", "--root", root, "--target", target, "--candidate", candidate,
                "--expected-target", "absent", "--expected-candidate", digest,
            )
            self.assertEqual((code, payload["error"]["code"]), (2, "CANDIDATE_INSIDE_ROOT"))

    def test_two_writers_cannot_accept_one_target_digest(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root, target = base / ".qp", base / ".qp/record"
            root.mkdir()
            target.write_bytes(b"base")
            expected = hashlib.sha256(b"base").hexdigest()
            candidates = []
            for value in (b"one", b"two"):
                path = base / value.decode()
                path.write_bytes(value)
                candidates.append((path, hashlib.sha256(value).hexdigest()))
            barrier, outcomes = threading.Barrier(3), []

            def writer(item):
                path, digest = item
                barrier.wait()
                code, payload = run(
                    "write", "--root", root, "--target", target, "--candidate", path,
                    "--expected-target", expected, "--expected-candidate", digest,
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
