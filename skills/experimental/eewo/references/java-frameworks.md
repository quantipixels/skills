# Java framework guards

Load only when the candidate uses the named framework. These rules were discovered through JVM Skills catalogue entries and source skills for Spring/JPA/Hibernate/jOOQ/Gradle, then narrowed against official framework documentation.

## Spring proxy and transaction boundaries

### `spring.proxy.self-invocation` (`BLOCK`)

**Avoid:** Expecting `@Transactional`, `@Async`, `@Cacheable`, or other proxy advice to apply when one method calls another method on `this`.

**Why:** Self-invocation bypasses the proxy, so the annotated behavior is not applied.

**Prefer:** Move the advised operation behind another bean/proxy boundary, call through the proxy only when justified, or use a non-proxy mechanism.

**Sources:** [Spring AOP proxying](https://docs.spring.io/spring-framework/reference/core/aop/proxying.html), [transaction annotations](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html).

### `spring.proxy.non-overridable-advice` (`BLOCK`)

**Avoid:** Placing proxy-based advice on private/final methods or classes where the selected proxy mechanism cannot intercept it.

**Why:** The annotation appears active while the call is never advised.

**Prefer:** An interceptable method/class or AspectJ/native mechanism selected deliberately.

**Source:** [Spring proxying limitations](https://docs.spring.io/spring-framework/reference/core/aop/proxying.html).

### `spring.transaction.checked-rollback-assumption` (`BLOCK`)

**Avoid:** Assuming every checked exception automatically rolls back a declarative transaction.

**Why:** Default rollback rules target runtime exceptions and errors; checked exceptions may commit.

**Prefer:** Configure rollback rules or translate to the domain exception type that matches the intended contract.

**Source:** [Spring rollback rules](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/rolling-back.html).

### `spring.transaction.swallowed-failure` (`BLOCK`)

**Avoid:** Catching a transactional failure, returning success/fallback, and expecting the transaction manager to infer rollback.

**Why:** The exception signal that drives rollback is removed; partial work may commit.

**Prefer:** Re-throw/translate, explicitly mark rollback-only at a true boundary, or isolate best-effort work in a separate transaction contract.

**Source:** [Spring declarative transactions](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative.html).

### `spring.transaction.remote-io-inside-long-transaction` (`WARN`)

**Avoid:** Holding database transactions and locks across slow remote calls, user interaction, or unbounded computation.

**Why:** Lock duration, connection occupancy, and rollback cost grow with unrelated latency.

**Prefer:** Short database units with an explicit consistency/outbox/saga design when remote coordination is required.

**Source:** [Spring transaction strategies](https://docs.spring.io/spring-framework/reference/data-access/transaction/strategies.html).

### `spring.async.void-unobserved-failure` (`BLOCK`)

**Avoid:** `@Async void` for work whose failure matters without an `AsyncUncaughtExceptionHandler` or external owner.

**Why:** The caller has no future through which to observe failure.

**Prefer:** Return `CompletableFuture`/another stage and compose it, or configure an explicit failure owner for genuine fire-and-forget work.

**Source:** [Spring `@Async`](https://docs.spring.io/spring-framework/reference/integration/scheduling.html#scheduling-annotation-support-async).

### `spring.bean.mutable-singleton-request-state` (`BLOCK`)

**Avoid:** Storing per-request/user mutable state in the default singleton bean scope.

**Why:** Concurrent requests share the same instance and overwrite each other's state.

**Prefer:** Method-local immutable data, an owned concurrent store, or the appropriate explicit scope.

**Source:** [Spring bean scopes](https://docs.spring.io/spring-framework/reference/core/beans/factory-scopes.html).

### `spring.webflux.blocking-event-loop` (`BLOCK`)

**Avoid:** Blocking JDBC, file, network, or sleep operations on Reactor event-loop threads.

**Why:** A small event-loop pool is stalled and unrelated requests stop progressing.

**Prefer:** Reactive/non-blocking APIs or isolate unavoidable blocking work on a bounded scheduler.

**Source:** [Reactor FAQ: wrapping blocking calls](https://projectreactor.io/docs/core/release/reference/faq.html#faq.wrap-blocking).

## JPA and Hibernate

### `jpa.fetch.eager-as-lazy-fix` (`WARN`)

**Avoid:** Switching broad associations to `EAGER` merely to suppress lazy-loading failures.

**Why:** Every load can pull large graphs and create hidden joins/N+1 behavior.

**Prefer:** Keep ownership/fetch needs explicit with query fetch joins, entity graphs, projections, or transaction-scoped mapping.

**Source:** [Hibernate fetching](https://docs.jboss.org/hibernate/orm/7.1/userguide/html_single/Hibernate_User_Guide.html#fetching).

### `jpa.query.n-plus-one` (`BLOCK`)

**Avoid:** Iterating entities and lazily loading the same association one query at a time.

**Why:** Query count grows with result size and can collapse latency/throughput.

**Prefer:** A query-specific fetch plan, projection, batch fetching, or explicit aggregate query.

**Source:** [Hibernate fetching strategies](https://docs.jboss.org/hibernate/orm/7.1/userguide/html_single/Hibernate_User_Guide.html#fetching).

### `jpa.fetch.collection-join-pagination` (`BLOCK`)

**Avoid:** Paginating a query that fetch-joins a to-many collection and assuming SQL-level page correctness.

**Why:** Row multiplication can force in-memory pagination or produce incomplete/distorted pages.

**Prefer:** Page root IDs first then fetch the graph, or use a query/projection designed for pagination.

**Source:** [Hibernate query pagination/fetch joins](https://docs.jboss.org/hibernate/orm/7.1/userguide/html_single/Hibernate_User_Guide.html#hql-limit-offset).

### `jpa.bulk-dml.stale-context` (`BLOCK`)

**Avoid:** Running JPQL/SQL bulk update/delete and continuing to trust already-managed entities.

**Why:** Bulk DML bypasses normal entity state synchronization and the persistence context becomes stale.

**Prefer:** Flush before the bulk operation when needed, then clear/refresh or isolate the operation.

**Source:** [Jakarta Persistence specification](https://jakarta.ee/specifications/persistence/3.2/jakarta-persistence-spec-3.2).

### `jpa.association.one-sided-bidirectional-update` (`BLOCK`)

**Avoid:** Updating only one side of a bidirectional association and assuming in-memory and persisted graphs remain consistent.

**Why:** The owning side controls persistence while the inverse side may expose stale state.

**Prefer:** Helper methods that update both sides as one invariant.

**Source:** [Hibernate bidirectional associations](https://docs.jboss.org/hibernate/orm/7.1/userguide/html_single/Hibernate_User_Guide.html#associations).

### `jpa.cascade.remove-many-to-many` (`BLOCK`)

**Avoid:** Cascading remove across many-to-many relationships between independently owned entities.

**Why:** Removing one aggregate can delete shared entities referenced elsewhere.

**Prefer:** Remove only the join link; model an explicit association entity when it has lifecycle/data.

**Source:** [Hibernate many-to-many lifecycle](https://docs.jboss.org/hibernate/orm/7.1/userguide/html_single/Hibernate_User_Guide.html#associations-many-to-many).

### `jpa.entity.generated-id-equality` (`WARN`)

**Avoid:** Equality/hash code that changes when a generated identifier is assigned while the entity is already in a set/map.

**Why:** Hash-based collections lose the entry and transient entities may compare incorrectly.

**Prefer:** A stable natural key when one exists or a documented identifier strategy consistent across transient/managed states.

**Source:** [Hibernate equals/hashCode](https://docs.jboss.org/hibernate/orm/7.1/userguide/html_single/Hibernate_User_Guide.html#domain-model-equalshashcode).

### `jpa.result.unbounded-materialization` (`BLOCK`)

**Avoid:** Loading an externally sized table/result graph fully into memory.

**Why:** Heap, persistence-context, and serialization costs grow without limit.

**Prefer:** Pagination, streaming with controlled persistence-context clearing, projections, or database-side aggregation.

**Source:** [Hibernate scrolling/streaming](https://docs.jboss.org/hibernate/orm/7.1/userguide/html_single/Hibernate_User_Guide.html#pc-batch-processing).

## jOOQ and Gradle

### `jooq.sql.interpolated-values` (`BLOCK`)

**Avoid:** Concatenating external values or identifiers into plain SQL strings.

**Why:** Values cross into SQL syntax and defeat binding, typing, plan reuse, and injection protection.

**Prefer:** Bind values/DSL parameters and allowlist any genuinely dynamic identifier.

**Source:** [jOOQ bind values](https://www.jooq.org/doc/latest/manual/sql-building/bind-values/).

### `gradle.dependency.dynamic-version` (`WARN`)

**Avoid:** `1.+`, `latest.release`, or other dynamic versions in reproducible builds.

**Why:** The same source can resolve to different artifacts over time.

**Prefer:** Fixed versions plus dependency locking/version catalogs and deliberate updates.

**Source:** [Gradle dynamic versions](https://docs.gradle.org/current/userguide/dependency_versions.html#sec:declaring_dependency_with_dynamic_version).

### `gradle.configuration.eager-task-realization` (`WARN`)

**Avoid:** Eagerly creating/configuring all tasks or using configuration-time APIs that realize unrelated tasks.

**Why:** Build configuration cost grows across every invocation.

**Prefer:** Task registration/configuration-avoidance APIs and lazy providers.

**Source:** [Gradle task configuration avoidance](https://docs.gradle.org/current/userguide/task_configuration_avoidance.html).

### `gradle.configuration.performing-task-work` (`BLOCK`)

**Avoid:** File/network/process work during the configuration phase that belongs to task execution.

**Why:** The work runs even when the task is not selected and can break configuration cache/reproducibility.

**Prefer:** Declare task inputs/outputs and perform side effects in the task action with lazy providers.

**Source:** [Gradle configuration cache requirements](https://docs.gradle.org/current/userguide/configuration_cache_requirements.html).
