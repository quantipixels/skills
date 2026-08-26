# Security-sensitive coding

**Priority:** CRITICAL  
**Rules:** 5

Security rules protect trust boundaries, secrets, resource limits, and parser configuration. Treat external input as data, not executable syntax.

Apply only the rules relevant to the candidate and its actual Java baseline. Repository and framework contracts take precedence when they deliberately specialize a rule.

<a id="sec-no-native-serialization-untrusted"></a>
## `sec-no-native-serialization-untrusted` — Do not deserialize untrusted Java object streams

> Prefer explicit data formats and schemas; if legacy deserialization is unavoidable, apply strict filters before reading objects.

### Why it matters

Native serialization can instantiate unexpected gadget graphs and invoke code during deserialization.

### Avoid

Avoid `ObjectInputStream.readObject()` on network, user, file-upload, or cross-trust data.

```java
try (var in = new ObjectInputStream(socket.getInputStream())) {
    return (Message) in.readObject();
}
```

### Prefer

Use JSON/CBOR/Protobuf/etc. with allowlisted types and validation, or configure `ObjectInputFilter` plus integrity/authentication.

```java
try (InputStream input = socket.getInputStream()) {
    byte[] payload = input.readNBytes(Math.addExact(maxBytes, 1));
    if (payload.length > maxBytes) {
        throw new PayloadTooLargeException(maxBytes);
    }
    Message message = jsonCodec.decode(payload, Message.class);
}
```

### Nuance

Filtering reduces risk but does not make an unstable Java serialization contract a good external protocol.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Serialization filtering:** <https://docs.oracle.com/en/java/javase/25/core/serialization-filtering1.html>
- **Secure coding guidelines:** <https://www.oracle.com/java/technologies/javase/seccodeguide.html>

<a id="sec-parameterized-sql"></a>
## `sec-parameterized-sql` — Bind SQL values instead of concatenating them

> Use PreparedStatement or a type-safe query API for every untrusted value.

### Why it matters

String concatenation allows data to alter SQL syntax and often mishandles quoting and encodings.

### Avoid

Avoid building WHERE, INSERT, ORDER, or LIMIT clauses from raw request strings.

```java
String sql = "select * from users where email = '" + email + "'";
statement.executeQuery(sql);
```

### Prefer

Bind values; allowlist and map identifiers/operators that cannot be parameterized.

```java
try (PreparedStatement statement =
         connection.prepareStatement("select * from users where email = ?")) {
    statement.setString(1, email);
    try (ResultSet rows = statement.executeQuery()) {
        return readUsers(rows);
    }
}
```

### Nuance

A prepared statement is only safe when the SQL structure itself is fixed or allowlisted.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **PreparedStatement:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.sql/java/sql/PreparedStatement.html>
- **Oracle secure coding guidelines:** <https://www.oracle.com/java/technologies/javase/seccodeguide.html>

<a id="sec-secure-random"></a>
## `sec-secure-random` — Use SecureRandom for security decisions

> Generate tokens, nonces, salts, keys, and unpredictable identifiers with a cryptographic RNG.

### Why it matters

`Random` and `ThreadLocalRandom` are designed for simulation/performance, not adversarial unpredictability.

### Avoid

Do not use timestamps, counters, UUID version assumptions, or ordinary PRNGs for secrets.

```java
String token = Long.toHexString(ThreadLocalRandom.current().nextLong());
```

### Prefer

Use `SecureRandom`, appropriate key generators, and protocol-defined entropy lengths.

```java
private static final SecureRandom SECURE_RANDOM = new SecureRandom();

byte[] bytes = new byte[32];
SECURE_RANDOM.nextBytes(bytes);
String token = Base64.getUrlEncoder().withoutPadding().encodeToString(bytes);
```

### Nuance

SecureRandom is not a password hashing function; use a dedicated password KDF.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **SecureRandom:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/security/SecureRandom.html>
- **Java security guide:** <https://docs.oracle.com/en/java/javase/25/security/>

<a id="sec-secret-redaction"></a>
## `sec-secret-redaction` — Keep secrets out of source and diagnostics

> Inject credentials from secret management and log only allowlisted/redacted fields.

### Why it matters

Repositories, exceptions, heap dumps, traces, and log aggregation are durable disclosure channels.

### Avoid

Avoid hard-coded keys, tokens in URLs, full authorization headers, or record `toString()` output containing secrets.

```java
log.info("login failed user={} token={}", userId, accessToken);
```

### Prefer

Use secret stores/environment bindings, dedicated sensitive-value types, and redaction at the logging boundary.

```java
log.info("login failed user={} tokenHash={}", userId, tokenFingerprint);
```

### Nuance

Hashing a secret does not automatically make it safe to log if the value has low entropy.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Oracle secure coding guidelines:** <https://www.oracle.com/java/technologies/javase/seccodeguide.html>
- **System.Logger:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/System.Logger.html>

<a id="sec-xml-external-entities"></a>
## `sec-xml-external-entities` — Disable external XML resolution for untrusted documents

> Configure XML parsers/transformers to reject external entities, DTDs, and unexpected resource access.

### Why it matters

Default or incomplete configuration can permit file disclosure, SSRF, and denial of service.

### Avoid

Do not parse untrusted XML with an unconfigured factory.

```java
DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
Document document = factory.newDocumentBuilder().parse(input);
```

### Prefer

Enable secure processing, disable external DTD/schema access, and use an explicit resolver/allowlist where external resources are required.

```java
DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
factory.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);
factory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
factory.setFeature("http://xml.org/sax/features/external-general-entities", false);
factory.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
factory.setAttribute(XMLConstants.ACCESS_EXTERNAL_DTD, "");
factory.setAttribute(XMLConstants.ACCESS_EXTERNAL_SCHEMA, "");
Document document = factory.newDocumentBuilder().parse(input);
```

### Nuance

JAXP has several factories; harden each parser, transformer, and schema boundary actually used.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **XMLConstants:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.xml/javax/xml/XMLConstants.html>
- **JAXP security guide:** <https://docs.oracle.com/en/java/javase/25/security/java-api-xml-processing-jaxp-security-guide.html>
