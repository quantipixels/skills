# Measured comparison

Read the [shared engineering contract](../references/engineering/delivery/engineering-contract.md) before applying this method. For verification of an already supplied repair, use the [existing-repair comparison](../references/engineering/diagnosis/diagnosis-probes.md#existing-repair-comparison) and stop at that evidence; correction still needs authority. The measured-improvement method below applies when the request asks for measured improvement or a keep/revert experiment.

Use when a consequential engineering claim needs baseline/candidate trials. A comparison-only request stops at the evidence; adoption requires delivery authority.

Establish the exact baseline, representative workload, useful improvement threshold, hard constraints, permitted edits and finite budget including confirmation. Prefer existing measurement tools and check that the harness exercises the target and reports missing or failed results.

Freeze workload and comparison criteria before candidate results. Pin versions, data, host and cache conditions that affect comparability; re-establish affected baselines when conditions change. Correctness, security and required behavior are hard gates. Skipping work, weakening proof or hiding shifted cost cannot establish improvement.

Use observed costs to choose small discriminating trials. Isolate reversible edits from unrelated work and measurement state. Check invariants before timing. Measure relevant setup, steady-state and end-to-end costs, including tools, retries and deferred work. Preserve required tail bounds; missing telemetry is unknown.

Repeat enough to expose variability, pair comparable inputs and alternate order where feasible. Serialize competing measurements. Differences within noise are inconclusive; confirm promising candidates with fresh measurements against the named baseline. The best noisy observation is not a winner.

For builds and CI, cover required clean and incremental paths with explicit cache state and comparable checks, artifacts and capacity. Exercise source, dependency or configuration changes to verify invalidation. A warm no-op build cannot establish a safe speedup. Distinguish cached proof from execution; measure the critical path rather than adding parallel durations.

Stop at the target, budget, exhausted useful hypotheses, interruption or material gap. Stop owned trials on interruption and report partial effects. Restore only owned changes; keep the original when no candidate qualifies.

Report candidate identities, hypotheses, conditions, invariant checks, measurements, disposition and limits in the existing record. Distinguish unrun, failed and inconclusive trials. For authorized adoption, follow Alága's delivery method, reuse valid proof and refresh comparisons affected by finalization.
