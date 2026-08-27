# Beans, dependency injection, and scopes

**Priority:** CRITICAL  
**Rules:** 5

Keep object construction, lifecycle, scope, and thread-safety explicit.

Apply only the rules whose trigger exists in the candidate. Preserve the detected Spring Boot, Spring Framework, Java, Jakarta, servlet/reactive, database, security, and deployment contracts.

Examples are illustrative; preserve the repository baseline, imports, build system, framework generation, public API, and operational constraints.

<a id="bean-constructor-required-dependencies"></a>
## `bean-constructor-required-dependencies` — Use constructors for required dependencies

> Express mandatory collaborators in a constructor or factory method and reserve setters for genuinely optional or reconfigurable dependencies.

### Why it matters

A fully constructed bean has a visible invariant and is easier to instantiate outside the container.

### Avoid

Do not hide required dependencies in field injection or mutable setters.

### Prefer

Use one unambiguous constructor; inject the smallest collaborator contract and keep optional dependencies explicit.

### Nuance

Framework-generated or legacy components may constrain construction. Adapt at the boundary rather than making field injection the general default.

### Example

**Avoid**

```java
@Service
class CheckoutService {
    @Autowired PaymentGateway gateway;
}
```

**Prefer**

```java
@Service
class CheckoutService {
    private final PaymentGateway gateway;

    CheckoutService(PaymentGateway gateway) {
        this.gateway = gateway;
    }
}
```

### Sources

- **Spring dependency injection:** <https://docs.spring.io/spring-framework/reference/core/beans/dependencies/factory-collaborators.html>

<a id="bean-container-owns-managed-instances"></a>
## `bean-container-owns-managed-instances` — Respect container ownership

> Obtain Spring-managed components through dependency injection and let the container run their lifecycle and post-processors.

### Why it matters

Calling `new` on a managed component or using a static `ApplicationContext` bypasses proxies, configuration, scopes, validation, and lifecycle callbacks.

### Avoid

Do not service-locate beans from domain code or instantiate `@Transactional`, `@Async`, secured, or configuration-bound components manually.

### Prefer

Inject the component, inject a factory/provider for runtime selection, or construct a non-managed core object deliberately.

### Nuance

Tests may construct plain services directly when no Spring semantics are under test.

### Sources

- **Spring dependency injection:** <https://docs.spring.io/spring-framework/reference/core/beans/dependencies/factory-collaborators.html>
- **ApplicationContext capabilities:** <https://docs.spring.io/spring-framework/reference/core/beans/context-introduction.html>

<a id="bean-singleton-thread-safe"></a>
## `bean-singleton-thread-safe` — Treat singleton beans as shared concurrent objects

> Keep singleton services stateless or protect mutable state with an explicit concurrency and lifecycle policy.

### Why it matters

The default singleton scope shares one instance across requests and threads; request data stored in fields leaks or races.

### Avoid

Do not store per-request user, transaction, accumulator, or security state in ordinary singleton fields.

### Prefer

Pass request state through method arguments, use request/session scope for genuine scoped state, or use a dedicated concurrent owner.

### Nuance

A singleton cache can be valid when it is bounded, thread-safe, observable, and has explicit invalidation.

### Sources

- **Spring bean scopes:** <https://docs.spring.io/spring-framework/reference/core/beans/factory-scopes.html>

<a id="bean-scope-crossing-explicit"></a>
## `bean-scope-crossing-explicit` — Make scope crossings explicit

> Use scoped proxies, `ObjectProvider`, factories, or method injection when a longer-lived bean needs shorter-lived instances.

### Why it matters

Injecting a prototype into a singleton resolves it once; request/session beans also need a proxy or provider outside their active scope.

### Avoid

Do not assume `prototype` means a new object on every method call or dereference.

### Prefer

Select the scope deliberately and request a new/scoped instance through the container only at the point the lifecycle requires it.

### Nuance

Prefer passing data over injecting web-scoped beans deep into application/domain code.

### Sources

- **Spring bean scopes:** <https://docs.spring.io/spring-framework/reference/core/beans/factory-scopes.html>
- **ObjectProvider API:** <https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/beans/factory/ObjectProvider.html>

<a id="bean-break-cycles-not-hide"></a>
## `bean-break-cycles-not-hide` — Break circular dependencies at the ownership boundary

> Treat a dependency cycle as evidence that responsibilities, events, or orchestration are entangled.

### Why it matters

Lazy injection, setters, or circular-reference flags can make partially initialized objects and order-dependent behavior.

### Avoid

Do not enable circular references or scatter `@Lazy` merely to make the context start.

### Prefer

Move orchestration to one owner, split shared policy, introduce a narrow event/port where timing permits, or merge components that are actually one unit.

### Nuance

A documented framework callback cycle may be unavoidable, but prove initialization order and isolate it.

### Sources

- **Spring dependency injection and circular dependencies:** <https://docs.spring.io/spring-framework/reference/core/beans/dependencies/factory-collaborators.html>
