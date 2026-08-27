# Streams, collectors, and pipelines

**Priority:** HIGH  
**Rules:** 5

Streams are strongest when a pipeline describes a result. They are not a universal replacement for loops or a permission to hide side effects.

Apply only the rules relevant to the candidate and its actual Java baseline. Repository and framework contracts take precedence when they deliberately specialize a rule.

<a id="stream-use-intent-terminal"></a>
## `stream-use-intent-terminal` — Use terminals that state the question

> Choose `anyMatch`, `findFirst`, `min`, `count`, `joining`, or a collector instead of materializing and re-inspecting.

### Why it matters

Intent-specific terminals can short-circuit and preserve semantics more directly.

### Avoid

Avoid `collect(toList()).isEmpty()`, sorting before `min`, or counting only to test existence.

```java
boolean any = users.stream()
    .filter(User::active)
    .toList()
    .size() > 0;
```

### Prefer

Match the terminal to the result and preserve encounter-order semantics.

```java
boolean any = users.stream().anyMatch(User::active);
```

### Nuance

A materialized collection is correct when the caller actually needs the collection.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Stream API:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html>
- **Java Streams skill corpus:** <https://github.com/martinfrancois/java-streams-skill>

<a id="stream-no-side-effects"></a>
## `stream-no-side-effects` — Keep stream operations non-interfering

> Do not mutate shared/external state from `map`, `filter`, `peek`, or `forEach` to produce the result.

### Why it matters

Stream implementations may reorder, elide, or parallelize behavioral parameters; side effects weaken reasoning and safety.

### Avoid

Avoid adding to an external list or incrementing shared counters inside a pipeline.

```java
var names = new ArrayList<String>();
users.stream()
    .filter(User::active)
    .forEach(user -> names.add(user.name()));
```

### Prefer

Use collectors, reductions, immutable transformations, or an explicit loop when the operation is inherently effectful.

```java
List<String> names = users.stream()
    .filter(User::active)
    .map(User::name)
    .toList();
```

### Nuance

A terminal `forEach` can be appropriate at an output boundary when ordering and failure behavior are deliberate.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Stream package side effects:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/package-summary.html#SideEffects>
- **Collector:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Collector.html>

<a id="stream-preserve-order"></a>
## `stream-preserve-order` — Preserve encounter order only when it is part of the result

> Use `findFirst`, ordered collectors, and stable operations when order selects the winner; use unordered alternatives only when values are equivalent.

### Why it matters

Changing `findFirst` to `findAny` or dropping ordering can silently change business behavior.

### Avoid

Do not label order removal as a performance optimization without proving equivalence.

```java
Order selected = orders.parallelStream()
    .filter(Order::eligible)
    .findAny()
    .orElseThrow();
```

### Prefer

State whether order matters and choose terminals/collectors accordingly.

```java
Order selected = orders.stream()
    .filter(Order::eligible)
    .findFirst()
    .orElseThrow();
```

### Nuance

Calling `unordered()` can unlock optimization for truly order-independent parallel pipelines.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Stream ordering:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/package-summary.html#Ordering>
- **findFirst/findAny:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html>

<a id="stream-parallel-only-measured"></a>
## `stream-parallel-only-measured` — Use parallel streams only with a measured workload contract

> Parallelize only splittable, CPU-bound, side-effect-free work large enough to exceed coordination cost.

### Why it matters

Parallel streams use shared runtime resources, can increase latency, and are poor fits for blocking I/O or small collections.

### Avoid

Avoid adding `parallelStream()` as a generic speed fix or inside shared server request paths without benchmarks.

```java
return requests.parallelStream()
    .map(client::callRemoteService)
    .toList();
```

### Prefer

Benchmark realistic data, confirm associative operations and thread safety, and consider explicit executors for owned concurrency.

```java
// Keep blocking I/O under an owned concurrency policy.
List<Future<Result>> futures = executor.invokeAll(tasks);
var results = new ArrayList<Result>(futures.size());
for (Future<Result> future : futures) {
    results.add(future.get());
}
return List.copyOf(results);
```

### Nuance

Virtual threads solve blocking-concurrency scale, not CPU data parallelism.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Stream parallelism:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/package-summary.html#Parallelism>
- **JEP 444 non-goals:** <https://openjdk.org/jeps/444>

<a id="stream-imperative-when-clearer"></a>
## `stream-imperative-when-clearer` — Use a loop when stateful control flow is the clearer model

> Prefer imperative code for complex early exits, checked I/O, mutation-heavy algorithms, or several dependent states.

### Why it matters

A pipeline with nested lambdas, mutable holders, or exception wrappers is harder to verify than direct control flow.

### Avoid

Do not force every loop into a stream or introduce custom collectors to conceal a simple state machine.

```java
return inputs.stream()
    .map(this::parse)
    .filter(Optional::isPresent)
    .map(Optional::get)
    .peek(this::audit)
    .takeWhile(this::withinBudget)
    .toList();
```

### Prefer

Use streams for transformations and aggregation; use loops for explicit stateful algorithms.

```java
var results = new ArrayList<Result>();
for (var input : inputs) {
    var parsed = parse(input);
    if (parsed.isEmpty()) break;

    Result result = parsed.get();
    if (!withinBudget(result)) break;

    audit(result);
    results.add(result);
}
return List.copyOf(results);
```

### Nuance

Java 24 Gatherers can express some stateful intermediate operations, but only use them when the project baseline and readability justify it.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Gatherer API:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Gatherer.html>
- **Stream API:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html>
