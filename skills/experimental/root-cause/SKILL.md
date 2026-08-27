---
name: root-cause
description: Establish the minimal causal explanation for one reproducible or directly observed failure by building and falsifying competing mechanisms. Use when the missing outcome is diagnosis rather than issue validity, code review, or implementation.
disable-model-invocation: true
---

# Root Cause

Find the smallest causal mechanism or causal set that explains the observed failure and its downstream symptoms. Keep diagnosis separate from issue triage, code review, and production delivery.

A useful diagnosis may contain:

```text
trigger
+ necessary enabling condition
+ propagation mechanism
+ missing containment, recovery, or detection
→ observed failure
```

Do not force a complex failure into one artificial linear “first cause.”

## 1. Pin the failure

Record the exact symptom, expected behaviour, first known trigger, candidate or revision, environment, reproducibility, available evidence, scope, and read/probe authority. A report, stack trace, reviewer claim, correlation, changed file, or temporal order is evidence—not a cause.

Use `se-triage` when the question is whether a supplied report is valid. Use `alaga` when the defect and required correction are already settled.

Reproduce the failure when safe. Otherwise pin one direct observation with enough identity to compare later evidence. Separate the primary failure from secondary errors, retries, recovery noise, and unrelated warnings.

## 2. Build and falsify competing explanations

Write a small competing-hypothesis table. For each hypothesis, state:

- proposed trigger and causal mechanism;
- necessary enabling conditions;
- propagation to the observed symptom;
- what current evidence it explains;
- one observation that distinguishes it from alternatives; and
- the smallest safe probe that can produce that observation.

Prefer read-only inspection, existing tests, logs, traces, configuration, history, and reversible diagnostic probes. Change one diagnostic variable at a time. Record what each result rules in, rules out, or leaves unresolved. Do not change several things to see what helps or retain a diagnostic mutation after the probe.

Follow the chain from trigger through state transition or computation to the visible failure. Distinguish root mechanism, enabling conditions, contributing factors, propagation, and missing containment/detection.

Prove a proposed minimal causal set at two levels:

1. **Set sufficiency** — under equivalent conditions, does the complete proposed set reproduce or explain the failure without a material gap?
2. **Factor necessity** — for every factor claimed as part of the minimal set, hold the other confirmed factors equivalent and remove or control that factor. The failure must cease or materially change in the predicted way.

A factor that has not passed a discriminating necessity probe is not part of a confirmed minimal set. Classify it as a contributing factor, contextual condition, or unresolved factor instead. When the diagnosis depends on an unproved factor, return `DIAGNOSED_BUT_UNPROVED` rather than `CONFIRMED_ROOT_CAUSE`.

This factor-level check may use a safe experiment, an existing natural comparison, trace evidence, source-level control-flow proof, or another observation that distinguishes the counterfactual. Do not require a dangerous live mutation when equivalent evidence already owns the claim.

A root cause is confirmed only when the causal explanation has no material gap, the proposed set is sufficient, every factor retained in the minimal set is individually necessary given the others, and discriminating evidence supports those claims.

## 3. Stop on evidence, not attempt quotas

Continue while another safe observation can materially update the causal model. Stop when:

- remaining hypotheses cannot be distinguished with available evidence;
- another safe probe cannot materially change the diagnosis;
- required observability, environment, credential, or authority is unavailable; or
- the failure cannot be reproduced and no equivalent direct evidence exists.

Do not invent hypothesis variants to appear exhaustive. Do not perform production correction attempts inside Root Cause.

## 4. Return the diagnosis

Return exactly one status:

- `CONFIRMED_ROOT_CAUSE` — the minimal causal explanation and discriminating proof are complete;
- `DIAGNOSED_BUT_UNPROVED` — one explanation best fits the evidence but a material proof gap remains;
- `EVIDENCE_BLOCKED` — a named evidence, environment, authority, credential, or observability gap prevents diagnosis; or
- `NOT_REPRODUCED` — the pinned failure could not be observed and no equivalent direct evidence exists.

Include:

```text
Failure identity
Status
Minimal causal mechanism or causal set
Per-factor necessity evidence
Contributing, contextual, and unresolved factors
Propagation and missing containment/detection
Decisive evidence
Falsified alternatives
Affected boundary
Confidence limits
Smallest useful next action
```

Do not present a plausible explanation as confirmed. When a confirmed diagnosis warrants production correction and that work is authorized, give `alaga` the exact diagnosis and required behaviour. Root Cause does not absorb delivery or final review.

Return inline by default. Persist through `akosile` only when a durable diagnosis is needed. Use `html-artifact` to visualise a substantial supplied terminal diagnosis when useful. Under an active plan, return Root Cause's native exact-current result rather than defining a plan-specific receipt.
