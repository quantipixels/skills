"""Regression tests for exact HTML token-validator exceptions."""

import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "html-token-validator.py"
spec = importlib.util.spec_from_file_location("html_token_validator", SCRIPT)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def test_entity_reference_is_not_reported_as_hex_color():
    result = validator.validate_html(
        '<link rel="stylesheet" href="design-tokens.css"><style>.x::before { content: "&#9670;"; }</style>',
        Path("fixture.html"),
    )
    assert not any("#9670" in error for error in result.errors)


def test_nearby_allowed_domain_does_not_suppress_unrelated_color():
    html = (
        '<link rel="stylesheet" href="design-tokens.css">'
        '<style>/* https://unsplash.com/photo */ .x { color: #123456; }</style>'
    )
    result = validator.validate_html(html, Path("fixture.html"))
    assert any("#123456" in error for error in result.errors)
