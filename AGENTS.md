# Repository guidance

This repository packages independently installable skills. Each skill lives at `skills/<name>/SKILL.md`; its directory and frontmatter name must agree. Keep supporting resources with the skill. Use native skill discovery rather than a second catalogue or generated `default_prompt` metadata. Preserve invocation permissions when moving skills.

Use `oro` for agent-facing instructions and human-facing prose. Keep a skill's method with that skill, workflow progression with its workflow, and host configuration with the host. A skill must remain usable when installed on its own; retain essential guidance locally even when a caller also states it.

Simplify repeated or obsolete guidance while preserving behavior, authority boundaries, and useful expertise. Keep scripts only when they provide a bounded result that prose cannot reliably provide. Repository-wide package validators belong under `scripts/skills/`; optional model comparisons belong under `evals/`, outside installable skills.

Match verification to the change. Keep checks that catch realistic failures of shipped mechanics; remove redundant or incidental checks. Do not recreate a check the user deliberately removed. When removing a script or workflow, remove references to its commands and claims of its results. Report what was actually verified.

Keep attribution and licences when moving or retiring material.
