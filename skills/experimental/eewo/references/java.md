# Java and JVM guards

These guards target language/JDK failure modes rather than a prescribed application architecture. Framework-specific rules live in [Java framework guards](java-frameworks.md).

## Values, collections, and streams

### `java.optional.unproved-get` (`BLOCK`)

**Avoid:** `Optional.get()` when absence is not already proved by the same control flow.

**Why:** Empty values become `NoSuchElementException` without an explicit domain outcome.

**Prefer:** `map`/`flatMap`, `orElse`/`orElseGet`, an intentional `orElseThrow`, or a nearby presence check.

**Source:** [Java SE `Optional`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html).

### `java.stream.stateful-behavior` (`BLOCK`)

**Avoid:** Stream lambdas that mutate the source or depend on mutable state, especially in parallel pipelines.

**Why:** Stream behavioral parameters must be non-interfering and generally stateless; ordering and visibility may not hold.

**Prefer:** Reductions/collectors, immutable transformations, or an explicit imperative loop when side effects are the real operation.

**Sources:** [Stream package](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/package-summary.html), [`Stream`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html).

### `java.stream.business-effect-in-peek` (`BLOCK`)

**Avoid:** Required writes, metrics, mutation, or control flow inside `peek`.

**Why:** Implementations may elide traversal/intermediate operations; required behavior may never execute.

**Prefer:** A terminal operation with explicit semantics or a separate imperative step. Keep `peek` diagnostic-only.

**Source:** [`Stream.peek`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html#peek(java.util.function.Consumer)).

### `java.stream.reused-or-unclosed` (`BLOCK`)

**Avoid:** Reusing a stream after a terminal operation or leaving an I/O-backed stream such as `Files.lines` unclosed.

**Why:** Streams are single-use; I/O-backed streams retain resources.

**Prefer:** Build a new pipeline and use try-with-resources for closeable stream sources.

**Source:** [`Stream`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html).

### `java.map.mutable-key` (`BLOCK`)

**Avoid:** Mutating fields that participate in `equals`/`hashCode` while an object is a map key or set element.

**Why:** The entry can become unreachable in its bucket and collection invariants break.

**Prefer:** Immutable keys or remove–mutate–reinsert with an explicit contract.

**Source:** [`Map`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html).

## Concurrency and lifecycle

### `java.thread.stop-suspend-resume` (`BLOCK`)

**Avoid:** `Thread.stop`, `suspend`, `resume`, or equivalent asynchronous-kill/suspension designs.

**Why:** Historical asynchronous termination released monitors around inconsistent objects; current `stop()` is removed in practice and always throws.

**Prefer:** Cooperative cancellation, interruption, executor/task cancellation, or structured concurrency.

**Sources:** [`Thread.stop`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Thread.html#stop()), [thread primitive deprecation](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/doc-files/threadPrimitiveDeprecation.html).

### `java.thread.swallowed-interrupt` (`BLOCK`)

**Avoid:** Catching `InterruptedException` and continuing without either propagating cancellation or restoring the interrupt flag.

**Why:** Higher-level cancellation is lost and shutdown can hang.

**Prefer:** Propagate, return/abort, or call `Thread.currentThread().interrupt()` before translating the exception.

**Source:** [`Thread.interrupt`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Thread.html#interrupt()).

### `java.monitor.wait-without-condition-loop` (`BLOCK`)

**Avoid:** Calling `wait()` under a one-time `if` check.

**Why:** Spurious wakeups and competing consumers can invalidate the condition before the thread proceeds.

**Prefer:** Hold the monitor and test the condition in a loop; prefer higher-level concurrency utilities when available.

**Source:** [`Object.wait`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()).

### `java.monitor.value-based-lock` (`BLOCK`)

**Avoid:** Synchronizing on boxed primitives, `Optional`, `Double`, or another value-based object.

**Why:** Equal instances are interchangeable and identity may not be stable; future implementations may break synchronization assumptions.

**Prefer:** A dedicated private lock or a concurrency primitive.

**Sources:** [Value-based classes](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/doc-files/ValueBased.html), [`Double`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Double.html).

### `java.executor.unbounded-queue` (`BLOCK`)

**Avoid:** Using executors with unbounded queues for externally driven work without an admission limit.

**Why:** Producers can outrun workers and exhaust heap while latency grows invisibly.

**Prefer:** A bounded `ThreadPoolExecutor`, rejection/backpressure policy, or structured per-request limits.

**Source:** [`Executors.newFixedThreadPool`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/Executors.html#newFixedThreadPool(int)).

### `java.future.unobserved-failure` (`BLOCK`)

**Avoid:** Launching `Future`/`CompletableFuture` work whose exceptional completion is never joined, returned, or observed.

**Why:** Failure disappears while dependent work may assume completion.

**Prefer:** Return/compose the stage, `join`/`get` at the owner boundary, or attach explicit exceptional handling and telemetry.

**Sources:** [`Future`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/Future.html), [`CompletableFuture`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/CompletableFuture.html).

### `java.common-pool.blocking` (`WARN`)

**Avoid:** Long blocking I/O inside common-pool `CompletableFuture`/parallel-stream work without capacity analysis.

**Why:** Shared worker starvation can delay unrelated tasks.

**Prefer:** A bounded executor suited to blocking work or virtual threads where the workload and library stack support them.

**Source:** [`CompletableFuture`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/CompletableFuture.html).

## Resources, numbers, and security

### `java.resource.not-try-with-resources` (`BLOCK`)

**Avoid:** Manually closing `AutoCloseable` resources only on the success path.

**Why:** Exceptions bypass cleanup and scarce resources leak.

**Prefer:** Try-with-resources; preserve suppressed exceptions.

**Source:** [Java try-with-resources](https://dev.java/learn/exceptions/try-with-resources/).

### `java.numeric.bigdecimal-from-double` (`BLOCK`)

**Avoid:** `new BigDecimal(double)` when a human decimal value or exact monetary literal is intended.

**Why:** The constructor preserves the binary floating-point approximation, producing surprising decimal values.

**Prefer:** A decimal string, integer minor units, or `BigDecimal.valueOf(double)` when converting an existing double is unavoidable.

**Source:** [`BigDecimal(double)`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/math/BigDecimal.html#%3Cinit%3E(double)).

### `java.numeric.floating-money` (`BLOCK`)

**Avoid:** Binary floating-point for exact money, quota, or accounting invariants.

**Why:** Representation and rounding errors accumulate and equality/scale rules become ambiguous.

**Prefer:** Integer minor units or `BigDecimal` with an explicit scale and rounding mode.

**Sources:** [`BigDecimal`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/math/BigDecimal.html), [`RoundingMode`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/math/RoundingMode.html).

### `java.date.shared-simpledateformat` (`BLOCK`)

**Avoid:** Sharing one mutable `SimpleDateFormat` across threads.

**Why:** Date formats are not synchronized and concurrent use corrupts parsing/formatting state.

**Prefer:** Immutable/thread-safe `java.time` formatters or confined formatter instances.

**Source:** [`DateFormat` synchronization](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/text/DateFormat.html#synchronization).

### `java.cleanup.finalizer-dependence` (`BLOCK`)

**Avoid:** Depending on `finalize()` for security, resource release, or correctness.

**Why:** Finalization is deprecated for removal and execution is not timely or guaranteed.

**Prefer:** Explicit `AutoCloseable` lifecycle, try-with-resources, and `Cleaner` only for defensive backup where appropriate.

**Source:** [`Object.finalize`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()).

### `java.serialization.untrusted-native` (`BLOCK`)

**Avoid:** Deserializing untrusted native Java serialization streams without an explicit filter and trust boundary.

**Why:** Object graphs can instantiate unexpected classes, consume resources, and trigger gadget behavior.

**Prefer:** Safer data formats and allowlisted schemas; when native serialization is unavoidable, configure serialization filters and limits.

**Source:** [JDK serialization filtering](https://docs.oracle.com/en/java/javase/25/core/serialization-filtering1.html).

### `java.exception.catch-throwable` (`BLOCK`)

**Avoid:** Routine application code catching `Throwable`/`Error` or empty-catching broad exceptions.

**Why:** Fatal VM/linkage conditions and unrelated defects are hidden; the operation may continue in an invalid state.

**Prefer:** Catch the narrow recoverable type, preserve cause/context, and let fatal conditions propagate unless at a true process boundary.

**Source:** [`Throwable`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Throwable.html).
