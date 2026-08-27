# Value semantics and immutability

**Priority:** CRITICAL  
**Rules:** 5

Immutable values are easier to share, cache, compare, and reason about. The important distinction is not syntax but ownership of mutable state.

Apply only the rules relevant to the candidate and its actual Java baseline. Repository and framework contracts take precedence when they deliberately specialize a rule.

<a id="value-immutable-default"></a>
## `value-immutable-default` — Make value objects immutable by default

> Establish all invariants at construction and avoid observable mutation afterward.

### Why it matters

Immutability simplifies equality, safe publication, concurrency, caching, and rollback reasoning.

### Avoid

Avoid setters on identifiers, money, coordinates, configuration snapshots, and other value-like objects.

```java
final class User {
    String email;
    void setEmail(String email) { this.email = email; }
}
```

### Prefer

Use records or final fields, validate construction, and return a new value for changes.

```java
record User(Email email) {
    User {
        Objects.requireNonNull(email);
    }
}
```

### Nuance

Entities with identity and lifecycle can be mutable; keep mutation owned and invariant-preserving.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Record classes:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.10>
- **Java Memory Model final fields:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-17.html#jls-17.5>

<a id="value-defensive-copy"></a>
## `value-defensive-copy` — Copy mutable inputs at ownership boundaries

> Do not retain caller-owned mutable arrays, collections, dates, buffers, or builders without an explicit shared-ownership contract.

### Why it matters

External mutation can silently violate invariants after construction.

### Avoid

Avoid assigning a provided `List` or array directly into an immutable-looking type.

```java
final class Batch {
    private final byte[] payload;
    Batch(byte[] payload) { this.payload = payload; }
}
```

### Prefer

Use `List.copyOf`, `Set.copyOf`, `Map.copyOf`, array copies, or a domain-specific immutable representation.

```java
final class Batch {
    private final byte[] payload;
    Batch(byte[] payload) { this.payload = payload.clone(); }
    byte[] payload() { return payload.clone(); }
}
```

### Nuance

Copying can be intentionally omitted for performance when the API clearly transfers ownership and proves exclusivity.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **List.copyOf:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html#copyOf(java.util.Collection)>
- **Arrays.copyOf:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Arrays.html>

<a id="value-unmodifiable-not-immutable"></a>
## `value-unmodifiable-not-immutable` — Distinguish unmodifiable views from immutable values

> Do not treat a read-only wrapper as proof that the backing data cannot change.

### Why it matters

`Collections.unmodifiableList` prevents writes through one reference but reflects mutations made through the backing collection.

### Avoid

Avoid storing a mutable list and exposing only an unmodifiable view while claiming snapshot semantics.

```java
this.items = Collections.unmodifiableList(items);
// The caller can still mutate items.
```

### Prefer

Use `copyOf` for a snapshot, or document a live read-only view when that is intentional.

```java
this.items = List.copyOf(items);
```

### Nuance

Live views are useful for owned state monitoring; the contract must say that contents can change.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Collections.unmodifiableList:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collections.html#unmodifiableList(java.util.List)>
- **List.copyOf:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html#copyOf(java.util.Collection)>

<a id="value-builder-for-complex-construction"></a>
## `value-builder-for-complex-construction` — Use builders only when construction is genuinely complex

> Prefer constructors or static factories for small mandatory state; use builders for many optional or order-independent choices.

### Why it matters

Builders improve readability for complex configuration but add mutable machinery, validation timing, and API surface.

### Avoid

Do not create a builder for a two-field value merely to follow a pattern.

```java
new ClientConfig(host, 443, true, Duration.ofSeconds(3),
    5, null, null, false);
```

### Prefer

Use compact constructors/static factories first; add a builder when call-site clarity or optional combinations justify it.

```java
ClientConfig.builder(host)
    .tls(true)
    .timeout(Duration.ofSeconds(3))
    .maxRetries(5)
    .build();
```

### Nuance

A staged builder can encode required ordering, but often a small set of domain types is simpler.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Record constructors:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.10.4>
- **Java API design guidance:** <https://dev.java/learn/classes-objects/>

<a id="value-no-expose-mutable-state"></a>
## `value-no-expose-mutable-state` — Do not leak mutable internals

> Return snapshots, immutable values, or narrow operations instead of exposing owned mutable objects.

### Why it matters

Leaked references let callers bypass synchronization, validation, eventing, and lifecycle rules.

### Avoid

Avoid getters that return an internal mutable list, map, array, buffer, or date object.

```java
List<Order> orders() {
    return orders;
}
```

### Prefer

Return immutable copies/views with an explicit contract, iterators/streams for traversal, or domain operations that preserve invariants.

```java
List<Order> orders() {
    return List.copyOf(orders);
}
```

### Nuance

High-performance APIs may expose buffers by agreement; document lifetime, mutability, and ownership precisely.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Collections Framework:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/doc-files/coll-overview.html>
- **MemorySegment:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/foreign/MemorySegment.html>
