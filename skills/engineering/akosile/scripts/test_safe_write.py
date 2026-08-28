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
    def test_snapshot_matches_bytes_and_absent_clears_stale_output(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root, target, output = base / ".qp", base / ".qp/record.md", base / "snapshot.md"
            root.mkdir()
            output.write_text("stale")
            code, payload = run("snapshot", "--root", root, "--target", target, "--output", output)
            self.assertEqual((code, payload["result"]["digest"], output.exists()), (0, "absent", False))
            target.write_bytes(b"current\n")
            code, payload = run("snapshot", "--root", root, "--target", target, "--output", output)
            self.assertEqual(code, 0)
            self.assertEqual(output.read_bytes(), b"current\n")
            self.assertEqual(payload["result"]["digest"], hashlib.sha256(b"current\n").hexdigest())
            self.assertFalse(any(root.glob(".*.lock")), "snapshot must not mutate the root with a lock")

    def test_snapshot_based_candidate_cannot_overwrite_a_later_change(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root, target = base / ".qp", base / ".qp/settings.json"
            snapshot, candidate = base / "snapshot.json", base / "candidate.json"
            root.mkdir()
            target.write_text('{"base": true}\n')
            _, payload = run("snapshot", "--root", root, "--target", target, "--output", snapshot)
            expected = payload["result"]["digest"]
            target.write_text('{"concurrent": true}\n')
            candidate.write_text(snapshot.read_text().replace("true", '"edited"'))
            code, payload = run(
                "write", "--root", root, "--target", target,
                "--candidate", candidate, "--expected", expected,
            )
            self.assertEqual((code, payload["error"]["code"]), (2, "STALE_TARGET"))
            self.assertEqual(target.read_text(), '{"concurrent": true}\n')

    def test_two_writers_cannot_accept_one_digest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "record.md"
            target.write_text("base\n")
            expected = hashlib.sha256(target.read_bytes()).hexdigest()
            candidates = []
            for value in ("one", "two"):
                path = root / f"{value}.md"
                path.write_text(value + "\n")
                candidates.append(path)
            barrier, outcomes = threading.Barrier(3), []

            def write(path):
                barrier.wait()
                code, payload = run(
                    "write", "--root", root, "--target", target,
                    "--candidate", path, "--expected", expected,
                )
                outcomes.append("OK" if code == 0 else payload["error"]["code"])

            threads = [threading.Thread(target=write, args=(path,)) for path in candidates]
            for thread in threads:
                thread.start()
            barrier.wait()
            for thread in threads:
                thread.join(10)
            self.assertCountEqual(outcomes, ["OK", "STALE_TARGET"])

    def test_rejects_outside_missing_and_symlinked_paths(self):
        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as outside:
            root, outside = Path(directory), Path(outside)
            candidate = outside / "candidate.md"
            candidate.write_text("candidate")
            cases = [
                (outside / "target.md", "TARGET_OUTSIDE_ROOT"),
                (root / "missing/target.md", "INVALID_TARGET_PARENT"),
            ]
            for target, expected in cases:
                with self.subTest(expected):
                    code, payload = run(
                        "write", "--root", root, "--target", target,
                        "--candidate", candidate, "--expected", "absent",
                    )
                    self.assertEqual((code, payload["error"]["code"]), (2, expected))

            real = root / "real"
            real.mkdir()
            for name, destination in (("outside-link", outside), ("inside-link", real)):
                link = root / name
                try:
                    link.symlink_to(destination, target_is_directory=True)
                except OSError:
                    return
                code, payload = run(
                    "write", "--root", root, "--target", link / "target.md",
                    "--candidate", candidate, "--expected", "absent",
                )
                self.assertEqual((code, payload["error"]["code"]), (2, "SYMLINK_PATH"))

            snapshot_parent = outside / "scratch-link"
            snapshot_parent.symlink_to(root, target_is_directory=True)
            code, payload = run(
                "snapshot", "--root", root, "--target", root / "new.md",
                "--output", snapshot_parent / "snapshot.md",
            )
            self.assertEqual((code, payload["error"]["code"]), (2, "SNAPSHOT_INSIDE_ROOT"))


if __name__ == "__main__":
    unittest.main()
