
# Measured experiment

Own a bounded baseline/candidate comparison and its keep/revert decision. A supported no-improvement or inconclusive result is valid; ordinary implementation and validation stay with their owners.

## Bound the experiment

Establish the target, representative workload, measurable objective, hard constraints, mutable scope, current candidate, available tools, and permitted effects. Use existing project knowledge when it could change the hypotheses or proof.

Set a finite budget for trials and confirmation. Use a small bounded run when none was supplied; do not initiate uncapped paid work. Analysis grants no edit, installation, dependency, disclosure, publication or destructive authority.

## Establish a valid comparison

Prefer an existing benchmark, profiler, runtime probe, or evaluation surface; record the baseline before changing the target. If required measurement, host access, or credentials are unavailable, report the gap rather than simulate a result.

Use `irinse` when profiler/trace, build, database or other measurement capture and reduction needs specialist guidance. Require the provenance and limits that affect comparability; Àdánwò retains the workload, hypothesis, constraints and keep/revert decision. Adequate native measurements need no extra route.

Require construct validity: measure the requested outcome. Correctness, security, required behaviour, compatibility and resource limits remain hard constraints; aggregate scores cannot offset violations.

Use a controlled comparison: pin representative inputs, candidate, data, dependency/runtime versions, host configuration and permissions. Verify that the harness exercises the target and propagates failed/missing results. Freeze workload, acceptance, improvement threshold and comparison method before candidate measurements. Record changes that affect comparability and re-establish the affected baseline; do not drop difficult cases or tune the judge to favour a candidate.

Separate setup, warmup, steady-state work, and end-to-end cost when they change the decision. Choose the relevant statistic: throughput for a throughput goal, tail latency for a latency obligation, or successful completion for an agent task. Averages do not replace a required tail bound. Include costs shifted into tools, workers, retries, and correction work; unavailable telemetry is unknown, not zero. Instruction length alone is not an observed saving.

Repeat enough to expose material variability. Where feasible, alternate or randomize baseline/candidate order and pair comparable inputs to limit environmental drift. Serialize measurements that contend for CPU, data, cache, service quota, or a worker pool. State uncontrolled conditions rather than implying laboratory control.

A candidate is ineligible when it skips required work, narrows the workload, weakens proof, changes failure into success, or moves cost outside the measured boundary without an accepted trade-off.

A difference within relevant noise is `inconclusive`, not a supported win or proof of equivalence. Repeat or stop honestly. Do not claim statistical significance without a suitable analysis and enough evidence.

Confirm promising candidates with fresh measurements against the baseline or current best under the same contract. Record the reference candidate for each comparison. The best noisy observation is not a winner merely because several variants were tried.

When a model or person scores results, fix the rubric and judge configuration, blind labels and vary order where feasible, and calibrate against accepted and rejected outputs. Judge agreement is not correctness proof; unacceptable outcomes and authority failures are hard rejections. Confirm on held-out work when selection may overfit. Record intervention and cache effects; synthetic or inspected evidence is not runtime evidence, and unavailable trials are `NOT_RUN`.

When comparing agent instructions, skill selection or model behavior on tasks, read [agent evaluation](agent-evaluation.md).

For build or CI improvements, measure the required clean and incremental paths with explicit cache state. Preserve the selected checks and produced artifacts. Exercise a relevant source, dependency or configuration change to show that cached or generated outputs invalidate correctly; a warm no-op build alone cannot establish a safe speedup. Keep executor capacity and job selection comparable, and include deferred or remote work in the cost boundary.

## Try only discriminating changes

Use a measured cost signature to rank plausible changes by expected benefit, risk and experiment cost; try the smallest change that distinguishes the live hypotheses. Evidence that work is costly is separate from evidence that it is safe to remove, cache, batch, defer, parallelize or move. Preserve identity, invalidation, coverage, ordering, latency, isolation, failure, cancellation, capacity and shifted-cost obligations that apply.

Within granted mutation authority, use native/project tools for reversible trials isolated from unrelated work and each other's measurement state. Do not require a complete delivery/review cycle for every discarded trial. Apply enough invariant checks to reject invalid candidates before timing or scoring them; required acceptance proof still governs adoption.

Record each trial's candidate, hypothesis, workload, invariant result, measurement, comparison and disposition. Keep a contender, revert an owned trial or remain inconclusive; restore only owned changes and keep the original when no candidate qualifies.

Stop when the target is confirmed, the budget is spent, useful hypotheses are exhausted, the user interrupts, or a material capability/authority gap blocks progress. Stop owned active trials on interruption and report any partial effects. Do not continue merely to reach an iteration count.

## Finalize the retained candidate

Use `alaga` for retained software changes and `oro` in its agent-facing branch for retained skill changes. Reuse current proof rather than rebuilding the experiment or repeating completed review. A measured advantage cannot replace required acceptance or independent review. If finalization changes the measured candidate or its conditions, refresh the affected comparison before claiming the improvement.

Return the baseline and final result, workload and conditions, meaningful comparisons, preserved constraints, exact retained candidate, verification limits, and stop reason. Distinguish unrun hypotheses from failed trials and a promising contender from an accepted result.

Keep the record in the conversation or existing destination; persist only for resumption, review or reuse. Publish only when requested through `wo-pr`. A measured winner is not automatically approved, integrated or released.
