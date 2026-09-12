# SureForge eval kit

Source: https://github.com/Da7-Tech/SureForge

Pinned commit: `dadf5110621739143063da5e4cbb33790d48c95d` (MIT; LICENSE retained).

Imported: the complete evals/ directory and its test_gates.py and test_metrics.py tests. The skill itself and unrelated package/install machinery are not imported. The original eval README refers to some files in that full upstream repository; use the pinned source for those references.

Local adaptation: metrics.py imports ROOT and load_json from evals.support instead of scripts.check_package. support.py preserves those upstream definitions without importing the whole package validator. Trailing blank lines were normalized during import. Keep all other source behavior and test definitions intact.

From this directory, run:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 -m evals.metrics --help
```

This kit supplies reusable scenario structures, fixtures, study/record formats, an abstract gate model, and metrics validation. It does not execute models. Its gate rules, activation labels, requirements, and three-arm efficacy checks are SureForge-specific. Define another skill's own oracles and study arms rather than treating agreement with SureForge's policy as universal correctness. Never overwrite the pinned fixtures or invent completed records to make another skill fit the aggregator.

No imported study has been run here. Package tests and synthetic metric fixtures remain mechanical evidence only.
