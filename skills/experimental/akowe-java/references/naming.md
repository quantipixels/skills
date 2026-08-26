# Naming, visibility, and communication

**Priority:** MEDIUM  
**Rules:** 5

Names and visibility are executable design: they define what readers can infer and what other code is allowed to depend on.

Apply only the rules relevant to the candidate and its actual Java baseline. Repository and framework contracts take precedence when they deliberately specialize a rule.

<a id="name-domain-language"></a>
## `name-domain-language` — Name by domain responsibility

> Use names that reveal the concept, invariant, or operation rather than the implementation technique.

### Why it matters

Domain names survive refactoring and reduce the amount of architecture a reader must reconstruct from generic classes.

### Avoid

Avoid names such as `DataUtil`, `CommonManager`, `Helper`, or `Processor` when a more specific responsibility exists.

```java
final class DataManager {
    void process(Item item) { /* ... */ }
}
```

### Prefer

Name the owned concept or operation: `TaxPolicy`, `PaymentAttempt`, `SessionExpiry`, `InvoiceNumber`.

```java
final class PaymentAuthorizer {
    Authorization authorize(Payment payment) { /* ... */ }
}
```

### Nuance

Technical names are appropriate for genuinely technical adapters, codecs, transports, and framework integration points.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JLS naming conventions:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-6.html#jls-6.1>
- **Google Java Style:** <https://google.github.io/styleguide/javaguide.html>

<a id="name-no-meaningless-suffixes"></a>
## `name-no-meaningless-suffixes` — Do not encode uncertainty in suffixes

> Use suffixes such as `Factory`, `Builder`, `Repository`, or `Adapter` only when the type actually fulfills that role.

### Why it matters

Habitual `Impl`, `Manager`, `Service`, and `Util` suffixes hide distinctions and create parallel names with no semantic value.

### Avoid

Avoid `OrderServiceImpl` when there is one implementation and the class can simply be `OrderService` or a domain-specific name.

```java
final class OrderServiceImpl implements OrderService { /* ... */ }
```

### Prefer

Name the concrete responsibility; introduce interface/concrete pairs only for real polymorphism or boundary isolation.

```java
final class DatabaseOrderRepository implements OrderRepository { /* ... */ }
```

### Nuance

Framework conventions can require established suffixes. Preserve them when they communicate a real role to the ecosystem.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Google Java Style naming:** <https://google.github.io/styleguide/javaguide.html#s5-naming>
- **JLS naming conventions:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-6.html#jls-6.1>

<a id="name-least-visibility"></a>
## `name-least-visibility` — Expose the smallest stable surface

> Keep types and members as inaccessible as the real collaboration boundary permits.

### Why it matters

Every visible member becomes a potential dependency, constraining refactoring and expanding the compatibility contract.

### Avoid

Do not make a type or member public for testing convenience or speculative reuse.

```java
public final class TokenParser {
    public String normalize(String token) { /* internal helper */ }
}
```

### Prefer

Use private or package access for implementation details, expose intentional APIs, and test through behavior or deliberate package boundaries.

```java
final class TokenParser {
    String normalize(String token) { /* package collaboration */ }
}
```

### Nuance

Package-private is useful for cohesive module internals, but it is not a substitute for sound public contracts.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JLS access control:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-6.html#jls-6.6>
- **Java modules:** <https://dev.java/learn/modules/>

<a id="name-var-when-obvious"></a>
## `name-var-when-obvious` — Use `var` only when it improves reading

> Use local-variable type inference when the initializer and name make the type and role obvious.

### Why it matters

`var` removes repetition but can also hide units, generic element types, or surprising factory results.

### Avoid

Avoid `var result = process(input);` when the concrete meaning is not visible nearby.

```java
Map<String, List<Order>> ordersByCustomer =
    loadOrdersByCustomer();
```

### Prefer

Use `var` for obvious constructors, factories, iterators, and long generic types; keep explicit types where they communicate the contract.

```java
var ordersByCustomer = loadOrdersByCustomer();
```

### Nuance

The decision is about information density, not a project-wide mandate for or against `var`.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Local-variable type inference:** <https://openjdk.org/jeps/286>
- **Java language updates:** <https://docs.oracle.com/en/java/javase/25/language/>

<a id="name-comments-explain-contract"></a>
## `name-comments-explain-contract` — Write comments for non-obvious contracts

> Document invariants, side effects, concurrency, ownership, security, and compatibility—not code narration.

### Why it matters

Comments that restate syntax decay quickly, while omitted hidden constraints cause incorrect maintenance.

### Avoid

Avoid comments such as `// increment counter` or Javadoc that repeats the signature.

```java
// Increment retryCount by one.
retryCount++;
```

### Prefer

Explain why a strange branch exists, what callers may rely on, which lock protects state, and what failure or resource behavior is promised.

```java
// Retry count is persisted before the call so a crash cannot reset the budget.
retryCount++;
```

### Nuance

Public APIs often deserve concise Javadoc even when implementation comments do not.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Javadoc guide:** <https://docs.oracle.com/en/java/javase/25/docs/specs/javadoc/doc-comment-spec.html>
- **Markdown documentation comments:** <https://openjdk.org/jeps/467>
