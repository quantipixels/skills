# Version and platform baseline

**Priority:** CRITICAL  
**Rules:** 5

Expert Java starts by matching the code to the project's real Java baseline. New syntax and APIs are valuable only when the compiler, runtime, consumers, and deployment platform all support them.

Apply only the rules relevant to the candidate and its actual Java baseline. Repository and framework contracts take precedence when they deliberately specialize a rule.

<a id="base-detect-java-version"></a>
## `base-detect-java-version` — Detect the Java baseline first

> Read the toolchain, `--release`, runtime image, and consumer compatibility before choosing syntax or APIs.

### Why it matters

Java source level, API availability, bytecode level, runtime behavior, and library consumer baselines are separate constraints. Guessing from a developer machine can produce code that compiles locally but fails in CI, packaging, or downstream applications.

### Avoid

Do not infer the baseline from the latest installed JDK or from one source file.

```java
// Built with JDK 26 locally, but the project targets Java 17.
return values.getFirst();
```

### Prefer

Read Maven/Gradle toolchains, compiler release flags, module metadata, CI images, deployment runtime, and published-library compatibility. State any unresolved assumption.

```kotlin
// build.gradle.kts
java {
    toolchain.languageVersion.set(JavaLanguageVersion.of(17))
}
tasks.withType<JavaCompile>().configureEach {
    options.release.set(17)
}
```

### Nuance

For libraries, the consumer baseline usually controls even when maintainers build with a newer JDK.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **javac tool specification:** <https://docs.oracle.com/en/java/javase/25/docs/specs/man/javac.html>
- **Java SE 26 API:** <https://docs.oracle.com/en/java/javase/26/docs/api/>

<a id="base-no-preview-by-default"></a>
## `base-no-preview-by-default` — Keep preview and incubator features opt-in

> Use preview or incubator APIs only when the repository explicitly enables and accepts their lifecycle risk.

### Why it matters

Preview features can change or disappear and require matching compile/run flags. Incubator modules are intentionally outside the permanent Java SE API contract.

### Avoid

Do not introduce `--enable-preview`, incubator modules, or preview APIs merely because the active JDK provides them.

```text
javac --enable-preview --release 26 src/main/java/App.java
// Preview syntax introduced without a repository decision.
```

### Prefer

Use GA language and library features by default. When preview use is authorized, pin the exact JDK, flags, deployment support, migration plan, and tests.

```java
// Use GA Java syntax for the declared baseline.
// Enable preview only in an explicitly accepted, pinned experiment.
return switch (state) {
    case READY -> start();
    case STOPPED -> stop();
};
```

### Nuance

A demo or research branch can reasonably accept preview risk; a broadly consumed library usually cannot.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Java SE 26 specifications:** <https://docs.oracle.com/en/java/javase/26/docs/specs/index.html>
- **JEP 12: Preview Features:** <https://openjdk.org/jeps/12>

<a id="base-use-release"></a>
## `base-use-release` — Compile with `--release` for the target platform

> Use the compiler release mechanism rather than source/target flags alone when targeting an older Java platform.

### Why it matters

`--release` constrains language level, bytecode target, and documented API signatures together. `-source` and `-target` alone can still let newer APIs leak into older-targeted code.

### Avoid

Do not claim Java 17 compatibility while compiling against unrestricted Java 25 or 26 APIs.

```text
javac -source 17 -target 17 Main.java
// Newer JDK APIs are still visible during compilation.
```

### Prefer

Configure Maven or Gradle to use the target release and test on a matching runtime where compatibility matters.

```text
javac --release 17 Main.java
```

### Nuance

Multi-release JARs are an advanced compatibility mechanism; use them only with a deliberate packaging and test matrix.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **javac `--release`:** <https://docs.oracle.com/en/java/javase/25/docs/specs/man/javac.html>
- **JEP 247:** <https://openjdk.org/jeps/247>

<a id="base-prefer-standard-library"></a>
## `base-prefer-standard-library` — Prefer fit-for-purpose Java SE APIs

> Use maintained Java SE abstractions before adding custom mechanisms or dependencies that solve the same problem.

### Why it matters

The JDK APIs integrate with the language, modules, security model, diagnostics, virtual threads, and long-term compatibility. Reimplementations often miss edge cases and operational behavior.

### Avoid

Do not hand-roll date/time, URI, path, HTTP, concurrency, collections, or encoding primitives when the platform already owns the contract.

```java
final class DateMath {
    static long addDays(long epochMillis, int days) {
        return epochMillis + days * 86_400_000L;
    }
}
```

### Prefer

Start with `java.time`, `Path`/`Files`, `URI`, `HttpClient`, collections, and `java.util.concurrent`; add a dependency only for a distinct capability.

```java
Instant expiresAt = createdAt.plus(Duration.ofDays(days));
```

### Nuance

Standard-library preference is not dependency prohibition. A focused library can be better when it materially improves correctness or domain fit.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Java SE 25 API overview:** <https://docs.oracle.com/en/java/javase/25/docs/api/>
- **Dev.java:** <https://dev.java/learn/>

<a id="base-remove-deprecated-for-removal"></a>
## `base-remove-deprecated-for-removal` — Treat removal deprecations as migration work

> Replace APIs deprecated for removal and verify the repository with deprecation-analysis tools.

### Why it matters

Removal deprecations represent an announced compatibility break, often because an API is unsafe, obsolete, or blocks platform evolution.

### Avoid

Do not suppress warnings around APIs such as asynchronous thread termination or obsolete platform facilities without a migration decision.

```java
thread.stop();
```

### Prefer

Inspect the replacement guidance, run `jdeprscan` where applicable, and isolate unavoidable compatibility shims behind a named boundary.

```java
cancelled.set(true);
thread.interrupt();
thread.join(timeout.toMillis());
```

### Nuance

Ordinary deprecation can be a softer signal; `forRemoval=true` materially raises urgency.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Deprecated API list:** <https://docs.oracle.com/en/java/javase/25/docs/api/deprecated-list.html>
- **jdeprscan:** <https://docs.oracle.com/en/java/javase/25/docs/specs/man/jdeprscan.html>
