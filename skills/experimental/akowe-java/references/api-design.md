# API design

**Priority:** CRITICAL  
**Rules:** 5

A strong Java API communicates ownership, absence, failure, mutability, units, and compatibility before implementation details.

Apply only the rules relevant to the candidate and its actual Java baseline. Repository and framework contracts take precedence when they deliberately specialize a rule.

<a id="api-contract-first"></a>
## `api-contract-first` — Design the caller-visible contract before implementation

> Define inputs, outputs, failure, absence, side effects, ownership, and version constraints before choosing internal machinery.

### Why it matters

Implementation-first APIs leak incidental structures and make later correction expensive.

### Avoid

Do not expose ORM entities, mutable internal collections, framework request types, or executor details by accident.

```java
CompletableFuture<User> load(UserId id) { /* implementation chosen first */ }
```

### Prefer

Use domain/JDK types and narrow interfaces that preserve the caller's actual decisions.

```java
// Contract first: absence, failure, cancellation, and ownership are explicit.
Optional<User> find(UserId id) throws RepositoryUnavailable { /* ... */ }
```

### Nuance

Internal APIs can evolve faster, but they still benefit from explicit ownership and failure contracts.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Java API specification:** <https://docs.oracle.com/en/java/javase/25/docs/api/>
- **Dev.java interfaces:** <https://dev.java/learn/interfaces/>

<a id="api-least-capability"></a>
## `api-least-capability` — Accept the least capability and expose the useful one

> Parameterize by the operations required rather than a concrete implementation.

### Why it matters

Narrow types increase caller choice and reduce coupling, while overly vague outputs force callers to inspect or cast.

### Avoid

Avoid accepting `ArrayList<T>` when iteration is enough, or returning raw `Object` when a domain type exists.

```java
void printUsers(ArrayList<User> users) { /* only iteration needed */ }
```

### Prefer

Accept `Iterable`, `Collection`, `List`, `Path`, `Clock`, or a focused interface according to required semantics.

```java
void printUsers(Iterable<User> users) { /* ... */ }
```

### Nuance

Do not generalize mechanically: `List` communicates order and indexed access that `Collection` does not.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Collections interfaces:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html>
- **Java interfaces:** <https://dev.java/learn/interfaces/>

<a id="api-empty-collections-not-null"></a>
## `api-empty-collections-not-null` — Return empty collections rather than `null`

> Represent 'no elements' with an empty collection and reserve nullability for a distinct absence contract.

### Why it matters

Empty collections preserve iteration and composition without extra control flow.

### Avoid

Do not make callers null-check a collection result that can naturally be empty.

```java
List<Order> ordersFor(CustomerId id) {
    return null;
}
```

### Prefer

Return `List.of()`, `Set.of()`, `Map.of()`, or another contract-appropriate empty value.

```java
List<Order> ordersFor(CustomerId id) {
    return List.of();
}
```

### Nuance

If absence and an empty result mean different things, model that difference explicitly with a result type or Optional.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **List.of:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html#of()>
- **Collections.emptyList:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collections.html#emptyList()>

<a id="api-static-factories"></a>
## `api-static-factories` — Use named factories when construction meaning matters

> Prefer static factories when a constructor cannot communicate validation, caching, conversion, or variant selection.

### Why it matters

Names such as `parse`, `from`, `of`, and `copyOf` reveal semantics that overloaded constructors cannot.

### Avoid

Avoid several same-shaped constructors distinguished only by documentation.

```java
new Money(1250, "EUR", true);
```

### Prefer

Keep constructors for direct construction; use named factories for conversion, normalization, caching, or subtype choice.

```java
Money.euros(12, 50);
Money.fromMinorUnits(1250, Currency.getInstance("EUR"));
```

### Nuance

Do not hide expensive I/O behind an innocent `of` factory; names should signal cost and failure.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Java class creation:** <https://dev.java/learn/classes-objects/creating-objects/>
- **JDK factory conventions:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html#of()>

<a id="api-avoid-boolean-parameters"></a>
## `api-avoid-boolean-parameters` — Replace ambiguous boolean controls

> Use distinct methods, enums, or option types when a boolean changes behavior in a way the call site cannot explain.

### Why it matters

Calls such as `send(message, true, false)` hide policy and are easy to swap.

### Avoid

Avoid multiple boolean flags and booleans that select fundamentally different operations.

```java
report.generate(true, false);
```

### Prefer

Use `sendSynchronously`, `DeliveryMode.DURABLE`, a configuration record, or separate commands.

```java
report.generate(OutputFormat.PDF, DetailLevel.SUMMARY);
```

### Nuance

A single obvious state value like `setEnabled(boolean)` can be perfectly clear.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Enum types:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.9>
- **Record classes:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.10>
