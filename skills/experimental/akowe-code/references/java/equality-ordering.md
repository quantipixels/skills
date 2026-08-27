# Equality, hashing, and ordering

**Priority:** CRITICAL  
**Rules:** 5

Java collections and algorithms assume equality and ordering contracts. Small mistakes here create lost keys, duplicate values, and nondeterministic behavior.

Apply only the rules relevant to the candidate and its actual Java baseline. Repository and framework contracts take precedence when they deliberately specialize a rule.

<a id="eq-equals-hashcode"></a>
## `eq-equals-hashcode` — Implement equals and hashCode together

> Equal objects must produce equal hash codes for the entire time they participate in hashed collections.

### Why it matters

Hash-based collections select buckets before checking equality; inconsistent implementations make entries unreachable or duplicated.

### Avoid

Do not override only one method or compute hashes from fields that equality ignores.

```java
@Override public boolean equals(Object other) {
    return other instanceof User u && id.equals(u.id);
}
// hashCode still uses Object identity.
```

### Prefer

Use the same stable state in both methods; records provide a correct component-based default.

```java
@Override public boolean equals(Object other) {
    return other instanceof User u && id.equals(u.id);
}
@Override public int hashCode() {
    return id.hashCode();
}
```

### Nuance

Caching a hash code is safe only for immutable equality state.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Object.equals/hashCode:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html>
- **HashMap:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/HashMap.html>

<a id="eq-symmetry-inheritance"></a>
## `eq-symmetry-inheritance` — Protect equality symmetry across inheritance

> Do not extend a value class with extra equality state unless substitutability remains sound.

### Why it matters

Mixing `instanceof` equality in a base class with additional subclass state commonly breaks symmetry or transitivity.

### Avoid

Avoid value-type inheritance hierarchies with changing equality semantics.

```java
class Point { int x, y; /* value equality */ }
class ColoredPoint extends Point { Color color; /* extra equality state */ }
```

### Prefer

Use composition, sealed hierarchies with explicit semantics, records, or final value classes.

```java
record Point(int x, int y) {}
record ColoredPoint(Point point, Color color) {}
```

### Nuance

Entity identity equality follows different rules; document when equality is based solely on a stable identifier.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Object.equals contract:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)>
- **Sealed classes:** <https://openjdk.org/jeps/409>

<a id="eq-no-mutable-keys"></a>
## `eq-no-mutable-keys` — Do not mutate map keys or set members

> Keep all state used by equality and hashing stable while an object is stored in a hash-based collection.

### Why it matters

Mutation can move the conceptual hash bucket without moving the stored entry, making lookup and removal fail.

### Avoid

Avoid mutable records/classes as keys unless equality state is immutable.

```java
var key = new ArrayList<>(List.of("a"));
map.put(key, value);
key.add("b"); // Lookup bucket no longer matches.
```

### Prefer

Use immutable keys or remove, mutate, and reinsert under a clearly owned operation.

```java
record Key(List<String> parts) {
    Key { parts = List.copyOf(parts); }
}
map.put(new Key(parts), value);
```

### Nuance

Identity-based maps deliberately use reference identity; choose them only when that is the domain contract.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **HashMap:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/HashMap.html>
- **IdentityHashMap:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/IdentityHashMap.html>

<a id="eq-comparator-consistency"></a>
## `eq-comparator-consistency` — Make comparator semantics explicit

> Ensure comparison is transitive and decide whether zero comparison must match equals.

### Why it matters

Sorted sets and maps use comparison, not `equals`, to determine uniqueness.

### Avoid

Do not use subtraction for numeric comparison or a comparator that changes with mutable external state.

```java
Comparator<Person> byAge = Comparator.comparingInt(Person::age);
// TreeSet silently treats different same-age people as duplicates.
```

### Prefer

Use `Comparator.comparing`, primitive comparators, chained tie-breakers, and documented null policy.

```java
Comparator<Person> byAgeThenId =
    Comparator.comparingInt(Person::age)
              .thenComparing(Person::id);
```

### Nuance

A comparator inconsistent with equals can be valid, but sorted-collection behavior must be intentional.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Comparator contract:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html>
- **Comparable:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Comparable.html>

<a id="eq-array-content"></a>
## `eq-array-content` — Compare arrays by content deliberately

> Use `Arrays.equals`, `deepEquals`, `compare`, or `mismatch` rather than object identity.

### Why it matters

Java arrays inherit identity-based `Object.equals` and `hashCode`.

### Avoid

Do not use `array1.equals(array2)` when value content matters.

```java
if (left.equals(right)) { /* compares array identity */ }
```

### Prefer

Choose the Arrays operation matching shallow/deep and equality/order semantics; copy mutable arrays at boundaries.

```java
if (Arrays.equals(left, right)) { /* compares elements */ }
```

### Nuance

For public value models, a list or dedicated value type may communicate semantics better than an array.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Arrays:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Arrays.html>
- **Object.equals:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)>
