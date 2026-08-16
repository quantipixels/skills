#!/usr/bin/env python3
"""
HTML Design Token Validator
Ensures all HTML assets (slides, infographics, etc.) use design tokens.
Source of truth: assets/design-tokens.css

Usage:
  python3 html-token-validator.py                    # Validate all HTML assets
  python3 html-token-validator.py --type slides      # Validate only slides
  python3 html-token-validator.py --type infographics # Validate only infographics
  python3 html-token-validator.py path/to/file.html  # Validate specific file
"""

import re
import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# Project root defaults to the caller's project, so this script is standalone.
PROJECT_ROOT = Path.cwd()
TOKENS_JSON_PATH = PROJECT_ROOT / 'assets' / 'design-tokens.json'
TOKENS_CSS_PATH = PROJECT_ROOT / 'assets' / 'design-tokens.css'

# Asset directories to validate
ASSET_DIRS = {
    'slides': PROJECT_ROOT / 'assets' / 'designs' / 'slides',
    'infographics': PROJECT_ROOT / 'assets' / 'infographics',
}

# Patterns that indicate hardcoded values (should use tokens)
FORBIDDEN_PATTERNS = [
    (r'(?<!&)#[0-9A-Fa-f]{3,8}\b', 'hex color'),
    (r'rgb\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\)', 'rgb color'),
    (r'rgba\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*,\s*[\d.]+\s*\)', 'rgba color'),
    (r'hsl\([^)]+\)', 'hsl color'),
    (r"font-family:\s*'[^v][^a][^r][^']*',", 'hardcoded font'),  # Exclude var()
    (r'font-family:\s*"[^v][^a][^r][^"]*",', 'hardcoded font'),
]

# Allowed exceptions (external images, etc.)
ALLOWED_EXCEPTIONS = [
    'pexels.com', 'unsplash.com', 'youtube.com', 'ytimg.com',
    'googlefonts', 'fonts.googleapis.com', 'fonts.gstatic.com',
]


class ValidationResult:
    """Validation result for a single file."""
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.passed = True

    def add_error(self, msg: str):
        self.errors.append(msg)
        self.passed = False

    def add_warning(self, msg: str):
        self.warnings.append(msg)


def load_css_variables() -> Dict[str, str]:
    """Load CSS variables from design-tokens.css."""
    variables = {}
    if TOKENS_CSS_PATH.exists():
        content = TOKENS_CSS_PATH.read_text()
        # Extract --var-name: value patterns
        for match in re.finditer(r'(--[\w-]+):\s*([^;]+);', content):
            variables[match.group(1)] = match.group(2).strip()
    return variables


def is_inside_block(content: str, match_pos: int, open_tag: str, close_tag: str) -> bool:
    """Check if position is inside a specific HTML block."""
    pre = content[:match_pos]
    tag_open = pre.rfind(open_tag)
    tag_close = pre.rfind(close_tag)
    return tag_open > tag_close


def is_allowed_exception(content: str, match_start: int, match_end: int) -> bool:
    """Allow a value only when the matched text is part of an allowed URL.

    A nearby domain name is not enough: the exact color token must be lexically
    inside the URL that owns the exception.
    """
    url_pattern = re.compile(r"(?:https?:)?//[^\s\"'<>]+", re.IGNORECASE)
    for url_match in url_pattern.finditer(content):
        if url_match.start() <= match_start and match_end <= url_match.end():
            url = url_match.group().lower()
            if any(exc in url for exc in ALLOWED_EXCEPTIONS):
                return True
    return False


def configure_project_root(project_root: Path):
    """Point all validator resources at an explicit project root."""
    global PROJECT_ROOT, TOKENS_JSON_PATH, TOKENS_CSS_PATH, ASSET_DIRS
    PROJECT_ROOT = project_root.resolve()
    TOKENS_JSON_PATH = PROJECT_ROOT / 'assets' / 'design-tokens.json'
    TOKENS_CSS_PATH = PROJECT_ROOT / 'assets' / 'design-tokens.css'
    ASSET_DIRS = {
        'slides': PROJECT_ROOT / 'assets' / 'designs' / 'slides',
        'infographics': PROJECT_ROOT / 'assets' / 'infographics',
    }


def get_context(content: str, pos: int, chars: int = 100) -> str:
    """Get surrounding context for a match position."""
    start = max(0, pos - chars)
    end = min(len(content), pos + chars)
    return content[start:end]


def validate_html(content: str, file_path: Path, verbose: bool = False) -> ValidationResult:
    """
    Validate HTML content for design token compliance.

    Checks:
    1. design-tokens.css import present
    2. No hardcoded colors in CSS (except in <script> for Chart.js)
    3. No hardcoded fonts
    4. Uses var(--token-name) pattern
    """
    result = ValidationResult(file_path)

    # 1. Check for design-tokens.css import
    if 'design-tokens.css' not in content:
        result.add_error("Missing design-tokens.css import")

    # 2. Check for forbidden patterns in CSS
    for pattern, description in FORBIDDEN_PATTERNS:
        for match in re.finditer(pattern, content):
            match_text = match.group()
            match_pos = match.start()
            context = get_context(content, match_pos)

            # Skip if in <script> block (Chart.js allowed)
            if is_inside_block(content, match_pos, '<script', '</script>'):
                if verbose:
                    result.add_warning(f"Allowed in <script>: {match_text}")
                continue

            # Skip if in allowed exception context (external URLs)
            if is_allowed_exception(content, match.start(), match.end()):
                if verbose:
                    result.add_warning(f"Allowed external: {match_text}")
                continue

            # Skip if part of var() reference (false positive)
            if 'var(' in context and match_text in context:
                # Check if it's a fallback value in var()
                var_pattern = rf'var\([^)]*{re.escape(match_text)}[^)]*\)'
                if re.search(var_pattern, context):
                    continue

            # Error if in <style> or inline style
            if is_inside_block(content, match_pos, '<style', '</style>'):
                result.add_error(f"Hardcoded {description} in <style>: {match_text}")
            elif 'style="' in context:
                result.add_error(f"Hardcoded {description} in inline style: {match_text}")

    # 3. Check for required var() usage indicators
    token_patterns = [
        r'var\(--color-',
        r'var\(--space-',
        r'var\(--font-',
        r'var\(--gradient-',
        r'var\(--slide-',
        r'var\(--card-',
        r'var\(--button-',
    ]
    token_count = sum(len(re.findall(p, content)) for p in token_patterns)

    if token_count < 5:
        result.add_warning(f"Low token usage ({token_count} var() references). Consider using more design tokens.")

    # 4. Every referenced custom property must be declared by the project
    # token contract or in an embedded declaration in this document.
    content_without_comments = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    referenced = set(re.findall(r'var\(\s*(--[\w-]+)', content_without_comments))
    embedded = {
        match.group(1)
        for match in re.finditer(r'(--[\w-]+)\s*:\s*[^;]+;', content_without_comments)
    }
    project_variables = set(load_css_variables())
    if referenced and not project_variables and not embedded:
        result.add_error(f"Token source not found or empty: {TOKENS_CSS_PATH}")
    for variable in sorted(referenced - project_variables - embedded):
        result.add_error(f"Undefined design token: {variable}")

    return result


def validate_file(file_path: Path, verbose: bool = False) -> ValidationResult:
    """Validate a single HTML file."""
    if not file_path.exists():
        result = ValidationResult(file_path)
        result.add_error("File not found")
        return result

    content = file_path.read_text()
    return validate_html(content, file_path, verbose)


def validate_directory(dir_path: Path, verbose: bool = False) -> List[ValidationResult]:
    """Validate all HTML files in a directory."""
    results = []
    if dir_path.exists():
        for html_file in sorted(dir_path.glob('*.html')):
            results.append(validate_file(html_file, verbose))
    return results


def print_result(result: ValidationResult, verbose: bool = False):
    """Print validation result for a file."""
    status = "✓" if result.passed else "✗"
    print(f"  {status} {result.file_path.name}")

    if result.errors:
        for error in result.errors[:5]:  # Limit output
            print(f"      ├─ {error}")
        if len(result.errors) > 5:
            print(f"      └─ ... and {len(result.errors) - 5} more errors")

    if verbose and result.warnings:
        for warning in result.warnings[:3]:
            print(f"      [warn] {warning}")


def print_summary(all_results: Dict[str, List[ValidationResult]]):
    """Print summary of all validation results."""
    total_files = 0
    total_passed = 0
    total_errors = 0

    print("\n" + "=" * 60)
    print("HTML DESIGN TOKEN VALIDATION SUMMARY")
    print("=" * 60)

    for asset_type, results in all_results.items():
        if not results:
            continue

        passed = sum(1 for r in results if r.passed)
        failed = len(results) - passed
        errors = sum(len(r.errors) for r in results)

        total_files += len(results)
        total_passed += passed
        total_errors += errors

        status = "✓" if failed == 0 else "✗"
        print(f"\n{status} {asset_type.upper()}: {passed}/{len(results)} passed")

        for result in results:
            if not result.passed:
                print_result(result)

    print("\n" + "-" * 60)
    if total_errors == 0:
        print(f"✓ ALL PASSED: {total_passed}/{total_files} files valid")
    else:
        print(f"✗ FAILED: {total_files - total_passed}/{total_files} files have issues ({total_errors} total errors)")
    print("-" * 60)

    return total_errors == 0


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Validate HTML assets for design token compliance',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                           # Validate all HTML assets
  %(prog)s --type slides             # Validate only slides
  %(prog)s --type infographics       # Validate only infographics
  %(prog)s path/to/file.html         # Validate specific file
  %(prog)s --colors                  # Show brand colors from tokens
"""
    )
    parser.add_argument('files', nargs='*', help='Specific HTML files to validate')
    parser.add_argument('-t', '--type', choices=['slides', 'infographics', 'all'],
                        default='all', help='Asset type to validate')
    parser.add_argument('-v', '--verbose', action='store_true', help='Show warnings')
    parser.add_argument('--colors', action='store_true', help='Print CSS variables from tokens')
    parser.add_argument('--project-root', type=Path, default=Path.cwd(), help='Project root containing assets/')

    args = parser.parse_args()
    configure_project_root(args.project_root)

    # Show colors mode
    if args.colors:
        variables = load_css_variables()
        print("\nDesign Tokens (from design-tokens.css):")
        print("-" * 40)
        for name, value in sorted(variables.items())[:30]:
            print(f"  {name}: {value}")
        if len(variables) > 30:
            print(f"  ... and {len(variables) - 30} more")
        return

    all_results: Dict[str, List[ValidationResult]] = {}

    # Validate specific files
    if args.files:
        results = []
        for file_path in args.files:
            path = Path(file_path)
            if path.exists():
                results.append(validate_file(path, args.verbose))
            else:
                result = ValidationResult(path)
                result.add_error("File not found")
                results.append(result)
        all_results['specified'] = results
    else:
        # Validate by type
        types_to_check = ASSET_DIRS.keys() if args.type == 'all' else [args.type]

        for asset_type in types_to_check:
            if asset_type in ASSET_DIRS:
                results = validate_directory(ASSET_DIRS[asset_type], args.verbose)
                all_results[asset_type] = results

    # Print results
    success = print_summary(all_results)

    if not success:
        sys.exit(1)


if __name__ == '__main__':
    main()
