# JPA and Hibernate persistence

**Priority:** CRITICAL  
**Rules:** 5

Control entity identity, fetch plans, persistence-context lifetime, query count, and batch behavior.

Apply only the rules whose trigger exists in the candidate. Preserve the detected Spring Boot, Spring Framework, Java, Jakarta, servlet/reactive, database, security, and deployment contracts.

Examples are illustrative; preserve the repository baseline, imports, build system, framework generation, public API, and operational constraints.

<a id="jpa-stable-entity-equality"></a>
## `jpa-stable-entity-equality` — Keep entity equality stable across lifecycle states

> Base equality/hash code on a stable natural key or a carefully designed identifier strategy, not all mutable fields.

### Why it matters

Hash changes break sets/maps; generated identifiers are null before persistence and proxy subclasses complicate class checks.

### Avoid

Do not generate entity equality from every field or include mutable associations.

### Prefer

Document the identity model, test transient/managed/detached/proxy cases, and keep hash behavior stable.

### Nuance

For many applications, reference identity inside one persistence context plus explicit value objects is simpler than custom entity equality.

### Sources

- **Hibernate equals and hashCode:** <https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#domain-model-pojo-equalshashcode>

<a id="jpa-explicit-fetch-plan"></a>
## `jpa-explicit-fetch-plan` — Define fetch shape per use case

> Use query fetch joins, entity graphs, projections, or batch fetching to load exactly the associations required by one operation.

### Why it matters

Default eager/lazy mappings are global guesses; serialization or mapper traversal can trigger hidden queries.

### Avoid

Do not mark associations EAGER to fix `LazyInitializationException` or rely on open-session-in-view to load arbitrary graphs.

### Prefer

Keep mappings conservative, select a fetch plan at the query boundary, and map to a detached DTO before leaving the transaction.

### Nuance

Multiple bag fetches and large join graphs can explode rows; sometimes several bounded queries are better.

### Example

**Avoid**

```java
@ManyToOne(fetch = FetchType.EAGER)
Customer customer;
```

**Prefer**

```java
@EntityGraph(attributePaths = "customer")
Optional<Order> findDetailedById(UUID id);
```

### Sources

- **Hibernate fetching:** <https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#fetching>
- **Spring Data entity graphs:** <https://docs.spring.io/spring-data/jpa/reference/jpa/entity-graph.html>

<a id="jpa-detect-n-plus-one"></a>
## `jpa-detect-n-plus-one` — Prove query count on collection and association paths

> Inspect generated SQL/statistics and test representative cardinality when a query traverses associations.

### Why it matters

N+1 behavior may pass correctness tests while production latency and connection usage grow linearly.

### Avoid

Do not assume `LAZY`, `JOIN FETCH`, or a repository projection automatically prevents every N+1 path.

### Prefer

Set the fetch plan, assert query count or use profiling, and verify pagination/duplicates with realistic data.

### Nuance

Batch fetching can reduce round trips without one giant join; choose from measured access shape.

### Sources

- **Hibernate fetching:** <https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#fetching>
- **Spring Data entity graphs:** <https://docs.spring.io/spring-data/jpa/reference/jpa/entity-graph.html>

<a id="jpa-keep-persistence-context-bounded"></a>
## `jpa-keep-persistence-context-bounded` — Bound the persistence context

> Map required data inside the transaction and clear/detach periodically during large batch work.

### Why it matters

A long-lived context retains every managed entity, performs dirty checking, and can return stale in-memory state.

### Avoid

Do not iterate a massive result and repeatedly call `save` without flush/clear or keep entities alive across web/session boundaries.

### Prefer

Use paging/scrolling, JDBC batching, periodic flush/clear, and detached commands/results for bulk workflows.

### Nuance

Bulk JPQL/SQL bypasses managed entity state; clear or refresh intentionally afterward.

### Sources

- **Hibernate persistence context:** <https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#pc>
- **Hibernate batching:** <https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#batch>

<a id="jpa-cascade-owned-lifecycle"></a>
## `jpa-cascade-owned-lifecycle` — Cascade only across true aggregate ownership

> Use cascade/orphan removal when the parent exclusively owns the child's lifecycle.

### Why it matters

Broad cascade can persist or delete shared entities and produce large unexpected graphs.

### Avoid

Do not apply `CascadeType.ALL` by habit or cascade remove across many-to-many/shared references.

### Prefer

Define aggregate ownership, apply only required cascade operations, and test delete/reparent/orphan behavior.

### Nuance

Database cascades and ORM cascades solve different layers; align them explicitly.

### Sources

- **Hibernate associations:** <https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#associations>
