---
name: root-cause
description: Establish the minimal causal explanation for one reproducible or directly observed failure by building and falsifying competing mechanisms. Use when the missing outcome is diagnosis rather than report validity, review, or correction delivery.
---

# Root Cause

Find the smallest causal mechanism/set that explains the observed failure and downstream symptoms. Diagnosis stays separate from triage/review/correction delivery.

A useful model may be:

```text
trigger + necessary enabling condition + propagation + missing containment/detection → observed failure
```

## Pin the failure

Record exact symptom, expected behavior, first known trigger, candidate/revision or event identity, environment/context, reproducibility, evidence, scope, and read/probe authority. A report, stack trace, correlation, changed artifact, or temporal order is evidence, not a cause.

Use `se-triage` when an engineering/software report still needs issue-validity classification. Use `alaga` only when the diagnosis is settled and the correction is a software/build delivery job; otherwise return the diagnosis to the current correction owner.

Reproduce safely when possible; otherwise pin one equivalent direct observation. Separate primary failure from secondary errors/retries/recovery noise.

## Competing mechanisms

Write a small hypothesis table. For each hypothesis state trigger/mechanism, necessary conditions, propagation, evidence explained, one distinguishing observation, and the smallest safe probe.

Read [probe commands](references/probe-commands.md) when bounded source/history/Git evidence can discriminate hypotheses. Prefer existing observations, tests, logs, traces, configuration, history, measurements, and reversible diagnostics that fit the domain. Change one diagnostic variable at a time.

For a proposed minimal causal set prove:

1. **Set sufficiency** — the full set explains/reproduces the failure without a material gap.
2. **Factor necessity** — for every claimed factor, hold other confirmed factors equivalent and remove/control that factor; the failure must cease/change as predicted.

A factor lacking a discriminating necessity observation is contributing/contextual/unresolved, not confirmed root cause.

## Stop on evidence

Continue only while another safe observation can materially update the causal model. Stop when remaining hypotheses cannot be distinguished, no safe probe can change the diagnosis, required environment/observability/authority is unavailable, or the failure cannot be reproduced and no equivalent direct evidence exists.

Do not perform correction attempts inside Root Cause.

## Result

Return one:

- `CONFIRMED_ROOT_CAUSE` — minimal causal explanation and discriminating proof complete;
- `DIAGNOSED_BUT_UNPROVED` — best explanation has a material proof gap;
- `EVIDENCE_BLOCKED` — named evidence/environment/authority/observability gap;
- `NOT_REPRODUCED` — pinned failure not observed and no equivalent direct evidence.

Include failure identity, minimal mechanism/set, per-factor necessity evidence, contributing/contextual/unresolved factors, propagation/containment, decisive evidence, falsified alternatives, affected boundary, confidence limits, and smallest useful next action.

When a durable diagnosis is needed, use the existing/user-selected destination; use `akosile` only when that destination is a repository-scoped QP workspace. Use `html-artifact` only when a substantial terminal diagnosis benefits from a visual view.
