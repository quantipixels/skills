#!/usr/bin/env python3
"""Run deterministic structural checks on portable HTML artifacts."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


STATUSES = ("Offline-ready", "Network-enhanced", "Companion bundle")


class ArtifactParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.html_lang = ""
        self.has_viewport = False
        self.in_title = False
        self.title_parts: list[str] = []
        self.text_parts: list[str] = []
        self.ids: set[str] = set()
        self.urls: list[tuple[str, str, str, int]] = []
        self.theme_controls: list[dict[str, str | None]] = []
        self.theme_icons: set[str] = set()
        self.details: list[dict[str, object]] = []
        self._detail_stack: list[int] = []
        self.in_script = False
        self.script_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        line, _ = self.getpos()
        if tag == "html":
            self.html_lang = values.get("lang") or ""
        if tag == "meta" and (values.get("name") or "").lower() == "viewport":
            self.has_viewport = True
        if tag == "title":
            self.in_title = True
        if tag == "script":
            self.in_script = True
        if values.get("id"):
            self.ids.add(values["id"] or "")
        for name in ("href", "src"):
            if values.get(name):
                self.urls.append((tag, name, values[name] or "", line))
        if "data-theme-toggle" in values:
            self.theme_controls.append({**values, "_tag": tag})
        if values.get("data-theme-icon"):
            self.theme_icons.add(values["data-theme-icon"] or "")
        if tag == "details":
            self.details.append({"line": line, "open": "open" in values, "summary": False})
            self._detail_stack.append(len(self.details) - 1)
        elif tag == "summary" and self._detail_stack:
            self.details[self._detail_stack[-1]]["summary"] = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False
        if tag == "script":
            self.in_script = False
        if tag == "details" and self._detail_stack:
            self._detail_stack.pop()

    def handle_data(self, data: str) -> None:
        self.text_parts.append(data)
        if self.in_title:
            self.title_parts.append(data)
        if self.in_script:
            self.script_parts.append(data)


def inspect(path: Path, content: str) -> dict[str, object]:
    parser = ArtifactParser()
    errors: list[str] = []
    warnings: list[str] = []
    remote_resources: list[str] = []

    try:
        parser.feed(content)
        parser.close()
    except Exception as error:  # HTMLParser raises only for malformed entities or overrides.
        errors.append(f"HTML parse failed: {error}")

    if not re.search(r"<!doctype\s+html\b", content, re.IGNORECASE):
        errors.append("Missing HTML5 doctype")
    if not parser.html_lang.strip():
        errors.append("Missing <html lang=\"…\">")
    if not "".join(parser.title_parts).strip():
        errors.append("Missing non-empty <title>")
    if not parser.has_viewport:
        errors.append("Missing viewport meta tag")

    visible_text = " ".join(" ".join(parser.text_parts).split())
    present_statuses = [status for status in STATUSES if status in visible_text]
    if len(present_statuses) != 1:
        errors.append("Show exactly one portability status: " + ", ".join(STATUSES))

    if len(parser.theme_controls) != 1:
        errors.append("Expected exactly one [data-theme-toggle] control")
    else:
        control = parser.theme_controls[0]
        if control.get("_tag") != "button":
            errors.append("Theme toggle must be a semantic <button>")
        if not control.get("aria-label") and not control.get("aria-labelledby"):
            errors.append("Theme toggle needs an accessible name")
    if not {"light", "dark"}.issubset(parser.theme_icons):
        errors.append("Theme toggle needs bundled light and dark icons")

    scripts = "\n".join(parser.script_parts)
    if "prefers-color-scheme" not in scripts or "matchMedia" not in scripts:
        errors.append("Theme initialization does not follow the system color preference")
    if not re.search(r"addEventListener\(\s*[\"']click[\"']", scripts):
        errors.append("Theme toggle has no user-choice handler")
    if re.search(r"\.innerHTML\s*=", scripts):
        errors.append("Inline script assigns to innerHTML")

    for detail in parser.details:
        line = detail["line"]
        if not detail["summary"]:
            errors.append(f"<details> at line {line} has no <summary>")
        if detail["open"]:
            warnings.append(f"<details> at line {line} starts open; confirm it is not secondary information")

    for tag, attribute, raw_url, line in parser.urls:
        parsed = urlsplit(raw_url)
        if parsed.scheme in {"http", "https"} or parsed.netloc:
            if not (tag == "a" and attribute == "href"):
                remote_resources.append(raw_url)
            continue
        if parsed.scheme == "javascript":
            errors.append(f"Unsafe javascript: URL at line {line}")
            continue
        if parsed.scheme in {"data", "mailto", "tel"}:
            continue
        if raw_url.startswith("#"):
            fragment = unquote(parsed.fragment)
            if fragment and fragment not in parser.ids:
                errors.append(f"Missing fragment target #{fragment} at line {line}")
            continue
        target_text = unquote(parsed.path)
        if not target_text or str(path) == "-":
            continue
        target = Path(target_text) if Path(target_text).is_absolute() else path.parent / target_text
        if not target.exists():
            errors.append(f"Missing local {attribute} target at line {line}: {raw_url}")

    if remote_resources:
        warnings.append(f"Disclose and verify {len(remote_resources)} remote runtime resource(s)")
    if "Offline-ready" in present_statuses and remote_resources:
        errors.append("Offline-ready artifact loads remote runtime resources")
    if "Network-enhanced" in present_statuses and not remote_resources:
        warnings.append("Network-enhanced status has no detected remote runtime resource")

    return {
        "path": str(path),
        "passed": not errors,
        "errors": errors,
        "warnings": warnings,
        "remote_resources": sorted(set(remote_resources)),
        "details_count": len(parser.details),
    }


def print_result(result: dict[str, object]) -> None:
    status = "PASS" if result["passed"] else "FAIL"
    print(f"{status} {result['path']}")
    for error in result["errors"]:
        print(f"  error: {error}")
    for warning in result["warnings"]:
        print(f"  warning: {warning}")
    resources = result["remote_resources"]
    if resources:
        print("  remote resources:")
        for resource in resources:
            print(f"    {resource}")


def main() -> int:
    argument_parser = argparse.ArgumentParser(description=__doc__)
    argument_parser.add_argument("paths", nargs="+", help="HTML files, or - for stdin")
    argument_parser.add_argument("--json", action="store_true", help="Emit machine-readable results")
    args = argument_parser.parse_args()

    results: list[dict[str, object]] = []
    stdin_used = False
    for raw_path in args.paths:
        path = Path(raw_path)
        if raw_path == "-":
            if stdin_used:
                results.append({
                    "path": "-", "passed": False, "errors": ["stdin can be read only once"],
                    "warnings": [], "remote_resources": [], "details_count": 0,
                })
                continue
            content = sys.stdin.read()
            stdin_used = True
        else:
            try:
                content = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as error:
                results.append({
                    "path": str(path), "passed": False, "errors": [str(error)],
                    "warnings": [], "remote_resources": [], "details_count": 0,
                })
                continue
        results.append(inspect(path, content))

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        for result in results:
            print_result(result)
    return 0 if all(result["passed"] for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
