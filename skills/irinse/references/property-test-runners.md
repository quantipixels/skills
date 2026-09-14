# Property-test runners

Use after `alaga` or the caller establishes a useful property and generator. Tool choice does not supply the oracle. Discover the repository's language, test engine, build and existing framework before suggesting another dependency.

For JVM projects, distinguish Maven from Gradle and jqwik from Jupiter/Kotest or other engines. jqwik uses the JUnit Platform; compiling a property class does not prove the engine discovered it. In Maven, inspect Surefire/Failsafe configuration, include patterns and reported property executions. Use the project wrapper and a named class first. Verify the selected framework version's current compatibility and license only when setup or upgrade is needed; do not pin a copied upstream version.

For Python, reuse Hypothesis when present; its saved examples, reproduction information and health checks help distinguish a counterexample from excessive filtering or a slow generator. For Rust, inspect existing proptest/quickcheck conventions and failure persistence. For Go, distinguish a property generator from native coverage-guided fuzzing: they select inputs differently, and neither creates an independent oracle. Do not introduce a framework when examples or an existing runner suffice.

Bound generated cases and runtime, confirm non-vacuous execution, and retain seed/reproduction data plus the smallest failing input. Do not silence framework health checks or disable deadlines globally merely to get green results. Treat shrinking or filtering failures separately from a falsified contract.

Official references: [jqwik guide](https://jqwik.net/docs/current/user-guide.html), [Hypothesis](https://hypothesis.readthedocs.io/), [proptest](https://proptest-rs.github.io/proptest/), [Go fuzzing](https://go.dev/doc/security/fuzz/). Consult the selected runner only; this is not a framework installation checklist.
