# Nullability and Optional

**Priority:** CRITICAL  
**Rules:** 5

Null is part of the API whether documented or not. Expert Java makes absence explicit and keeps Optional focused on return-value composition.

Apply only the rules relevant to the candidate and its actual Java baseline. Repository and framework contracts take precedence when they deliberately specialize a rule.

<a id="null-explicit-model"></a>
## `null-explicit-model` — Choose one absence representation per boundary

> Decide whether absence is impossible, nullable, optional, empty, or an error, and encode that decision consistently.

### Why it matters

Mixed conventions force callers to guess whether null, empty, or an exception is possible.

### Avoid

Do not return `null` from one implementation and `Optional.empty()` from another under the same contract.

```java
User findUser(UserId id) {
    return null; // Is absence normal, invalid, or an error?
}
```

### Prefer

Use annotations and types to state the boundary; validate non-null preconditions early.

```java
Optional<User> findUser(UserId id) {
    return repository.find(id);
}
```

### Nuance

Interop with legacy or framework APIs may require nullable adapters; contain the translation.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Objects.requireNonNull:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Objects.html#requireNonNull(T)>
- **JSpecify:** <https://jspecify.dev/>

<a id="null-jspecify"></a>
## `null-jspecify` — Use a nullness model that tools can check

> Adopt package/module defaults and explicit exceptions rather than relying on prose or IDE inference alone.

### Why it matters

Checked nullness turns a large class of runtime failures into review or compile-time findings.

### Avoid

Avoid ad-hoc mixes of incompatible nullability annotations with no analyzer configuration.

```java
String normalize(String value) {
    return value.strip(); // Null contract is undocumented.
}
```

### Prefer

Use JSpecify-compatible annotations with Error Prone/NullAway or another project-standard checker.

```java
@NullMarked
package com.example.accounts;

// Nullable exceptions are explicit under the package default.
String normalize(String value) { return value.strip(); }
```

### Nuance

Annotations are a contract, not runtime validation. External input still needs checks.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JSpecify specification:** <https://jspecify.dev/docs/spec/>
- **NullAway:** <https://github.com/uber/NullAway>

<a id="null-optional-return"></a>
## `null-optional-return` — Use Optional primarily for return-value absence

> Return Optional when a single value may be absent and callers benefit from composition.

### Why it matters

Optional makes absence explicit, but fields, parameters, and collections of Optional often add wrappers without clarifying ownership.

### Avoid

Avoid Optional parameters, nullable Optionals, and Optional-wrapped collections unless the extra state is meaningful.

```java
@Nullable User findUser(UserId id) { /* ... */ }
```

### Prefer

Use overloads/configuration types for optional inputs and empty collections for no elements.

```java
Optional<User> findUser(UserId id) { /* ... */ }
```

### Nuance

Framework serialization and persistence support for Optional varies; keep it at service/API boundaries unless verified.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Optional API note:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html>
- **Java Optional skill corpus:** <https://github.com/martinfrancois/java-optionals-skill>

<a id="null-no-optional-get"></a>
## `null-no-optional-get` — Do not reopen Optional with unchecked `get()`

> Bind, transform, default, or throw with explicit meaning instead of assuming presence.

### Why it matters

`get()` converts an absence contract into an uninformative `NoSuchElementException` unless presence is already proved.

### Avoid

Avoid `isPresent()` followed by `get()` for ordinary value flow.

```java
if (user.isPresent()) {
    return user.get().email();
}
return "unknown";
```

### Prefer

Use `map`, `flatMap`, `orElseGet`, `ifPresent`, pattern branches at checked boundaries, or `orElseThrow` with a domain exception.

```java
return user.map(User::email).orElse("unknown");
```

### Nuance

A guarded `get()` can be acceptable at an awkward checked-I/O boundary; keep the proof adjacent.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Optional.get:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html#get()>
- **Optional best practices corpus:** <https://github.com/martinfrancois/java-optionals-skill>

<a id="null-lazy-fallback"></a>
## `null-lazy-fallback` — Keep Optional fallback computation lazy

> Use `orElseGet` when the fallback allocates, performs I/O, mutates state, or can fail.

### Why it matters

`orElse` evaluates its argument even when the Optional is present.

### Avoid

Do not call an expensive or effectful fallback inside `orElse`.

```java
return cached.orElse(loadFromDatabase(id));
```

### Prefer

Use `orElseGet(() -> fallback())`; use `orElse` for already-computed trivial constants.

```java
return cached.orElseGet(() -> loadFromDatabase(id));
```

### Nuance

The distinction is semantic as well as performance-related when the fallback has side effects.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Optional.orElse:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html#orElse(T)>
- **Optional.orElseGet:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html#orElseGet(java.util.function.Supplier)>
