---
name: ko-skill
description: Author or validate one portable agent skill, or audit a bounded skill portfolio. Use `author` for creation or revision, `validate` for an exact read-only candidate verdict, and `audit` for a read-only portfolio audit; focus on ownership, concise capability-preserving instructions, integration, state, and proportionate proof.
---

# Kọ Skill

## Modes

- `author`: create or revise one skill; mutate only the authorized source and required integration surfaces.
- `validate`: assess one exact skill candidate; read-only.
- `audit`: read [portfolio audit](references/portfolio-audit.md) and assess the declared portfolio; read-only.

Never infer installation, activation, publication, provider, or other external mutation authority.

Kọ Skill owns skill authoring. Other specialists may supply evidence or own adjacent artifacts, but they do not replace Kọ Skill for creating, revising, or validating a skill.

## Pin the contract

Read host and repository instructions, the candidate and direct resources, and affected metadata, package, catalog, router, and decision records. Pin the exact candidate, mode, mutation authority, desired outcome, triggers, exclusions, adjacent owners, and starting state.

Treat these states independently: `source`, `installed`, `active`, and `published`. Evidence for one does not prove another.

- Good: `source=verified; installed=unknown; active=unknown; published=unknown`.
- Bad: “Source is verified, so the active skill is current.”

Revise an existing outcome owner instead of creating a competitor. Create a skill only for a recurring independent outcome, decision, or failure mode that ordinary documentation does not solve. Infer the requested location when safe.

For a behavior correction, exercise the exact pre-change candidate with a realistic raw goal when safe; otherwise record the evidence gap. Preserve behavior that already satisfies the target contract.

## Preserve capabilities

In `author`, treat user constraints as the target contract. Before changing prose, map the complete `SKILL.md` and direct references across these lenses:

```text
selection | outcome and modes | representation and control flow
authority, safety, and recovery | proof and tests | state and lifecycle
owners and integration | stop and report contract
```

Mark each capability `retain | change | move | remove`; give every change an owner and reason. A sentence inventory is not capability proof.

Write for a capable agent. Put triggers and bounded outcome in the description. Match precision to risk. Keep common rules in `SKILL.md`; give conditional references exact load triggers and boundaries. Use an example when it replaces prose or prevents material error, a script for repeated deterministic work, and an asset only when output uses it. Preserve one ordered workflow when sequence matters.

Merge rules with the same behavioral effect. Keep a second representation only for a distinct decision, authority, safety, recovery, verification, or owner boundary. Remove rationale, history, generic advice, and reference-owned procedure. Word count measures change, not quality.

## Prove the candidate

Define the smallest proof before editing:

- `structural`: check applicable schema, metadata, paths, references, packaging, routing, and deterministic invariants;
- `baseline`: record pre-change behavior for a correction or equivalence claim; it cannot accept the final candidate;
- `forward`: use the smallest fresh no-context raw goal only for material uncertainty in selection, authority, safety, state, branching, or output;
- `final`: reread the exact final candidate and rerun only structural or forward proof affected by the change.

For behavior-preserving compression, compare old and new with the same raw goal, repository candidate, authority, and stop condition. Hide the expected answer. Deny credentials and mutation unless a disposable scenario authorizes them. Add an independent reviewer only when consequence or ambiguity requires it.

Do not create a prompt-evaluation harness to justify wording. Follow the repository policy for persistent evaluations and deterministic tests. If proof grows materially, ask whether to simplify, defer, or continue.

In `validate`, return `VERIFIED` only when every required check passes against the exact candidate. Return `CHANGES_REQUIRED` for a proved defect and `INSUFFICIENT_EVIDENCE` for a material proof gap. Do not fix the candidate.

## Integrate and report

In `author`, keep host metadata and affected package, release, catalog, and router surfaces consistent. Preserve unrelated work. For a provider-capable skill, propagate the complete applicable repository safety contract into its independently installed owner; never add a shared provider runtime without an architecture decision. Send accepted durable project decisions to their knowledge owner when the repository authorizes that destination.

Report mode, exact candidate, authority, boundary, changed files, capability dispositions, checks, behavioral evidence or gaps, and final `source | installed | active | published` state. For material compression, include before-and-after counts. Install, activate, synchronize, publish, or hand off only with separate authority.
