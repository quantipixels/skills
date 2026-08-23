"""Shared search-core regression coverage for logo and CIP adapters."""

import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS_DIR))

from search_core import BM25, _search_csv


def test_shared_bm25_and_csv_adapter_return_ranked_rows(tmp_path):
    csv_file = tmp_path / "records.csv"
    csv_file.write_text("name,keywords\nPrimary,blue modern\nSecondary,red classic\n")

    results = _search_csv(
        csv_file,
        ["name", "keywords"],
        ["name", "keywords"],
        "blue",
        1,
    )

    assert results == [{"name": "Primary", "keywords": "blue modern"}]
    assert BM25().tokenize("logo icon") == ["logo", "icon"]
