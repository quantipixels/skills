#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stdlib-only regression tests for the Amoye BM25 retrieval engine."""

import sys
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPTS_DIR))

from core import AVAILABLE_STACKS, BM25, CSV_CONFIG, detect_domain, search, search_stack


class TestTokenizer(unittest.TestCase):
    def test_short_domain_terms_are_kept(self):
        bm25 = BM25()
        tokens = bm25.tokenize("UI and UX design with 3D and AI")
        self.assertIn("ui", tokens)
        self.assertIn("3d", tokens)
        self.assertIn("ai", tokens)

    def test_stopwords_removed(self):
        bm25 = BM25()
        tokens = bm25.tokenize("this is for the team to do")
        for stopword in ("is", "for", "the", "to", "do"):
            self.assertNotIn(stopword, tokens)

    def test_synonym_normalization(self):
        bm25 = BM25()
        self.assertEqual(bm25.tokenize("e-commerce store"), bm25.tokenize("ecommerce store"))
        self.assertEqual(bm25.tokenize("dark-mode toggle"), bm25.tokenize("dark toggle"))


class TestSearchDomains(unittest.TestCase):
    def test_ui_is_searchable_in_style_domain(self):
        result = search("ui minimalism", domain="style", max_results=1)
        self.assertGreater(result["count"], 0)

    def test_accessibility_query_hits_ux(self):
        result = search("accessibility contrast wcag keyboard", domain="ux", max_results=3)
        self.assertGreater(result["count"], 0)

    def test_zero_result_query_reports_suggestions_not_error(self):
        result = search("zzqqxx totally made up gibberish", domain="ux", max_results=2)
        self.assertEqual(result["count"], 0)
        self.assertIn("suggestions", result)
        self.assertNotIn("error", result)

    def test_invalid_max_results_is_a_structured_empty_result(self):
        for limit in (0, -1, 51):
            with self.subTest(limit=limit):
                result = search("design", domain="ux", max_results=limit)
                self.assertEqual(result["error"]["code"], "invalid_max_results")
                self.assertEqual(result["count"], 0)
                self.assertEqual(result["results"], [])

    def test_unreadable_csv_is_a_structured_empty_result(self):
        import core

        original_data_dir = core.DATA_DIR
        try:
            core.DATA_DIR = Path("/private/path-that-does-not-exist")
            result = search("design", domain="ux", max_results=1)
        finally:
            core.DATA_DIR = original_data_dir

        self.assertEqual(result["count"], 0)
        self.assertEqual(result["results"], [])
        self.assertIn(result["error"]["code"], {"data_missing", "data_unreadable"})

    def test_every_configured_domain_file_exists_and_is_searchable(self):
        for domain in CSV_CONFIG:
            with self.subTest(domain=domain):
                result = search("design", domain=domain, max_results=1)
                self.assertNotIn("error", result, f"domain '{domain}' failed: {result.get('error')}")

    def test_every_stack_file_exists_and_is_searchable(self):
        for stack in AVAILABLE_STACKS:
            with self.subTest(stack=stack):
                result = search_stack("performance", stack, max_results=1)
                self.assertNotIn("error", result, f"stack '{stack}' failed: {result.get('error')}")


class TestDomainDetection(unittest.TestCase):
    def test_style_keywords_route_to_style(self):
        self.assertEqual(detect_domain("glassmorphism dark ui"), "style")

    def test_accessibility_keywords_route_to_ux(self):
        self.assertEqual(detect_domain("accessibility contrast wcag"), "ux")

    def test_ambiguous_query_returns_runner_up(self):
        domain, _runner_up = detect_domain("font pairing elegant crypto", return_scores=True)
        self.assertIsNotNone(domain)

    def test_empty_query_falls_back_to_style(self):
        self.assertEqual(detect_domain("...!!!???"), "style")


if __name__ == "__main__":
    unittest.main()
