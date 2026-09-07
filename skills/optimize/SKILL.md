---
name: optimize
description: Find a measured improvement to a working system or agent workflow when the winning change is unknown. Use for bounded variant experiments, not diagnosis alone, read-only simplification, experiential prototypes, routine skill validation, or an already-selected correction.
metadata:
  maturity: experimental
---

# Optimize

Own the search for a measurably better candidate: the experiment question, comparison, and stop decision. A supported no-improvement result is valid. Do not turn ordinary implementation or validation into an optimization campaign.

## Bound the experiment

Establish the target, representative workload, measurable objective, hard constraints, mutable scope, current candidate, available tools, and permitted effects. Use existing project knowledge when it could change the hypotheses or proof.

Set a finite resource budget covering trials and confirmation before starting. Use a small bounded run when none was supplied; never initiate uncapped paid work. Analysis alone does not authorize edits. Installation, new dependencies, external disclosure, publication, and destructive actions retain their own authority requirements.

## Establish a valid comparison

Read [measurement and comparison](references/measurement.md). Prefer an existing benchmark, profiler, runtime probe, or evaluation surface; record the baseline before changing the target. If required measurement, host access, or credentials are unavailable, report the gap rather than simulate a result.

## Try only discriminating changes

Locate the cost or uncertainty when a cheaper observation would change which candidate is worth trying. Rank plausible changes by expected benefit, risk, and experiment cost; try the smallest discriminating change first.

Within granted mutation authority, use native/project tools for reversible trials isolated from unrelated work and each other's measurement state. Do not require a complete delivery/review cycle for every discarded trial. Apply enough invariant checks to reject invalid candidates before timing or scoring them; required acceptance proof still governs adoption.

Use the comparison evidence to keep a contender, revert an owned trial, or leave the result inconclusive. These conclusions grant no new mutation authority. Restore only owned changes; never overwrite unrelated work. Keep the original candidate when no tested variant qualifies.

Stop when the target is confirmed, the budget is spent, useful hypotheses are exhausted, the user interrupts, or a material capability/authority gap blocks progress. Stop owned active trials on interruption and report any partial effects. Do not continue merely to reach an iteration count.

## Finalize the retained candidate

Use `alaga` for retained software changes and `ko-skill` for retained skill changes. Reuse current proof rather than rebuilding the experiment or repeating completed review. A measured advantage cannot replace required acceptance or independent review. If finalization changes the measured candidate or its conditions, refresh the affected comparison before claiming the improvement.

Return the baseline and final result, workload and conditions, meaningful comparisons, preserved constraints, exact retained candidate, verification limits, and stop reason. Distinguish unrun hypotheses from failed trials and a promising contender from an accepted result.

Keep the experiment record in the conversation or existing destination; persist only for needed resumption, review, or reuse. Publish only when requested, using `seda-pr`. A measured winner is not automatically approved, integrated, or released.
