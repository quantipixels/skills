# Performance and allocation

**Priority:** HIGH  
**Rules:** 5

Expert Java performance work begins with evidence and system shape. The JIT, GC, workload, and data distribution can overturn intuition.

Apply only the rules relevant to the candidate and its actual Java baseline. Repository and framework contracts take precedence when they deliberately specialize a rule.

<a id="perf-profile-before-tuning"></a>
## `perf-profile-before-tuning` — Profile representative workloads before optimizing

> Use JFR, profilers, metrics, and benchmarks to identify the limiting resource and hot path.

### Why it matters

Unmeasured optimization often targets cold code or trades one bottleneck for another.

### Avoid

Avoid performance claims based solely on micro-level intuition or one wall-clock run.

```java
// Hand-written fast path added before proving this code is hot.
String normalize(String value) {
    return manuallyNormalize(value);
}
```

### Prefer

Capture workload, warmup, allocation, contention, I/O, and percentile latency evidence before and after.

```java
// Record JFR/profile evidence, then optimize the measured hot path.
try (var recording = new Recording()) {
    recording.start();
    runWorkload();
}
```

### Nuance

Correctness and complexity improvements need not wait for profiling when the defect is already established.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JFR guide:** <https://docs.oracle.com/en/java/javase/25/jfapi/why-use-jfr-api.html>
- **JMH:** <https://github.com/openjdk/jmh>

<a id="perf-complexity-data-structure"></a>
## `perf-complexity-data-structure` — Fix algorithmic and data-structure cost first

> Choose lookup, ordering, queueing, and traversal structures from workload complexity.

### Why it matters

An O(n²) scan dominates small allocation and syntax choices as data grows.

### Avoid

Do not micro-optimize lambdas while repeatedly scanning lists for keyed lookups.

```java
for (Order order : orders) {
    if (allowedIds.contains(order.id())) { /* allowedIds is a List */ }
}
```

### Prefer

Use maps/sets/indexes, sorting, batching, or one-pass algorithms when they preserve the contract.

```java
Set<OrderId> allowedIds = Set.copyOf(ids);
for (Order order : orders) {
    if (allowedIds.contains(order.id())) { /* ... */ }
}
```

### Nuance

For tiny bounded data, a linear list can be simpler and faster; use realistic sizes.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Collections Framework:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/doc-files/coll-overview.html>
- **JMH:** <https://github.com/openjdk/jmh>

<a id="perf-primitive-specialization"></a>
## `perf-primitive-specialization` — Avoid boxing in measured numeric hot paths

> Use primitive arrays, primitive streams, and primitive functional interfaces when boxing is material.

### Why it matters

Boxing adds objects, indirection, cache pressure, and GC work.

### Avoid

Avoid `Stream<Integer>` or `Map<Integer, ...>` in a proven tight numeric kernel when a primitive representation fits.

```java
long total = values.stream()
    .map(Integer::longValue)
    .reduce(0L, Long::sum);
```

### Prefer

Use `IntStream`, `LongStream`, arrays, buffers, or a specialized library after measurement.

```java
long total = values.stream()
    .mapToLong(Integer::longValue)
    .sum();
```

### Nuance

Do not sacrifice API clarity for speculative boxing avoidance in ordinary business code.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Primitive streams:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/IntStream.html>
- **Primitive functional interfaces:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/package-summary.html>

<a id="perf-avoid-repeated-allocation"></a>
## `perf-avoid-repeated-allocation` — Remove repeated conversion and allocation in hot loops

> Hoist stable parsing, regex compilation, charset lookup, formatting, and temporary collection creation when evidence shows cost.

### Why it matters

Small per-element allocations multiply into GC pressure at scale.

### Avoid

Avoid compiling a Pattern, parsing the same URI, or rebuilding identical formatters for every item.

```java
for (String value : values) {
    if (Pattern.compile(expression).matcher(value).matches()) { /* ... */ }
}
```

### Prefer

Reuse immutable thread-safe helpers and precompute stable values within the correct lifecycle.

```java
Pattern pattern = Pattern.compile(expression);
for (String value : values) {
    if (pattern.matcher(value).matches()) { /* ... */ }
}
```

### Nuance

Do not cache mutable or context-sensitive objects without understanding thread safety and invalidation.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Pattern:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/regex/Pattern.html>
- **DateTimeFormatter:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/time/format/DateTimeFormatter.html>

<a id="perf-cache-bounded"></a>
## `perf-cache-bounded` — Every cache needs bounds and invalidation

> Define maximum size, expiry/refresh, key cardinality, failure behavior, and ownership before caching.

### Why it matters

An unbounded cache is a memory leak with delayed symptoms; stale values can be correctness defects.

### Avoid

Avoid `static ConcurrentHashMap` memoization for attacker- or data-controlled keys.

```java
private final Map<Key, Value> cache = new ConcurrentHashMap<>();
```

### Prefer

Use a maintained bounded cache or an owned map with explicit eviction, metrics, and invalidation.

```java
// Use the project's maintained bounded-cache implementation.
private final BoundedCache<Key, Value> cache = BoundedCache.create(
    10_000, Duration.ofMinutes(10));
```

### Nuance

Caching immutable finite metadata can be safely unbounded when the domain proves the bound.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **ConcurrentHashMap:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ConcurrentHashMap.html>
- **JFR memory analysis:** <https://docs.oracle.com/en/java/javase/25/jfapi/why-use-jfr-api.html>
