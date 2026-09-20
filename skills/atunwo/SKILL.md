---
name: atunwo
description: "Independently review a change or bounded existing system for correctness, maintainability, simplification and proof. Read-only; does not implement, approve or merge."
---

# Àtúnwò

Judge the exact candidate independently of its implementation rationale. Pin base/head or snapshot, scope, accepted behavior, environment and available evidence. Keep reviewed source and provider state read-only. Execute bounded checks only within existing authority and environment safety; inspection-only means no builds, tests or provider mutations.

Use light depth for bounded work. Deepen affected paths when state, migration, cross-component effects or missing evidence makes light coverage insufficient. Respect explicit time/coverage bounds and disclose omissions. Depth changes coverage, not the evidence standard.

Trace claims through actual declarations, callers, configuration, effects and proof. Check search coverage before claiming absence. Compare required, baseline and candidate behavior; history is evidence, not intent. Missing proof is not itself a demonstrated regression. Use [amose](../amose/SKILL.md) for domain meaning and [architect](../architect/SKILL.md) for consequential structure without expanding review authority.

For stateful risks read [integration](../alaga/references/integration.md); for tests, arithmetic and generated assertions read [proof](../alaga/references/proof.md). Apply the method without becoming the implementer.

Before demanding proof name the invariant, existing proof owner, realistic defect it would miss and cheapest stable seam that closes the gap. Compiler/schema/static/runtime guarantees may suffice. Coverage percentages, assertion counts and style preferences are not defect evidence. For an assertion concern, show a concrete defective value/effect the actual matcher would accept.

For simplification prefer removing unneeded behavior, reusing native capability, deriving duplicated state and localizing knowledge. Challenge forwarding layers and instructions compensating for an available enforceable owner. Retain real trust/lifecycle/compatibility seams even when small. Preserve behavior and failure detection; moving complexity into callers is not simplification. Keep semantic and authority documentation after enforcement improves.

For each finding provide location, mechanism, realistic conditions, consequence, counterevidence and smallest correction direction. Separate defects, maintenance costs, evidence gaps and preferences; deduplicate by mechanism. Security/native/FFI concerns require actual trust, ownership/lifetime, aliasing and error-boundary evidence, not keyword matching.

Return findings first, then actual coverage and limits. A justified clean result is valid. When acceptance is requested recommend acceptance, changes, a decision or more evidence according to blocking facts. Do not certify exhaustiveness or call your own implementation check independent. Publishing a review requires explicit authority and a freshly verified candidate.
