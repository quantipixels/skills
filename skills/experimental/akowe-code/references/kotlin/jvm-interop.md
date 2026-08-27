# Kotlin JVM interop and public ABI

Use when Kotlin crosses Java, reflection, serialization, framework, or binary compatibility boundaries.

<a id="kt-jvm-platform-types"></a>
## `kt-jvm-platform-types` — Resolve platform-type uncertainty at the edge

Convert Java platform types into precise Kotlin nullable/non-null contracts at one adapter boundary. Do not let uncertainty spread inward.

<a id="kt-jvm-defaults-overloads"></a>
## `kt-jvm-defaults-overloads` — Treat defaults and overloads as ABI choices

Default arguments are primarily a Kotlin source feature. Add `@JvmOverloads` or explicit overloads only when Java/framework callers actually need them.

<a id="kt-jvm-wildcards"></a>
## `kt-jvm-wildcards` — Control generic signatures intentionally

Use `@JvmSuppressWildcards`, `@JvmWildcard`, variance, and collection types only after checking the Java-facing signature. Do not optimize a Kotlin-only view while breaking Java consumers.

<a id="kt-jvm-reflection-serialization"></a>
## `kt-jvm-reflection-serialization` — Prove framework construction and serialization behavior

Constructor defaults, nullability, value classes, sealed hierarchies, reflection, and serializer modules can change runtime behavior. Test the actual framework/wire boundary rather than relying on source-level intuition.

<a id="kt-jvm-exceptions"></a>
## `kt-jvm-exceptions` — Preserve cross-language failure contracts

Kotlin has no checked-exception enforcement for callers. Use `@Throws` where Java/Objective-C interoperability requires a declared contract and avoid silently changing Java-facing failure semantics.

## Sources

- Kotlin Java interop: <https://kotlinlang.org/docs/java-to-kotlin-interop.html>
- Kotlin annotations / JVM interop: <https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/>
