# Configuration, profiles, and secrets

**Priority:** CRITICAL  
**Rules:** 5

Bind external configuration into typed, validated, observable contracts.

Apply only the rules whose trigger exists in the candidate. Preserve the detected Spring Boot, Spring Framework, Java, Jakarta, servlet/reactive, database, security, and deployment contracts.

Examples are illustrative; preserve the repository baseline, imports, build system, framework generation, public API, and operational constraints.

<a id="config-properties-for-groups"></a>
## `config-properties-for-groups` — Use `@ConfigurationProperties` for owned configuration groups

> Bind related settings to one typed object instead of scattering strings through `@Value` fields.

### Why it matters

Type-safe binding supports relaxed names, metadata, conversion, validation, ownership, and tests.

### Avoid

Do not use many unrelated `@Value` expressions or read `Environment` throughout business code.

### Prefer

Define a stable prefix, bind a record/class, enable scanning/registration, and inject the configuration object into its owner.

### Nuance

Use `@Value` for a genuinely isolated value or Spring expression; do not force every constant into a properties class.

### Example

**Avoid**

```java
@Service
class Mailer {
    @Value("${mail.host}") String host;
    @Value("${mail.port}") int port;
}
```

**Prefer**

```java
@ConfigurationProperties("mail")
record MailProperties(String host, int port) {}

@Service
class Mailer {
    Mailer(MailProperties properties) { }
}
```

### Sources

- **Spring Boot externalized configuration:** <https://docs.spring.io/spring-boot/reference/features/external-config.html>

<a id="config-validate-at-startup"></a>
## `config-validate-at-startup` — Fail fast on invalid required configuration

> Validate configuration properties during context startup and model required, range, format, and nested constraints.

### Why it matters

Late configuration failures appear under load and can produce partially functioning instances.

### Avoid

Do not default production-critical endpoints, credentials, or capacities to placeholder values just to start.

### Prefer

Use `@Validated`, Jakarta constraints, nested `@Valid`, and custom validators where cross-field invariants require them.

### Nuance

Optional features may have optional configuration; validate only when the feature is enabled.

### Sources

- **Configuration properties validation:** <https://docs.spring.io/spring-boot/reference/features/external-config.html>

<a id="config-understand-precedence"></a>
## `config-understand-precedence` — Reason from the complete property-source order

> Identify the winning source and active profile/import before changing a property that appears ineffective.

### Why it matters

Command-line arguments, environment variables, profile documents, imports, test properties, and defaults can override one another.

### Avoid

Do not duplicate the same key across several files or add another source before locating the current winner.

### Prefer

Use the documented precedence, origin tracking, and configuration metadata; keep one authoritative default and explicit environment overrides.

### Nuance

Lists replace rather than merge in several binding scenarios; verify the exact binding semantics for complex structures.

### Sources

- **Spring Boot externalized configuration:** <https://docs.spring.io/spring-boot/reference/features/external-config.html>

<a id="config-profiles-select-environments"></a>
## `config-profiles-select-environments` — Use profiles for deployment/configuration groups, not business decisions

> Profiles should select beans or configuration appropriate to an environment or operating mode.

### Why it matters

When product behavior depends on profile strings, the real feature policy becomes hidden in deployment configuration and hard to test.

### Avoid

Do not encode customer entitlements, workflow states, or permanent feature flags as Spring profiles.

### Prefer

Use explicit feature/configuration properties or domain policy for runtime behavior; keep profile expressions small and documented.

### Nuance

A profile may activate a local stub or production integration; the integration contract should remain the same.

### Sources

- **Spring Boot profiles:** <https://docs.spring.io/spring-boot/reference/features/profiles.html>

<a id="config-secrets-stay-external"></a>
## `config-secrets-stay-external` — Keep secrets out of source and diagnostic endpoints

> Inject secrets from the deployment secret mechanism, environment, or config tree and minimize their lifetime and exposure.

### Why it matters

Properties files, Git history, logs, `/env`, and `/configprops` can become disclosure channels.

### Avoid

Do not commit production secrets, place tokens in profile files, or render complete configuration objects in logs.

### Prefer

Use mounted secret/config trees or an approved secret store, sanitize metadata, and secure or disable sensitive actuator access.

### Nuance

Environment variables are transport, not automatically a secure store; follow the platform's secret controls.

### Sources

- **Spring Boot externalized configuration and config trees:** <https://docs.spring.io/spring-boot/reference/features/external-config.html>
- **Actuator endpoints:** <https://docs.spring.io/spring-boot/reference/actuator/endpoints.html>
