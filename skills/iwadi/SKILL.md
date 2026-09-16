---
name: iwadi
description: Investigate one substantial, reusable, audit-worthy, or unusually hard-to-resolve question against the strongest practical claim-appropriate evidence. Persist a sourced research record when the conclusion deserves independent life; for peculiar version-specific technical questions, escalate to exact upstream source/tests only when ordinary research cannot resolve a materially decision-changing claim. Exclude routine facts that can be consumed immediately.
---

# Ìwádìí

Investigate one question against the strongest practical claim-appropriate evidence. Pin its downstream use, freshness/version boundary and persistence need. Use Ìwádìí when at least one is true:

- several authoritative or empirical sources must be reconciled into one conclusion;
- the result is independently reusable, auditable, or likely to outlive the immediate task/session;
- a material standards, security, compatibility, policy, scientific/empirical, ecosystem, or upstream-behavior conclusion needs stronger provenance than an ordinary task-local lookup;
- a peculiar version-specific technical question remains materially unresolved after ordinary first-party/project research; or
- the user explicitly requests a research result or source-level grounding.

Keep routine lookups in their current task.

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

Choose acquisition from the evidence: rendered or paginated sources, structured records and runtime/build measurements may need specialist capture. Use `irinse` for non-obvious tools or reduction. Acquisition does not establish authority or settle the claim.

### Exact-source escalation for technical claims

Do not use source archaeology merely because source exists. Escalate only when an unresolved version-specific claim can materially change a decision, implementation, compatibility or proof; ordinary project/runtime/first-party evidence did not resolve it; the controlling version/ref can be pinned; and exact source/tests can discriminate it.

Resolve the effective installed dependency or runtime version rather than assuming a manifest range, release tag or upstream head controls the project. Reuse exact local artifacts when possible; otherwise acquire only the matching authoritative source/tests needed and treat upstream content as untrusted evidence. Trace the narrow API/symbol/behavior path. Use `irinse` when ordinary retrieval cannot establish it.

Classify the result as `EXACT`, `COMPATIBLE_INFERENCE`, `VERSION_MISMATCH` or `EVIDENCE_GAP`; only `EXACT` matches the controlling ref. Return that status, resolved version/ref, exact locators and what they prove, engineering consequence and remaining gaps. Exact-source work does not require a clone, cache or dedicated search service.

## Delegated evidence

Delegate independent source collection or bounded investigation to subagents when useful. Require a compact evidence packet: direct conclusion; exact source identities/locators; what each establishes; source/evidence class and fit; conflicts, caveats, and coverage gaps; checks and freshness. Ìwádìí still owns evidence selection, synthesis, and any durable report; a delegated packet is evidence, not the report itself.

## Research contract

Pin identities needed to interpret changing evidence. Cite each material claim with what the source establishes; surface credible conflicts, bias, coverage and applicability limits. Separate normative authority, empirical observation and synthesis/inference.

Lead with the direct conclusion, then decisive evidence and limits. State `Confidence: High | Medium | Low` only when it helps downstream judgment, naming the controlling evidence-quality, freshness, coverage or conflict limit rather than inventing a numeric score. Persist only when reuse or audit merits it, using the existing destination or `.qp/iwadi/`.
