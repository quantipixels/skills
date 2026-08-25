#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Search the bundled Amoye UI/UX datasets with BM25 retrieval."""

import argparse
import io
import json
import sys

from core import AVAILABLE_STACKS, CSV_CONFIG, MAX_RESULTS, MAX_RESULTS_LIMIT, UNTRUNCATED_COLS, search, search_stack

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding and sys.stderr.encoding.lower() != "utf-8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

TRUNCATE_AT = 300


def format_output(result, full=False):
    if "error" in result:
        error = result["error"]
        return f"Error: {error.get('message', error) if isinstance(error, dict) else error}"

    output = []
    if result.get("stack"):
        output.append("## UI/UX Stack Search Results")
        output.append(f"**Stack:** {result['stack']} | **Query:** {result['query']}")
    else:
        output.append("## UI/UX Search Results")
        domain_note = result["domain"]
        if result.get("auto_detected"):
            domain_note += " (auto-detected"
            if result.get("runner_up_domain"):
                domain_note += f", runner-up: {result['runner_up_domain']}"
            domain_note += ")"
        output.append(f"**Domain:** {domain_note} | **Query:** {result['query']}")
    output.append(f"**Source:** {result['file']} | **Found:** {result['count']} results\n")

    if result["count"] == 0:
        output.append("No matches. Broaden the query before falling back to general guidance.")
        suggestions = result.get("suggestions") or []
        if suggestions:
            output.append(f"**Closest known terms:** {', '.join(suggestions)}")
        return "\n".join(output)

    for index, row in enumerate(result["results"], 1):
        output.append(f"### Result {index}")
        for key, value in row.items():
            value_str = str(value)
            if not full and key not in UNTRUNCATED_COLS and len(value_str) > TRUNCATE_AT:
                value_str = value_str[:TRUNCATE_AT] + "..."
            output.append(f"- **{key}:** {value_str}")
        output.append("")
    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(description="Search bundled UI/UX guidance")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--domain", "-d", choices=list(CSV_CONFIG.keys()), help="Search domain")
    parser.add_argument("--stack", "-s", choices=AVAILABLE_STACKS, help="Stack-specific search")
    parser.add_argument("--max-results", "-n", type=int, default=MAX_RESULTS)
    parser.add_argument("--json", action="store_true", help="Output structured JSON")
    parser.add_argument("--full", action="store_true", help="Do not truncate long fields")
    args = parser.parse_args()

    if not 1 <= args.max_results <= MAX_RESULTS_LIMIT:
        result = {
            "error": {"code": "invalid_max_results", "message": f"max_results must be 1-{MAX_RESULTS_LIMIT}"},
            "query": args.query,
            "count": 0,
            "results": [],
        }
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(format_output(result), file=sys.stderr)
        return 2

    result = (
        search_stack(args.query, args.stack, args.max_results)
        if args.stack
        else search(args.query, args.domain, args.max_results)
    )
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(format_output(result, full=args.full))
    return 0 if "error" not in result else 2


if __name__ == "__main__":
    raise SystemExit(main())
