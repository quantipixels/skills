"""Regression tests for safe CIP HTML rendering."""

import importlib.util
from unittest.mock import patch
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "render-html.py"
spec = importlib.util.spec_from_file_location("render_html", SCRIPT)
render_html = importlib.util.module_from_spec(spec)
spec.loader.exec_module(render_html)
generate_html = render_html.generate_html


def test_generate_html_escapes_dynamic_text_and_attributes(tmp_path):
    images_dir = tmp_path / "images"
    images_dir.mkdir()
    (images_dir / "business-card.png").write_bytes(b"not a real image")

    output = tmp_path / "presentation.html"
    with patch.object(
        render_html,
        "get_cip_brief",
        return_value={
            "industry": {"Industry": 'tech <img src=x onerror=alert(1)>'},
            "style": {"Style Name": 'style "quoted"', "Mood": "bold & clear"},
        },
    ), patch.object(
        render_html,
        "get_deliverable_info",
        return_value={
            "title": 'Card "quoted" & safe',
            "concept": "<concept>",
            "purpose": "& purpose",
            "specs": "<specs>",
        },
    ):
        result = generate_html(
            'Acme <script>alert("x")</script> & Co',
            'tech <img src=x onerror=alert(1)>',
            images_dir,
            output_path=output,
        )

    html = output.read_text()
    assert result == str(output)
    assert "<script>alert" not in html
    assert "&lt;script&gt;alert(\"x\")&lt;/script&gt;" in html
    assert "&lt;img src=x onerror=alert(1)&gt;" in html
    assert 'alt="Card &quot;quoted&quot; &amp; safe"' in html
