# Virtual threads and task concurrency

**Priority:** HIGH  
**Rules:** 5

Virtual threads make thread-per-task blocking code scalable for waiting-heavy workloads. They do not remove downstream limits, CPU limits, or cancellation design.

Apply only the rules relevant to the candidate and its actual Java baseline. Repository and framework contracts take precedence when they deliberately specialize a rule.

<a id="vthread-blocking-io"></a>
## `vthread-blocking-io` — Use virtual threads for abundant blocking tasks

> Run independent I/O-bound tasks in one virtual thread per task instead of translating them into callback chains solely for scalability.

### Why it matters

Virtual threads retain ordinary stack traces, exceptions, and blocking APIs while using platform threads efficiently during waits.

### Avoid

Do not rewrite clear blocking code into `CompletableFuture` chains only to avoid platform-thread cost.

```java
CompletableFuture<User> user =
    CompletableFuture.supplyAsync(() -> client.loadUser(id));
```

### Prefer

Use framework support, `Thread.ofVirtual`, or `Executors.newVirtualThreadPerTaskExecutor` for task-oriented blocking work.

```java
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    Future<User> user = executor.submit(() -> client.loadUser(id));
    return user.get();
}
```

### Nuance

Confirm library blocking operations cooperate with the runtime and measure the end-to-end system.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JEP 444:** <https://openjdk.org/jeps/444>
- **Executors virtual-thread executor:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/Executors.html#newVirtualThreadPerTaskExecutor()>

<a id="vthread-dont-pool"></a>
## `vthread-dont-pool` — Do not pool virtual threads

> Create a fresh virtual thread per task; use semaphores or resource pools to constrain scarce dependencies.

### Why it matters

Virtual threads are cheap task containers, so pooling them reintroduces queueing and obscures the real constrained resource.

### Avoid

Avoid fixed-size virtual-thread pools.

```java
var pool = Executors.newFixedThreadPool(1000, Thread.ofVirtual().factory());
```

### Prefer

Use an unbounded-per-task virtual-thread executor and separately bound database connections, remote concurrency, or memory.

```java
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    return executor.submit(task).get();
}
```

### Nuance

Task admission can still require a bounded queue at the application boundary; that is not a virtual-thread pool.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JEP 444 implications:** <https://openjdk.org/jeps/444>
- **Thread.Builder.OfVirtual:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Thread.Builder.OfVirtual.html>

<a id="vthread-bound-external-resources"></a>
## `vthread-bound-external-resources` — Bound scarce resources, not threads

> Limit concurrent access to databases, APIs, files, memory, and rate-limited services even when threads are plentiful.

### Why it matters

Millions of tasks can still exhaust connection pools, heap, descriptors, and downstream capacity.

### Avoid

Do not treat virtual-thread count as the only concurrency control.

```java
for (URI uri : uris) {
    Thread.startVirtualThread(() -> download(uri));
}
```

### Prefer

Use semaphores, connection pools, backpressure, admission control, deadlines, and bulkheads around the actual resource.

```java
var permits = new Semaphore(32);
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    var tasks = new ArrayList<Future<Void>>(uris.size());
    for (URI uri : uris) {
        tasks.add(executor.submit(() -> {
            permits.acquire();
            try {
                download(uri);
                return null;
            } finally {
                permits.release();
            }
        }));
    }
    for (Future<Void> task : tasks) {
        task.get();
    }
}
```

### Nuance

The bound should reflect measured capacity and overload policy, not an arbitrary legacy thread-pool size.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JEP 444:** <https://openjdk.org/jeps/444>
- **Semaphore:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/Semaphore.html>

<a id="vthread-no-cpu-speedup"></a>
## `vthread-no-cpu-speedup` — Do not use virtual-thread count to accelerate CPU work

> Size CPU parallelism near available processors and use data-parallel/executor tools appropriate to the algorithm.

### Why it matters

Virtual threads do not create more CPU; oversubscription adds scheduling and memory overhead.

### Avoid

Avoid spawning one virtual thread per element for compute-bound transformations.

```java
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    return executor.invokeAll(cpuHeavyTasks);
}
```

### Prefer

Use sequential algorithms, ForkJoin/parallel streams after measurement, or a bounded platform-thread executor.

```java
try (var executor =
         Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors())) {
    return executor.invokeAll(cpuHeavyTasks);
}
```

### Nuance

Mixed tasks can use virtual threads while separately bounding CPU-heavy sections.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JEP 444 non-goals:** <https://openjdk.org/jeps/444>
- **ForkJoinPool:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ForkJoinPool.html>

<a id="vthread-scoped-values"></a>
## `vthread-scoped-values` — Prefer ScopedValue for bounded one-way context

> On Java 25+, use ScopedValue instead of mutable ThreadLocal when context is inherited read-only through a bounded call.

### Why it matters

Scoped values have lexical lifetime, cannot be mutated by callees, and avoid forgotten ThreadLocal cleanup across numerous virtual threads.

### Avoid

Avoid ThreadLocal as an implicit resource pool or unbounded request context.

```java
static final ThreadLocal<RequestContext> CONTEXT = new ThreadLocal<>();
CONTEXT.set(context);
try { handle(); } finally { CONTEXT.remove(); }
```

### Prefer

Pass parameters directly when practical; otherwise bind immutable context with ScopedValue for a defined dynamic scope.

```java
static final ScopedValue<RequestContext> CONTEXT = ScopedValue.newInstance();

ScopedValue.where(CONTEXT, context).run(Handler::handle);
```

### Nuance

ScopedValue does not replace mutable per-thread state and its values still require safe sharing.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **ScopedValue API:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/ScopedValue.html>
- **JEP 506:** <https://openjdk.org/jeps/506>
