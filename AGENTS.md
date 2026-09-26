# Repository guidance

This repository packages one canonical skill at `skills/alarina/SKILL.md`. All QP capabilities are focused commands under `skills/alarina/commands/`; supporting methods and resources remain under `skills/alarina/references/<domain>/`. Playbooks compose commands. Do not restore standalone QP skill entrypoints or nested discovery metadata. Preserve invocation permissions when moving or splitting commands.

Use Alárinà's `oro-sigidi` command for agent-facing instructions and `oro-eniyan` for human-facing prose. Keep expertise with its reference, workflow progression with its workflow, and host configuration with the host. `routes.yaml` owns the command inventory and generated menu; provider adapters own namespaces and supported metadata. Installing Alárinà must include its complete reference tree.

When implementation changes this repository's components, ownership, dependency direction or flows, check the canonical `ARCHITECTURE.md` or scoped architecture overview against the final code and update affected sections through Alárinà's `architect-document` command. Keep README and other affected reader instructions current through the delivery/documentation workflows. Record why no architecture update is needed when the impact is not obvious; do not create an overview for a routine change with no architectural effect.

Simplify repeated or obsolete guidance while preserving behavior, authority boundaries, and useful expertise. Choose cohesive command boundaries through `oro-sigidi`; do not split by technical layer or checklist step. Keep scripts only when they provide a bounded result that prose cannot reliably provide. Shared installed utilities belong under `skills/alarina/scripts/`, with interpretation at the owning method. Repository-wide package validators belong under `scripts/skills/`; optional model comparisons belong under `evals/`, outside installable skills.

Match verification to the change. Keep checks that catch realistic failures of shipped mechanics; remove redundant or incidental checks. Do not recreate a check the user deliberately removed. When removing a script or workflow, remove references to its commands and claims of its results. Report what was actually verified.

Keep attribution and licences when moving or retiring material.
