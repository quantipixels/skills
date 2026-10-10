"""One entry point for CI checks, or just a staged package snapshot for the hook."""
import argparse
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package-root", type=Path,
                        help="Only validate the package at this path (used by pre-commit).")
    args = parser.parse_args()
    if args.package_root is not None:
        commands = [["scripts/skills/check_package.py", "--root", str(args.package_root)]]
    else:
        missing = [name for name in ("git", "java", "javac") if shutil.which(name) is None]
        if missing:
            print(f"check: missing tools: {', '.join(missing)}; install Git and JDK 17 to run the CI checks.", file=sys.stderr)
            return 1
        commands = [
            ["scripts/skills/check_package.py"],
            ["tests/smoke_package.py"],
            ["scripts/skills/test_session_evidence.py"],
            ["scripts/skills/test_worktrees.py"],
            ["-m", "unittest", "discover", "-s", "evals/engineering", "-p", "test_*.py"],
            ["-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"],
        ]
    for command in commands:
        print(f"check: python {' '.join(command)}", flush=True)
        result = subprocess.run([sys.executable, *command], cwd=ROOT)
        if result.returncode:
            return result.returncode if result.returncode > 0 else 1
    print("PASS: all requested checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
