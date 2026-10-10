# Measured comparison

Use when a consequential engineering claim needs baseline/candidate trials. A comparison-only request stops at the evidence; adoption requires delivery authority.

Establish the exact baseline, representative workload, useful improvement threshold, hard constraints, permitted edits and finite budget including confirmation. Prefer existing measurement tools and check that the harness exercises the target and reports missing or failed results.

Freeze workload and comparison criteria before candidate results. Define observable drift that would invalidate the comparison, distinguishing uncertainty in reported latency from uncertainty in the keep/revert decision. Pin versions, data, host and cache conditions that affect comparability; re-establish affected baselines when conditions change. Correctness, security and required behavior are hard gates. Skipping work, weakening proof or hiding shifted cost cannot establish improvement.

Use observed costs to choose small discriminating trials. Isolate reversible edits from unrelated work and measurement state. Check invariants before timing. Measure relevant setup, steady-state and end-to-end costs, including tools, retries and deferred work. Preserve required tail bounds; missing telemetry is unknown.

Repeat enough to expose variability, pair comparable inputs and alternate order where feasible. Serialize competing measurements. Differences within noise are inconclusive; confirm promising candidates with fresh measurements against the named baseline. The best noisy observation is not a winner.

For builds and CI, cover required clean and incremental paths with explicit cache state and comparable checks, artifacts and capacity. Exercise source, dependency or configuration changes to verify invalidation. A warm no-op build cannot establish a safe speedup. Distinguish cached proof from execution; measure the critical path rather than adding parallel durations.

Stop at the target, budget, exhausted useful hypotheses, interruption or material gap. Stop owned trials on interruption and report partial effects. Restore only owned changes; keep the original when no candidate qualifies.

Report candidate identities, hypotheses, conditions, invariant checks, measurements, disposition and limits in the existing record. Distinguish unrun, failed and inconclusive trials. For authorized adoption, the builder applies the change and reuses valid proof and refreshes comparisons affected by finalization.

## Benchmark checklist

Use before reporting any timing, throughput or size comparison. A request for a rough number may use one run with the work and error checks below, and a claim limited to that.

1. **Claim.** Write what you intend to show before you run anything, including the baseline.
2. **Harness.** Read it. Confirm it times the target and not setup, the wrong build or a cached answer.
3. **Limiter.** Say what bounds the number (CPU, memory, disk, network, lock, the harness itself). Needed for any causal claim; not needed for a plain bounded timing.
4. **Fair tuning.** Give each side the same build mode, flags, data, warm-up and cache state.
5. **Correct work.** Check outputs and error counts, and that the timed region does the work you claim. A fast run that skips work or fails is not a result. Check the number against physical bounds.
6. **Repeat.** At least five alternating runs per side (A B A B ...). Report the median and the spread.
7. **No small wins.** Do not claim a difference smaller than the run-to-run variation; call it inconclusive.
8. **Relevance.** Say whether the timed path matters end to end for the user.

Profile in a separate run from the timed ones. Use tools that exist on the host (on macOS, for example, `sample` or Instruments, not Linux-only ones).
