# Java

Research baseline: Java 17–26 guidance distilled from the former `akowe-java` experiment. Recheck volatile release/support facts after 2026-08-27.

Use only items relevant to the candidate.

- Detect `--release`, toolchain, runtime image, consumer baseline, preview/incubator flags, and framework constraints before using newer APIs or syntax.
- Prefer immutable/value-oriented models; use records for true value carriers and sealed hierarchies when they make a closed state space explicit.
- Keep generics precise: no raw types; isolate unavoidable unchecked casts; use variance from actual producer/consumer contracts rather than wildcard-heavy APIs.
- Make nullability explicit. Use project nullness annotations/JSpecify when established; use `Optional` primarily at return boundaries, not as a field/parameter fashion.
- Keep `equals`/`hashCode` stable and consistent; never put mutable equality keys into hashed collections.
- Prefer specific failure contracts, preserve causes, do not swallow exceptions/cancellation, and do not catch `Error` for ordinary recovery.
- Use collections/streams when they express intent clearly; avoid side-effectful or automatically parallel streams. Imperative loops are better when ordering/state/failure becomes clearer.
- Minimize shared mutable state. Make happens-before/atomicity real rather than assuming thread-safe containers make compound actions safe.
- Virtual threads suit many blocking I/O tasks; do not pool them, do not expect CPU speedups, and still bound scarce downstream resources.
- Own `ExecutorService`, `HttpClient`, files, streams, and other resources explicitly; use try-with-resources where the API is closeable and configure finite remote timeouts.
- Use `BigDecimal`/exact arithmetic and `java.time` according to domain precision; inject/control time when behavior depends on the clock.
- Prefer standard JDK APIs and measure before performance tuning. Avoid JDK internals and unbounded caches/allocation hot paths.
- Keep security-sensitive parsing/serialization explicit: parameterized SQL, secure randomness, bounded input, hardened XML, no native Java serialization for untrusted data.
- Let tests prove behavior/contracts at stable seams; deterministic time/randomness and real provider/database integration matter when semantics depend on them.

Primary sources:

- Java SE docs: <https://docs.oracle.com/en/java/javase/>
- OpenJDK JEP index: <https://openjdk.org/jeps/0>
- Dev.java: <https://dev.java/>
