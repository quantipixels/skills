#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Logo Design Core - BM25 search engine for logo design guidelines
"""

import sys
from pathlib import Path

SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(SCRIPT_ROOT))
from search_core import _search_csv

# ============ CONFIGURATION ============
DATA_DIR = Path(__file__).parent.parent.parent / "data" / "logo"
MAX_RESULTS = 3

CSV_CONFIG = {
    "style": {
        "file": "styles.csv",
        "search_cols": ["Style Name", "Category", "Keywords", "Best For"],
        "output_cols": ["Style Name", "Category", "Keywords", "Primary Colors", "Secondary Colors", "Typography", "Effects", "Best For", "Avoid For", "Complexity", "Era"]
    },
    "color": {
        "file": "colors.csv",
        "search_cols": ["Palette Name", "Category", "Keywords", "Psychology", "Best For"],
        "output_cols": ["Palette Name", "Category", "Keywords", "Primary Hex", "Secondary Hex", "Accent Hex", "Background Hex", "Text Hex", "Psychology", "Best For", "Avoid For"]
    },
    "industry": {
        "file": "industries.csv",
        "search_cols": ["Industry", "Keywords", "Recommended Styles", "Mood"],
        "output_cols": ["Industry", "Keywords", "Recommended Styles", "Primary Colors", "Typography", "Common Symbols", "Mood", "Best Practices", "Avoid"]
    }
}


def detect_domain(query):
    """Auto-detect the most relevant domain from query"""
    query_lower = query.lower()

    domain_keywords = {
        "style": ["style", "minimalist", "vintage", "modern", "retro", "geometric", "abstract", "emblem", "badge", "wordmark", "mascot", "luxury", "playful", "corporate"],
        "color": ["color", "palette", "hex", "#", "rgb", "blue", "red", "green", "gold", "warm", "cool", "vibrant", "pastel"],
        "industry": ["tech", "healthcare", "finance", "legal", "restaurant", "food", "fashion", "beauty", "education", "sports", "fitness", "real estate", "crypto", "gaming"]
    }

    scores = {domain: sum(1 for kw in keywords if kw in query_lower) for domain, keywords in domain_keywords.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "style"


def search(query, domain=None, max_results=MAX_RESULTS):
    """Main search function with auto-domain detection"""
    if domain is None:
        domain = detect_domain(query)

    config = CSV_CONFIG.get(domain, CSV_CONFIG["style"])
    filepath = DATA_DIR / config["file"]

    if not filepath.exists():
        return {"error": f"File not found: {filepath}", "domain": domain}

    results = _search_csv(filepath, config["search_cols"], config["output_cols"], query, max_results)

    return {
        "domain": domain,
        "query": query,
        "file": config["file"],
        "count": len(results),
        "results": results
    }


def search_all(query, max_results=2):
    """Search across all domains and combine results"""
    all_results = {}
    for domain in CSV_CONFIG.keys():
        result = search(query, domain, max_results)
        if result.get("results"):
            all_results[domain] = result["results"]
    return all_results
