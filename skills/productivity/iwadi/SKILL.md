---
name: iwadi
description: Investigate one substantial, reusable, audit-worthy, or unusually hard-to-resolve question against the strongest practical claim-appropriate evidence. Persist a sourced research record when the conclusion deserves independent life; for peculiar version-specific technical questions, escalate to exact upstream source/tests only when ordinary research cannot resolve a materially decision-changing claim. Exclude routine facts that can be consumed immediately.
---

# Ìwádìí

Investigate one question against the strongest practical evidence appropriate to the claim. Default to the cheapest evidence capable of resolving it responsibly; preserve the result as a research record only when independent persistence is useful.

Pin the question, claim type, intended downstream use, freshness/version boundary, required evidence, and whether the result needs durable persistence before collecting sources.

## Admission

Use Ìwádìí when at least one is true:

- several authoritative or empirical sources must be reconciled into one conclusion;
- the result is independently reusable, auditable, or likely to outlive the immediate task/session;
- a material standards, security, compatibility, policy, scientific/empirical, ecosystem, or upstream-behavior conclusion needs stronger provenance than an ordinary task-local lookup;
- a peculiar version-specific technical question remains materially unresolved after ordinary first-party/project research; or
- the user explicitly requests a research result or source-level grounding.

Do not create a durable research record for one/few routine facts, a small known documentation read, or a transient lookup whose result is immediately consumed by another owner. Let the active owner perform that bounded lookup directly.

## Match evidence to the claim

Do not use one universal source hierarchy. Prefer the source class that most directly and reliably establishes the actual claim:

```text
current/local state
→ direct observation, measurement, runtime/project evidence

authoritative or normative claim
→ the owning law, policy, standard, specification, official decision, or first-party record

aggregate empirical claim
→ the strongest applicable high-quality synthesis/review, then the underlying studies/data as needed

specific empirical mechanism/result
→ relevant primary studies/data plus applicable synthesis/context

software/tool/upstream behavior
→ exact project/runtime evidence → official docs/spec/release evidence → exact upstream source/tests when escalation is earned
```

A primary source is not automatically stronger merely because it is primary. A synthesis is not automatically stronger merely because it aggregates. Judge fitness from claim match, methodology/authority, recency/version, directness, coverage, and material limitations.

### Exact-source escalation for technical claims

Do **not** jump to upstream source archaeology merely because source exists. Escalate only when all of these hold:

- the unresolved technical claim can materially change a decision, implementation, compatibility judgment, or proof;
- ordinary project/runtime/first-party research produced no valuable resolution because the question is too peculiar, version-specific, ambiguous, contradictory, or under-documented;
- the controlling project/dependency version or ref can be pinned; and
- tracing exact upstream implementation/tests is likely to discriminate the remaining uncertainty.

When that threshold is met, read [exact source grounding](references/exact-source-grounding.md). Stop if cheaper evidence already resolves the claim sufficiently.

## Context isolation

Delegate collection only when the investigation is substantially noisier than its useful conclusion and the active host/context rules permit it. The purpose is to keep source-search volume out of the primary reasoning context, not to delegate merely because subagents exist. Do not delegate a small known read or raw material the current agent must immediately edit.

When delegation is useful, require one compact evidence packet:

- direct conclusion;
- exact source URLs/identities plus relevant sections, symbols, study/result locators, or locations;
- what each source establishes;
- source/evidence class and why it fits the claim;
- conflicts, surprises, caveats, and coverage gaps; and
- checks performed and freshness.

The current agent owns evidence selection, synthesis, the durable report when one is warranted, and any task action that consumes the findings. A delegated packet is evidence, not the report itself.

## Research contract

1. Use the strongest practical evidence appropriate to each material claim rather than defaulting to one source type.
2. Pin source version/revision, retrieval date, population/timeframe, or other identity needed to keep the evidence interpretable when it can change materially.
3. Cite each material claim's source and state what the evidence supports without stretching it.
4. State material conflicts between credible evidence and any gap, bias, uncertainty, or applicability limit that constrains the conclusion.
5. Separate authoritative/normative statements from empirical observations and from your synthesis/inference.
6. Lead with the question and direct conclusion/verdict, then present supporting evidence and limits without reproducing the discovery transcript.
7. When the result deserves independent persistence, use the existing or user-selected durable research/knowledge destination. When the selected destination is a repository-scoped QP workspace, persist through `akosile` with `owner: iwadi`, `record_type: research`, and the stable research topic as subject. Do not require a repository merely because `.qp` is one available destination; when no durable destination is available or authorized, return the complete sourced result and report the persistence gap instead of blocking the research itself.
8. When Ìwádìí is only supporting another owner and persistence adds no independent value, return the compact sourced finding to that owner and stop instead of creating a record by ceremony.
