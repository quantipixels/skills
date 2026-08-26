#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BM25 retrieval over the bundled slide strategy, layout, copy, and chart data."""

import csv
import re
from collections import defaultdict
from math import log
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"
MAX_RESULTS = 3

CSV_CONFIG = {
    "strategy": {
        "file": "slide-strategies.csv",
        "search_cols": ["strategy_name", "keywords", "goal", "audience", "narrative_arc"],
        "output_cols": ["strategy_name", "keywords", "slide_count", "structure", "goal", "audience", "tone", "narrative_arc", "sources"],
    },
    "layout": {
        "file": "slide-layouts.csv",
        "search_cols": ["layout_name", "keywords", "use_case", "recommended_for"],
        "output_cols": ["layout_name", "keywords", "use_case", "content_zones", "visual_weight", "cta_placement", "recommended_for", "avoid_for", "css_structure"],
    },
    "copy": {
        "file": "slide-copy.csv",
        "search_cols": ["formula_name", "keywords", "use_case", "emotion_trigger", "slide_type"],
        "output_cols": ["formula_name", "keywords", "components", "use_case", "example_template", "emotion_trigger", "slide_type", "source"],
    },
    "chart": {
        "file": "slide-charts.csv",
        "search_cols": ["chart_type", "keywords", "best_for", "when_to_use", "slide_context"],
        "output_cols": ["chart_type", "keywords", "best_for", "data_type", "when_to_use", "when_to_avoid", "max_categories", "slide_context", "css_implementation", "accessibility_notes"],
    },
}

AVAILABLE_DOMAINS = list(CSV_CONFIG.keys())


class BM25:
    def __init__(self, k1=1.5, b=0.75):
        self.k1 = k1
        self.b = b
        self.corpus = []
        self.doc_lengths = []
        self.avgdl = 0
        self.idf = {}
        self.doc_freqs = defaultdict(int)
        self.N = 0

    def tokenize(self, text):
        text = re.sub(r"[^\w\s]", " ", str(text).lower())
        return [word for word in text.split() if len(word) > 2]

    def fit(self, documents):
        self.corpus = [self.tokenize(document) for document in documents]
        self.N = len(self.corpus)
        if self.N == 0:
            return
        self.doc_lengths = [len(document) for document in self.corpus]
        self.avgdl = sum(self.doc_lengths) / self.N
        for document in self.corpus:
            for word in set(document):
                self.doc_freqs[word] += 1
        for word, frequency in self.doc_freqs.items():
            self.idf[word] = log((self.N - frequency + 0.5) / (frequency + 0.5) + 1)

    def score(self, query):
        query_tokens = self.tokenize(query)
        scores = []
        for index, document in enumerate(self.corpus):
            term_freqs = defaultdict(int)
            for word in document:
                term_freqs[word] += 1
            score = 0
            for token in query_tokens:
                if token not in self.idf:
                    continue
                tf = term_freqs[token]
                denominator = tf + self.k1 * (
                    1 - self.b + self.b * self.doc_lengths[index] / self.avgdl
                )
                score += self.idf[token] * (tf * (self.k1 + 1)) / denominator
            scores.append((index, score))
        return sorted(scores, key=lambda item: item[1], reverse=True)


def _load_csv(filepath):
    with open(filepath, "r", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _search_csv(filepath, search_cols, output_cols, query, max_results):
    if not filepath.exists():
        return []
    data = _load_csv(filepath)
    documents = [" ".join(str(row.get(column, "")) for column in search_cols) for row in data]
    bm25 = BM25()
    bm25.fit(documents)
    results = []
    for index, score in bm25.score(query)[:max_results]:
        if score > 0:
            row = data[index]
            results.append({column: row.get(column, "") for column in output_cols if column in row})
    return results


def detect_domain(query):
    query_lower = query.lower()
    domain_keywords = {
        "strategy": ["pitch", "deck", "investor", "seed", "series", "demo", "sales", "webinar", "conference", "board", "qbr", "structure"],
        "layout": ["slide", "layout", "grid", "column", "title", "hero", "section", "cta", "screenshot", "quote", "timeline", "comparison", "pricing", "team"],
        "copy": ["headline", "copy", "formula", "aida", "pas", "hook", "cta", "benefit", "objection", "proof", "testimonial", "urgency", "scarcity"],
        "chart": ["chart", "graph", "bar", "line", "pie", "funnel", "metrics", "data", "visualization", "kpi", "trend", "comparison", "heatmap", "gauge"],
    }
    scores = {
        domain: sum(1 for keyword in keywords if keyword in query_lower)
        for domain, keywords in domain_keywords.items()
    }
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "strategy"


def search(query, domain=None, max_results=MAX_RESULTS):
    domain = domain or detect_domain(query)
    config = CSV_CONFIG.get(domain, CSV_CONFIG["strategy"])
    filepath = DATA_DIR / config["file"]
    if not filepath.exists():
        return {"error": f"File not found: {filepath}", "domain": domain}
    results = _search_csv(filepath, config["search_cols"], config["output_cols"], query, max_results)
    return {
        "domain": domain,
        "query": query,
        "file": config["file"],
        "count": len(results),
        "results": results,
    }


def search_all(query, max_results=2):
    return {
        domain: result
        for domain in AVAILABLE_DOMAINS
        if (result := search(query, domain, max_results)).get("count", 0) > 0
    }
