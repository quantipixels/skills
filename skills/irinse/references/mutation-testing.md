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

## Maven / PIT and Kotlin

The official Maven entry point is `mvn test-compile org.pitest:pitest-maven:mutationCoverage`; prefer the repository wrapper and existing configuration. Verify selected-version options before use. Bound `targetClasses` and `targetTests`; class globs must account for intended nested classes. Request XML explicitly when machine-readable evidence is needed. Discover JUnit/TestNG integration rather than assuming Jupiter. Multi-module coverage and aggregation have restrictions; verify that the selected module really sees the covering tests.

Kotlin/JVM bytecode can be mutated, but source mapping and generated methods require care. PIT's built-in Kotlin filter is not comprehensive language support and is independent of the JUnit 5 plugin. The old open-source Kotlin plugin is archived; verify current official support, compatibility and licensing if setup is requested. Do not transplant Gradle configuration into Maven or silently exclude all generated methods. No dependency addition is required to consult this reference.

Sources: [PIT Maven](https://pitest.org/quickstart/maven/), [PIT FAQ](https://pitest.org/faq/), [archived Kotlin plugin](https://github.com/pitest/pitest-kotlin). Method informed by [JVM mutation-testing](https://github.com/jvm-skills/jvm-skills/tree/c6d477fb61d834f82d43e4fc3eec102dccf1e5d2/.claude/skills/mutation-testing) and [dotnet test-gap-analysis](https://github.com/dotnet/skills/tree/24f7cfbd42ad7bf52bcd67372816b982c38c64c6/plugins/dotnet-test/skills/test-gap-analysis); their default gates, bootstrap settings and automatic triage verdicts are not adopted.
