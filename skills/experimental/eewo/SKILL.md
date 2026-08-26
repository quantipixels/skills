---
name: eewo
description: Curate evidence-backed prohibited coding patterns in private local QP records, resolve a small task-scoped guard pack, and prepare sanitized contribution proposals without making local learning depend on upstream publication. Use only when the user explicitly opts into the experimental pattern-guard workflow.
disable-model-invocation: true
---

# Èèwọ̀

Maintain a local-first catalogue of known-bad coding behaviours. Narrow the solution space without prescribing one architecture or pretending that avoiding known failures proves correctness.

`eewo` is experimental and explicit. It owns pattern semantics, lifecycle, scoping, guard-pack composition, and contribution reconciliation. `akosile` owns workspace paths and safe writes. Implementation, code-review verdicts, project knowledge, companion-tool operation, and provider publication remain with their existing owners.

## 1. Pin the pattern boundary

Establish the exact repository or subject, candidate identity when one exists, language/framework/version evidence, lifecycle phase, local-write authority, and whether personal scope, repository scope, or both are allowed.

Read [source resolution](references/source-resolution.md). Load only published packs relevant to the detected language or framework. Do not load every language pack or every local pattern merely because it exists.

Treat review comments, incidents, user corrections, community skills, catalog listings, linter output, and model suggestions as evidence, not rules. A local observation may be recorded without becoming active policy.

## 2. Curate patterns, not preferences

Read [pattern contract](references/pattern-contract.md) before creating, promoting, superseding, retiring, or contributing a pattern.

A durable pattern must identify:

- the invariant it protects;
- the prohibited behaviour, expressed semantically rather than as a token ban when possible;
- a credible failure mechanism;
- the smallest applicable scope;
- at least one safe path;
- legitimate exceptions and required proof when they exist; and
- provenance sufficient to revisit the rule later.

Prefer primary language/framework documentation and source over community guidance. Use [mining sources](references/mining-sources.md) to discover candidate material. Community skills can reveal useful failure classes, but do not copy their blanket prescriptions into active policy without corroboration and narrowing.

Keep rule lifecycle and contribution lifecycle independent. A locally active rule remains locally active while a proposal is pending, rejected, changed upstream, or never contributed.

Do not activate an inferred preference automatically. A direct user instruction such as “never do this again in my projects” can authorize local activation after the rule is scoped and checked for obvious unsafe overreach. Otherwise activation requires explicit confirmation or independently established project authority.

## 3. Resolve one exact-current guard pack

For implementation or review, select only `active` patterns applicable to the exact task. Merge constraints from the sources in [source resolution](references/source-resolution.md), reconcile duplicates by failure mechanism, and stop on a material unresolved conflict rather than choosing silently.

Persist a substantial guard pack through `akosile` in repository scope:

```text
owner: eewo
record_type: guard-pack
subject: <exact candidate or task identity>
```

The guard pack must contain:

```text
Candidate: <exact identity>
Phase: implementation | review | other
Sources: <source scope, pattern id, revision/version>
Digest: <stable digest when the host can produce one>

Applicable invariants
Applicable prohibitions
Safe paths and exceptions
Required deterministic checks
Known coverage limits
```

Pin the pack for the active candidate. New findings discovered after implementation or review begins may be recorded for the next pack, but must not mutate the pack already governing the current candidate.

A guard pack is a closed-world check for known failures. It never replaces acceptance criteria, tests, architecture reasoning, or open-ended defect discovery.

## 4. Learn from implementation and review

During implementation, use the guard pack as constraints and keep design freedom elsewhere. During review, check every applicable rule and continue searching for novel defects outside the pack.

Classify a new observation as one of:

```text
existing-rule violation
existing-rule refinement
novel candidate
one-off correction
false positive
promising non-binding pattern
material decision required
```

Record only evidence-backed observations. Send session/corpus recurrence analysis to `ayewo-igba-ise`; send volatile factual validation to `iwadi`; use `ro-wo` when generalisation, alternatives, or exceptions materially control promotion. Use `irinse` when a mature rule should move into Clippy, Error Prone, ArchUnit, Ruff, Semgrep, or another deterministic mechanism.

## 5. Keep local learning independent from contribution

Never stage or publish `.qp` or the personal QP workspace.

When contribution is requested, create an immutable sanitized proposal receipt from one exact local pattern revision. The proposal records source pattern id, source revision, source digest when available, target repository/pack, portable rule content, public evidence, and excluded private evidence. Later local revisions do not alter the proposal.

Do not export raw proprietary code, private paths, internal issue text, credentials, private transcripts, reviewer identity, or local-only metrics. Prefer an allowlist of portable fields over redacting an arbitrary local record.

`eewo` may prepare the exact contribution content and reconciliation result. Use `seda-pr` for commit/push/PR or MR publication when separately authorized.

After upstream acceptance, modification, or rejection, reconcile rather than replace the local rule. Classify accepted content as `equivalent`, `narrower`, `broader`, or `conflicting`; preserve stricter private overlays and evidence unless the user explicitly retires them.

## 6. Report

Return:

```text
Eewo result
Subject: <identity>
Scope: personal | repository | both | published-only
Operation: observe | curate | activate | resolve | contribute | reconcile
Pattern records: <ids/revisions changed or none>
Guard pack: <identity/digest or none>
Contribution: local_only | draft | submitted | accepted | rejected | diverged | none
Evidence: <primary and supporting sources>
Conflicts: <none or exact unresolved conflict>
Next consumer: <alaga | atunwo | irinse | seda-pr | none>
Limits: <coverage/freshness/privacy limits>
```
