#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate the CSV/schema inputs consumed by the Amoye retrieval engine."""

import csv
import json
import sys

from core import CSV_CONFIG, STACK_CONFIG, _STACK_COLS, DATA_DIR

JSON_COLUMNS = {"Decision_Rules"}


def _read_rows(filepath):
    with open(filepath, "r", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames or [], list(reader)


def _check_file(label, filepath, search_cols, output_cols, problems):
    if not filepath.exists():
        problems.append(f"[{label}] missing file: {filepath}")
        return
    try:
        headers, rows = _read_rows(filepath)
    except (csv.Error, UnicodeDecodeError, OSError) as error:
        problems.append(f"[{label}] failed to parse {filepath.name}: {error}")
        return

    header_set = set(headers)
    for column in set(search_cols) | set(output_cols):
        if column not in header_set:
            problems.append(f"[{label}] {filepath.name}: expected column '{column}' not found in header")

    if "No" in header_set:
        seen = {}
        for row_index, row in enumerate(rows, start=2):
            key = row.get("No", "")
            if key in seen:
                problems.append(f"[{label}] {filepath.name}: duplicate 'No' value '{key}' on rows {seen[key]} and {row_index}")
            else:
                seen[key] = row_index
    elif label.startswith("stack:"):
        problems.append(f"[{label}] {filepath.name}: missing 'No' index column used by the other stack datasets")

    for row_index, row in enumerate(rows, start=2):
        for column in JSON_COLUMNS:
            if column in row and row[column]:
                try:
                    json.loads(row[column])
                except json.JSONDecodeError as error:
                    problems.append(f"[{label}] {filepath.name} row {row_index}: column '{column}' is not valid JSON: {error}")


def main():
    problems = []
    for domain, config in CSV_CONFIG.items():
        _check_file(f"domain:{domain}", DATA_DIR / config["file"], config["search_cols"], config["output_cols"], problems)
    for stack, config in STACK_CONFIG.items():
        _check_file(f"stack:{stack}", DATA_DIR / config["file"], _STACK_COLS["search_cols"], _STACK_COLS["output_cols"], problems)

    if problems:
        print(f"FAILED: {len(problems)} data integrity issue(s) found:\n")
        for problem in problems:
            print(f"  - {problem}")
        return 1

    print(f"OK: validated {len(CSV_CONFIG)} domain files and {len(STACK_CONFIG)} stack files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
