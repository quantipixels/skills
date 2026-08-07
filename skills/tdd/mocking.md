# When to Mock

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

Pass external dependencies in rather than creating them internally:

```java
// Easy to mock
final class PaymentProcessor {
    private final PaymentClient paymentClient;

    PaymentProcessor(PaymentClient paymentClient) {
        this.paymentClient = paymentClient;
    }

    PaymentResult process(Order order) {
        return paymentClient.charge(order.total());
    }
}

// Hard to mock
final class HardCodedPaymentProcessor {
    private final PaymentClient paymentClient =
        new StripeClient(System.getenv("STRIPE_KEY"));

    PaymentResult process(Order order) {
        return paymentClient.charge(order.total());
    }
}
```

**2. Prefer SDK-style interfaces over generic clients**

Create one specific operation for each external action instead of one generic operation with conditional logic:

```kotlin
// GOOD: Each operation is independently mockable
interface UserApi {
    fun getUser(id: UserId): ExternalUser
    fun getOrders(userId: UserId): List<ExternalOrder>
    fun createOrder(request: CreateExternalOrder): ExternalOrder
}

// BAD: Mocking requires conditional logic inside the mock
interface GenericApi {
    fun <T> execute(
        endpoint: String,
        method: HttpMethod,
        body: Any?,
    ): T
}
```

The SDK approach means:

- Each mock returns one specific shape
- No conditional logic in test setup
- It is easier to see which endpoints a test exercises
- Each operation has type safety
