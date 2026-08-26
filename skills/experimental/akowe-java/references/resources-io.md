# Resources, files, HTTP, and I/O

**Priority:** CRITICAL  
**Rules:** 5

I/O code must make lifetime, encoding, bounds, timeouts, and ownership explicit.

Apply only the rules relevant to the candidate and its actual Java baseline. Repository and framework contracts take precedence when they deliberately specialize a rule.

<a id="io-try-with-resources"></a>
## `io-try-with-resources` — Close every AutoCloseable deterministically

> Use try-with-resources for owned AutoCloseable resources; close or shut down older-baseline executors through the same explicit owner.

### Why it matters

Deterministic close handles success and failure while preserving suppressed exceptions.

### Avoid

Avoid manual close calls scattered across branches or reliance on finalization/GC.

```java
InputStream input = Files.newInputStream(path);
return input.readAllBytes(); // input not closed on every path
```

### Prefer

Acquire AutoCloseable resources in the try header in ownership order and keep their scope minimal. On Java baselines where ExecutorService is AutoCloseable, include it; on older baselines, shut it down in a reliable owner/finally boundary.

```java
try (InputStream input = Files.newInputStream(path)) {
    return parser.parse(input);
}
```

### Nuance

Do not close a resource the method does not own. Non-I/O streams over in-memory data usually need no close, and ExecutorService did not extend AutoCloseable on Java 17.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Try-with-resources:** <https://dev.java/learn/exceptions/try-with-resources/>
- **AutoCloseable (Java 25):** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/AutoCloseable.html>
- **ExecutorService (Java 17):** <https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ExecutorService.html>

<a id="io-path-files"></a>
## `io-path-files` — Use Path and Files for filesystem work

> Represent filesystem locations as Path rather than concatenated strings.

### Why it matters

Path preserves platform semantics and Files provides maintained, exception-aware operations.

### Avoid

Avoid manual separator concatenation, string prefix security checks, and legacy `File` APIs in new code.

```java
String config = baseDir + "/" + tenant + "/config.json";
```

### Prefer

Use `Path.resolve`, `normalize`, `toRealPath` where required, and `Files` operations.

```java
Path config = baseDir.resolve(tenant).resolve("config.json").normalize();
```

### Nuance

Normalization alone does not resolve symlinks; security boundaries may require real-path containment checks.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Path:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/nio/file/Path.html>
- **Files:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/nio/file/Files.html>

<a id="io-explicit-charset"></a>
## `io-explicit-charset` — Specify text encodings at boundaries

> Use an explicit charset for persistent, networked, or interoperable text.

### Why it matters

Platform defaults can differ across hosts and deployments, corrupting or misreading data.

### Avoid

Avoid constructors and conversions whose charset depends on the default when the format has a defined encoding.

```java
String text = new String(bytes);
Files.write(path, text.getBytes());
```

### Prefer

Use `StandardCharsets.UTF_8` or the protocol/file-specified charset.

```java
String text = new String(bytes, StandardCharsets.UTF_8);
Files.writeString(path, text, StandardCharsets.UTF_8);
```

### Nuance

Java's default charset is UTF-8 from JDK 18, but explicit boundary contracts remain clearer and support older baselines.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JEP 400:** <https://openjdk.org/jeps/400>
- **StandardCharsets:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/nio/charset/StandardCharsets.html>

<a id="io-bound-memory"></a>
## `io-bound-memory` — Stream or bound externally sized data

> Do not read arbitrary files, HTTP bodies, archives, or result sets fully into memory without a limit.

### Why it matters

Valid large inputs or hostile payloads can exhaust heap and stall GC.

### Avoid

Avoid `readAllBytes`, unbounded `BodyHandlers.ofByteArray`, or collecting entire streams when size is external.

```java
byte[] payload = response.body().readAllBytes();
```

### Prefer

Enforce size limits, stream incrementally, paginate, spool to disk, or reject oversized input.

```java
try (InputStream in = response.body()) {
    byte[] payload = in.readNBytes(Math.addExact(maxBytes, 1));
    if (payload.length > maxBytes) {
        throw new PayloadTooLargeException(maxBytes);
    }
    return parser.parse(payload);
}
```

### Nuance

Whole-value reads are appropriate for small trusted configuration with a documented maximum.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Files.readAllBytes:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/nio/file/Files.html#readAllBytes(java.nio.file.Path)>
- **HttpResponse.BodyHandlers:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.net.http/java/net/http/HttpResponse.BodyHandlers.html>

<a id="io-httpclient-reuse-timeouts"></a>
## `io-httpclient-reuse-timeouts` — Reuse HTTP clients and set timeout contracts

> Share configured HttpClient instances and define connect/request/deadline behavior.

### Why it matters

Clients own connection pools and TLS/session state; per-call clients waste resources, while missing timeouts can hold work indefinitely.

### Avoid

Avoid constructing an HttpClient for each request or relying on implicit infinite waiting.

```java
HttpResponse<String> load(URI uri) {
    return HttpClient.newHttpClient()
        .send(HttpRequest.newBuilder(uri).build(), BodyHandlers.ofString());
}
```

### Prefer

Reuse an immutable client, set connect and request timeouts, handle interruption/cancellation, and bound response bodies.

```java
private final HttpClient client = HttpClient.newBuilder()
    .connectTimeout(Duration.ofSeconds(2))
    .build();

HttpRequest request = HttpRequest.newBuilder(uri)
    .timeout(Duration.ofSeconds(5))
    .GET()
    .build();
```

### Nuance

A request timeout is not a complete end-to-end deadline when retries or multiple calls are involved.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **HttpClient:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.net.http/java/net/http/HttpClient.html>
- **HttpRequest.Builder.timeout:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.net.http/java/net/http/HttpRequest.Builder.html#timeout(java.time.Duration)>
