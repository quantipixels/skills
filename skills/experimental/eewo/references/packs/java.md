# Java starter guard pack

These are high-confidence seeds, not a general Java architecture manual.

## `java.optional.unproved-get`

- Kind: advisory
- Applies: `java.util.Optional` where absence is possible.
- Invariant: absence must have explicit domain/control-flow semantics.
- Do not: use `Optional.get()` as an implicit assertion that a value exists.
- Failure mechanism: `get()` throws `NoSuchElementException` when empty; the JDK API explicitly prefers `orElseThrow()` when an exception is intended.
- Safe paths: `map`/`flatMap`, `orElse`/`orElseGet`, explicit `orElseThrow`, or a locally proven presence check where that control flow is clearer.
- Source: Java SE 25 `Optional` API documentation.

## `java.stream.stateful-side-effects`

- Kind: prohibition
- Applies: Java Stream behavioral parameters, especially parallel streams.
- Invariant: stream results must not depend on mutable side effects whose ordering, visibility, or invocation is unspecified.
- Do not: mutate shared accumulators or encode required behavior in `map`, `filter`, `peek`, or similar side effects.
- Failure mechanism: the JDK gives limited guarantees for side-effect visibility, thread affinity, invocation, and ordering; parallel execution can make mutable accumulators incorrect.
- Safe paths: reductions, collectors, `toList`, or an explicit imperative loop when side effects are the real operation.
- Source: Java SE 25 `java.util.stream` package documentation.

## `java.thread.stop`

- Kind: prohibition
- Applies: Java thread cancellation.
- Invariant: cancellation must not expose objects after asynchronous termination breaks protected invariants.
- Do not: use `Thread.stop()` or recreate its asynchronous-kill semantics.
- Failure mechanism: the JDK documents `Thread.stop()` as inherently unsafe because monitors can be released while protected objects are inconsistent; the method is deprecated for removal.
- Safe paths: cooperative cancellation with state/interrupts or the structured cancellation mechanism appropriate to the executor/task abstraction.
- Source: Java SE 25 `Thread` API and thread primitive deprecation documentation.

## Mining note

Use `jvmskills.com` to discover focused JVM failure domains such as Hibernate/JPA, Spring, jOOQ, Gradle, testing, and migration. Validate proposed rules against the owning project/vendor documentation before activation.
