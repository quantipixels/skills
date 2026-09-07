# Measurement and comparison

The metric must represent the requested outcome. Correctness, security, required behaviour, compatibility, and resource limits are hard constraints: an aggregate score cannot compensate for violating them.

## Trust the baseline

Use representative inputs and pin the candidate, data, dependency/runtime versions, host configuration, and permissions that materially affect the result. Check that the harness exercises the target and propagates failed or missing results. Choose the useful improvement threshold and comparison method before seeing candidate measurements.

Freeze the workload, acceptance constraints, and comparison method. When a necessary change affects comparability, record it and re-establish the affected baseline; do not remove difficult cases or tune the judge to favour a candidate.

Separate setup, warmup, steady-state work, and end-to-end cost when they change the decision. Choose the relevant statistic: throughput for a throughput goal, tail latency for a latency obligation, or successful completion for an agent task. Averages do not replace a required tail bound. Include costs shifted into tools, workers, retries, and correction work; unavailable telemetry is unknown, not zero. Instruction length alone is not an observed saving.

Repeat enough to expose material variability. Where feasible, alternate or randomize baseline/candidate order and pair comparable inputs to limit environmental drift. Serialize measurements that contend for CPU, data, cache, service quota, or a worker pool. State uncontrolled conditions rather than implying laboratory control.

## Reject false improvements

A candidate is ineligible when it skips required work, narrows the workload, weakens proof, changes failure into success, or moves cost outside the measured boundary without an accepted trade-off.

For example, a validator that checks half the files can look twice as fast. Preserve the required file and rejection coverage before comparing time. A batching change may improve throughput while violating a response-time bound; both obligations must survive.

A difference within relevant noise is `inconclusive`, not a supported win or proof of equivalence. Repeat or stop honestly. Do not claim statistical significance without a suitable analysis and enough evidence.

Confirm promising candidates with fresh measurements against the baseline or current best under the same contract. Record the reference candidate for each comparison. The best noisy observation is not a winner merely because several variants were tried.

## Judged outcomes

When a model or person scores results, fix the rubric and judge configuration, blind candidate labels and vary presentation order where feasible, and calibrate against concrete accepted and rejected outputs. Judge agreement is not independent correctness proof. Keep unacceptable outcomes and authority failures as hard rejections rather than averaged penalties.

Confirm on fresh or held-out tasks when selection on the original examples could overfit. Record human intervention, cache effects, and missing observations. A synthetic transcript or source inspection is not an observed runtime measurement; mark unavailable runtime trials `NOT_RUN`.

## Keep the record useful

Record the candidate, hypothesis, workload, invariant result, measurement, comparison, and disposition. Omit unused fields and reuse an existing destination when persistence is needed. No universal schema, permanent benchmark catalogue, or standing prompt-wording tests are required.
