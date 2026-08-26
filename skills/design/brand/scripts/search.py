#!/usr/bin/env python3
"""Search bundled Brand identity CSV evidence and return ranked rows."""
from __future__ import annotations

import argparse
import csv
import json
import re
import sqlite3
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
KIND_DOMAINS = {
    "logo": {"style": "logo/styles.csv", "color": "logo/colors.csv", "industry": "logo/industries.csv"},
    "cip": {
        "deliverable": "cip/deliverables.csv",
        "industry": "cip/industries.csv",
        "mockup": "cip/mockup-contexts.csv",
        "style": "cip/styles.csv",
    },
    "icon": {"style": "icon/styles.csv"},
}


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def query_tokens(query: str) -> list[str]:
    return [token for token in re.findall(r"[\w-]+", query.lower()) if len(token) > 1]


def rank(rows: list[dict[str, str]], query: str, limit: int) -> list[dict[str, str]]:
    tokens = query_tokens(query)
    if not rows or not tokens:
        return []
    try:
        connection = sqlite3.connect(":memory:")
        connection.execute("CREATE VIRTUAL TABLE docs USING fts5(content)")
        connection.executemany(
            "INSERT INTO docs(rowid, content) VALUES (?, ?)",
            ((index + 1, " ".join(str(value) for value in row.values())) for index, row in enumerate(rows)),
        )
        expression = " OR ".join(f'"{token}"' for token in tokens)
        indexes = [rowid - 1 for (rowid,) in connection.execute(
            "SELECT rowid FROM docs WHERE docs MATCH ? ORDER BY bm25(docs) LIMIT ?", (expression, limit)
        )]
        return [rows[index] for index in indexes]
    except sqlite3.OperationalError:
        scored = []
        for index, row in enumerate(rows):
            text = " ".join(row.values()).lower()
            score = sum(text.count(token) for token in tokens)
            if score:
                scored.append((score, -index, row))
        return [row for _, _, row in sorted(scored, reverse=True)[:limit]]
    finally:
        if "connection" in locals():
            connection.close()


def detect_domain(kind: str, query: str) -> str:
    lowered = query.lower()
    options = KIND_DOMAINS[kind]
    for candidate in options:
        if candidate in lowered or candidate.rstrip("y") in lowered:
            return candidate
    if kind == "logo":
        return "industry"
    if kind == "cip":
        return "deliverable"
    return next(iter(options))


def search(kind: str, domain: str, query: str, limit: int) -> dict[str, Any]:
    relative = KIND_DOMAINS[kind][domain]
    path = DATA_DIR / relative
    if not path.is_file():
        return {"kind": kind, "domain": domain, "query": query, "file": relative, "count": 0, "results": [], "error": "data file missing"}
    rows = rank(read_rows(path), query, limit)
    return {"kind": kind, "domain": domain, "query": query, "file": relative, "count": len(rows), "results": rows}


def render(result: dict[str, Any]) -> str:
    lines = ["## Brand identity search evidence", f"**Kind:** {result['kind']} | **Domain:** {result['domain']} | **Query:** {result['query']}", f"**Source:** {result['file']} | **Found:** {result['count']}\n"]
    if result.get("error"):
        return "\n".join(lines + [f"Error: {result['error']}"])
    if not result["results"]:
        return "\n".join(lines + ["No matches."])
    for index, row in enumerate(result["results"], 1):
        lines.append(f"### Result {index}")
        lines.extend(f"- **{key}:** {value}" for key, value in row.items() if value not in (None, ""))
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--kind", choices=sorted(KIND_DOMAINS), required=True)
    parser.add_argument("--domain")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--max-results", "-n", type=int, default=3)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.max_results < 1 or args.max_results > 50:
        parser.error("--max-results must be between 1 and 50")
    allowed = KIND_DOMAINS[args.kind]
    if args.domain and args.domain not in allowed:
        parser.error(f"--domain for {args.kind} must be one of: {', '.join(allowed)}")
    domains = list(allowed) if args.all else [args.domain or detect_domain(args.kind, args.query)]
    results = [search(args.kind, domain, args.query, args.max_results) for domain in domains]
    payload: Any = {result["domain"]: result for result in results} if args.all else results[0]
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    elif args.all:
        print("\n\n".join(render(result) for result in results))
    else:
        print(render(results[0]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
