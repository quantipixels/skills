---
name: ko-skill
description: Author, revise, or validate one portable agent skill through one shared workflow, or audit a bounded skill portfolio. Focus on ownership, concise capability-preserving instructions, integration, state, and proportionate proof.
---

# Kọ Skill

Create, revise, or validate one exact skill through this workflow. The requested operation and explicit mutation authority determine whether files may change; validation is read-only. For a bounded portfolio audit, read [portfolio audit](references/portfolio-audit.md), return its read-only result, and do not edit, install, activate, synchronize, or publish skills.

Never infer installation, activation, publication, provider, or other external mutation authority.

`ko-skill` owns skill authoring. Other specialists may supply evidence or own adjacent artifacts, but they do not replace `ko-skill` for creating, revising, or validating a skill.

## Pin the contract

Read host and repository instructions, the candidate and direct resources, and affected metadata, package, catalog, router, and decision records. Pin the exact candidate, operation, mutation authority, desired outcome, triggers, exclusions, adjacent owners, and starting state.

Treat these states independently: `source`, `installed`, `active`, and `published`. Evidence for one does not prove another.

- Good: `source=verified; installed=unknown; active=unknown; published=unknown`.
- Bad: “Source is verified, so the active skill is current.”

When a readable installed copy exists, compare its identifier and relevant content before reporting installed state. Report actions performed separately from observed Git, provider, installed, active, or published state.

Revise an existing outcome owner instead of creating a competitor. Create a skill only for a recurring independent outcome, decision, or failure mode that ordinary documentation does not solve. Infer the requested location when safe.

For a behavior correction, exercise the exact pre-change candidate with a realistic raw goal when safe; otherwise record the evidence gap. Preserve behavior that already satisfies the target contract.

## Preserve and validate capabilities

Treat user constraints as the target contract. Before changing or validating the skill, map the complete `SKILL.md` and direct references across these lenses:

```text
selection | outcome and modes | representation and control flow
authority, safety, and recovery | proof and tests | state and lifecycle
owners and integration | stop and report contract
```

Mark each capability `retain | change | move | remove`; give every change an owner and reason. A sentence inventory is not capability proof.

Trace the complete contract through instructions, applicable resources, metadata, routing, and observable output. Treat changed, universal, exclusive, safety, authority, portability, accessibility, and verification claims as proof obligations. Test sibling resources and applicable normal, failure, misuse, locale, state, trust, recovery, and fallback paths. Verify that modes, statuses, and classifications are non-overlapping and sufficient. Structural success cannot accept a semantically unproved candidate.

Name a new or changed mode with the shortest clear verb or verb phrase. Prefer names such as `audit`, `review`, `clean`, and `deep-clean`. Do not repeat the skill name, target artifact, implementation detail, or context that the owning skill already supplies. Add a qualifier only when it changes authority, risk, or outcome and the unqualified name would be ambiguous.

Before adding a rule, first try to merge, replace, move, or remove existing prose without losing capability. Add net-new instruction only when no current rule owns the required behavior.

Write for a capable agent. Put triggers and bounded outcome in the description. Match precision to risk. Keep common rules in `SKILL.md`; give conditional references exact load triggers and boundaries. Use an example when it replaces prose or prevents material error, a script for repeated deterministic work, and an asset only when output uses it. Preserve one ordered workflow when sequence matters.

Merge rules with the same behavioral effect. Keep a second representation only for a distinct decision, authority, safety, recovery, verification, or owner boundary. Remove rationale, history, generic advice, and reference-owned procedure. Word count measures change, not quality.

Keep a dependency at its boundary and name it by exact identifier: ``Use `seda-ticket` to create tickets; persist its exact-current result.`` The caller may own triggers, inputs, freshness, integration, acceptance, authority, recovery, and stop behavior; it must not copy the dependency's procedure, resources, checks, statuses, schema, or lifecycle. Repeat only independently required safety, trust, provider, or authority rules.

## Prove the candidate

Define the smallest proof before acting:

- `structural`: check applicable schema, metadata, paths, references, packaging, routing, and deterministic invariants;
- `baseline`: record pre-change behavior for a correction or equivalence claim; it cannot accept the final candidate;
- `forward`: use the smallest fresh no-context raw goal only for material uncertainty in selection, authority, safety, state, branching, or output;
- `final`: reread the exact final candidate and rerun only structural or forward proof affected by the change.

For behavior-preserving compression, compare old and new with the same raw goal, repository candidate, authority, and stop condition. Hide the expected answer. Deny credentials and mutation unless a disposable scenario authorizes them. Add an independent reviewer only when consequence or ambiguity requires it.

Do not create a prompt-evaluation harness to justify wording. Follow the repository policy for persistent evaluations and deterministic tests. If proof grows materially, ask whether to simplify, defer, or continue.

For validation, return `VERIFIED` only when every required structural and behavioral check passes against the exact candidate. Return `CHANGES_REQUIRED` for a proved defect and `INSUFFICIENT_EVIDENCE` for a material proof gap. Do not fix the candidate.

## Integrate and report

When mutation is authorized, keep host metadata and affected package, release, catalog, and router surfaces consistent. Preserve unrelated work. For a provider-capable skill, propagate the complete applicable repository safety contract into its independently installed owner; never add a shared provider runtime without an architecture decision. Send accepted durable project decisions to their knowledge owner when the repository authorizes that destination.

Report operation, exact candidate, authority, boundary, changed files, capability dispositions, checks, behavioral evidence or gaps, and final `source | installed | active | published` state. For material compression, include before-and-after counts. Install, activate, synchronize, publish, or hand off only with separate authority.
