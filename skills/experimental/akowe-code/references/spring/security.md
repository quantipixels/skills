# Spring Security boundaries

**Priority:** CRITICAL  
**Rules:** 5

Make authentication, request authorization, method authorization, browser protections, and credential handling explicit.

Apply only the rules whose trigger exists in the candidate. Preserve the detected Spring Boot, Spring Framework, Java, Jakarta, servlet/reactive, database, security, and deployment contracts.

Examples are illustrative; preserve the repository baseline, imports, build system, framework generation, public API, and operational constraints.

<a id="sec-explicit-filter-chain"></a>
## `sec-explicit-filter-chain` — Define an explicit, ordered `SecurityFilterChain`

> Declare which requests are public, authenticated, role/authority constrained, or denied, with the most specific rules first.

### Why it matters

Implicit defaults and broad matchers can expose endpoints or make one chain shadow another.

### Avoid

Do not end with `anyRequest().permitAll()` as a convenience or rely on controller presence for protection.

### Prefer

Prefer deny-by-default, isolate management endpoints, and test anonymous, authenticated, forbidden, and chain-order cases.

### Nuance

Multiple chains are valid for different protocols, but give each a precise matcher and order.

### Example

**Avoid**

```java
http.authorizeHttpRequests(auth -> auth
    .anyRequest().permitAll());
```

**Prefer**

```java
http.authorizeHttpRequests(auth -> auth
    .requestMatchers("/public/**", "/status/ready").permitAll()
    .anyRequest().authenticated());
```

### Sources

- **Spring Security authorize HTTP requests:** <https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html>

<a id="sec-method-authorization"></a>
## `sec-method-authorization` — Enforce sensitive use cases at the service boundary

> Use method authorization for operations whose permission must hold regardless of HTTP, messaging, scheduling, or internal invocation path.

### Why it matters

URL rules protect one adapter; another entry point can bypass them.

### Avoid

Do not scatter role checks inside controller branches or assume method security is enabled automatically.

### Prefer

Enable method security, express domain-oriented authorities/policies, and test the proxied invocation path.

### Nuance

Avoid duplicating the same rule in every layer; HTTP rules can remain coarse while the service owns the invariant.

### Sources

- **Spring Security method security:** <https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html>

<a id="sec-csrf-matches-auth-model"></a>
## `sec-csrf-matches-auth-model` — Keep CSRF protection aligned with browser authentication

> Retain CSRF protection for browser flows that automatically send session cookies or credentials.

### Why it matters

A browser can issue authenticated state-changing requests across origins even when the attacker cannot read the response.

### Avoid

Do not disable CSRF globally because the API uses JSON or because CORS is configured.

### Prefer

Disable or ignore CSRF only for stateless token-authenticated endpoints that do not rely on browser-managed credentials, and test the complete authentication model.

### Nuance

Applications can have separate browser and stateless chains with different CSRF policies.

### Sources

- **Spring Security CSRF:** <https://docs.spring.io/spring-security/reference/servlet/exploits/csrf.html>

<a id="sec-cors-central-and-specific"></a>
## `sec-cors-central-and-specific` — Configure CORS once with explicit origins, methods, headers, and credentials

> Spring Security must see CORS processing before authentication because preflight requests lack cookies.

### Why it matters

Duplicated MVC, filter, proxy, and annotation policies drift and can create wildcard credential exposure.

### Avoid

Do not combine `allowCredentials=true` with unrestricted origins or reflect arbitrary origins without an allowlist.

### Prefer

Use a central `CorsConfigurationSource` or the owning MVC config and test preflight plus actual requests.

### Nuance

CORS is not authorization; still authenticate and authorize the resource.

### Sources

- **Spring Security CORS:** <https://docs.spring.io/spring-security/reference/servlet/integrations/cors.html>

<a id="sec-credential-storage-and-redaction"></a>
## `sec-credential-storage-and-redaction` — Use adaptive password hashing and never expose credentials

> Delegate password storage to a supported `PasswordEncoder` and keep tokens, sessions, keys, and credentials out of logs and error bodies.

### Why it matters

Fast hashes and raw credential diagnostics make database or telemetry compromise materially worse.

### Avoid

Do not use plaintext, general-purpose digest algorithms, reversible encryption for passwords, or log bearer tokens.

### Prefer

Use a delegating encoder with an adaptive algorithm and upgrade encoding over time; redact authentication material at every boundary.

### Nuance

API keys and tokens have different storage/rotation contracts but share the no-logging rule.

### Sources

- **Spring Security password storage:** <https://docs.spring.io/spring-security/reference/features/authentication/password-storage.html>
- **Spring Security credentials erasure:** <https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/credentials-container.html>
