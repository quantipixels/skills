---
title: A file a skill needs at runtime must live inside that skill
category: skill-design
tags: [packaging, scripts, skill-dir, records-home, qp-records, check-package]
problem_type: bug
date: 2026-10-10
---

## Context
`alarina`'s records rule says each checkout gets a `.qp` link to its records home. The script that creates the link was at the repo root, `scripts/qp_records.py`.

## What went wrong or was non-obvious
The checks passed and the script had tests, but no skill shipped or called it. Hosts install each skill as its own folder, so installed users never had the script, and agents skipped the link; checkouts of this very repo had none. Two more skills only worked from a repo checkout: one ran `python3 skills/<name>/scripts/...`, another pointed at a sibling skill's files.

## Guidance
Anything a skill needs at runtime (scripts, references, assets) lives inside that skill's folder, and links stay inside it. Run bundled scripts as `"$SKILL_DIR/scripts/..."` with `SKILL_DIR` set to the folder holding the SKILL.md. Call another skill by name, never through its files. Repository tooling (validators, evals) stays outside skills.

## Evidence
`skills/alarina/scripts/qp_records.py`; `scripts/skills/check_package.py` fails on links that leave a skill folder, on `skills/<name>/` paths inside skills, and on bundled scripts run without `$SKILL_DIR`.
