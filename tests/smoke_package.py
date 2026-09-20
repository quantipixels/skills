"""Exercise the package CLI on disposable inputs; no mocks, installs or model calls."""
from pathlib import Path
import subprocess
import sys
import tempfile

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/skills/check_package.py"


def write(root: Path, name: str, content: str) -> Path:
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def run(root: Path, status: int, diagnostic: str = "") -> None:
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--root", str(root)],
        capture_output=True, text=True, timeout=10,
    )
    if result.returncode != status or diagnostic not in result.stderr:
        raise RuntimeError(f"Expected exit {status} / {diagnostic!r}; got {result.returncode}:\n{result.stdout}{result.stderr}")


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="qp-package-smoke-") as temporary:
        root = Path(temporary) / "package"
        entry = "---\nname: example\ndescription: A usable skill\n---\nUse `seda-pr` when publication is authorized.\n"
        skill = write(root, "skills/example/SKILL.md", entry)
        write(root, ".codex-plugin/plugin.json", '{"name":"qp-skills","skills":"./skills/"}')
        write(root, ".claude-plugin/plugin.json", '{"name":"qp-skills"}')
        write(root, "evals/engineering/observations/past.md", "[Historical source](retired.md)\n")
        run(root, 0)

        # An active directory must not gain the historical archive exemption by name.
        for folder in ("skills/example/observations", "docs/observations"):
            bad = write(root, f"{folder}/current.md", "[Missing reference](missing.md)\n")
            run(root, 1, "missing link target")
            bad.unlink()

        metadata = root / "skills/example/agents/openai.yaml"
        metadata.parent.mkdir(parents=True)
        outside = write(root.parent, "external.yaml", "interface: {}\n")
        metadata.symlink_to(outside)
        run(root, 1, "host metadata escapes package")
        metadata.unlink()
        metadata.symlink_to("missing.yaml")
        run(root, 1, "host metadata is not a readable file")
        metadata.unlink()
        write(root, "skills/example/agents/shared.yaml", "interface: {}\n")
        metadata.symlink_to("shared.yaml")
        run(root, 0)
        metadata.unlink()

        skill.write_text(entry.replace("name: example", "name: example\ndisable-model-invocation: true"), encoding="utf-8")
        run(root, 1, "invocation policies disagree")
        write(root, "skills/example/agents/openai.yaml", "policy:\n  allow_implicit_invocation: false\n")
        run(root, 0)
        skill.write_text(entry.replace("name: example", "name: example\nname: other"), encoding="utf-8")
        run(root, 1, "duplicate mapping key")
        skill.unlink()
        run(root, 1, "no skill entrypoints found")
    print("PASS: package CLI, active references, metadata boundaries and failing exit status")


if __name__ == "__main__":
    main()
