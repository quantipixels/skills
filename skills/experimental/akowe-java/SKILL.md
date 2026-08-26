---
name: akowe-java
description: Encode expert Java 17–26 language and JDK practice for implementation, review, refactoring, and API design. Use when Java source changes need baseline-aware guidance on types, APIs, nullability, collections, streams, concurrency, virtual threads, exceptions, resources, security, testing, observability, performance, modules, or interop. Framework-neutral; preserve repository/framework contracts and do not own implementation or final review verdicts.
license: MIT
disable-model-invocation: true
metadata:
  version: "1.0.0"
  rules: 105
  categories: 21
  researched: "2026-08-26"
  java:
    minimum-guidance: "17"
    current-lts: "25"
    current-feature: "26"
---

# Akọ̀wé Java

Encode what expert modern Java looks like: explicit contracts, strong value semantics, baseline-aware API choices, controlled concurrency, observable failure, and proof proportionate to risk.

This is an experimental lightweight knowledge skill. It must be selected explicitly while its rule coverage, retrieval shape, and interaction with project/framework conventions are evaluated. It does not prescribe one architecture, framework, build tool, testing library, or application shape. It supplies focused Java language and JDK judgment to the owner already implementing or reviewing the candidate.

## Apply the baseline before the advice

1. Read the repository's Java toolchain, compiler `--release`, CI/runtime image, library consumer baseline, enabled preview/incubator flags, and framework constraints.
2. Treat the project baseline as authoritative. Java 25 is the current LTS and Java 26 is the current feature release at this skill revision; neither fact authorizes newer syntax or APIs in an older project.
3. Do not introduce preview or incubator features unless the repository explicitly accepts their flags, runtime coupling, and migration risk.
4. Preserve established framework and repository conventions when they deliberately specialize a language-level rule. Challenge them only with concrete evidence, not fashion.

## Load only what the candidate needs

`SKILL.md` is the navigation layer. Each reference contains five cohesive rules; open only the categories relevant to the code in front of you, then use only the matching rule headings.

- Writing or refactoring: inspect the touched types, APIs, state, failure paths, concurrency model, I/O, and proof boundary; load the categories that control those choices.
- Reviewing: treat rule names as hypotheses. Trace the actual candidate to a caller-visible or operational consequence before reporting a defect.
- Upgrading Java: start with [Version and platform baseline](references/baseline.md), then load categories for the APIs or language features being changed.
- Framework work: apply these language/JDK rules underneath the owning Spring, Jakarta, persistence, build, or platform contract. This skill does not invent framework policy.

Category priorities mean:

- `CRITICAL` — correctness, compatibility, safety, security, or public-contract guidance; satisfy it or establish a concrete exception.
- `HIGH` — strong expert default whose deviation needs candidate-specific benefit and proof.
- `MEDIUM` — contextual default; optimize for clarity and repository fit rather than mechanical compliance.

## Category index

| Category | Priority | Rule IDs |
| --- | --- | --- |
| [Version and platform baseline](references/baseline.md) | CRITICAL | `base-detect-java-version`, `base-no-preview-by-default`, `base-use-release`, `base-prefer-standard-library`, `base-remove-deprecated-for-removal` |
| [Naming, visibility, and communication](references/naming.md) | MEDIUM | `name-domain-language`, `name-no-meaningless-suffixes`, `name-least-visibility`, `name-var-when-obvious`, `name-comments-explain-contract` |
| [Types and generics](references/types-generics.md) | CRITICAL | `type-no-raw-types`, `type-pecs`, `type-no-wildcard-return`, `type-isolate-unchecked-casts`, `type-domain-value-objects` |
| [Value semantics and immutability](references/values-immutability.md) | CRITICAL | `value-immutable-default`, `value-defensive-copy`, `value-unmodifiable-not-immutable`, `value-builder-for-complex-construction`, `value-no-expose-mutable-state` |
| [Records, sealed types, and pattern matching](references/modern-data.md) | HIGH | `modern-records-for-values`, `modern-record-validate`, `modern-sealed-hierarchies`, `modern-exhaustive-switch`, `modern-pattern-matching` |
| [API design](references/api-design.md) | CRITICAL | `api-contract-first`, `api-least-capability`, `api-empty-collections-not-null`, `api-static-factories`, `api-avoid-boolean-parameters` |
| [Nullability and Optional](references/nullability.md) | CRITICAL | `null-explicit-model`, `null-jspecify`, `null-optional-return`, `null-no-optional-get`, `null-lazy-fallback` |
| [Equality, hashing, and ordering](references/equality-ordering.md) | CRITICAL | `eq-equals-hashcode`, `eq-symmetry-inheritance`, `eq-no-mutable-keys`, `eq-comparator-consistency`, `eq-array-content` |
| [Exceptions and failure contracts](references/exceptions.md) | CRITICAL | `err-specific-contract`, `err-preserve-cause`, `err-no-swallow`, `err-no-catch-error`, `err-no-exception-control-flow` |
| [Collections](references/collections.md) | HIGH | `coll-program-to-interface`, `coll-immutable-boundaries`, `coll-copy-on-store-return`, `coll-enumset-enummap`, `coll-size-capacity` |
| [Streams, collectors, and pipelines](references/streams.md) | HIGH | `stream-use-intent-terminal`, `stream-no-side-effects`, `stream-preserve-order`, `stream-parallel-only-measured`, `stream-imperative-when-clearer` |
| [Concurrency and the Java Memory Model](references/concurrency.md) | CRITICAL | `conc-minimize-shared-mutable`, `conc-happens-before`, `conc-own-executors`, `conc-restore-interrupt`, `conc-atomic-compound-actions` |
| [Virtual threads and task concurrency](references/virtual-threads.md) | HIGH | `vthread-blocking-io`, `vthread-dont-pool`, `vthread-bound-external-resources`, `vthread-no-cpu-speedup`, `vthread-scoped-values` |
| [Resources, files, HTTP, and I/O](references/resources-io.md) | CRITICAL | `io-try-with-resources`, `io-path-files`, `io-explicit-charset`, `io-bound-memory`, `io-httpclient-reuse-timeouts` |
| [Numeric and time correctness](references/numeric-time.md) | CRITICAL | `num-bigdecimal-string`, `num-bigdecimal-equality`, `num-exact-arithmetic`, `time-java-time`, `time-clock-injection` |
| [Performance and allocation](references/performance.md) | HIGH | `perf-profile-before-tuning`, `perf-complexity-data-structure`, `perf-primitive-specialization`, `perf-avoid-repeated-allocation`, `perf-cache-bounded` |
| [Security-sensitive coding](references/security.md) | CRITICAL | `sec-no-native-serialization-untrusted`, `sec-parameterized-sql`, `sec-secure-random`, `sec-secret-redaction`, `sec-xml-external-entities` |
| [Testing and proof](references/testing.md) | HIGH | `test-behavior-contract`, `test-boundary-parameterized`, `test-deterministic-time-random`, `test-no-sleep`, `test-real-boundary-integration` |
| [Logging, metrics, and diagnostics](references/observability.md) | MEDIUM | `obs-project-logging-api`, `obs-parameterized-structured`, `obs-correlation-context`, `obs-log-exception-once`, `obs-jfr-diagnostics` |
| [Modules, dependencies, and packaging](references/modules-packaging.md) | MEDIUM | `mod-release-flag`, `mod-public-internal-boundary`, `mod-no-split-packages`, `mod-minimize-dependencies`, `mod-reproducible-build` |
| [Reflection, serialization, and native interop](references/reflection-interop.md) | MEDIUM | `reflect-prefer-language-apis`, `reflect-respect-module-encapsulation`, `serial-explicit-wire-format`, `interop-no-jdk-internals`, `interop-ffm-over-jni` |

## Working contract

For each applicable rule:

```text
candidate construct
→ relevant rule and project baseline
→ contract or failure mechanism
→ smallest fitting Java/JDK design
→ compiler, test, static-analysis, or runtime proof
```

Prefer the simplest solution that preserves the requested behavior and established contracts. Do not rewrite functioning code merely to display a newer language feature. Do not turn contextual guidance into a universal lint.

When this skill supports another owner:

- `alaga` owns implementation, integration, tests, and handoff.
- `atunwo` owns code-review discovery, finding validation, and verdict.
- `pare` owns maintainability-only simplification review.
- `solution-architect` owns architecture.
- `irinse` owns setup and operation of Error Prone, NullAway, SpotBugs, ArchUnit, JFR tools, or other companion tooling.
- `ko-skill` owns changes to this published skill.

Return the rules applied, assumptions about the Java baseline, material exceptions, and proof performed. State coverage limits when the task also depends on framework, database, distributed-system, native, or deployment semantics outside this skill.

## Maintenance

The rules are an original synthesis of Java SE/JDK specifications, OpenJDK JEPs, official API documentation, maintained tool documentation, and selected community Java skill corpora. Read [authoring and maintenance](references/authoring.md) before changing the rule set and [source map](references/source-map.md) when auditing provenance or freshness.
