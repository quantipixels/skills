---
name: iwadi
description: Investigate one substantial, reusable, audit-worthy, or unusually hard-to-resolve question against high-trust primary sources. Persist a sourced Markdown research record when the conclusion deserves independent life; for peculiar version-specific questions, escalate to exact upstream source/tests only when ordinary web and first-party research cannot resolve a materially decision-changing claim. Exclude routine facts that can be consumed immediately.
---

# Ìwádìí

Investigate one question against the strongest practical primary evidence. Default to the cheapest evidence capable of resolving the claim; preserve the result as a Markdown research record only when independent persistence is useful.

Pin the question, intended downstream use, freshness/version boundary, required evidence, and whether the result needs durable persistence before collecting sources.

## Admission

Use Ìwádìí when at least one is true:

- several primary sources must be reconciled into one conclusion;
- the result is independently reusable, auditable, or likely to outlive the immediate task/session;
- a material standards, security, compatibility, policy, ecosystem, or upstream-behavior conclusion needs stronger provenance than an ordinary task-local lookup;
- a peculiar version-specific technical question remains materially unresolved after ordinary web/first-party research; or
- the user explicitly requests a research result or source-level grounding.

Do not create a durable research record for one/few routine facts, a small known documentation read, or a transient lookup whose result is immediately consumed by another owner. Let the active owner perform that bounded lookup directly.

### Evidence escalation

Start with exact current contextual evidence and ordinary research against current first-party sources: official docs, specifications, standards, policy/decision records, release/migration notes, maintained examples, first-party APIs, and available source snippets/tests when relevant and easy to reach.

Do **not** jump to upstream source archaeology merely because source exists. Escalate only when all of these hold:

- the unresolved claim can materially change a decision, implementation, compatibility judgment, or proof;
- ordinary web/first-party research produced no valuable resolution because the question is too peculiar, version-specific, ambiguous, contradictory, or under-documented;
- the controlling project/dependency version or ref can be pinned; and
- tracing exact upstream implementation/tests is likely to discriminate the remaining uncertainty.

When that threshold is met, read [exact source grounding](references/exact-source-grounding.md). Stop if the cheaper evidence already resolves the claim sufficiently.

## Context isolation

Delegate collection only when the investigation is substantially noisier than its useful conclusion and the active host/context rules permit it. The purpose is to keep source-search volume out of the primary reasoning context, not to delegate merely because subagents exist. Do not delegate a small known read or raw material the current agent must immediately edit.

When delegation is useful, require one compact evidence packet:

- direct conclusion;
- exact primary-source URLs or identities plus relevant sections, symbols, or locations;
- what each source proves;
- conflicts, surprises, caveats, and coverage gaps; and
- checks performed and freshness.

The current agent owns source selection, synthesis, the durable report when one is warranted, and any task action that consumes the findings. A delegated packet is evidence, not the report itself.

## Research contract

1. Prefer **primary sources** — official docs, source code, specs, standards, authoritative policy/decision records, first-party APIs — and follow every material claim back to the source that owns it.
2. Pin a source version, revision, or retrieval date when its content can change materially.
3. Cite each material claim's source and state what the evidence supports without stretching it.
4. State material conflicts between primary sources and any evidence gap that limits the conclusion.
5. Lead with the question and direct conclusion/verdict, then present supporting evidence and limits without reproducing the discovery transcript.
6. When the result deserves independent persistence, use the existing or user-selected durable research/knowledge destination. When the selected destination is a repository-scoped QP workspace, persist through `akosile` with `owner: iwadi`, `record_type: research`, and the stable research topic as subject. Do not require a repository merely because `.qp` is one available destination; when no durable destination is available or authorized, return the complete sourced result and report the persistence gap instead of blocking the research itself.
7. When Ìwádìí is only supporting another owner and persistence adds no independent value, return the compact sourced finding to that owner and stop instead of creating a record by ceremony.
