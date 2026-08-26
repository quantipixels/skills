---
name: root-cause
description: Establish why one reproducible or directly observed failure occurs by building and falsifying a complete causal chain. Use when the missing outcome is diagnosis rather than issue validity, code review, or implementation.
disable-model-invocation: true
---

# Root Cause

Find the first causal mechanism that explains the observed failure and its downstream symptoms. Keep diagnosis separate from issue triage, code review, and production delivery.

## 1. Pin the failure

Record the exact symptom, expected behavior, first known trigger, candidate or revision, environment, reproducibility, available evidence, scope, and read or mutation authority. A report, stack trace, reviewer claim, correlation, or changed file is evidence, not a cause.

When the question is whether a supplied report is valid, use `se-triage` instead. When the defect and required correction are already settled, use `alaga` instead.

Reproduce the failure when safe. Otherwise pin one direct observation with enough identity to compare later evidence. Separate the primary failure from secondary errors, retries, recovery noise, and unrelated warnings.

## 2. Build and falsify hypotheses

Write a small competing-hypothesis table. For each hypothesis, state:

- the proposed causal mechanism;
- what evidence it explains;
- one observation that would distinguish it from the alternatives; and
- the smallest safe probe that can produce that observation.

Test one hypothesis or diagnostic variable at a time. Prefer read-only inspection, existing tests, logs, traces, configuration, history, and reversible probes. Record what each result rules in or rules out. Do not change several things to see what helps, call temporal order causation, or retain a diagnostic mutation after the probe.

Follow the chain from trigger through state transition or computation to the user-visible symptom. A root cause is confirmed only when the chain has no material explanatory gap and a discriminating proof supports the mechanism.

After two or three materially different hypotheses fail without convergence, stop and explain the missing observation or model instead of generating variants. After three failed correction attempts, stop fixing and diagnose why the causal model or acceptance boundary is wrong.

## 3. Return the diagnosis

Return exactly one status:

- `CONFIRMED_ROOT_CAUSE` — the causal chain and discriminating proof are complete;
- `DIAGNOSED_BUT_UNPROVED` — one mechanism best explains the evidence, but material proof is missing;
- `EVIDENCE_BLOCKED` — a named environment, authority, credential, observability, or evidence gap prevents diagnosis; or
- `NOT_REPRODUCED` — the pinned failure could not be observed and no equivalent direct evidence exists.

Include the exact failure identity, causal chain, decisive evidence, falsified alternatives, affected boundary, confidence limits, and smallest useful next action. Do not present a plausible hypothesis as confirmed.

When a confirmed diagnosis warrants a production correction and that work is authorized, give `alaga` the exact candidate, causal mechanism, required behavior, regression boundary, exclusions, and proof. Root Cause may prepare a bounded fix contract; it does not absorb delivery or final review.

## 4. Persist only when useful

Return inline by default. When the user or caller requires a durable diagnosis, resolve one record through `akosile` at that persistence boundary:

```text
owner: root-cause
record_type: diagnosis
subject: <stable failure identity>
```

Store the exact-current failure, hypotheses, proof, causal chain, status, and next action in `record.md`. Under an active Atọ́nà plan, return a compact diagnosis receipt to the plan instead of creating a competing initiative report. Generate a terminal HTML view only when the durable diagnosis is substantial and a human visual explanation materially helps; HTML is not required throughout the investigation.
