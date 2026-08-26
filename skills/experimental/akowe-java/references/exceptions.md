# Exceptions and failure contracts

**Priority:** CRITICAL  
**Rules:** 5

Exceptions are part of the API. Expert code preserves causality, distinguishes recoverability, and avoids turning expected control flow into stack unwinding.

Apply only the rules relevant to the candidate and its actual Java baseline. Repository and framework contracts take precedence when they deliberately specialize a rule.

<a id="err-specific-contract"></a>
## `err-specific-contract` — Throw the most specific meaningful exception

> Choose an exception whose type and message tell the caller what failed and what action is possible.

### Why it matters

Generic `Exception` or `RuntimeException` forces callers to parse text or catch unrelated failures.

### Avoid

Do not declare `throws Exception` or throw raw runtime exceptions for distinct domain failures.

```java
throw new RuntimeException("failed");
```

### Prefer

Reuse suitable JDK exceptions for preconditions/state and define domain exceptions when callers need the distinction.

```java
throw new OrderNotFoundException(orderId);
```

### Nuance

Do not create a new exception class for every line; types should represent actionable failure categories.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Java exceptions tutorial:** <https://dev.java/learn/exceptions/>
- **RuntimeException:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/RuntimeException.html>

<a id="err-preserve-cause"></a>
## `err-preserve-cause` — Preserve the causal chain when translating failures

> Pass the original throwable as the cause and add boundary-relevant context.

### Why it matters

Dropping the cause destroys the evidence needed to diagnose the actual failure.

### Avoid

Avoid `throw new DomainException(e.getMessage())` and logging then throwing a new unrelated exception.

```java
catch (IOException e) {
    throw new ConfigException("cannot load config");
}
```

### Prefer

Use `new DomainException("operation and stable context", e)` and let one owner log the terminal failure.

```java
catch (IOException e) {
    throw new ConfigException("cannot load " + path, e);
}
```

### Nuance

Messages must not expose secrets or unbounded data.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Throwable causes:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Throwable.html>
- **Secure coding guidelines:** <https://www.oracle.com/java/technologies/javase/seccodeguide.html>

<a id="err-no-swallow"></a>
## `err-no-swallow` — Never convert failure into silent success

> Handle, propagate, aggregate, or deliberately observe every caught failure.

### Why it matters

Empty catches and default returns conceal partial state and make downstream behavior misleading.

### Avoid

Avoid `catch (Exception ignored) {}` and fallback values that are indistinguishable from success.

```java
try {
    publish(event);
} catch (Exception ignored) {
}
```

### Prefer

Catch narrowly, restore invariants, attach context, record allowed best-effort loss, or rethrow.

```java
try {
    publish(event);
} catch (PublishException e) {
    metrics.increment("event.publish.failed");
    throw e;
}
```

### Nuance

Best-effort cleanup may suppress secondary failures; use suppressed exceptions or explicit telemetry.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Throwable suppressed exceptions:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Throwable.html#getSuppressed()>
- **Try-with-resources:** <https://dev.java/learn/exceptions/try-with-resources/>

<a id="err-no-catch-error"></a>
## `err-no-catch-error` — Do not catch Error or Throwable in ordinary code

> Let VM, linkage, and resource-failure errors propagate unless an outermost isolation boundary has a precise policy.

### Why it matters

Catching `OutOfMemoryError`, `StackOverflowError`, or linkage errors can continue execution in an invalid process state.

### Avoid

Avoid `catch (Throwable t)` around business logic, worker loops, or retries.

```java
try {
    runTask();
} catch (Throwable failure) {
    return TaskResult.failed(failure);
}
```

### Prefer

Catch expected exception types; reserve broad outer-boundary catches for reporting/isolation before termination or task failure.

```java
try {
    runTask();
} catch (TaskException failure) {
    return TaskResult.failed(failure);
}
```

### Nuance

Testing frameworks and containers may catch Throwable as infrastructure; application code should not imitate that casually.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Error:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Error.html>
- **Throwable:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Throwable.html>

<a id="err-no-exception-control-flow"></a>
## `err-no-exception-control-flow` — Do not use exceptions for expected branching

> Represent frequent, normal alternatives with types, conditions, or results.

### Why it matters

Exception control flow obscures intent, allocates stack traces, and conflates expected absence with faults.

### Avoid

Avoid parsing by repeatedly throwing, or using `IndexOutOfBoundsException` to terminate normal loops.

```java
try {
    return values.get(index);
} catch (IndexOutOfBoundsException e) {
    return fallback;
}
```

### Prefer

Validate/select before the operation, return Optional/result types where appropriate, or use APIs that expose the alternative.

```java
return index >= 0 && index < values.size()
    ? values.get(index)
    : fallback;
```

### Nuance

Parsing APIs often use exceptions by contract; translate at the boundary rather than pre-validating with a weaker duplicate parser.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Java exceptions tutorial:** <https://dev.java/learn/exceptions/>
- **Optional:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html>
