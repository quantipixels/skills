# Kotlin

Research baseline: Kotlin 2.4 line; Kotlin 2.4.10 was the latest bug-fix release at the 2026-08-27 cutoff. Preserve the repository's language/API/JVM/KMP baseline.

- Model nullability in types; isolate Java platform-type uncertainty at interop boundaries instead of spreading `!!` or nullable ambiguity.
- Prefer data classes for immutable value/data carriers, not automatically for mutable identity-bearing framework entities.
- Use sealed classes/interfaces and exhaustive `when` when the domain has a closed state model; avoid parallel booleans/nullables for lifecycle states.
- Use value classes only where boxing/reflection/serialization/framework boundaries are understood and proven.
- Keep extension functions close to the concept they clarify; do not use extensions to hide ownership or make unrelated APIs look native.
- Use scope functions (`let`, `run`, `apply`, `also`, `with`) when receiver/result semantics are obvious; avoid nested chains that obscure control flow or null handling.
- Prefer collection operations for clear transformations and sequences only when laziness materially helps; do not add lazy layers to small bounded collections by default.
- Structured concurrency owns coroutine lifetime. Avoid `GlobalScope`, orphaned scopes, and detached work without a lifecycle owner.
- Propagate cancellation; do not catch `CancellationException` as a normal failure. Use `withContext` for dispatcher boundaries, not as a generic wrapper.
- Synchronize shared state deliberately. `StateFlow`/`SharedFlow` are state/event primitives with distinct replay/ownership semantics; do not treat them as interchangeable event buses.
- Prefer `Flow` for asynchronous streams when the consumer benefits from suspension/cancellation/backpressure semantics; do not wrap every collection/result in Flow.
- Keep Java interop intentional: SAMs, checked exceptions, wildcards, nullability annotations, default arguments, `@Jvm*` annotations, and reflection can change the public ABI.
- For KMP, keep common code free of platform APIs unless behind a real `expect`/`actual` or interface boundary; do not create multiplatform abstractions for one platform without need.
- Prefer deterministic coroutine tests with test dispatchers/schedulers and explicit cancellation/time advancement rather than sleeps.

Primary sources:

- Kotlin releases: <https://kotlinlang.org/docs/releases.html>
- Kotlin coroutines guide: <https://kotlinlang.org/docs/coroutines-guide.html>
- Kotlin/JVM interop: <https://kotlinlang.org/docs/java-to-kotlin-interop.html>
