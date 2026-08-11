---
name: alakowe
description: Maintain one project's canonical domain knowledge across terminology, context boundaries, decision records, living documentation, and root .nongoal. Use when domain language must be clarified, confirmed knowledge or an ADR must be recorded, canonical documentation must be reconciled, or project non-goals must change; exclude architecture planning, implementation, generic documentation templates, and unconfirmed decisions.
---

# Alakowe

Keep one project's durable knowledge coherent with confirmed decisions, explicit exclusions, and the exact current candidate. Own active domain-language clarification and canonical reconciliation, not the underlying product or architecture decision.

## 1. Establish authority and current evidence

Read repository instructions, the complete root `.nongoal` when present, existing domain and context records, decision records, affected living documentation, and the relevant code, tests, history, plan, or implementation candidate.

Pin the supplied decision, plan, or candidate identity. Separate authority to decide from authority to write. Treat a supplied conclusion as input until its scope, confirmation, and identity are current. If evidence or authority conflicts, report the conflict and do not choose a preferred truth silently.

When the request conflicts with `.nongoal`, pause the conflicting work and ask whether the request is a one-time exception or an authorized change to the project boundary. Absence from `.nongoal` does not prove that a direction is in scope.

Without write authority, inspect and return the required reconciliation without modifying files.

## 2. Sharpen the domain model

Focus on project-specific language that changes scope, ownership, state, behavior, or communication. Do not build a glossary for its own sake.

Compare the user's language, current canonical documents, code, tests, and history. Treat code as evidence of current behavior, not automatic domain authority.

For each material vague, overloaded, or conflicting term, relationship, or rule:

1. Record the competing meanings and affected contexts.
2. Give one concrete scenario whose expected outcome differs between those meanings.
3. Identify the authority needed to settle the difference.
4. Use `arojinle` when a material user decision remains. When an architecture plan owns the decision, return the conflict and required decision to `atona`.
5. After confirmation, update the existing canonical destination with the adopted term, useful alternatives to avoid, relevant relationship or boundary, scenario, provenance, and affected surfaces.

Preserve the repository's existing knowledge structure. When a clear canonical equivalent already exists, use it and state why it is the repository's current domain-knowledge destination.

When no equivalent is found or supplied, ask the user to choose between:

1. creating root `CONTEXT.md`, the recommended default; or
2. providing the existing equivalent or another destination.

Do not create a destination until the user confirms the choice. If the choice remains unanswered, report reconciliation as blocked. A new `CONTEXT.md` establishes a location, not a content template: do not impose mandatory headings, `CONTEXT-MAP.md`, a glossary file, or a context directory.

## 3. Record qualifying architecture decisions

Create or update an ADR only when the decision is confirmed and all three conditions hold:

- it is costly or hard to reverse;
- its reason would be surprising without context; and
- credible alternatives created a real trade-off.

Use the repository's current location, naming, status, and content conventions. Require information sufficient to preserve the context, decision, alternatives, consequences, status, and authority, but do not impose headings or a template.

When a decision changes, preserve history through the repository's supersession or deprecation convention. Do not rewrite an accepted record to make current code appear consistent.

## 4. Maintain `.nongoal`

`.nongoal` is an optional, Git-tracked project-boundary file at the repository root. It records items, ideas, directions, features, or concerns that the project is not pursuing. It is not a backlog.

- Read and interpret any existing human-readable format without converting it.
- Do not create an empty file merely because Alakowe ran.
- When creation is explicitly authorized, default to a bare list with no heading, schema, identifiers, statuses, or mandatory rationales.
- Add, remove, or materially reinterpret an entry only with explicit boundary authority.
- Do not clean up or reorder unrelated entries incidentally.
- A conflict requires an explicit one-time exception or an authorized update before the conflicting direction proceeds.

An ADR may explain a consequential non-goal, but a `.nongoal` entry does not require an ADR.

## 5. Reconcile and verify

Map each affected durable claim to its current source of authority and canonical destination. Classify each destination as `updated`, `already correct`, `not applicable`, or `blocked`, with evidence.

Change only the affected existing sources. Remove, correct, supersede, or clearly mark contradictory current guidance. Keep code-local comments and API documentation with the implementation owner unless they are part of the requested canonical reconciliation.

Do not generate generic README, API, OpenAPI, changelog, glossary, or ADR templates. Do not absorb plans, research reports, standalone HTML artifacts, or general writing merely because they are documents.

Re-read every changed destination against the confirmed authority and exact candidate. Verify terminology, context boundaries, ADR lifecycle links, `.nongoal`, references, and stale claims. If the decision, plan, or candidate changes, mark the affected result stale and repeat reconciliation.

Return:

```text
Alakowe result
Candidate: <decision, plan, commit, tree, or working-tree identity>
Authority: <confirmed source, scope, and write authority>

Domain model
- <term, relationship, or context boundary> — confirmed | unresolved | unchanged — <evidence>

Destinations
- <path> — updated | already correct | not applicable | blocked — <evidence>

ADR
- required | not required | blocked — <record or reason>

Project boundary
- .nongoal — absent | unchanged | updated | blocks candidate | exception confirmed

Verification: <checks and limitations>
Verdict: RECONCILED | BLOCKED
```
