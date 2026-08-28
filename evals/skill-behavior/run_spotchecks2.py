#!/usr/bin/env python3
from __future__ import annotations

import run_spotchecks as runner

runner.SELECTED_IDS = [
    "amoye-blank-slate",
    "banner-supplied-spec",
    "eto-existing-system",
    "akosile-concurrency",
    "amose-term-conflict",
    "wo-pr-large",
    "wo-pr-required-gap",
    "root-cause-timeout",
    "arojinle-multiround",
    "html-simple-report",
]

if __name__ == "__main__":
    raise SystemExit(runner.main())
