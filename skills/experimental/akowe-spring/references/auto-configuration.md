# Auto-configuration and starter design

**Priority:** HIGH  
**Rules:** 5

Use Boot's conditional extension model without stealing control from applications.

Apply only the rules whose trigger exists in the candidate. Preserve the detected Spring Boot, Spring Framework, Java, Jakarta, servlet/reactive, database, security, and deployment contracts.

Examples are illustrative; preserve the repository baseline, imports, build system, framework generation, public API, and operational constraints.

<a id="auto-prefer-starters-managed"></a>
## `auto-prefer-starters-managed` — Use the owning Boot starter and managed modules

> Choose the starter that matches the technology and Boot generation so auto-configuration, logging, validation, tests, and transitive versions align.

### Why it matters

Boot 4 modularization moved and renamed modules/starters; relying on accidental transitive dependencies makes upgrades brittle.

### Avoid

Do not add random implementation jars until a class appears or use classic starters as the permanent dependency model.

### Prefer

Start with the relevant starter, inspect the dependency tree, and add lower-level modules only for a documented reason.

### Nuance

During Boot 4 migration, classic starters can be a temporary bridge; remove them once explicit modules are known.

### Sources

- **Spring Boot 4 migration guide:** <https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide>
- **Spring Boot build systems:** <https://docs.spring.io/spring-boot/reference/using/build-systems.html>

<a id="auto-back-off-user-control"></a>
## `auto-back-off-user-control` — Auto-configuration must back off

> Create defaults only when the application has not supplied its own bean, property, or classpath decision.

### Why it matters

A library that unconditionally registers infrastructure makes customization and coexistence impossible.

### Avoid

Do not use unconditional component scanning or bean names that override application beans.

### Prefer

Use targeted `@ConditionalOnClass`, `@ConditionalOnMissingBean`, `@ConditionalOnProperty`, and ordered auto-configuration.

### Nuance

Conditions are evaluated against the bean definitions visible at that time; document ordering assumptions.

### Example

**Avoid**

```java
@AutoConfiguration
class ClientAutoConfiguration {
    @Bean Client client() { return new Client(); }
}
```

**Prefer**

```java
@AutoConfiguration
@ConditionalOnClass(Client.class)
class ClientAutoConfiguration {
    @Bean
    @ConditionalOnMissingBean
    Client client() { return new Client(); }
}
```

### Sources

- **Creating auto-configuration:** <https://docs.spring.io/spring-boot/reference/features/developing-auto-configuration.html>
- **ConditionalOnMissingBean:** <https://docs.spring.io/spring-boot/api/java/org/springframework/boot/autoconfigure/condition/ConditionalOnMissingBean.html>

<a id="auto-register-explicitly"></a>
## `auto-register-explicitly` — Register auto-configuration through Boot metadata

> Use `@AutoConfiguration` and the current imports metadata rather than expecting consumers to scan library packages.

### Why it matters

Component scanning couples discovery to package layout and may pull in unintended beans.

### Avoid

Do not place a library auto-configuration under the consumer's scan root or require `@ComponentScan` instructions.

### Prefer

List auto-configuration classes in the supported metadata and keep component scanning inside the library narrow or absent.

### Nuance

Boot 3 and 4 starter internals differ; detect the supported producer range before attempting one artifact for both generations.

### Sources

- **Creating auto-configuration:** <https://docs.spring.io/spring-boot/reference/features/developing-auto-configuration.html>
- **Spring Boot 4 migration guide:** <https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide>

<a id="auto-customize-before-replace"></a>
## `auto-customize-before-replace` — Use Boot customization hooks before replacing infrastructure

> Inject Boot-provided builders and customizers so SSL, codecs, metrics, tracing, timeouts, and environment conventions remain attached.

### Why it matters

Replacing a core bean can silently disable auto-configured instrumentation or later customizers.

### Avoid

Do not create raw `ObjectMapper`, `RestClient`, `WebClient`, task executor, or datasource instances when Boot exposes a builder/customizer path.

### Prefer

Customize the provided builder or register the narrow documented customizer; replace the bean only when the whole lifecycle is intentionally yours.

### Nuance

A full replacement is valid for a materially different implementation, but verify every lost auto-configured capability.

### Sources

- **Spring Boot auto-configuration:** <https://docs.spring.io/spring-boot/reference/using/auto-configuration.html>
- **Calling REST services:** <https://docs.spring.io/spring-boot/reference/io/rest-client.html>

<a id="auto-use-condition-report"></a>
## `auto-use-condition-report` — Use the condition report to explain configuration

> Inspect the condition evaluation report and bean definitions before guessing why an auto-configuration did or did not apply.

### Why it matters

Classpath, property, missing-bean, web-application, and ordering conditions can all control one outcome.

### Avoid

Do not add duplicate beans, exclusions, or broad component scans from symptoms alone.

### Prefer

Run with debug/actuator conditions where authorized, inspect positive and negative matches, then change the smallest controlling input.

### Nuance

Treat the report as sensitive operational data; do not expose it publicly.

### Sources

- **Spring Boot auto-configuration:** <https://docs.spring.io/spring-boot/reference/using/auto-configuration.html>
- **Conditions actuator endpoint:** <https://docs.spring.io/spring-boot/api/rest/actuator/conditions.html>
