---
name: root-cause
description: Establish the minimal causal explanation for one reproducible or directly observed failure by building and falsifying competing mechanisms. Use when the missing outcome is diagnosis rather than report validity, review, or correction delivery.
---

# Root Cause

Find the smallest causal mechanism or sufficient causal set that explains the observed failure and downstream symptoms. Diagnosis stays separate from triage/review/correction delivery.

A useful model may be:

```text
trigger + enabling conditions + propagation + missing containment/detection → observed failure
```

## Pin the failure

Record exact symptom, expected behavior, first known trigger, candidate/revision or event identity, environment/context, reproducibility, evidence, scope, and read/probe authority. A report, stack trace, correlation, changed artifact, or temporal order is evidence, not a cause.

Use `se-triage` when an engineering/software report still needs issue-validity classification. Use `alaga` only when the diagnosis is settled and the correction is a software/build delivery job; otherwise return the diagnosis to the current correction owner.

Reproduce safely when possible; otherwise pin one equivalent direct observation. Separate primary failure from secondary errors, retries, compensating behavior, and recovery noise.

## Competing mechanisms

Write a small hypothesis table. For each hypothesis state trigger/mechanism, enabling conditions, propagation, evidence explained, one distinguishing observation, and the smallest safe probe.

Read [probe commands](references/probe-commands.md) when bounded source/history/Git evidence can discriminate hypotheses. Prefer existing observations, tests, logs, traces, configuration, history, measurements, and reversible diagnostics that fit the domain.

Choose each next observation or intervention for its ability to distinguish the live hypotheses, not because a preferred debugging ritual exists. Control material confounders where practical. Vary one factor at a time only when that probe can actually discriminate the mechanism; when interactions or coupled conditions are plausible, design the observation/probe to expose those interactions rather than pretending the factors are independent.

For a proposed causal explanation establish:

1. **Explanatory sufficiency** — the proposed mechanism/set explains or reproduces the observed failure and material downstream symptoms without an unresolved causal gap.
2. **Factor support** — each claimed causal factor has discriminating evidence showing its contribution in the relevant context. When feasible, removing/controlling a factor should change the outcome or a predicted mediator as expected.
3. **Conditionality and alternatives** — do not label a factor globally necessary when another sufficient pathway, interaction, or context can produce the same failure. State whether the factor is necessary for this observed pathway, contributing, enabling, interacting, or unresolved.

A factor lacking discriminating support is contextual/contributing/unresolved, not a confirmed root cause merely because it occurred before the failure.

## Stop on evidence

Continue only while another safe observation can materially update the causal model. Stop when remaining hypotheses cannot be distinguished, no safe probe can change the diagnosis, required environment/observability/authority is unavailable, or the failure cannot be reproduced and no equivalent direct evidence exists.

Do not perform correction attempts inside Root Cause.

## Result

Return one:

- `CONFIRMED_ROOT_CAUSE` — minimal causal mechanism/set and discriminating evidence are sufficient for the observed failure/path;
- `DIAGNOSED_BUT_UNPROVED` — best explanation has a material causal/evidence gap;
- `EVIDENCE_BLOCKED` — named evidence/environment/authority/observability gap;
- `NOT_REPRODUCED` — pinned failure not observed and no equivalent direct evidence.

Include failure identity, minimal mechanism/set, per-factor evidence and causal role, interactions/alternative sufficient paths when material, contributing/contextual/unresolved factors, propagation/containment, decisive evidence, falsified alternatives, affected boundary, confidence limits, and smallest useful next action.

When a durable diagnosis is needed, use the existing/user-selected destination; use `akosile` only when that destination is a repository-scoped `.qp` workspace. Use `html-artifact` only when a substantial terminal diagnosis benefits from a visual view.
