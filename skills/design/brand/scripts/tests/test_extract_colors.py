"""Regression tests for shell-free Brand color extraction."""

import json
import shutil
import subprocess
from pathlib import Path

import pytest


SCRIPTS = Path(__file__).resolve().parent.parent


def test_extract_colors_returns_shell_free_argument_vector(tmp_path):
    node = shutil.which("node")
    if not node:
        pytest.skip("node not available")

    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "brand-guidelines.md").write_text(
        "### Primary\n\n#112233\n\n### Secondary\n\n#445566\n"
    )
    image = tmp_path / 'x"; touch should-not-run; #.png'
    image.write_bytes(b"fixture")

    result = subprocess.run(
        [node, str(SCRIPTS / "extract-colors.cjs"), str(image), "--json"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload["extraction"]["executable"] == "magick"
    assert payload["extraction"]["args"][0] == str(image)
    assert "extractionCommand" not in payload
    assert not (tmp_path / "should-not-run").exists()
