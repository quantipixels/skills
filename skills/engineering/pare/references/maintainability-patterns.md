# Maintainability patterns

Use this when a candidate or audited subsystem shows a recurring maintainability signal that needs calibrated investigation. These patterns are **signals, never findings**. A recommendation still requires candidate-specific evidence of maintenance cost, ownership failure, invalid state, unnecessary mechanism, or a smaller credible form.

Repository instructions, accepted architecture/domain constraints, confirmed local craft, exact code behavior, and current platform facts outrank a generic heuristic. A local pattern is not immune from defect or complexity evidence, but do not present a textbook preference as a repository violation.

## Mysterious name

**Signal:** a name hides the domain concept, state, responsibility, or unit it represents.

**Good finding:** `pending` actually means `payment-authorized-but-not-captured`; callers branch on the distinction and current naming causes repeated misuse.

**Bad finding:** prefer a longer synonym because it sounds clearer without showing ambiguity or maintenance consequence.

**Counterexample:** short conventional names inside a tiny local algorithm can be clearer than verbose domain prose.

**Evidence that upgrades it:** conflicting caller assumptions, repeated clarifying comments, incorrect branch behavior, or domain-language mismatch.

## Duplicated policy

**Signal:** the same business, lifecycle, validation, mapping, or failure rule appears in several places.

**Good finding:** three entry points independently compute eligibility and have already diverged on one condition; move the policy to its natural owner.

**Bad finding:** two similar loops share syntax but operate under different contracts.

**Evidence that upgrades it:** same invariant, same change reason, divergent copies, or repeated synchronized edits.

## Feature envy / displaced responsibility

**Signal:** code repeatedly reaches into another owner's state to make decisions that belong with that state.

**Good finding:** service code reads five aggregate fields and reproduces the aggregate's transition rule; move the transition behind the aggregate owner.

**Bad finding:** an application coordinator reads a result to decide which independent workflow to start.

**Evidence that upgrades it:** intimate foreign-state knowledge, repeated cross-owner branching, invalid transitions, or synchronization burden.

## Data clump

**Signal:** the same group of values travels together because it represents one concept or contract.

**Good finding:** `currency`, `amount`, and `scale` are passed independently through many APIs and invalid combinations exist; use the existing money type or introduce one owned value only if it closes that state space.

**Bad finding:** package three unrelated arguments into a parameter object merely to shorten a signature.

**Evidence that upgrades it:** repeated co-change, invariant coupling, invalid combinations, or lost units/identity.

## Primitive obsession

**Signal:** primitives carry domain identity, units, state, or validation that callers must remember manually.

**Good finding:** raw strings for verified/unverified phone identity allow unsupported values and repeated parsing; use an owned type/state model.

**Bad finding:** wrap every integer or string in a type with no invariant or behavior.

**Evidence that upgrades it:** invalid values, repeated conversion/validation, unit mistakes, or branching on encoded primitive states.

## Repeated switches

**Signal:** the same variant/state dispatch appears across several locations.

**Good finding:** every new payment method requires synchronized switches in validation, execution, failure mapping, and display; localize the behavior where the variant is owned.

**Bad finding:** one exhaustive switch is the clearest local representation of a closed state machine.

**Evidence that upgrades it:** repeated co-change, missing branch defects, or scattered owner policy.

## Shotgun surgery

**Signal:** one conceptual change requires small edits across many unrelated locations.

**Good finding:** changing retry policy touches six callers because retry semantics have no owner; move the policy behind the integration boundary.

**Bad finding:** a legitimate public contract change updates independent consumers that each own different behavior.

**Evidence that upgrades it:** same reason for change, repeated synchronized edits, or omissions caused by scattered policy.

## Divergent change

**Signal:** one module changes for several unrelated reasons or owners.

**Good finding:** a single service changes for billing policy, provider transport, reporting layout, and persistence migration; separate by owned responsibility where that reduces coupled change.

**Bad finding:** split a cohesive module because it has several methods.

**Evidence that upgrades it:** unrelated change histories, mixed authority/lifecycle, conflicting proof seams, or broad dependency fan-in caused by unrelated responsibilities.

## Speculative generality

**Signal:** abstraction, configuration, interface, hook, or extension point exists for unproved variation.

**Good finding:** two interfaces and a factory wrap one stable implementation and no current contract requires substitution; delete or inline the variation seam.

**Bad finding:** remove an adapter that owns a real external API, trust, lifecycle, compatibility, or testing boundary because there is only one provider today.

**Evidence that upgrades it:** no current responsibility, no consumers requiring variation, forwarding-only behavior, or hypothetical rationale.

## Message chain

**Signal:** callers navigate a long ownership graph to obtain data or trigger behavior.

**Good finding:** callers repeatedly traverse `order.customer.profile.account.region` and then implement region policy; expose the policy/result at the correct owner.

**Bad finding:** a short local read of nested immutable data with no repeated policy or coupling consequence.

**Evidence that upgrades it:** repeated chain knowledge, fragile navigation, null/state handling replicated by callers, or foreign policy decisions.

## Middle man

**Signal:** a type forwards calls while owning no policy, lifecycle, translation, state, trust, or integration responsibility.

**Good finding:** wrapper mirrors every repository method unchanged; remove it and depend on the actual owner.

**Bad finding:** label a provider adapter as middle man when it owns authentication, retries, error translation, compatibility, or isolation.

**Evidence that upgrades it:** forwarding-only implementation, no independent contract, no boundary consequence, and safe direct ownership.

## Invalid or duplicated state

**Signal:** stored/derived state can disagree or represents combinations the domain does not permit.

**Good finding:** stored order total can diverge from owned line items; derive it at the owner when timing/cost contracts allow.

**Bad finding:** derive a value that must be snapshotted for legal/audit history or expensive external computation.

**Evidence that upgrades it:** divergence path, synchronization code, stale reads, impossible combinations, or duplicate state transitions.

## Thin abstraction

**Signal:** a seam has interface/coordination cost similar to or greater than the behavior it hides.

**Good finding:** interface + implementation + factory only rename one library call; use the library directly.

**Bad finding:** reject a small public interface that hides substantial policy or gives high leverage to callers.

**Evidence that upgrades it:** deletion preserves contracts while removing navigation, forwarding, test doubles, or configuration ceremony.

## Proof-shaped implementation

**Signal:** production structure exists mainly to satisfy shallow or implementation-detail tests rather than a real runtime contract.

**Good finding:** public accessor and wrapper exist only so tests can inspect a private intermediate value; move proof to the stable observable invariant and delete the production seam when safe.

**Bad finding:** remove an observability seam required by operations because tests also use it.

**Evidence that upgrades it:** no runtime consumer, stronger proof owner exists, and deletion preserves public/operational contracts.

## Convert a signal into a recommendation

Before retaining a pattern-based finding, answer:

```text
What exact maintenance or state cost exists?
What owner or contract is misplaced, duplicated, or missing?
What is the smallest credible form?
What counterexample could make the current shape correct?
What evidence rules that counterexample out?
What proof would show the smaller form preserves behavior?
```

If those answers are weak, keep investigating or return no finding. Do not accumulate a smell inventory as if count or presence were a quality score.
