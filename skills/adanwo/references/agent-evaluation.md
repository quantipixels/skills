# Agent evaluation

Use with the measured-experiment method when a skill, prompt, routing rule or model choice is the comparison target. Keep general experimental controls and judged-outcome calibration in their existing references.

State which claim is being tested: discovery, selection, loading, task execution or incremental benefit. Supplying a skill directly bypasses discovery. Asking for a route measures a decision, not execution. A successful guided run without a control cannot attribute the outcome to the guidance.

Compare the intended variable. For an instruction comparison, hold model, effort, tools, permissions and task conditions compatible; for a model comparison, hold the instructions compatible. Use fresh sessions or a controlled equivalent so shared history does not reveal earlier answers. The host supplies lifecycle and isolation; distinct directories alone do not establish either.

Give actors realistic tasks and necessary contracts without the private judging criteria, preferred solution or other actors' answers. Include the nearest plausible task where the guidance should stay inactive when selection matters. Keep output labels blind for judgment when feasible; do not hide facts actors need to do the real work.

Verify outcomes through actual artifacts and independent observations of important effects. Use available host traces for claims about skill loading or tool use; self-reported invocation is insufficient. Treat code, tests and harness changes returned by an actor as candidates requiring inspection, especially when they could make an incorrect result appear successful.

Record completed, failed, blocked and invalid runs separately. Include retries, corrections and human intervention in the comparison; missing telemetry is unknown. A checker defect invalidates affected verdicts: preserve the original results, fix the shared contract/checker from independent evidence, and reassess every affected arm consistently. An unchanged-artifact recheck is not a fresh model run.

Use the existing result record for candidate identity, conditions, outcome evidence and limits. Reserve effectiveness claims for a suitable matched comparison; report structural checks, supplied-candidate smoke outcomes and native discovery as distinct evidence.
