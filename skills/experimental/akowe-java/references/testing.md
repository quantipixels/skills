# Testing and proof

**Priority:** HIGH  
**Rules:** 5

Tests should prove observable contracts and important failure paths while remaining deterministic and maintainable.

Apply only the rules relevant to the candidate and its actual Java baseline. Repository and framework contracts take precedence when they deliberately specialize a rule.

<a id="test-behavior-contract"></a>
## `test-behavior-contract` — Test behavior through stable contracts

> Assert caller-visible results, state transitions, side effects, and failures rather than private implementation steps.

### Why it matters

Implementation-coupled tests block safe refactoring without improving confidence.

### Avoid

Avoid verifying every internal call or exposing private members solely for tests.

```java
verify(repository).save(any());
verify(clock).instant();
```

### Prefer

Test through public/package contracts; use focused unit tests for pure logic and integration tests for adapters.

```java
assertEquals(request.email(), service.create(request).email());
```

### Nuance

Interaction verification is appropriate when the interaction itself is the contract, such as exactly-once publication.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JUnit 5 user guide:** <https://junit.org/junit5/docs/current/user-guide/>
- **Java testing on Dev.java:** <https://dev.java/learn/testing/>

<a id="test-boundary-parameterized"></a>
## `test-boundary-parameterized` — Use parameterized tests for input partitions

> Cover equivalence classes and boundaries with named data rather than duplicated test bodies.

### Why it matters

Data-driven tests make omissions visible and reduce copy/paste drift.

### Avoid

Avoid dozens of nearly identical methods or one opaque loop with no per-case reporting.

```java
@Test void rejectsMinusOne() { /* duplicate body */ }
@Test void rejectsZero() { /* duplicate body */ }
@Test void acceptsOne() { /* duplicate body */ }
```

### Prefer

Use `@ParameterizedTest`, method sources, and descriptive case names for valid/invalid partitions.

```java
@ParameterizedTest
@CsvSource({"-1,false", "0,false", "1,true"})
void validatesBoundary(int value, boolean valid) {
    assertEquals(valid, validator.isValid(value));
}
```

### Nuance

A scenario with unique setup or failure meaning deserves a dedicated test.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JUnit parameterized tests:** <https://junit.org/junit5/docs/current/user-guide/#writing-tests-parameterized-tests>

<a id="test-deterministic-time-random"></a>
## `test-deterministic-time-random` — Control time, randomness, locale, and environment

> Inject or pin nondeterministic dependencies so tests do not depend on the current machine or instant.

### Why it matters

Wall-clock, random, timezone, locale, and environment coupling creates flaky and non-reproducible tests.

### Avoid

Avoid `Thread.sleep`, `Instant.now`, default locale/timezone, and uncontrolled random values in assertions.

```java
@Test
void tokenExpires() {
    Token token = service.issue();
    assertTrue(token.expiresAt().isAfter(Instant.now()));
}
```

### Prefer

Use Clock, seeded/supplied randomness, explicit locale/zone, and test configuration.

```java
Clock clock = Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC);
Token token = new TokenService(clock, seededRandom).issue();
assertEquals(clock.instant().plus(ttl), token.expiresAt());
```

### Nuance

Property tests may intentionally vary seeds; record the failing seed for reproduction.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Clock:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/time/Clock.html>
- **RandomGenerator:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/random/RandomGenerator.html>

<a id="test-no-sleep"></a>
## `test-no-sleep` — Synchronize tests on observable conditions, not sleep

> Wait for completion, a latch, future, event, or bounded condition with diagnostic timeout.

### Why it matters

Sleep is both slower than necessary and too short under load.

### Avoid

Avoid arbitrary delays to 'let the async work finish'.

```java
service.start();
Thread.sleep(1000);
assertTrue(service.ready());
```

### Prefer

Join futures/tasks, await latches, poll a stable observable state with a deadline, or use framework test support.

```java
service.start();
assertTrue(service.readyFuture().get(2, TimeUnit.SECONDS));
```

### Nuance

A timeout remains necessary to prevent hangs; make failure output expose the pending state.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **CountDownLatch:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/CountDownLatch.html>
- **Future:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/Future.html>

<a id="test-real-boundary-integration"></a>
## `test-real-boundary-integration` — Test real adapters at critical boundaries

> Use actual serialization, SQL, HTTP, filesystem, modules, or framework configuration where mocks cannot prove compatibility.

### Why it matters

Mocks prove the test author's model, not the external system's current contract.

### Avoid

Avoid testing persistence mappings or wire formats solely through repository/client mocks.

```java
when(mapper.writeValueAsString(any())).thenReturn("{}");
assertTrue(adapter.send(order).isSuccessful());
```

### Prefer

Keep unit logic fast, then add focused integration/contract tests for high-risk adapters.

```java
String json = realMapper.writeValueAsString(order);
Order decoded = realMapper.readValue(json, Order.class);
assertEquals(order, decoded);
```

### Nuance

Do not turn every test into full-system setup; choose the smallest real boundary that can falsify the claim.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JUnit user guide:** <https://junit.org/junit5/docs/current/user-guide/>
- **Java HTTP Client:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.net.http/java/net/http/package-summary.html>
