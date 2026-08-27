# Logging, metrics, and diagnostics

**Priority:** MEDIUM  
**Rules:** 5

Observability should explain system state without changing it, leaking it, or duplicating the same failure across layers.

Apply only the rules relevant to the candidate and its actual Java baseline. Repository and framework contracts take precedence when they deliberately specialize a rule.

<a id="obs-project-logging-api"></a>
## `obs-project-logging-api` — Use the repository's logging abstraction consistently

> Follow the established logging facade/provider rather than mixing System.out, JUL, System.Logger, and other APIs.

### Why it matters

Mixed APIs fragment configuration, correlation, formatting, and test capture.

### Avoid

Avoid direct console prints in services and libraries except intentional CLI output.

```java
System.out.println("order failed " + orderId);
```

### Prefer

Use the project logger with appropriate level, structured context, and lazy/parameterized messages.

```java
log.warn("order processing failed orderId={}", orderId, failure);
```

### Nuance

Library code should avoid forcing an application logging backend.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **System.Logger:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/System.Logger.html>
- **SLF4J manual:** <https://www.slf4j.org/manual.html>

<a id="obs-parameterized-structured"></a>
## `obs-parameterized-structured` — Log stable structured fields

> Emit event name, identifiers, dimensions, and outcomes as fields rather than concatenated prose.

### Why it matters

Structured events are queryable and avoid unnecessary message construction when disabled.

### Avoid

Avoid string concatenation and dumping full objects/request bodies.

```java
log.info("processed " + count + " orders for " + tenant);
```

### Prefer

Use parameterized APIs and allowlisted values such as operation, entity ID, attempt, duration, and result.

```java
log.info("orders processed tenant={} count={} outcome={}",
    tenant, count, outcome);
```

### Nuance

High-cardinality fields can be appropriate in logs but harmful as metric labels.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **System.Logger:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/System.Logger.html>
- **JFR API:** <https://docs.oracle.com/en/java/javase/25/docs/api/jdk.jfr/jdk/jfr/package-summary.html>

<a id="obs-correlation-context"></a>
## `obs-correlation-context` — Propagate correlation context with bounded lifetime

> Carry request/trace identity through the execution path without mutable global state.

### Why it matters

Missing or leaked context makes multi-request logs ambiguous and can associate events with the wrong user/request.

### Avoid

Avoid static mutable context and ThreadLocal values that are not cleared.

```java
static String currentRequestId;
```

### Prefer

Use framework context propagation, explicit parameters, or ScopedValue on Java 25+ for bounded one-way context.

```java
ScopedValue.where(REQUEST_ID, requestId)
    .run(() -> handler.handle(request));
```

### Nuance

Correlation identifiers are not authorization and should not contain secrets.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **ScopedValue:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/ScopedValue.html>
- **JEP 444 thread locals:** <https://openjdk.org/jeps/444>

<a id="obs-log-exception-once"></a>
## `obs-log-exception-once` — Log a failure at the layer that owns its outcome

> Preserve exceptions through lower layers and log once where the operation is abandoned, retried, or translated to an external result.

### Why it matters

Logging at every catch produces duplicate noise and can expose data several times.

### Avoid

Avoid log-and-rethrow at each layer with no new decision.

```java
catch (IOException e) {
    log.error("read failed", e);
    throw new StorageException(e); // logged again above the boundary
}
```

### Prefer

Add context to the exception; log with stack trace at the terminal owner and measure retry/failure outcomes separately.

```java
catch (IOException e) {
    throw new StorageException("read " + path, e);
}
// The owning request/job boundary logs the abandoned operation once.
```

### Nuance

A lower layer may log a distinct local recovery event while still propagating another failure.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Throwable cause chain:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Throwable.html>
- **System.Logger:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/System.Logger.html>

<a id="obs-jfr-diagnostics"></a>
## `obs-jfr-diagnostics` — Use JFR and JDK tools for runtime evidence

> Capture allocation, GC, locks, threads, I/O, and custom events with Java Flight Recorder before inventing bespoke diagnostics.

### Why it matters

JFR integrates with the JVM and has low-overhead event semantics that ad-hoc logs often cannot reproduce.

### Avoid

Avoid enabling massive debug logging to diagnose contention or allocation blindly.

```java
// Add bespoke counters before observing JVM behavior.
AtomicLong allocationGuess = new AtomicLong();
```

### Prefer

Use JFR, `jcmd`, thread dumps, and focused custom JFR events tied to operational questions.

```java
try (Recording recording = new Recording()) {
    recording.enable("jdk.ObjectAllocationSample");
    recording.enable("jdk.JavaMonitorEnter");
    recording.start();
    runWorkload();
    recording.dump(output);
}
```

### Nuance

Define retention and privacy boundaries for recordings; they can contain sensitive metadata.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JFR guide:** <https://docs.oracle.com/en/java/javase/25/jfapi/>
- **jcmd:** <https://docs.oracle.com/en/java/javase/25/docs/specs/man/jcmd.html>
