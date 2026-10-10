# Evidence and findings

Detail behind the review method. Read it when a claim depends on identity, preserved behavior, proof strength or provider state.

## Ground the judgment

Pin candidate or snapshot, comparison base, scope, accepted behavior and evidence. Reuse the caller's requirements, risks, proof and requested decision. Follow callers, tests, configuration and history only to establish or falsify a material claim in the actual product and runtime.

Compare the brief's consequential interpretations with the actual requirement sources. An author-added concession needs a confirmed decision; an unresolved interpretation stays visible in the judgment. Tests written by the implementer are evidence, not the definition of intent. A delivery review judges the accepted change; a PR follow-up judges changed or contested evidence; a system assessment judges the bounded existing system.

A blocking gap (domain meaning, a consequential user choice, an external fact, an unresolved technical structure) goes back to the caller with the evidence. Stay read-only; do not invent requirements, start delivery or reopen unrelated decisions.

For provider reviews, pin target, base and head and preserve discussion identity. Missing or truncated evidence is a gap. Publish only when authorized; refresh the candidate before writing and verify the effect before retrying an uncertain write. A changed base or head invalidates dependent conclusions.

Distinguish source inspection, executed proof and live acceptance. Resolve declarations, overloads and callers when identity controls a claim; spelling matches are insufficient. A search absence needs known path, ignore rules, index freshness and result-limit coverage. Tool output, earlier findings and author rationale are leads, not validation. Rerun checks contaminated by concurrent operations on shared state.

## Assess and substantiate

Consider compliance, engineering quality, proof and credible failure paths separately. Passing tests do not establish maintainability; preference does not establish a defect. Use [boundary failures](boundary-failures.md) when framework enforcement, authorization, identity addressing, state, concurrency, retries, migration, recovery, verification gates or provider boundaries matter.

Compare baseline, current and required behavior. Historical implementation does not establish intent. Trace accepted differences and consequences to real consumers. Inspect existing implementations and comparable usage before alleging duplication or convention drift; cite the path and the concrete consequence. Different semantics or a justified departure need not share an implementation. For enums and statuses, inspect transitions, stored and wire representations and consumers; compilation does not prove integration.

When preservation is uncertain, compare material inputs and defaults, identity and admission, transitions, outputs and wire types, effects and errors, ordering, retries, concurrency and recovery. Cover cross-entry-point sequences among shared-state writers. Mark behavior preserved, intentionally changed, lost, disputed or unproved with exact source and proof provenance. Corrected requirements invalidate dependent conclusions.

Choose proof that distinguishes a plausible regression: characterization, differential checks, or focused contract, integration or concurrency checks at the affected boundary. Separate inspected, executed and proposed checks. Missing evidence is not demonstrated loss; material unknowns prevent an unconditional accept. Request extra proof only for a named realistic regression that existing guarantees cannot catch, at the cheapest stable boundary; missing per-method coverage is not a finding. For test consolidation, weak assertions or generated tests, use [test effectiveness](test-effectiveness.md).

For each finding, name location, mechanism, consequence, assumptions and the smallest correction direction. Seek counterevidence and safeguards; separate defects, maintenance costs, evidence gaps and preferences. Deduplicate by mechanism. Reject speculative requirements and unrelated debt. For a change, show how the candidate causes or exposes the issue; existing-system reviews may report older weaknesses. Rank by demonstrated consequence and realistic conditions, not repair effort. Maintenance findings need a concrete comprehension or change cost.

Other lenses: "is this safe to merge" uses [safety proof](safety-proof.md); several models reviewing one packet use [panel review](panel-review.md); unsafe or native code and FFI use [native boundaries](native-boundaries.md). For security-sensitive caller mistakes, challenge defaults, invalid configuration and errors at the protected effect.

## Verdicts

For acceptance, return `RECOMMEND_ACCEPT`, `RECOMMEND_CHANGES`, `DECISION_REQUIRED` or `INSUFFICIENT_EVIDENCE` according to blockers and evidence. Existing-system, structure and simplification-only reviews need no acceptance verdict. State depth and actual coverage; deep review is not exhaustive certification. When useful, classify contested claims as `CONFIRMED | NARROWED | REJECTED | DUPLICATE | UNPROVED`.
