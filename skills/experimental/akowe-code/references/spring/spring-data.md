# Spring Data repositories and queries

**Priority:** HIGH  
**Rules:** 5

Keep repository contracts aligned with aggregate ownership, query semantics, result size, and concurrency.

Apply only the rules whose trigger exists in the candidate. Preserve the detected Spring Boot, Spring Framework, Java, Jakarta, servlet/reactive, database, security, and deployment contracts.

Examples are illustrative; preserve the repository baseline, imports, build system, framework generation, public API, and operational constraints.

<a id="data-repository-owned-contract"></a>
## `data-repository-owned-contract` — Expose repositories through application-owned contracts

> Use Spring Data interfaces where they clarify aggregate persistence, but keep controllers and unrelated features from depending on generic CRUD internals.

### Why it matters

A globally shared `JpaRepository<Entity, Id>` makes any caller able to mutate persistence without the use-case invariant.

### Avoid

Do not pass repository interfaces directly into web adapters or expose `save` as the whole domain API.

### Prefer

Wrap or scope repositories behind the application operation when mutation rules, authorization, or events matter.

### Nuance

Simple admin/internal CRUD can use repositories directly when that is truly the accepted contract.

### Sources

- **Spring Data repository concepts:** <https://docs.spring.io/spring-data/commons/reference/repositories/core-concepts.html>

<a id="data-query-shape-explicit"></a>
## `data-query-shape-explicit` — Use the clearest query representation

> Use derived query names for short unambiguous predicates and move complex joins, projections, updates, and dynamic criteria to explicit queries/specifications.

### Why it matters

Very long method names hide precedence, fetch shape, null behavior, and database cost.

### Avoid

Do not encode a reporting query as a twenty-token repository method or concatenate user input into JPQL/SQL.

### Prefer

Choose `@Query`, named queries, Specifications, Query by Example, Querydsl, JDBC, or jOOQ according to the actual contract and repository stack.

### Nuance

A complex query may deserve a dedicated read repository rather than forcing the aggregate repository to own it.

### Sources

- **Spring Data JPA query methods:** <https://docs.spring.io/spring-data/jpa/reference/jpa/query-methods.html>

<a id="data-bound-result-size"></a>
## `data-bound-result-size` — Never return an unbounded collection by accident

> Use pagination, slicing, scrolling/streaming, batching, or explicit limits for data sets controlled by production growth.

### Why it matters

A harmless `findAll()` in development can load millions of rows, entities, and associations later.

### Avoid

Do not return `List` from a query whose maximum cardinality is not an invariant.

### Prefer

Choose `Page` only when total count is required; use `Slice`/keyset/scrolling when count cost or mutation makes it unsuitable.

### Nuance

Streaming repository results still require an open resource/transaction and deterministic closure.

### Example

**Avoid**

```java
List<AuditEvent> findAllByTenantId(UUID tenantId);
```

**Prefer**

```java
Slice<AuditEventView> findByTenantId(
    UUID tenantId,
    Pageable pageable
);
```

### Sources

- **Spring Data query return types:** <https://docs.spring.io/spring-data/commons/reference/repositories/query-return-types-reference.html>
- **Spring Data scrolling:** <https://docs.spring.io/spring-data/jpa/reference/jpa/query-methods.html#jpa.query-methods.scroll>

<a id="data-projection-for-read-model"></a>
## `data-projection-for-read-model` — Select only the read model the caller needs

> Use interface/class/record projections or explicit DTO queries for read paths that do not require managed entities.

### Why it matters

Loading full entities and associations increases memory, dirty-checking, serialization risk, and N+1 exposure.

### Avoid

Do not use open projections with arbitrary SpEL for hot or complex queries without measuring the generated access pattern.

### Prefer

Select fields explicitly, keep projection semantics stable, and test the generated query and nullability.

### Nuance

Entities remain appropriate when the operation modifies the aggregate inside a transaction.

### Sources

- **Spring Data projections:** <https://docs.spring.io/spring-data/jpa/reference/repositories/projections.html>

<a id="data-locking-and-versioning"></a>
## `data-locking-and-versioning` — Choose concurrency control deliberately

> Use optimistic versioning for ordinary concurrent edits and add pessimistic locking only when contention and transaction design justify it.

### Why it matters

Lost updates and duplicate processing appear when reads and writes assume exclusive access without a version/constraint/lock.

### Avoid

Do not add a database lock without bounding transaction duration or blindly retry every optimistic conflict.

### Prefer

Define the invariant, database constraint, lock mode, retry/merge policy, and user-visible conflict behavior.

### Nuance

Idempotency keys and unique constraints often solve creation races better than row locks.

### Sources

- **Spring Data JPA locking:** <https://docs.spring.io/spring-data/jpa/reference/jpa/locking.html>
- **Jakarta Persistence locking:** <https://jakarta.ee/specifications/persistence/3.2/jakarta-persistence-spec-3.2#locking-and-concurrency>
