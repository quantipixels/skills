# Records, sealed types, and pattern matching

**Priority:** HIGH  
**Rules:** 5

Modern Java features reduce accidental state and make closed models explicit. Use them when they sharpen the domain, not as syntax decoration.

Apply only the rules relevant to the candidate and its actual Java baseline. Repository and framework contracts take precedence when they deliberately specialize a rule.

<a id="modern-records-for-values"></a>
## `modern-records-for-values` — Use records for transparent data aggregates

> Choose a record when the API is fundamentally its components and value semantics.

### Why it matters

Records provide final components, accessors, canonical construction, and value-based `equals`, `hashCode`, and `toString`.

### Avoid

Do not use a record for mutable entities, hidden representation, lazy state, or subclasses.

```java
final class Point {
    private final int x;
    private final int y;
    // constructor, accessors, equals, hashCode, toString
}
```

### Prefer

Use records for commands, events, coordinates, identifiers, configuration snapshots, and result aggregates.

```java
record Point(int x, int y) {}
```

### Nuance

Record components are shallowly immutable; copy mutable component values when snapshot semantics are required.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JEP 395:** <https://openjdk.org/jeps/395>
- **JLS record classes:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.10>

<a id="modern-record-validate"></a>
## `modern-record-validate` — Validate record invariants in the compact constructor

> Reject invalid component combinations at the record boundary.

### Why it matters

A record's generated methods assume its components are the complete state. Allowing invalid values creates durable invalid instances.

### Avoid

Do not rely on every caller to validate components before construction.

```java
record Percentage(int value) {}
```

### Prefer

Use the compact constructor to normalize or reject values, and defensively copy mutable components.

```java
record Percentage(int value) {
    Percentage {
        if (value < 0 || value > 100) {
            throw new IllegalArgumentException("percentage out of range");
        }
    }
}
```

### Nuance

Normalization must preserve the public meaning of components; surprising canonicalization can make equality confusing.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JLS record constructors:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.10.4>
- **JEP 395:** <https://openjdk.org/jeps/395>

<a id="modern-sealed-hierarchies"></a>
## `modern-sealed-hierarchies` — Seal hierarchies that are intentionally closed

> Use sealed classes or interfaces when the permitted variants are part of the domain contract.

### Why it matters

Closed hierarchies support exhaustive reasoning and prevent unknown subclasses from violating assumptions.

### Avoid

Do not seal extension points intended for third-party implementations.

```java
interface PaymentResult {}
final class Approved implements PaymentResult {}
final class Declined implements PaymentResult {}
// Any module may add an unhandled implementation.
```

### Prefer

Seal internal/domain sum types; keep open interfaces for genuine plugins and public SPIs.

```java
sealed interface PaymentResult permits Approved, Declined {}
record Approved(String authorization) implements PaymentResult {}
record Declined(String reason) implements PaymentResult {}
```

### Nuance

The permitted set is a compatibility commitment. Adding a subtype can break exhaustive client switches.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JEP 409:** <https://openjdk.org/jeps/409>
- **JLS sealed classes:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.1.1.2>

<a id="modern-exhaustive-switch"></a>
## `modern-exhaustive-switch` — Use exhaustive switch expressions for closed states

> Let the compiler prove that every enum or sealed variant produces a result.

### Why it matters

Switch expressions avoid fall-through and make missing cases visible during model evolution.

### Avoid

Avoid a `default` arm that hides an omitted known variant when exhaustiveness can be checked.

```java
String label(Status status) {
    return switch (status) {
        case ACTIVE -> "active";
        default -> "other";
    };
}
```

### Prefer

List every enum/sealed case; use `default` only for truly open input or compatibility handling.

```java
String label(Status status) {
    return switch (status) {
        case ACTIVE -> "active";
        case PAUSED -> "paused";
        case CLOSED -> "closed";
    };
}
```

### Nuance

A library switching over another library's enum may need a defensive default for version skew.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JEP 441:** <https://openjdk.org/jeps/441>
- **JLS switch expressions:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-15.html#jls-15.28>

<a id="modern-pattern-matching"></a>
## `modern-pattern-matching` — Use pattern matching to bind proven types

> Prefer `instanceof` and switch patterns over repeated tests and casts.

### Why it matters

Pattern variables keep the test and binding together, reducing cast drift and nested control flow.

### Avoid

Avoid `if (x instanceof Foo) { Foo foo = (Foo) x; ... }` in modern baselines.

```java
if (value instanceof String) {
    String text = (String) value;
    return text.strip();
}
```

### Prefer

Use `if (x instanceof Foo foo)` and pattern switches where they improve exhaustiveness.

```java
if (value instanceof String text) {
    return text.strip();
}
```

### Nuance

Do not turn a straightforward polymorphic method call into a type switch merely to use new syntax.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Pattern matching for instanceof:** <https://openjdk.org/jeps/394>
- **Pattern matching for switch:** <https://openjdk.org/jeps/441>
