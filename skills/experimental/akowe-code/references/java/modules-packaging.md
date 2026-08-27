# Modules, dependencies, and packaging

**Priority:** MEDIUM  
**Rules:** 5

Build and module boundaries make compatibility, reflection, services, and dependency ownership explicit.

Apply only the rules relevant to the candidate and its actual Java baseline. Repository and framework contracts take precedence when they deliberately specialize a rule.

<a id="mod-release-flag"></a>
## `mod-release-flag` — Align source, bytecode, and API baseline

> Configure compiler toolchains and `--release` in one source of truth.

### Why it matters

Mismatched IDE, CI, test, and packaging JDKs create accidental compatibility and reproducibility failures.

### Avoid

Avoid relying on the developer's JAVA_HOME or duplicating version numbers across plugins.

```text
// Maven says 17, Gradle toolchain says 21, CI runs 25.
```

### Prefer

Use Maven/Gradle toolchains, compiler release, CI matrices, and enforcer checks appropriate to the project.

```kotlin
// One build-owned baseline.
java {
    toolchain.languageVersion.set(JavaLanguageVersion.of(17))
}
tasks.withType<JavaCompile>().configureEach {
    options.release.set(17)
}
```

### Nuance

Running tests on newer JDKs is useful, but must not silently change the compile contract.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **javac:** <https://docs.oracle.com/en/java/javase/25/docs/specs/man/javac.html>
- **Maven compiler release:** <https://maven.apache.org/plugins/maven-compiler-plugin/examples/set-compiler-release.html>

<a id="mod-public-internal-boundary"></a>
## `mod-public-internal-boundary` — Separate exported API from internal implementation

> Export only packages that consumers should compile against and keep internals unexported/unopened.

### Why it matters

Accidental public packages and deep reflection become compatibility obligations.

### Avoid

Avoid broad `exports`/`opens` and public utility packages used only inside one module.

```java
module com.example.orders {
    exports com.example.orders.internal;
}
```

### Prefer

Use module exports, package visibility, service interfaces, and qualified opens for deliberate framework access.

```java
module com.example.orders {
    exports com.example.orders.api;
}
```

### Nuance

Non-modular projects can still enforce API/internal package conventions and compatibility checks.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Module declarations:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-7.html#jls-7.7>
- **Module API:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Module.html>

<a id="mod-no-split-packages"></a>
## `mod-no-split-packages` — Avoid split packages across modules and artifacts

> Give each package one clear owning module/artifact.

### Why it matters

Split packages conflict with JPMS and make class loading, resources, sealing, and ownership ambiguous.

### Avoid

Avoid adding classes to the same package from several modules or generated artifacts.

```text
// artifact-a and artifact-b both define com.example.shared
```

### Prefer

Refactor shared contracts into an owned module/package and keep adapters in distinct packages.

```text
// Each package has one artifact/module owner.
com.example.shared.api
com.example.shared.impl
```

### Nuance

The class path can tolerate split packages, but migration and tooling remain fragile.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JPMS resolution:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/module/package-summary.html>
- **Module system tutorial:** <https://dev.java/learn/modules/>

<a id="mod-minimize-dependencies"></a>
## `mod-minimize-dependencies` — Add dependencies for distinct owned capability

> Prefer a small, maintained dependency surface and remove libraries duplicated by the JDK or existing stack.

### Why it matters

Every dependency adds version, security, licensing, transitive, startup, native-image, and upgrade cost.

### Avoid

Avoid utility libraries for one trivial method or overlapping libraries for the same concern.

```text
implementation("legacy:http-client:1.0")
implementation("other:date-utils:2.0")
```

### Prefer

Check JDK/existing capabilities, inspect transitive dependencies, pin via managed versions, and document the boundary.

```text
// Use java.net.http and java.time when they meet the contract.
// Retain dependencies only for distinct capabilities.
```

### Nuance

A well-maintained library that owns a hard problem is often safer than custom code.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **jdeps:** <https://docs.oracle.com/en/java/javase/25/docs/specs/man/jdeps.html>
- **Java SE API:** <https://docs.oracle.com/en/java/javase/25/docs/api/>

<a id="mod-reproducible-build"></a>
## `mod-reproducible-build` — Make generated and packaged output reproducible

> Pin toolchains/plugins, isolate generated sources, avoid environment-dependent content, and verify the produced artifact.

### Why it matters

Non-reproducible builds undermine debugging, supply-chain verification, caching, and rollback.

### Avoid

Avoid embedding current timestamps, host paths, mutable remote versions, or untracked generated code without intent.

```kotlin
version = System.getenv("BUILD_VERSION")
archiveFileName = "app-${System.currentTimeMillis()}.jar"
```

### Prefer

Use dependency locks/BOMs, deterministic archive settings, clean builds, and artifact inspection/signing.

```kotlin
version = providers.gradleProperty("releaseVersion").get()
tasks.withType<AbstractArchiveTask>().configureEach {
    isPreserveFileTimestamps = false
    isReproducibleFileOrder = true
}
```

### Nuance

Release metadata may legitimately contain time; keep it in a defined manifest/source rather than incidental build state.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **jar tool:** <https://docs.oracle.com/en/java/javase/25/docs/specs/man/jar.html>
- **jarsigner:** <https://docs.oracle.com/en/java/javase/25/docs/specs/man/jarsigner.html>
