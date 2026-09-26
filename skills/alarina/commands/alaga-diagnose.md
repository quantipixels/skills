# Diagnosis

Read the [shared engineering contract](../references/engineering/delivery/engineering-contract.md) before applying this method.

Find the smallest causal mechanism or sufficient causal set that explains the observed failure and downstream symptoms. Diagnosis stays separate from triage/review/correction delivery.

Delegate when parallel work, separate context or independent scrutiny earns its briefing and integration cost. Otherwise work directly. Require concise findings and evidence links, and preserve any required review independence.

A useful model may be:

```text
trigger + enabling conditions + propagation + missing containment/detection → observed failure
```

## Pin the failure

Record exact symptom, expected behavior, first known trigger, candidate/revision or event identity, environment/context, reproducibility, evidence, scope, and read/probe authority. A report, stack trace, correlation, changed artifact, or temporal order is evidence, not a cause.

If the failing path is hidden in an unfamiliar codebase, use [sawari](sawari.md) to locate the relevant implementation and consumers. Bring its source map and limits back to the competing mechanisms below; exploration does not establish a cause or authorize a repair.

Reproduce safely when possible; otherwise pin one equivalent direct observation. Separate primary failure from secondary errors, retries, compensating behavior, and recovery noise.

Use the smallest feedback loop that can distinguish the reported symptom from the intended behavior. A failing test, focused runtime probe, trace replay, browser check, benchmark, or direct observation can serve. Minimize the reproduction when it materially sharpens the diagnosis; do not delay a useful hypothesis merely because a runnable loop is unavailable.

## Competing mechanisms

Maintain a small set of competing hypotheses. Capture the trigger/mechanism, enabling conditions, propagation, evidence explained, distinguishing observation, and smallest safe probe where each is material. Use a table when several live hypotheses benefit from side-by-side comparison; a short comparison is enough for a simple decisive probe.

Read [probe discipline](../references/engineering/diagnosis/diagnosis-probes.md) for bounded history/repair comparisons, cross-component failures, order-dependent tests or temporary instrumentation. Prefer existing observations, tests, logs, traces, configuration, history, measurements, and reversible diagnostics that fit the domain.

For runtime artifacts, pin capture conditions, useful work, cache state and symbol availability. CPU attribution needs the relevant caller path and inclusive versus self cost; retained memory needs a retaining path rather than allocation volume; a stall needs the wait chain and awaited owner. Correlate event identifiers and intervals. Missing symbols limit attribution, and a hotspot or paired trace alone does not prove cause.

For query behavior, inspect generated statements, round trips, result cardinality/order and the relevant plan at representative scale. Fewer queries do not establish improvement if results or resource use worsen. A plan-analysis command may execute its statement; keep the probe within existing data and mutation authority.

Choose each next observation or intervention for its ability to distinguish the live hypotheses, not because a preferred debugging ritual exists. Control material confounders where practical. Vary one factor at a time only when that probe can actually discriminate the mechanism; when interactions or coupled conditions are plausible, design the observation/probe to expose those interactions rather than pretending the factors are independent.

For a proposed causal explanation establish:

1. **Explanatory sufficiency** — the proposed mechanism/set explains or reproduces the observed failure and material downstream symptoms without an unresolved causal gap.
2. **Factor support** — each claimed causal factor has discriminating evidence showing its contribution in the relevant context. When feasible, removing/controlling a factor should change the outcome or a predicted mediator as expected.
3. **Conditionality and alternatives** — do not label a factor globally necessary when another sufficient pathway, interaction, or context can produce the same failure. State whether the factor is necessary for this observed pathway, contributing, enabling, interacting, or unresolved.

A factor lacking discriminating support is contextual/contributing/unresolved, not a confirmed root cause merely because it occurred before the failure.

## Stop on evidence

After confirming a root cause, use [variant analysis](../references/engineering/diagnosis/variant-analysis.md) when the request or evidence warrants finding related instances. Keep the search bounded to that mechanism; confirmation alone does not require a repository-wide sweep.

Continue only while another safe observation can materially update the causal model. Stop when remaining hypotheses cannot be distinguished, no safe probe can change the diagnosis, required environment/observability/authority is unavailable, or the failure cannot be reproduced and no equivalent direct evidence exists.

Keep correction delivery outside diagnosis. When existing request or caller authority permits reversible diagnostic edits, a patch may be used only when it is the smallest safe discriminator, remains isolated from the accepted candidate, and is reverted or handed off explicitly after observation. It does not become the correction by implication.

## Result

Return one:

- `CONFIRMED_ROOT_CAUSE` — minimal causal mechanism/set and discriminating evidence are sufficient for the observed failure/path;
- `DIAGNOSED_BUT_UNPROVED` — best explanation has a material causal/evidence gap;
- `EVIDENCE_BLOCKED` — named evidence/environment/authority/observability gap;
- `NOT_REPRODUCED` — pinned failure not observed and no equivalent direct evidence.

Include the failure identity, minimal mechanism/set, decisive evidence, causal roles, and falsified alternatives. Add interactions or alternative sufficient paths, contributing/contextual/unresolved factors, propagation/containment, affected boundary, confidence limits, and the smallest useful next action when material. A simple diagnosis resolved by one decisive probe may be correspondingly concise, but must still make the causal inference and ruled-out alternative explicit.

If temporary instrumentation remains for an authorized next step, include its exact marker/locations and cleanup owner in the same handoff. It is outstanding work, not part of the accepted repair by default.

Preserve a needed durable diagnosis in the existing project destination. Use [html-artifact](html-artifact.md) as needed.
