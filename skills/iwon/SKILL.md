---
name: iwon
description: Ìwọ̀n. Produces a measurement verdict (keep, revert or inconclusive) from a fair baseline-versus-candidate comparison, benchmark setup or check, and correct units and scaling. Use for "is it faster", "benchmark this", "keep or revert".
---

# Ìwọ̀n

**Output:** a measurement verdict with its evidence. It stops at the evidence; a comparison does not authorize adopting the change.

**Needs:** a candidate and a baseline, or a claim to test, plus a workload that stands for real use. If the request is too thin, or is not measurement, return to the caller and say what is missing.

## Method

**Workflow** (`asoju`): to move a metric over several rounds, hillclimb: one change per round, a cheap model runs the harness, you keep or revert.

Use the job the request names:

- **Measured comparison**: decide keep or revert for a change whose benefit is a claim. Read [measured comparison](references/measured-comparison.md), which also holds the benchmark checklist.
- **Units and scaling**: check numbers that carry a unit, a scale or a basis (money, time, size, rates, conversions). Read [units and scaling](references/units-and-scaling.md).

Rules:

- Fix the baseline, the workload and the threshold for "better" before you look at candidate results.
- Correctness, security and required behavior are hard gates. Skipping work, weakening proof or moving cost somewhere unmeasured is not an improvement.
- Say what was not run, failed or was inconclusive. A noisy result is reported as noisy.
- Use the project's own measurement tools first. Do not change production to create a measurement.

## Done

Baseline and candidate are identified, conditions are stated, and the verdict follows from the pre-fixed threshold.

## Return

Return the baseline and candidate identities, the conditions, the measurements, the verdict (keep, revert or inconclusive) and the limits.
