# Collections

**Priority:** HIGH  
**Rules:** 5

Choose collections from semantic requirements—order, uniqueness, lookup, mutation, concurrency—not habit.

Apply only the rules relevant to the candidate and its actual Java baseline. Repository and framework contracts take precedence when they deliberately specialize a rule.

<a id="coll-program-to-interface"></a>
## `coll-program-to-interface` — Declare collection contracts by interface

> Use `List`, `Set`, `Map`, `Deque`, or another semantic interface unless callers need implementation-specific behavior.

### Why it matters

Interface types preserve implementation freedom and communicate the operations the API promises.

### Avoid

Avoid public `ArrayList`, `HashMap`, or `LinkedList` types without a concrete contract reason.

```java
ArrayList<Order> loadOrders() { /* ... */ }
```

### Prefer

Select the interface by order, duplicates, key lookup, queueing, or sorted semantics, then choose the implementation internally.

```java
List<Order> loadOrders() { /* ... */ }
```

### Nuance

Implementation types are appropriate for construction details and specialized performance APIs.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Collections Framework overview:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/doc-files/coll-overview.html>
- **Collection:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html>

<a id="coll-immutable-boundaries"></a>
## `coll-immutable-boundaries` — Use immutable collection factories for fixed values

> Represent fixed small data and snapshots with `of`/`copyOf` rather than mutable collections plus convention.

### Why it matters

Immutable collections prevent accidental updates and clearly state ownership.

### Avoid

Avoid constructing an `ArrayList` that no caller is intended to modify.

```java
return Collections.unmodifiableList(orders);
```

### Prefer

Use `List.of`, `Set.of`, `Map.of`, or copy factories and document whether iteration order is part of the contract.

```java
return List.copyOf(orders);
```

### Nuance

These factories reject nulls and may not preserve implementation-specific mutability/order assumptions.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **List.of:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html#of(E...)>
- **Map.of:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html#of()>

<a id="coll-copy-on-store-return"></a>
## `coll-copy-on-store-return` — Copy collections when ownership changes

> Take a snapshot when storing caller data or returning owned mutable state.

### Why it matters

Shared mutable collections allow mutation to bypass validation and synchronization.

### Avoid

Do not retain and return the same mutable collection across an ownership boundary.

```java
this.roles = roles;
return roles;
```

### Prefer

Copy on input/output, or expose a live view only with explicit lifecycle and concurrency semantics.

```java
this.roles = Set.copyOf(roles);
return roles;
```

### Nuance

Large-copy cost can justify an immutable persistent structure or transfer-of-ownership API.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **List.copyOf:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html#copyOf(java.util.Collection)>
- **Collections.unmodifiableCollection:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collections.html#unmodifiableCollection(java.util.Collection)>

<a id="coll-enumset-enummap"></a>
## `coll-enumset-enummap` — Use EnumSet and EnumMap for enum domains

> Choose specialized enum collections when keys/elements are enum constants.

### Why it matters

They are compact, type-safe, fast, and express that the domain is finite.

### Avoid

Avoid `HashSet<Enum>` and `HashMap<Enum, V>` by default.

```java
Set<Permission> permissions = new HashSet<>();
Map<Status, Handler> handlers = new HashMap<>();
```

### Prefer

Use `EnumSet` for flags/subsets and `EnumMap` for enum-indexed data.

```java
Set<Permission> permissions = EnumSet.noneOf(Permission.class);
Map<Status, Handler> handlers = new EnumMap<>(Status.class);
```

### Nuance

Immutable snapshots still require wrapping/copying because these implementations are mutable.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **EnumSet:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/EnumSet.html>
- **EnumMap:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/EnumMap.html>

<a id="coll-size-capacity"></a>
## `coll-size-capacity` — Size known collections and buffers deliberately

> Provide expected capacity when the size is known and material.

### Why it matters

Repeated resizing and rehashing adds allocation and copying in hot or large paths.

### Avoid

Do not micro-tune every tiny collection or use misleading exact capacities.

```java
List<Result> results = new ArrayList<>();
for (Input input : inputs) results.add(process(input));
```

### Prefer

Pre-size large `ArrayList`, `HashMap`, buffers, and builders from trustworthy estimates.

```java
List<Result> results = new ArrayList<>(inputs.size());
for (Input input : inputs) results.add(process(input));
```

### Nuance

Capacity is a performance hint, not a correctness contract; measure before complex sizing formulas.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **ArrayList constructors:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/ArrayList.html>
- **HashMap constructors:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/HashMap.html>
