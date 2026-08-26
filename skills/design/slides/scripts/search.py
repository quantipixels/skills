#!/usr/bin/env python3
"""Search bundled slide strategy, layout, copy, and chart CSV evidence."""
from __future__ import annotations

import argparse
import csv
import json
import re
import sqlite3
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DOMAIN_FILES = {
    "strategy": "slide-strategies.csv",
    "layout": "slide-layouts.csv",
    "copy": "slide-copy.csv",
    "chart": "slide-charts.csv",
}
HINTS = {
    "chart": ("chart", "graph", "metric", "trend", "data", "kpi"),
    "copy": ("headline", "copy", "hook", "cta", "proof", "objection"),
    "layout": ("layout", "grid", "hero", "timeline", "comparison", "quote", "team"),
    "strategy": ("pitch", "deck", "investor", "sales", "board", "webinar", "structure"),
}


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def tokens(query: str) -> list[str]:
    return [token for token in re.findall(r"[\w-]+", query.lower()) if len(token) > 1]


def rank(rows: list[dict[str, str]], query: str, limit: int) -> list[dict[str, str]]:
    wanted = tokens(query)
    if not rows or not wanted:
        return []
    try:
        connection = sqlite3.connect(":memory:")
        connection.execute("CREATE VIRTUAL TABLE docs USING fts5(content)")
        connection.executemany(
            "INSERT INTO docs(rowid, content) VALUES (?, ?)",
            ((index + 1, " ".join(str(value) for value in row.values())) for index, row in enumerate(rows)),
        )
        expression = " OR ".join(f'"{token}"' for token in wanted)
        indexes = [rowid - 1 for (rowid,) in connection.execute(
            "SELECT rowid FROM docs WHERE docs MATCH ? ORDER BY bm25(docs) LIMIT ?", (expression, limit)
        )]
        return [rows[index] for index in indexes]
    except sqlite3.OperationalError:
        scored = []
        for index, row in enumerate(rows):
            text = " ".join(row.values()).lower()
            score = sum(text.count(token) for token in wanted)
            if score:
                scored.append((score, -index, row))
        return [row for _, _, row in sorted(scored, reverse=True)[:limit]]
    finally:
        if "connection" in locals():
            connection.close()


def detect_domain(query: str) -> str:
    lowered = query.lower()
    scores = {domain: sum(hint in lowered for hint in hints) for domain, hints in HINTS.items()}
    winner = max(scores, key=scores.get)
    return winner if scores[winner] else "strategy"


def search(query: str, domain: str, limit: int) -> dict[str, Any]:
    filename = DOMAIN_FILES[domain]
    path = DATA_DIR / filename
    if not path.is_file():
        return {"domain": domain, "query": query, "file": filename, "count": 0, "results": [], "error": "data file missing"}
    results = rank(read_rows(path), query, limit)
    return {"domain": domain, "query": query, "file": filename, "count": len(results), "results": results}


def render(result: dict[str, Any]) -> str:
    lines = [f"## Slide {result['domain']} search evidence", f"**Query:** {result['query']} | **Source:** {result['file']} | **Found:** {result['count']}\n"]
    if result.get("error"):
        return "\n".join(lines + [f"Error: {result['error']}"])
    if not result["results"]:
        return "\n".join(lines + ["No matches."])
    for index, row in enumerate(result["results"], 1):
        lines.append(f"### Result {index}")
        lines.extend(f"- **{key.replace('_', ' ').title()}:** {value}" for key, value in row.items() if value not in (None, ""))
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--domain", "-d", choices=sorted(DOMAIN_FILES))
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--max-results", "-n", type=int, default=3)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.max_results < 1 or args.max_results > 50:
        parser.error("--max-results must be between 1 and 50")
    domains = list(DOMAIN_FILES) if args.all else [args.domain or detect_domain(args.query)]
    results = [search(args.query, domain, args.max_results) for domain in domains]
    payload: Any = {result["domain"]: result for result in results} if args.all else results[0]
    print(json.dumps(payload, indent=2, ensure_ascii=False) if args.json else "\n\n".join(render(result) for result in results))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
