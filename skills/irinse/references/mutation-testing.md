# Bounded mutation testing

Use when a requested campaign or a concrete test-effectiveness question warrants executing changed behavior. Irinse owns tool readiness and evidence; alaga owns fixes and atunwo owns independent judgment. A source-inferred gap is not an executed survivor. Review-only authority does not permit source mutations.

## Establish a valid experiment

Discover the actual language, build system, module layout, test engine and existing mutation configuration. Run the relevant unmodified tests first; confirm tests actually executed and passed. Compilation, an empty selection or a cached report is not that baseline.

Name target classes/functions, covering tests, operator scope, total wall-clock limit and per-mutant timeout before execution. Reuse an agreed budget or choose a bounded one and report it. An empty target must not expand to the whole repository. Keep shared test resources exclusive where interference could invalidate evidence.

Prefer the existing runner. Before a manual mutation, establish exclusive ownership of affected source and test resources. Retain exact pre-edit bytes and the unrelated diff, apply one intended change, then restore only that change immediately after its test. Verify restoration even after interruption. Unexpected concurrent edits contaminate the run: stop the campaign and preserve both versions. Restore the owned mutation only when its hunk can be removed without losing concurrent work; otherwise report the restoration blocker. Never reset a file or repository over unrelated changes.

## Interpret the result

| Outcome | Evidence and limit |
| --- | --- |
| Killed | Executed mutation caused a relevant test failure; distinguish infrastructure failures. |
| Survived | Mutation executed and selected tests passed; inspect whether behavior actually differs. |
| Uncovered | Runner reports no reaching tests; separate this from an inferred source gap. |
| Equivalent | Contract-based reasoning establishes no observable difference in the supported domain. Failed attempts to kill it do not establish equivalence. |
| Timeout | Execution exceeded its limit; investigate timing before treating it as useful detection. |
| Execution error / non-viable | Build, runner, resource or invalid-mutant failure; not evidence of weak assertions. |
| Incomplete | Campaign stopped or evidence is missing; retain completed outcomes and unassessed scope separately. |

Preserve the runner's raw status alongside interpretation. For a consequential survivor, identify an input or sequence exposing the changed public result or effect. Pattern-based triage supplies leads, never automatic equivalence. Generated code and logging are not automatically irrelevant to a contract. Return fixes to alaga; when strengthening tests, rerun the same mutant and restore the passing baseline. No score gate is implied.

Use the repository wrapper/configuration and current runner documentation. Verify actual test discovery, target/module coverage, generated-bytecode/source mapping and language-plugin compatibility. Historical plugin support is not a current capability claim; no dependency addition follows from this reference.
