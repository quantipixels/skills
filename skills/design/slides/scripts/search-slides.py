#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Search the bundled slide strategy, layout, copy, and chart datasets."""

import argparse
import json

from slide_search_core import AVAILABLE_DOMAINS, search, search_all


def format_result(result, domain):
    lines = []
    title_fields = {
        "strategy": "strategy_name",
        "layout": "layout_name",
        "copy": "formula_name",
        "chart": "chart_type",
    }
    title = result.get(title_fields[domain], "N/A")
    lines.append(f"**{title}**")
    for key, value in result.items():
        if key == title_fields[domain] or value in (None, ""):
            continue
        lines.append(f"  {key.replace('_', ' ').title()}: {value}")
    return "\n".join(lines)


def print_domain(domain, result):
    print(f"\n--- {domain.upper()} ---")
    if result.get("error"):
        print(result["error"])
        return
    if not result.get("results"):
        print("No matches.")
        return
    for item in result["results"]:
        print(format_result(item, domain))
        print()


def main():
    parser = argparse.ArgumentParser(description="Search slide design datasets")
    parser.add_argument("query", help="Search query")
    parser.add_argument("-d", "--domain", choices=AVAILABLE_DOMAINS)
    parser.add_argument("-n", "--max-results", type=int, default=3)
    parser.add_argument("--all", action="store_true", help="Search every domain")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.max_results < 1:
        parser.error("--max-results must be positive")

    if args.all:
        result = search_all(args.query, args.max_results)
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
            return
        for domain in AVAILABLE_DOMAINS:
            if domain in result:
                print_domain(domain, result[domain])
        return

    result = search(args.query, args.domain, args.max_results)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return
    print_domain(result.get("domain", args.domain or "strategy"), result)


if __name__ == "__main__":
    main()
