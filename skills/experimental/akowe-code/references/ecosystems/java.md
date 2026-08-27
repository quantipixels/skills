# Java guidance index

Research baseline: Java 17–26 guidance preserved from the former `akowe-java` experiment. The public Java skill is retired; this index routes Akọ̀wé Code into the detailed category references without loading the full catalogue.

Establish the repository's Java baseline first: toolchain, compiler `--release`, runtime image, library consumer baseline, preview/incubator flags, and framework constraints. Then open only categories controlling the touched code.

Priority meanings:

- `CRITICAL` — correctness, compatibility, safety, security, or public-contract guidance; satisfy it or establish a concrete exception.
- `HIGH` — strong expert default whose deviation needs candidate-specific benefit and proof.
- `MEDIUM` — contextual guidance; optimize for clarity and repository fit rather than mechanical compliance.

| Candidate mechanism | Priority | Detailed reference |
| --- | --- | --- |
| Java/JDK baseline, release flags, preview/incubator, deprecated-for-removal APIs | CRITICAL | [Version and platform baseline](../java/baseline.md) |
| Naming, visibility, comments, domain language | MEDIUM | [Naming, visibility, and communication](../java/naming.md) |
| Generics, variance, raw/unchecked types, value types | CRITICAL | [Types and generics](../java/types-generics.md) |
| Immutability, defensive copies, mutable exposure | CRITICAL | [Value semantics and immutability](../java/values-immutability.md) |
| Records, sealed types, exhaustive/pattern matching | HIGH | [Modern data modelling](../java/modern-data.md) |
| Public/internal API contracts, factories, boolean parameters | CRITICAL | [API design](../java/api-design.md) |
| Nullness annotations, Optional, platform/interoperability absence | CRITICAL | [Nullability and Optional](../java/nullability.md) |
| Equality, hashing, mutable keys, ordering, arrays | CRITICAL | [Equality, hashing, and ordering](../java/equality-ordering.md) |
| Exception contracts, causes, swallowing, interruption | CRITICAL | [Exceptions and failure contracts](../java/exceptions.md) |
| Collection boundaries, copies, enum collections, capacity | HIGH | [Collections](../java/collections.md) |
| Streams, collectors, ordering, side effects, parallelism | HIGH | [Streams, collectors, and pipelines](../java/streams.md) |
| Shared state, happens-before, executors, atomic compound actions | CRITICAL | [Concurrency and Java Memory Model](../java/concurrency.md) |
| Blocking I/O with virtual threads, task ownership, scoped values | HIGH | [Virtual threads and task concurrency](../java/virtual-threads.md) |
| Files, streams, charsets, HTTP clients, resource lifetime | CRITICAL | [Resources, files, HTTP, and I/O](../java/resources-io.md) |
| BigDecimal/exact arithmetic, java.time, controlled clocks | CRITICAL | [Numeric and time correctness](../java/numeric-time.md) |
| Profiling, complexity/data structures, allocation, caches | HIGH | [Performance and allocation](../java/performance.md) |
| Serialization, SQL, randomness, secrets, XML/input hardening | CRITICAL | [Security-sensitive coding](../java/security.md) |
| Stable behavioral proof, parameterization, time/randomness, real boundaries | HIGH | [Testing and proof](../java/testing.md) |
| Logging, metrics, correlation, exception ownership, JFR | MEDIUM | [Logging, metrics, and diagnostics](../java/observability.md) |
| Modules, dependencies, public/internal packaging, reproducibility | MEDIUM | [Modules, dependencies, and packaging](../java/modules-packaging.md) |
| Reflection, explicit wire formats, module encapsulation, FFM/JNI | MEDIUM | [Reflection, serialization, and native interop](../java/reflection-interop.md) |

Use rule headings as hypotheses, not a lint set. Apply only a rule whose trigger exists in the exact candidate and trace it to a concrete contract, failure mechanism, idiomatic/craft improvement, or proof seam.

Framework guidance may specialize Java behavior because of proxying, transactions, lifecycle, serialization, scheduling, or runtime ownership. It must not silently weaken Java correctness, cancellation, resource, security, or compatibility contracts.

Primary source families and freshness boundaries are recorded in [the Akọ̀wé Code source map](../source-map.md).
