# Numeric and time correctness

**Priority:** CRITICAL  
**Rules:** 5

Numbers and time carry units, precision, range, chronology, and timezone semantics. Choose types and operations that preserve them.

Apply only the rules relevant to the candidate and its actual Java baseline. Repository and framework contracts take precedence when they deliberately specialize a rule.

<a id="num-bigdecimal-string"></a>
## `num-bigdecimal-string` — Construct decimal values without binary-float artifacts

> Use decimal strings or `BigDecimal.valueOf` rather than `new BigDecimal(double)` for human decimal values.

### Why it matters

Most decimal fractions are not exactly representable as binary floating point.

### Avoid

Avoid `new BigDecimal(0.1)` for money, rates, or decimal protocol values.

```java
BigDecimal price = new BigDecimal(0.1);
```

### Prefer

Use `new BigDecimal("0.1")`, parsed source text, or `BigDecimal.valueOf(double)` when starting from a double.

```java
BigDecimal price = new BigDecimal("0.10");
// or BigDecimal.valueOf(0.1) when starting from a double contract
```

### Nuance

Define scale and rounding at the operation/domain boundary, not as scattered defaults.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **BigDecimal constructors:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/math/BigDecimal.html>
- **RoundingMode:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/math/RoundingMode.html>

<a id="num-bigdecimal-equality"></a>
## `num-bigdecimal-equality` — Choose BigDecimal numeric or representation equality deliberately

> Use `compareTo` for numeric equivalence and `equals` only when scale is part of identity.

### Why it matters

`1.0` and `1.00` compare numerically equal but are not `equals`-equal.

### Avoid

Do not use BigDecimal as a map key or assertion value without deciding whether scale matters.

```java
new BigDecimal("2.0").equals(new BigDecimal("2.00")); // false
```

### Prefer

Normalize scale by domain rule or use `compareTo(...) == 0` for numeric equality.

```java
new BigDecimal("2.0").compareTo(new BigDecimal("2.00")) == 0; // true
```

### Nuance

Changing scale can affect division and presentation; do not strip it blindly.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **BigDecimal equals/compareTo:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/math/BigDecimal.html>

<a id="num-exact-arithmetic"></a>
## `num-exact-arithmetic` — Detect integer overflow when it violates the contract

> Use exact arithmetic, bounds checks, or wider/domain types for counts, sizes, money minor units, and offsets.

### Why it matters

Java integer overflow wraps silently.

### Avoid

Avoid multiplication/addition on attacker- or data-controlled sizes without proving bounds.

```java
int total = quantity * unitPriceMinor;
```

### Prefer

Use `Math.addExact`, `multiplyExact`, checked conversion, or BigInteger where unbounded values are required.

```java
long total = Math.multiplyExact((long) quantity, unitPriceMinor);
```

### Nuance

Wraparound is valid for some hashes and low-level algorithms; make that intent explicit.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Math exact methods:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Math.html>
- **JLS integer operations:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-15.html>

<a id="time-java-time"></a>
## `time-java-time` — Use java.time types that match the timeline

> Choose Instant, OffsetDateTime, ZonedDateTime, LocalDate, Duration, or Period according to the domain.

### Why it matters

A `long` or legacy Date does not communicate timezone, calendar, or unit semantics.

### Avoid

Avoid storing local civil time as an Instant or elapsed duration as a timestamp.

```java
long expiresAtMillis = System.currentTimeMillis() + ttlSeconds * 1000L;
```

### Prefer

Use Instant for machine timeline points, LocalDate for calendar dates, and explicit zones/offsets for civil timestamps.

```java
Instant expiresAt = clock.instant().plus(Duration.ofSeconds(ttlSeconds));
```

### Nuance

Persist the original zone/offset when future human interpretation depends on it.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **java.time package:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/time/package-summary.html>
- **Dev.java date time:** <https://dev.java/learn/date-time/>

<a id="time-clock-injection"></a>
## `time-clock-injection` — Inject Clock at time-dependent boundaries

> Use a Clock to make current-time behavior deterministic and testable.

### Why it matters

Direct calls to `Instant.now()` or `LocalDate.now()` couple logic to the wall clock and create flaky boundary tests.

### Avoid

Avoid sprinkling current-time reads through domain logic.

```java
boolean expired(Instant deadline) {
    return Instant.now().isAfter(deadline);
}
```

### Prefer

Read time once at the boundary or inject `Clock`, then pass explicit instants/dates.

```java
final class Expiry {
    private final Clock clock;
    boolean expired(Instant deadline) {
        return clock.instant().isAfter(deadline);
    }
}
```

### Nuance

Do not add Clock to code that does not depend on current time; explicit values are simpler.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Clock:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/time/Clock.html>
- **Instant.now(Clock):** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/time/Instant.html#now(java.time.Clock)>
