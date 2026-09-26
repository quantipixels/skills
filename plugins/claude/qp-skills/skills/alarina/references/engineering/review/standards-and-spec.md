# Standards and specification review

Read for a delivery candidate, including the review stage after Red → Green implementation. Keep Atúnwò's scope, evidence requirements and read-only boundary.

## Establish two independent questions

**Specification:** Does this candidate deliver the accepted behavior? Use the actual request, specification, ticket and confirmed decisions; a separate spec file is not required. Identify missing or partial requirements, incorrect outcomes and unrequested behavior. Cite the controlling requirement and affected path. Tests written by the implementer are evidence, not the definition of the user's intent.

**Standards:** Does this candidate meet applicable project conventions and justify its design? Read relevant repository instructions, contributor guidance, architecture and ADRs. Cite the actual rule for a violation. Project decisions override generic preferences. Use current formatter, compiler and lint evidence for what those tools establish; spend judgment on what they do not settle rather than duplicating their diagnostics.

Load detailed judgment-based standards here from the project's established owner, such as `CODEBASE_STANDARD.md`, `CODING_STANDARDS.md` or a contributor guide. Their shared authority does not require the implementer to carry the entire review checklist during construction. Mechanical violations should be covered by a suitable existing check; if the check is absent or ineffective, distinguish that enforcement gap from the candidate's violation and return any authorized repair to Alága.

Separate the questions even when one reviewer handles a bounded change. Use independently briefed reviewers when the breadth or competing concerns justify separate context, following [coordination](../../productivity/coordination.md). Give both the same pinned candidate and comparison base; supply the specification to its reviewer and standards sources to theirs. No fixed two-worker roster is required. Findings never authorize changes by themselves.

## Refactoring judgment

Assess the coherent working candidate before prescribing structural changes. Use [simplification](simplification.md) when unnecessary complexity is material and [module design](../architecture/module-design.md) when interface depth or ownership needs analysis. Fowler-style smells are hypotheses about change cost, not automatic violations or mechanical recipes:

- Similar code warrants extraction when it duplicates knowledge that must change together; different domain rules may need separate implementations.
- A repeated field group or primitive representation warrants a type when it hides a real invariant; do not wrap values merely to satisfy a label.
- Scattered edits or a module with several change reasons warrant inspecting ownership; do not infer the right boundary from file length or force one responsibility per command.
- A forwarding layer or navigation chain warrants tracing caller knowledge and real boundary guarantees before removal.
- An extension point without an actual consumer warrants a YAGNI challenge; preserve justified compatibility and recovery behavior.

For each warranted refactor, state the affected location, concrete burden, smallest correction direction and behavior/proof that must survive. Distinguish a blocking standard violation, a justified maintenance concern and an optional preference. A working, clear implementation may need no refactor.

Alága applies accepted changes and verifies them. Reassess affected findings against the new candidate when needed; retain valid earlier evidence for untouched paths. If a reviewer is separately assigned implementation, treat its edited portion as authored work when choosing any required independent review.
