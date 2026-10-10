---
name: atunwo
description: Produces a review verdict with evidence-ranked findings. Covers a code change or PR, an existing codebase, the structure of a design, or a supplied fix ("is this PR's fix real"). Use for code review, "is this safe to merge", codebase assessment, simplification review, design review, or checking a proposed repair. Read-only; it does not make the corrections.
---

# Àtúnwò

Output: a working record (report) holding a review verdict, with findings ranked by demonstrated consequence.

Needs: a named change, branch, PR, system boundary, design candidate or supplied fix, and what it must do. If either is missing, or the request is not a review, return to the caller and say what is missing.

Judge the requested boundary independently. Keep source and Git state read-only. A review does not authorize corrections, approval, merge or deployment.

## Method

**Workflows** (`asoju`): for a large diff, lens fan-out (cheap scanners flag risks, you validate only the flags); for a high-stakes change, a two-model panel. A long change history or thread first gets a reader record.

Pick the subject; each has its own reference:

- **Change or PR**: judge correctness, behavior preservation, maintainability and proof of the accepted change.
- **Existing system**: read [codebase assessment](references/codebase-assessment.md); simplification focus, [simplification](references/simplification.md).
- **Structure of a design**: read [structure lens](references/structure-lens.md).
- **Supplied fix**: read [supplied fix](references/supplied-fix.md).
- **Skill or prompt change**: judge it against `ilana`'s authoring standard, plus whether agents would behave as intended.

Choose depth:

- **light** (default for a bounded review): inspect the relevant change or representative boundary, immediate consumers and existing proof. Trace concrete concerns far enough to substantiate or dismiss them.
- **deep**: when requested, or when credible state, cross-component, migration or unresolved-evidence risks make light insufficient. Trace producers, consumers, shared-state writers and failure and recovery paths end to end. Report unassessed areas. State or async syntax alone does not require deep.

Depth changes coverage, not the evidence standard or permission to act. Respect an explicit light or time-bounded request and surface the need for more instead of silently widening. Choose lenses from plausible consequences: authorization and security, data integrity, compatibility, concurrency and retries, performance, operation and recovery, test effectiveness. Trace the consequential boundary even for a tiny diff; a large mechanical change with strong proof needs neither every lens nor a roster. Respect requested focuses (defects, tests, simplification, a subsystem). Simplification-only and parity-only requests stay inspection-only: no tests, builds, provider writes or acceptance verdicts.

Ground every claim in evidence, not tool output, author rationale or earlier findings. Read [evidence and findings](references/evidence-and-findings.md) for pinning the candidate, identity, preservation, proof strength, provider reviews, finding format and the verdict names. When a finding hinges on a cause not yet known, or a structural redesign is needed, say so and return it to the caller.

## Done

Every finding names location, mechanism, consequence, assumptions and the smallest correction direction, with counterevidence sought. Depth and actual coverage are stated, and the evidence is separated into inspected, executed and proposed. For acceptance questions the verdict is one of `RECOMMEND_ACCEPT`, `RECOMMEND_CHANGES`, `DECISION_REQUIRED` or `INSUFFICIENT_EVIDENCE`; a supplied fix gets `fixed`, `insufficient fix` or `inconclusive`.

## Return

Lead with findings or a justified clean result, then scope, decisive evidence and limits. Name future proof without claiming a proposed fix works. Write the report only when asked.
