# Concurrency and the Java Memory Model

**Priority:** CRITICAL  
**Rules:** 5

Correct concurrent Java depends on ownership, happens-before relationships, cancellation, and lifecycle—not merely thread-safe collection classes.

Apply only the rules relevant to the candidate and its actual Java baseline. Repository and framework contracts take precedence when they deliberately specialize a rule.

<a id="conc-minimize-shared-mutable"></a>
## `conc-minimize-shared-mutable` — Prefer task ownership and message passing

> Keep mutable state confined to one thread/task/owner whenever practical.

### Why it matters

Every shared mutable variable requires a complete synchronization policy across all accesses and lifecycle transitions.

### Avoid

Avoid broad synchronized state bags accessed by unrelated operations.

```java
final class Counter {
    int value;
    void increment() { value++; }
}
```

### Prefer

Use immutable messages, local state, concurrent queues, actors/owners, or narrow synchronized components.

```java
final class Counter {
    private final AtomicLong value = new AtomicLong();
    void increment() { value.incrementAndGet(); }
}
```

### Nuance

Shared state can be appropriate; document the lock/atomic owner and invariants.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JLS threads and locks:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-17.html>
- **java.util.concurrent:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/package-summary.html>

<a id="conc-happens-before"></a>
## `conc-happens-before` — Establish a real happens-before edge

> Use locks, volatile fields, atomics, thread start/join, or concurrent utilities to publish and observe state safely.

### Why it matters

Without happens-before, another thread may see stale values or a partially initialized object.

### Avoid

Do not rely on timing, sleep, 'it was assigned first', or single-core behavior.

```java
boolean ready;
Data data;

// Writer
data = load();
ready = true;

// Reader may observe ready without initialized data.
```

### Prefer

Choose one synchronization mechanism that covers every access and prove safe publication.

```java
volatile boolean ready;
Data data;

data = load();
ready = true; // volatile write safely publishes prior writes
```

### Nuance

Final-field semantics help immutable construction but do not make referenced mutable objects thread-safe.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JLS happens-before:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-17.html#jls-17.4.5>
- **Concurrent package memory consistency:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/package-summary.html#MemoryVisibility>

<a id="conc-own-executors"></a>
## `conc-own-executors` — Give every executor a lifecycle owner

> Create, size, monitor, shut down, and reject work under one explicit owner.

### Why it matters

Unowned executors leak threads, hide backlogs, and make shutdown nondeterministic.

### Avoid

Avoid ad-hoc executor creation inside request methods or libraries that never close it.

```java
Response handle(Request request) {
    var pool = Executors.newFixedThreadPool(8);
    return pool.submit(() -> process(request)).get();
}
```

### Prefer

Inject/share an application-owned executor, use try-with-resources for per-scope executors where supported, and define rejection/shutdown behavior.

```java
final class RequestProcessor implements AutoCloseable {
    private final ExecutorService pool = Executors.newFixedThreadPool(8);

    Future<Response> handle(Request request) {
        return pool.submit(() -> process(request));
    }

    @Override
    public void close() {
        pool.shutdown();
        try {
            if (!pool.awaitTermination(5, TimeUnit.SECONDS)) {
                pool.shutdownNow();
            }
        } catch (InterruptedException interrupted) {
            pool.shutdownNow();
            Thread.currentThread().interrupt();
        }
    }
}
```

### Nuance

The common ForkJoinPool is shared infrastructure; do not block it with arbitrary I/O.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **ExecutorService:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ExecutorService.html>
- **ForkJoinPool:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ForkJoinPool.html>

<a id="conc-restore-interrupt"></a>
## `conc-restore-interrupt` — Preserve interruption as cancellation

> When catching InterruptedException, either propagate it or restore the thread's interrupt status before exiting/translation.

### Why it matters

Swallowing interruption defeats cooperative cancellation and can prevent orderly shutdown.

### Avoid

Avoid logging and continuing after `InterruptedException` without a documented policy.

```java
catch (InterruptedException e) {
    throw new ServiceException("interrupted");
}
```

### Prefer

`Thread.currentThread().interrupt()` when translating to another exception or return path; stop work promptly.

```java
catch (InterruptedException e) {
    Thread.currentThread().interrupt();
    throw new ServiceException("interrupted", e);
}
```

### Nuance

Code that owns the thread's interruption policy may consume it, but that decision belongs at a clear boundary.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Thread interruption:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Thread.html#interrupt()>
- **InterruptedException:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/InterruptedException.html>

<a id="conc-atomic-compound-actions"></a>
## `conc-atomic-compound-actions` — Make compound state transitions atomic

> A thread-safe variable or collection does not make check-then-act sequences atomic.

### Why it matters

Operations such as 'if absent then put' can interleave and violate uniqueness or initialization invariants.

### Avoid

Avoid `if (!map.containsKey(k)) map.put(k, value)` on shared maps.

```java
if (!cache.containsKey(key)) {
    cache.put(key, load(key));
}
```

### Prefer

Use `computeIfAbsent`, `putIfAbsent`, atomic update methods, or a lock that covers the whole invariant.

```java
return cache.computeIfAbsent(key, this::load);
```

### Nuance

Mapping functions must respect the concurrent collection's reentrancy and side-effect contract.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **ConcurrentMap:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ConcurrentMap.html>
- **AtomicReference:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/atomic/AtomicReference.html>
