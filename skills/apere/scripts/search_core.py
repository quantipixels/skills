#!/usr/bin/env python3
"""Shared BM25 and CSV search primitives for Àpẹrẹ specialist adapters."""

import csv
import re
from collections import defaultdict
from math import log


class BM25:
    """Small stdlib-only BM25 ranking implementation."""

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
        text = re.sub(r'[^\w\s]', ' ', str(text).lower())
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
        self.idf = {
            word: log((self.N - frequency + 0.5) / (frequency + 0.5) + 1)
            for word, frequency in self.doc_freqs.items()
        }

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
                numerator = tf * (self.k1 + 1)
                denominator = tf + self.k1 * (
                    1 - self.b + self.b * self.doc_lengths[index] / self.avgdl
                )
                score += self.idf[token] * numerator / denominator
            scores.append((index, score))
        return sorted(scores, key=lambda item: item[1], reverse=True)


def _load_csv(filepath):
    """Load CSV rows for a specialist adapter."""
    with open(filepath, 'r', encoding='utf-8', newline='') as handle:
        return list(csv.DictReader(handle))


def _search_csv(filepath, search_cols, output_cols, query, max_results):
    """Search one specialist CSV and return positive-scoring rows."""
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
