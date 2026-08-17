# When to mock

Prefer mocks at **system boundaries**:

- External APIs, such as payment and email providers
- Databases, sometimes; prefer a test database
- Time and randomness
- File systems, sometimes

Prefer not to mock:

- Your own classes or modules
- Internal collaborators

Mock an internal boundary only when a narrower unit test has clear value and the mock represents a stable contract. Prefer a real implementation when it is fast and deterministic.

## Designing for Mockability

At system boundaries, design interfaces that are easy to mock.

**1. Use dependency injection**

**Good:** inject the stable boundary.

```java
final class PaymentProcessor {
    private final PaymentClient client;

    PaymentProcessor(PaymentClient client) {
        this.client = client;
    }
}
```

**Bad:** construct the provider internally.

```java
final class PaymentProcessor {
    private final PaymentClient client =
        new StripeClient(System.getenv("STRIPE_KEY"));
}
```

**2. Prefer SDK-style interfaces over generic clients**

**Good:** expose typed operations.

```kotlin
interface UserApi {
    fun getUser(id: UserId): ExternalUser
    fun createOrder(request: CreateExternalOrder): ExternalOrder
}
```

**Bad:** expose one generic operation.

```kotlin
interface GenericApi {
    fun <T> execute(endpoint: String, method: HttpMethod, body: Any?): T
}
```

Specific operations give each mock one result shape without conditional setup and show which operation the test exercises.
