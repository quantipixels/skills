# Stack detection

Detect the stack from authoritative project evidence before selecting guidance.

## Evidence order

1. Repository/toolchain instructions and locked build configuration.
2. Language/compiler/runtime version declarations.
3. Dependency/BOM/plugin metadata and framework modules.
4. Deployment/runtime image when it constrains APIs.
5. Source imports/annotations only as supporting evidence.

Record:

```text
language + version/baseline
runtime/platform
general framework + version
material modules (web, data, security, reactive, etc.)
build/dependency-management owner
preview/EAP/incubator flags
consumer compatibility range when this is a library
```

Do not infer a newer API baseline because a newer JDK/Kotlin/OTP is installed locally. Do not assume framework defaults from current online documentation when the repository is on an older generation.

## Multi-stack candidates

Load only layers that control the touched code. Examples:

```text
Kotlin + Spring + JPA
→ Kotlin + Spring packs; Spring/JPA-specific guidance specializes generic Kotlin/JVM guidance.

Elixir + Phoenix LiveView
→ Elixir + Phoenix packs; Phoenix process/web lifecycle specializes generic OTP process guidance.

Java library with no framework
→ Java pack only.
```

For an unknown framework, do not create a new public skill. Pin its exact version and use the bounded research policy for the task-local questions that can change the implementation.
