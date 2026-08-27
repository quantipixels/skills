# Kotlin baseline and type modeling

**Research baseline:** Kotlin 2.4 line at the 2026-08-27 cutoff. Preserve the repository's language/API/JVM/KMP baseline and framework constraints.

Apply only rules whose trigger exists in the candidate.

<a id="kt-base-platform"></a>
## `kt-base-platform` — Pin the actual Kotlin/platform baseline

Use the project language/API version, compiler plugins, JVM target, KMP targets, and framework-managed versions as authority. A newer local compiler does not authorize newer language/API behavior.

<a id="kt-base-nullability"></a>
## `kt-base-nullability` — Model absence in types

Keep nullable values explicit and resolve uncertain Java/platform types at the interop boundary. Avoid spreading `!!`, platform-type ambiguity, or nullable wrappers through internal APIs.

<a id="kt-base-closed-state"></a>
## `kt-base-closed-state` — Make closed state spaces explicit

Use sealed classes/interfaces or enums when lifecycle/domain states are mutually exclusive and known. Prefer one state model over parallel booleans/nullables that permit impossible combinations.

<a id="kt-base-value-shape"></a>
## `kt-base-value-shape` — Use data/value classes only where their semantics fit

Data classes suit value/data carriers; value classes suit narrow domain wrappers when boxing, reflection, serialization, and framework boundaries are understood. Do not use generated equality/copy semantics blindly for identity-bearing mutable entities.

## Sources

- Kotlin releases: <https://kotlinlang.org/docs/releases.html>
- Kotlin classes/data classes/sealed classes/value classes: <https://kotlinlang.org/docs/classes.html>
