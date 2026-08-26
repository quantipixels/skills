#!/usr/bin/env python3
"""Search bundled Amoye UI/UX CSV evidence and return ranked rows."""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
import sqlite3
import sys
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
MAX_RESULTS = 3
MAX_RESULTS_LIMIT = 50
TRUNCATE_AT = 300

DOMAIN_FILES = {
    "style": "styles.csv",
    "color": "colors.csv",
    "chart": "charts.csv",
    "landing": "landing.csv",
    "product": "products.csv",
    "ux": "ux-guidelines.csv",
    "typography": "typography.csv",
    "icons": "icons.csv",
    "gsap": "motion.csv",
    "react": "react-performance.csv",
    "web": "app-interface.csv",
    "google-fonts": "google-fonts.csv",
}

DOMAIN_HINTS = {
    "chart": ("chart", "graph", "metric", "trend", "dashboard", "visualization"),
    "color": ("color", "palette", "contrast", "dark", "light"),
    "typography": ("font", "type", "heading", "body", "readability"),
    "google-fonts": ("google font", "font family", "variable font"),
    "landing": ("landing", "conversion", "hero", "cta"),
    "icons": ("icon", "symbol", "glyph"),
    "gsap": ("motion", "animation", "transition", "gsap"),
    "react": ("react", "rerender", "bundle", "memo"),
    "web": ("form", "focus", "keyboard", "loading", "error", "navigation"),
    "ux": ("accessibility", "a11y", "usability", "touch", "feedback"),
    "style": ("style", "visual", "minimal", "premium", "brutalist"),
    "product": ("product", "saas", "commerce", "mobile", "dashboard"),
}


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def tokens(query: str) -> list[str]:
    return [part for part in re.findall(r"[\w-]+", query.lower()) if len(part) > 1]


def fallback_rank(rows: list[dict[str, str]], query: str, limit: int) -> list[dict[str, str]]:
    wanted = tokens(query)
    scored = []
    for index, row in enumerate(rows):
        text = " ".join(str(value) for value in row.values()).lower()
        score = sum(text.count(token) for token in wanted)
        if score:
            scored.append((score, -index, row))
    return [row for _, _, row in sorted(scored, reverse=True)[:limit]]


def rank_rows(rows: list[dict[str, str]], query: str, limit: int) -> list[dict[str, str]]:
    if not rows or not tokens(query):
        return []
    try:
        connection = sqlite3.connect(":memory:")
        connection.execute("CREATE VIRTUAL TABLE docs USING fts5(content)")
        connection.executemany(
            "INSERT INTO docs(rowid, content) VALUES (?, ?)",
            ((index + 1, " ".join(str(value) for value in row.values())) for index, row in enumerate(rows)),
        )
        expression = " OR ".join(f'"{token.replace(chr(34), chr(34) * 2)}"' for token in tokens(query))
        indexes = [
            rowid - 1
            for (rowid,) in connection.execute(
                "SELECT rowid FROM docs WHERE docs MATCH ? ORDER BY bm25(docs) LIMIT ?",
                (expression, limit),
            )
        ]
        return [rows[index] for index in indexes]
    except sqlite3.OperationalError:
        return fallback_rank(rows, query, limit)
    finally:
        if "connection" in locals():
            connection.close()


def detect_domain(query: str) -> str:
    lowered = query.lower()
    scores = {
        domain: sum(1 for hint in hints if hint in lowered)
        for domain, hints in DOMAIN_HINTS.items()
    }
    winner = max(scores, key=scores.get)
    return winner if scores[winner] else "product"


def search_file(path: Path, query: str, limit: int) -> dict[str, Any]:
    if not path.is_file():
        return {"error": {"code": "data_missing", "message": f"File not found: {path}"}, "count": 0, "results": []}
    rows = read_rows(path)
    results = rank_rows(rows, query, limit)
    return {"file": str(path.relative_to(DATA_DIR)), "query": query, "count": len(results), "results": results}


def search_domain(query: str, domain: str | None, limit: int) -> dict[str, Any]:
    selected = domain or detect_domain(query)
    result = search_file(DATA_DIR / DOMAIN_FILES[selected], query, limit)
    result.update(domain=selected, auto_detected=domain is None)
    return result


def search_stack(query: str, stack: str, limit: int) -> dict[str, Any]:
    result = search_file(DATA_DIR / "stacks" / f"{stack}.csv", query, limit)
    result.update(stack=stack)
    return result


def format_output(result: dict[str, Any], full: bool) -> str:
    if result.get("error"):
        error = result["error"]
        return f"Error: {error.get('message', error)}"
    kind = f"Stack: {result['stack']}" if result.get("stack") else f"Domain: {result['domain']}"
    lines = ["## UI/UX search evidence", f"**{kind} | Query:** {result['query']}", f"**Source:** {result['file']} | **Found:** {result['count']}\n"]
    if not result["results"]:
        return "\n".join(lines + ["No matches. Broaden the query before using general guidance."])
    for index, row in enumerate(result["results"], 1):
        lines.append(f"### Result {index}")
        for key, value in row.items():
            rendered = str(value)
            if not full and len(rendered) > TRUNCATE_AT:
                rendered = rendered[:TRUNCATE_AT] + "..."
            lines.append(f"- **{key}:** {rendered}")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--domain", "-d", choices=sorted(DOMAIN_FILES))
    stacks = sorted(path.stem for path in (DATA_DIR / "stacks").glob("*.csv"))
    parser.add_argument("--stack", "-s", choices=stacks)
    parser.add_argument("--max-results", "-n", type=int, default=MAX_RESULTS)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--full", action="store_true")
    args = parser.parse_args()
    if not 1 <= args.max_results <= MAX_RESULTS_LIMIT:
        parser.error(f"--max-results must be between 1 and {MAX_RESULTS_LIMIT}")
    result = search_stack(args.query, args.stack, args.max_results) if args.stack else search_domain(args.query, args.domain, args.max_results)
    print(json.dumps(result, indent=2, ensure_ascii=False) if args.json else format_output(result, args.full))
    return 2 if result.get("error") else 0


if __name__ == "__main__":
    raise SystemExit(main())
