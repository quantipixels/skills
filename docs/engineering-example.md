# A retry fix that earns its complexity

A payment service sends a transfer, then loses the provider's reply. The caller retries. How do we avoid paying twice without building an unnecessary new subsystem?

This is an illustrative engineering case informed by QP's controlled retry and upgrade exercises. It explains a decision and the proof it needs. The provider contract below is assumed; no general model-performance gain is established.

## Establish the contract before choosing machinery

Assume the service already has a stable ID for each logical settlement and stores completed settlements. The provider accepts an idempotency key: within its supported scope and retention window, repeating the same key and intent returns the original result; reusing it for a different amount is rejected.

**Idempotency** means that retrying the same logical operation preserves its allowed effect. It does not mean that every request succeeds, or that a local transaction controls a remote provider.

The decision is whether the existing settlement ID can serve as that key. Check its uniqueness, tenant/environment scope, provider format and retention limits, and whether one settlement can legitimately require several distinct transfers. A familiar provider feature is useful only if its actual contract covers this operation.

| Approach | What it owns | When it fits |
| --- | --- | --- |
| New key on every attempt | No stable identity across retries | Unsuitable for the stated duplicate-effect constraint |
| Reuse the settlement ID and existing completion records | One identity for one logical effect, including previously completed work | Fits when the verified provider and business contracts align |
| Persist a separate key and operation lifecycle | Key mapping, state transitions, recovery and migration | Worth considering when existing identity or provider guarantees are insufficient |

The third approach is not inherently wrong. It must buy a needed guarantee that justifies the responsibility it adds. Fewer application lines are also not automatically better: work may merely have moved into configuration or operations.

## Prove the boundary that could fail

A test that throws before the provider transfers anything does not reproduce the lost-reply failure. The important sequence is:

1. Let the provider complete the transfer.
2. Lose its reply before the service records completion.
3. Reopen the service against its durable state and retry the same settlement.
4. Observe the provider's effect count and the application's durable result.

This is **fault injection**: introduce the particular failure at a controlled test boundary so the test can distinguish safe recovery from duplicate work. Keep it in an authorized test environment.

Also start from a database containing a settlement completed by the old implementation. Upgrade, retry it, and verify that the old completion still prevents another transfer. A clean-database pass cannot answer that question. Test changed intent under the same identity when the contract requires rejection.

In QP's retained local exercise, both initial designs passed the fresh-database acceptance checks. The additional upgrade probe exposed a duplicate transfer in the design that ignored existing completion records. That is evidence about those fixtures and outputs, not proof that a particular prompt sentence caused the design or that adding a table is always wrong. The exercise and its limitations are summarized in [PR #152](https://github.com/quantipixels/skills/pull/152).

## Keep the conclusions separate

Idempotency handles repeated operations. **Isolation** concerns overlapping operations that act on shared state. Two distinct refunds can each pass a sequential check and still exceed a shared limit under overlap. That needs a separate invariant, enforcement choice and relevant concurrent proof.

When many action orders matter, **stateful property testing** generates sequences against a small independent model of the promised behavior. It can search for a failing order and shrink it to a shorter explanation. Generated sequential actions do not establish correctness under concurrent execution.

Within QP, `architect` owns a consequential identity or shared-state design, `alaga` implements and proves the changed behavior, `atunwo` judges the candidate and its evidence independently, and `irinse` resolves a non-obvious tool requirement. Use only the owners needed for the actual question.

Sources: [AWS on idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/), [PostgreSQL isolation](https://www.postgresql.org/docs/current/transaction-iso.html), and [Hypothesis stateful testing](https://hypothesis.readthedocs.io/en/latest/stateful.html). The stated provider contract is an assumption of this example; verify a real provider's contract before applying it.
