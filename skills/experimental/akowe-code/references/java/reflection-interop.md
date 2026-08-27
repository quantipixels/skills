# Reflection, serialization, and native interop

**Priority:** MEDIUM  
**Rules:** 5

Dynamic mechanisms trade compile-time guarantees for runtime flexibility. Keep them narrow and respect module, lifetime, and schema boundaries.

Apply only the rules relevant to the candidate and its actual Java baseline. Repository and framework contracts take precedence when they deliberately specialize a rule.

<a id="reflect-prefer-language-apis"></a>
## `reflect-prefer-language-apis` — Prefer ordinary language and service mechanisms over reflection

> Use interfaces, method references, annotation processing, ServiceLoader, or the Class-File API when they solve the problem directly.

### Why it matters

Reflection moves errors to runtime, weakens refactoring, and complicates modules and native images.

### Avoid

Avoid reflective access for internal convenience or to bypass visibility.

```java
Method method = target.getClass().getDeclaredMethod("handle", Event.class);
method.setAccessible(true);
method.invoke(target, event);
```

### Prefer

Use reflection at framework/tool boundaries with cached metadata, explicit errors, and focused tests.

```java
interface EventHandler {
    void handle(Event event);
}
handler.handle(event);
```

### Nuance

Frameworks legitimately require reflection; application code should not reproduce a general container casually.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Dev.java reflection:** <https://dev.java/learn/reflection/>
- **ServiceLoader:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/ServiceLoader.html>

<a id="reflect-respect-module-encapsulation"></a>
## `reflect-respect-module-encapsulation` — Do not solve access errors with broad opens

> Treat illegal reflective access as an architecture signal and open only the required package to the required module.

### Why it matters

`--add-opens` and open modules bypass strong encapsulation and expand attack/compatibility surfaces.

### Avoid

Avoid global `ALL-UNNAMED` opens as a permanent production fix.

```java
method.setAccessible(true); // relies on illegal deep reflection
```

### Prefer

Upgrade the library, use public APIs, add qualified `opens`, or isolate the compatibility adapter.

```java
module producer {
    opens com.example.model to approved.serializer;
}
```

### Nuance

Migration flags can be temporary; record why they exist and how they will be removed.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Module opens:** <https://docs.oracle.com/javase/specs/jls/se25/html/jls-7.html#jls-7.7.2>
- **JEP 403:** <https://openjdk.org/jeps/403>

<a id="serial-explicit-wire-format"></a>
## `serial-explicit-wire-format` — Use explicit versioned schemas for durable or remote data

> Do not make Java object shape the external storage/message contract by accident.

### Why it matters

Class names, fields, constructors, serialVersionUID, and library versions evolve differently from business schemas.

### Avoid

Avoid native Java serialization as a new database, cache, message, or API format.

```java
final class Order implements Serializable {
    Customer customer;
    Money total;
}
```

### Prefer

Choose a documented format/schema, define compatibility rules, validate inputs, and test old/new fixtures.

```java
record OrderMessage(String id, long totalMinor, String currency) {}
// Map explicitly through a versioned JSON/Protobuf schema.
```

### Nuance

In-process ephemeral serialization has a narrower risk but still needs trust and lifecycle bounds.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **Java object serialization spec:** <https://docs.oracle.com/en/java/javase/25/docs/specs/serialization/>
- **Serialization filtering:** <https://docs.oracle.com/en/java/javase/25/core/serialization-filtering1.html>

<a id="interop-no-jdk-internals"></a>
## `interop-no-jdk-internals` — Do not depend on unsupported JDK internals

> Use Java SE/JDK supported APIs rather than `sun.*`, non-exported packages, or implementation-specific behavior.

### Why it matters

Internal APIs can change without compatibility guarantees and are increasingly encapsulated.

### Avoid

Avoid reflection or command-line opens to keep internal APIs accessible.

```java
import sun.misc.Unsafe;
```

### Prefer

Use supported replacements, contribute missing capability, or isolate a version-pinned adapter with tests.

```java
import java.lang.invoke.VarHandle;
// or another supported Java SE/JDK API matching the requirement
```

### Nuance

Some `jdk.*` modules are supported JDK APIs but not Java SE; state that portability boundary.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JEP 403:** <https://openjdk.org/jeps/403>
- **JDK API overview:** <https://docs.oracle.com/en/java/javase/25/docs/api/>

<a id="interop-ffm-over-jni"></a>
## `interop-ffm-over-jni` — Prefer the Foreign Function and Memory API for new native interop

> On Java 22+, use `java.lang.foreign` instead of introducing JNI when the supported API fits.

### Why it matters

FFM provides explicit lifetimes, layouts, downcalls/upcalls, and safer memory access without generated JNI glue.

### Avoid

Avoid new JNI code solely because it is the historical option.

```java
native long checksum(long address, long size);
```

### Prefer

Use Arena/MemorySegment/Linker with confined lifetimes, bounds, and native-library validation.

```java
try (Arena arena = Arena.ofConfined()) {
    MemorySegment data = arena.allocateFrom(ValueLayout.JAVA_BYTE, bytes);
    int result = (int) checksumHandle.invokeExact(data, data.byteSize());
}
```

### Nuance

JNI remains necessary for existing ecosystems and capabilities not covered by FFM; isolate it behind a Java API.

The snippets are illustrative; preserve the repository baseline, surrounding contract, imports, checked-exception policy, and framework ownership.

### Sources

- **JEP 454:** <https://openjdk.org/jeps/454>
- **java.lang.foreign:** <https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/foreign/package-summary.html>
