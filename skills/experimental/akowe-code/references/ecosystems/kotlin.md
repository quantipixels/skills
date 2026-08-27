# Kotlin

Research baseline: Kotlin 2.4 line; Kotlin 2.4.10 was the latest bug-fix release at the 2026-08-27 cutoff. Preserve the repository's language/API/JVM/KMP and framework baseline.

Load only categories controlling the touched mechanism:

| Category | Use for |
| --- | --- |
| [Baseline and type modeling](../kotlin/baseline-types.md) | language/platform baseline, nullability, sealed/data/value modeling |
| [Coroutines and lifecycle](../kotlin/coroutines-lifecycle.md) | scopes, cancellation, dispatchers, supervision, blocking boundaries |
| [Flow and shared state](../kotlin/flow-state.md) | Flow, StateFlow/SharedFlow, hot/cold streams, buffering, collectors |
| [JVM interop and public ABI](../kotlin/jvm-interop.md) | Java platform types, defaults/overloads, wildcards, reflection/serialization, failures |
| [Multiplatform and testing](../kotlin/multiplatform-testing.md) | common/platform boundaries, expect/actual, coroutine/lifecycle/framework proof |

Framework guidance may specialize Kotlin behavior at proxy, serialization, persistence, request, or lifecycle boundaries, but must not weaken cancellation, type safety, resource ownership, or caller contracts.

Primary sources: <https://kotlinlang.org/docs/releases.html>, <https://kotlinlang.org/docs/coroutines-guide.html>, <https://kotlinlang.org/docs/java-to-kotlin-interop.html>, <https://kotlinlang.org/docs/multiplatform.html>.
