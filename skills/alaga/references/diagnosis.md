# Diagnosis

Find the smallest causal mechanism or sufficient causal set that explains the observed failure. Diagnosis stays separate from intake, review and correction.

Pin the symptom, expected behavior, candidate/event, environment, reproducibility, existing evidence and probe authority. Separate the primary failure from retries, secondary errors and recovery noise. Use a safe reproduction or equivalent direct observation; lack of a runnable loop does not block a useful hypothesis.

Maintain only live competing mechanisms. For each, name the trigger, enabling conditions, propagation, explained evidence and the smallest observation that could distinguish it. Use existing tests, logs, traces, configuration, history and reversible probes; read [probe discipline](diagnosis-probes.md) for history/repair comparisons, cross-component failures or order-dependent tests. Use `irinse` for non-obvious capture or attribution while retaining causal judgment here.

A confirmed explanation needs:

- explanatory sufficiency for the failure and material symptoms;
- discriminating support for each claimed factor; and
- honest conditionality where interactions or alternative sufficient paths exist.

Temporal order and correlation are not causes. Classify a factor as necessary for this path, contributing, enabling, interacting or unresolved. Isolated diagnostic edits remain probes, not accepted fixes, and must be reverted or explicitly handed off.

## Variants of a confirmed cause

When related instances are in scope, calibrate a text, structural, symbol or flow search against the known failing instance or correct revision. Generalize one dimension at a time and compare trigger, enabling conditions, effect and containment. Separate confirmed variants, look-alikes, unresolved candidates and unassessed areas. A bounded negative search does not prove repository-wide absence, and variant discovery does not authorize correction.

## Result

Stop when another safe observation cannot materially update the model. Return one:

- CONFIRMED_ROOT_CAUSE — sufficient mechanism and discriminating evidence;
- DIAGNOSED_BUT_UNPROVED — best explanation retains a material gap;
- EVIDENCE_BLOCKED — named environment, observability or authority gap; or
- NOT_REPRODUCED — neither the failure nor equivalent evidence was observed.

Include the failure identity, mechanism, decisive evidence, falsified alternatives, causal roles and material limits. Preserve a durable diagnosis only when needed.
