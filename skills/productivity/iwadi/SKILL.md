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

Do not use one universal source hierarchy. Prefer the source class that most directly/reliably establishes the actual claim:

```text
current/local state
→ direct observation, measurement, runtime/project evidence

authoritative/normative claim
→ owning law, policy, standard, specification, official decision, or first-party record

aggregate empirical claim
→ strongest applicable high-quality synthesis/review, then underlying studies/data as needed

specific empirical mechanism/result
→ relevant primary studies/data plus applicable synthesis/context

software/tool/upstream behavior
→ exact project/runtime evidence → official docs/spec/release evidence → exact upstream source/tests when escalation is earned
```

A primary source is not automatically stronger merely because it is primary; a synthesis is not automatically stronger because it aggregates. Judge fitness from claim match, methodology/authority, recency/version, directness, coverage, and material limitations.

### Exact-source escalation for technical claims

Do not jump to source archaeology merely because source exists. Escalate only when the unresolved claim can materially change a decision/implementation/compatibility/proof, ordinary project/runtime/first-party research did not resolve it, controlling version/ref can be pinned, and exact source/tests are likely to discriminate the uncertainty. When earned, read [exact source grounding](references/exact-source-grounding.md).

## Context isolation

Delegate collection only when the investigation is substantially noisier than its useful conclusion and the active host/context rules permit it. The purpose is to keep search volume out of primary reasoning context, not to delegate merely because subagents exist.

When delegation is useful, require a compact evidence packet: direct conclusion; exact source identities/locators; what each establishes; source/evidence class and fit; conflicts/surprises/caveats/coverage gaps; checks/freshness.

The current agent owns evidence selection, synthesis, durable report when warranted, and task action consuming the findings. A delegated packet is evidence, not the report itself.

## Research contract

1. Use the strongest practical evidence appropriate to each material claim rather than defaulting to one source type.
2. Pin source version/revision, retrieval date, population/timeframe, or other identity needed to keep evidence interpretable when it can change materially.
3. Cite each material claim's source and state what it supports without stretching it.
4. State material conflicts between credible evidence and any gap, bias, uncertainty, or applicability limit constraining the conclusion.
5. Separate authoritative/normative statements from empirical observations and from synthesis/inference.
6. Lead with the question and direct conclusion/verdict, then supporting evidence and limits without reproducing the discovery transcript.
7. When evidence strength materially helps downstream judgment, state `Confidence: High | Medium | Low` separately from the conclusion and explain the controlling source-quality/directness/consistency/freshness/coverage/conflict limit. Do not invent numeric confidence without a meaningful model. State what evidence could materially overturn or narrow the conclusion when non-obvious.
8. When the result deserves independent persistence, use the existing/user-selected durable research/knowledge destination. When repository-scoped `.qp` persistence is selected, use `akosile` with the research owner/subject. Do not require a repository merely because `.qp` persistence is available.
9. When Ìwádìí only supports another owner and persistence adds no independent value, return the compact sourced finding and stop instead of creating a record by ceremony.
