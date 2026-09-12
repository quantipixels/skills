"""Minimal extraction from SureForge scripts/check_package.py; see ../LICENSE."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def _constant(value):
    raise ValueError("non-finite JSON constant")


def load_json(text):
    return json.loads(text, object_pairs_hook=_pairs, parse_constant=_constant)
