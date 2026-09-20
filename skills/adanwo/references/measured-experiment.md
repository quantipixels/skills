
# Measured experiment

Own the search for a measurably better candidate: the experiment question, comparison, and stop decision. A supported no-improvement result is valid. An unknown implementation alone does not require an experiment: use this skill when comparative trials and a measured keep/revert decision are needed to establish the requested result. Keep ordinary implementation or validation with its owner.

## Bound the experiment

Establish the target, representative workload, measurable objective, hard constraints, mutable scope, current candidate, available tools, and permitted effects. Use existing project knowledge when it could change the hypotheses or proof.

Set a finite resource budget covering trials and confirmation before starting. Use a small bounded run when none was supplied; never initiate uncapped paid work. Analysis alone does not authorize edits. Installation, new dependencies, external disclosure, publication, and destructive actions retain their own authority requirements.

## Establish a valid comparison

Prefer an existing benchmark, profiler, runtime probe, or evaluation surface; record the baseline before changing the target. If required measurement, host access, or credentials are unavailable, report the gap rather than simulate a result.

Use the project's or host's existing capability when profiler/trace, build, database or other measurement capture and reduction needs specialist guidance. Require the provenance and limits that affect comparability; Àdánwò retains the workload, hypothesis, constraints and keep/revert decision. Adequate native measurements need no extra route.

The metric must represent the requested outcome. Correctness, security, required behaviour, compatibility, and resource limits are hard constraints: an aggregate score cannot compensate for violating them.

### Trust the baseline

Use representative inputs and pin the candidate, data, dependency/runtime versions, host configuration, and permissions that materially affect the result. Check that the harness exercises the target and propagates failed or missing results. Choose the useful improvement threshold and comparison method before seeing candidate measurements.

Freeze the workload, acceptance constraints, and comparison method. When a necessary change affects comparability, record it and re-establish the affected baseline; do not remove difficult cases or tune the judge to favour a candidate.

Separate setup, warmup, steady-state work, and end-to-end cost when they change the decision. Choose the relevant statistic: throughput for a throughput goal, tail latency for a latency obligation, or successful completion for an agent task. Averages do not replace a required tail bound. Include costs shifted into tools, workers, retries, and correction work; unavailable telemetry is unknown, not zero. Instruction length alone is not an observed saving.

Repeat enough to expose material variability. Where feasible, alternate or randomize baseline/candidate order and pair comparable inputs to limit environmental drift. Serialize measurements that contend for CPU, data, cache, service quota, or a worker pool. State uncontrolled conditions rather than implying laboratory control.

### Reject false improvements

A candidate is ineligible when it skips required work, narrows the workload, weakens proof, changes failure into success, or moves cost outside the measured boundary without an accepted trade-off.

For example, a validator that checks half the files can look twice as fast. Preserve the required file and rejection coverage before comparing time. A batching change may improve throughput while violating a response-time bound; both obligations must survive.

A difference within relevant noise is `inconclusive`, not a supported win or proof of equivalence. Repeat or stop honestly. Do not claim statistical significance without a suitable analysis and enough evidence.

Confirm promising candidates with fresh measurements against the baseline or current best under the same contract. Record the reference candidate for each comparison. The best noisy observation is not a winner merely because several variants were tried.

When a model or person scores the results, read [judged outcomes](judged-outcomes.md).

When comparing agent instructions, skill selection or model behavior on tasks, read [agent evaluation](agent-evaluation.md).

For build or CI improvements, measure the required clean and incremental paths with explicit cache state. Preserve the selected checks and produced artifacts. Exercise a relevant source, dependency or configuration change to show that cached or generated outputs invalidate correctly; a warm no-op build alone cannot establish a safe speedup. Distinguish fresh execution from cached proof and use the dependency critical path rather than adding parallel task durations. Keep executor capacity and job selection comparable, and include deferred or remote work in the cost boundary.

## Try only discriminating changes

Locate the cost or uncertainty when a cheaper observation would change which candidate is worth trying. Rank plausible changes by expected benefit, risk, and experiment cost; try the smallest discriminating change first.

Use a measured cost signature to generate hypotheses; the table suggests candidates, not prescriptions. Evidence that work is slow is separate from evidence that it is safe to remove, defer or share.

| Observed signature | Candidate hypothesis | Constraint to preserve or measure |
| --- | --- | --- |
| Work completes but no required consumer or effect uses it | Eliminate the work | Prove absence of required outputs, effects and compatibility obligations |
| Cost grows mainly with input or retained-data size | Partition, prune or bound the processed set | Preserve result coverage and include filtering, coordination and missed-case cost |
| The same effective input triggers the same expensive result repeatedly | Cache or reuse the result | Define identity, invalidation, freshness, consistency and memory bounds |
| A repeated scan or lookup dominates the critical path | Add a lookup structure or move justified work off that path | Include maintenance, storage, queueing and failure cost |
| Fixed overhead repeats for many small operations | Batch compatible operations | Preserve latency bounds, isolation, ordering and partial-failure behavior |
| Variable waiting dominates while spare capacity exists | Try bounded hedging or replication | Control duplicate effects, cancellation, load and correlated failures |
| Results are computed eagerly but often unused | Make evaluation lazy | Preserve observable ordering, error timing and resource lifetime |
| Required work need not complete within the user's wait | Schedule it outside the response path | Preserve durable completion, retries, visibility and consistency; count shifted cost |

Within granted mutation authority, use native/project tools for reversible trials isolated from unrelated work and each other's measurement state. Do not require a complete delivery/review cycle for every discarded trial. Apply enough invariant checks to reject invalid candidates before timing or scoring them; required acceptance proof still governs adoption.

Record each trial's candidate, hypothesis, workload, invariant result, measurement, comparison, and disposition. Use this evidence to keep a contender, revert an owned trial, or leave the result inconclusive. These conclusions grant no new mutation authority. Restore only owned changes; never overwrite unrelated work. Keep the original candidate when no tested variant qualifies.

Stop when the target is confirmed, the budget is spent, useful hypotheses are exhausted, the user interrupts, or a material capability/authority gap blocks progress. Stop owned active trials on interruption and report any partial effects. Do not continue merely to reach an iteration count.

## Finalize the retained candidate

Use `alaga` for retained software changes and `oro` in its agent-facing branch for retained skill changes. Reuse current proof rather than rebuilding the experiment or repeating completed review. A measured advantage cannot replace required acceptance or independent review. If finalization changes the measured candidate or its conditions, refresh the affected comparison before claiming the improvement.

Return the baseline and final result, workload and conditions, meaningful comparisons, preserved constraints, exact retained candidate, verification limits, and stop reason. Distinguish unrun hypotheses from failed trials and a promising contender from an accepted result.

Keep the experiment record in the conversation or existing destination; persist only for needed resumption, review, or reuse. Omit unused fields; no universal schema, permanent benchmark catalogue, or standing prompt-wording tests are required. Publish only when requested, using `wo-pr` in publication mode. A measured winner is not automatically approved, integrated, or released.
