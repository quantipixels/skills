"""Regression tests for exact HTML token-validator exceptions."""

import importlib.util
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "html-token-validator.py"
spec = importlib.util.spec_from_file_location("html_token_validator", SCRIPT)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class HtmlTokenValidatorTest(unittest.TestCase):
    def test_entity_reference_is_not_reported_as_hex_color(self):
        result = validator.validate_html(
            '<link rel="stylesheet" href="design-tokens.css"><style>.x::before { content: "&#9670;"; }</style>',
            Path("fixture.html"),
        )
        self.assertFalse(any("#9670" in error for error in result.errors))

    def test_nearby_allowed_domain_does_not_suppress_unrelated_color(self):
        html = (
            '<link rel="stylesheet" href="design-tokens.css">'
            '<style>/* https://unsplash.com/photo */ .x { color: #123456; }</style>'
        )
        result = validator.validate_html(html, Path("fixture.html"))
        self.assertTrue(any("#123456" in error for error in result.errors))

    def test_empty_validation_scope_fails(self):
        output = StringIO()
        with redirect_stdout(output):
            success = validator.print_summary({"slides": [], "infographics": []})

        self.assertFalse(success)
        self.assertIn("NO FILES VALIDATED", output.getvalue())

    def test_complete_embedded_token_source_is_standalone_and_ignores_its_primitive_values(self):
        html = (
            '<style>\n/* Design Tokens (embedded for standalone HTML) */\n'
            ':root { --color-primary: #123456; --color-foreground: #FFFFFF; }\n'
            '</style><style>.x { color: var(--color-primary); }</style>'
        )
        result = validator.validate_html(html, Path("fixture.html"))

        self.assertTrue(result.passed, result.errors)

    def test_embedded_token_source_does_not_hide_consumer_hardcoded_color(self):
        html = (
            '<style>\n/* Design Tokens (embedded for standalone HTML) */\n'
            ':root { --color-primary: #123456; }\n'
            '</style><style>.x { color: #ABCDEF; }</style>'
        )
        result = validator.validate_html(html, Path("fixture.html"))

        self.assertTrue(any("#ABCDEF" in error for error in result.errors))

    def test_embedded_token_source_still_rejects_undefined_reference(self):
        original_root = validator.PROJECT_ROOT
        with tempfile.TemporaryDirectory() as project_root:
            try:
                validator.configure_project_root(Path(project_root))
                html = (
                    '<style>\n/* Design Tokens (embedded for standalone HTML) */\n'
                    ':root { --color-primary: #123456; }\n'
                    '</style><style>.x { color: var(--color-missing); }</style>'
                )
                result = validator.validate_html(html, Path("fixture.html"))
            finally:
                validator.configure_project_root(original_root)

        self.assertTrue(any("--color-missing" in error for error in result.errors))

    def test_project_css_does_not_fill_missing_standalone_embedded_token(self):
        original_root = validator.PROJECT_ROOT
        with tempfile.TemporaryDirectory() as project_root:
            root = Path(project_root)
            (root / "assets").mkdir()
            (root / "assets" / "design-tokens.css").write_text(
                ":root { --color-primary: #123456; }"
            )
            try:
                validator.configure_project_root(root)
                html = (
                    '<style>\n/* Design Tokens (embedded for standalone HTML) */\n'
                    ':root { --color-foreground: #FFFFFF; }\n'
                    '</style><style>.x { color: var(--color-primary); }</style>'
                )
                result = validator.validate_html(html, Path("fixture.html"))
            finally:
                validator.configure_project_root(original_root)

        self.assertTrue(any("--color-primary" in error for error in result.errors))


if __name__ == "__main__":
    unittest.main()
