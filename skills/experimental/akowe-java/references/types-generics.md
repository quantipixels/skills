# Types and generics

**Priority:** CRITICAL  
**Rules:** 5

Expert Java uses the type system to preserve meaning while respecting erasure, variance, and interoperability limits.

Apply only the rules relevant to the candidate and its actual Java baseline. Repository and framework contracts take precedence when they deliberately specialize a rule.

<a id="type-no-raw-types"></a>
## `type-no-raw-types` — Never use raw generic types in new code

> Parameterize generic types or use a justified wildcard rather than discarding type information.

### Why it matters

Raw types disable compile-time checks and move failures into casts at runtime. They also infect callers with unchecked warnings.

### Avoid

Avoid `List values`, `Class type`, and raw `Comparable` except at unavoidable legacy boundaries.

```java
List values = load();
String first = (String) values.get(0);
```

### Prefer

Use `List<Value>`, `Class<?>`, bounded type parameters, or a narrow adapter that contains the unchecked legacy interaction.

```java
List<String> values = load();
String first = values.get(0);
```

### Nuance

A raw type may be necessary when interoperating with pre-generics APIs; isolate and document it.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JLS raw types:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html#jls-4.8>
- **Dev.java generics:** <https://dev.java/learn/generics/>

<a id="type-pecs"></a>
## `type-pecs` — Use variance according to producer and consumer roles

> Use `? extends T` for producers and `? super T` for consumers at API boundaries.

### Why it matters

Correct variance preserves substitutability without weakening the entire API to raw types or casts.

### Avoid

Do not require `List<Base>` when callers should be able to provide `List<Subtype>` for read-only use.

```java
static void copy(List<Number> source, List<Number> target) { /* ... */ }
```

### Prefer

Apply PECS narrowly: read from extends, write to super, and use invariant `T` when both operations are required.

```java
static <T> void copy(List<? extends T> source, List<? super T> target) {
    target.addAll(source);
}
```

### Nuance

Do not scatter wildcards through internal code when a named type parameter expresses the relationship more clearly.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JLS wildcards:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html#jls-4.5.1>
- **Dev.java wildcards:** <https://dev.java/learn/generics/wildcards/>

<a id="type-no-wildcard-return"></a>
## `type-no-wildcard-return` — Avoid wildcard-heavy return types

> Return a useful stable abstraction rather than forcing wildcard capture onto every caller.

### Why it matters

Wildcard return types commonly shift generic complexity outward and make composition harder.

### Avoid

Avoid returning `List<? extends Event>` when the API owns a clear `List<Event>` view.

```java
Optional<? extends Account> findAccount(AccountId id) { /* ... */ }
```

### Prefer

Use a concrete element supertype, a named generic method/type parameter, or a domain-specific read-only abstraction.

```java
Optional<Account> findAccount(AccountId id) { /* ... */ }
```

### Nuance

Covariant wildcard returns can be correct for framework SPI surfaces; use them only when the variance is part of the contract.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JLS type arguments:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html#jls-4.5.1>
- **Collections Framework:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/doc-files/coll-overview.html>

<a id="type-isolate-unchecked-casts"></a>
## `type-isolate-unchecked-casts` — Confine unchecked operations behind one proved boundary

> Keep unchecked casts and heap-pollution risk local, tested, and documented.

### Why it matters

Type erasure sometimes makes a cast unavoidable, but spreading suppressions hides unrelated defects and weakens future refactors.

### Avoid

Do not place `@SuppressWarnings("unchecked")` on a class or broad method to silence a small cast.

```java
@SuppressWarnings("unchecked")
T value = (T) raw;
use(value);
```

### Prefer

Move the cast into the smallest helper, validate runtime shape where possible, document the invariant, and return a typed result.

```java
static <T> T checkedCast(Object value, Class<T> type) {
    return type.cast(value);
}
```

### Nuance

Varargs of non-reifiable types may require `@SafeVarargs`; apply it only when the implementation cannot corrupt the array.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JLS heap pollution:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html#jls-4.12.2.1>
- **SafeVarargs:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/SafeVarargs.html>

<a id="type-domain-value-objects"></a>
## `type-domain-value-objects` — Represent domain primitives with domain types

> Use records or small immutable classes when two values share a JVM type but not a meaning.

### Why it matters

Distinct types prevent parameter swaps, centralize validation, and let APIs communicate units and invariants.

### Avoid

Avoid passing several unrelated `String`, `long`, or `UUID` values whose roles are distinguished only by names.

```java
void transfer(long sourceId, long targetId, long cents) { /* ... */ }
```

### Prefer

Introduce types such as `CustomerId`, `Money`, `EmailAddress`, or `RetryCount` when the distinction changes correctness.

```java
record AccountId(long value) {}
record Money(long minorUnits, Currency currency) {}

void transfer(AccountId source, AccountId target, Money amount) { /* ... */ }
```

### Nuance

Do not wrap every primitive mechanically; add a value object when it protects a real boundary or behavior.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Record classes:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.10>
- **JEP 395:** <https://openjdk.org/jeps/395>
