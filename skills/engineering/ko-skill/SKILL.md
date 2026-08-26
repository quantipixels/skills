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

For validation, the candidate is the complete skill package and its applicable integration surfaces unless the user explicitly limits the review to a diff. Use a diff to identify changed obligations, not to narrow a full-candidate review.

Treat these states independently: `source`, `installed`, `active`, and `published`. Evidence for one does not prove another.

- Good: `source=verified; installed=unknown; active=unknown; published=unknown`.
- Bad: “Source is verified, so the active skill is current.”

When a readable installed copy exists, compare its identifier and relevant content before reporting installed state. Report actions performed separately from observed Git, provider, installed, active, or published state.

Revise an existing outcome owner instead of creating a competitor. Create a skill only for a recurring independent outcome, decision, or failure mode that ordinary documentation does not solve. Infer the requested location when safe.

For a behavior correction, use pinned existing evidence when it establishes the failure. Otherwise, exercise the exact pre-change candidate with a realistic raw goal when safe. When it is not safe, record the evidence gap. Preserve behavior that already satisfies the target contract.

When session history or prior outputs supply improvement evidence, use an exact-current `ayewo-igba-ise` result for retrospective mining; `ko-skill` consumes that evidence and owns confirmation, authoring, and proof. Pin the authorized evidence roots and time range. Distinguish directly stated preferences from inferred patterns; require user confirmation before making an inferred preference durable. For an update, preserve accepted behavior that new evidence does not contradict and assess only the changed evidence. Do not search unrelated workspaces or private histories.

## Classify the control shape

Before judging instruction depth, classify the skill as `lightweight` or `workflow` from the control its outcome actually requires. Reach, importance, or the number of situations in which a skill applies do not make it a workflow.

Use `lightweight` when a small set of consequential invariants can reliably change agent behavior and the outcome does not require an internal lifecycle, ordered multi-stage coordination, recovery protocol, or several independently authorized side effects. A lightweight skill may still own a broad judgment rule or one composed artifact as its native result. Prefer the smallest instruction set that creates the required behavioral delta; do not add phases, statuses, schemas, failure taxonomies, or authority ceremony merely to make the skill look complete.

Use `workflow` when correctness depends on ordered stages, durable or externally changing state, multiple candidates or actors, stale-result handling, retries or partial failure, recovery, or distinct side-effect authorities. Give only those boundaries the state, checks, receipts, and stop conditions they need.

Escalate a lightweight skill to a workflow only when observed failures prove that an omitted control boundary matters. Simplify a workflow when its stages or state no longer change safe execution. Treat classification as an authoring judgment, not permanent metadata unless a host or repository has a concrete use for persisting it.

For either shape, require an independently useful outcome and completion boundary. A lightweight completion boundary can be implicit in one exact result, such as a verdict, explanation, handoff, or composed research artifact; it does not need a state machine.

## Preserve and validate capabilities

Treat user constraints as the target contract. Before changing or validating the skill, map the complete `SKILL.md` and direct references across these lenses:

```text
selection | outcome and modes | representation and control flow
authority, safety, and recovery | proof and tests | state and lifecycle
owners and integration | stop and report contract
```

Apply only the lenses material to the classified control shape. For a lightweight skill, absence of workflow machinery is not a defect unless the missing control can change correctness, authority, safety, or completion. For a workflow, verify every stateful or ordered boundary that the outcome depends on.

Mark each capability `retain | change | move | remove`; give every change an owner and reason. A sentence inventory is not capability proof.

Trace the complete contract through instructions, applicable resources, metadata, routing, and observable output. Treat changed, universal, exclusive, safety, authority, portability, accessibility, and verification claims as proof obligations. Select sibling resources and execution paths from specific proof obligations or credible failure mechanisms. Test applicable normal, failure, misuse, locale, state, trust, recovery, and fallback paths; do not manufacture inapplicable branches for a lightweight skill. Verify that modes, statuses, and classifications that exist are non-overlapping and sufficient. Structural success cannot accept a semantically unproved candidate.

Name a new or changed mode with the shortest clear verb or verb phrase. Prefer names such as `audit`, `review`, `clean`, and `deep-clean`. Do not repeat the skill name, target artifact, implementation detail, or context that the owning skill already supplies. Add a qualifier only when it changes authority, risk, or outcome and the unqualified name would be ambiguous.

Before adding a rule, first try to merge, replace, move, or remove existing prose without losing capability. Add net-new instruction only when no current rule owns the required behavior.

Write for a capable agent. Front-load the job, distinct trigger branches, and boundaries in the description so truncation preserves selection. Keep selector-facing descriptions and host summaries focused on the skill's owned outcome, trigger, and exclusions; do not name resolver or supporting skills there merely to explain implementation. Routing skills are the exception when choosing another owner is itself the outcome. Name and invoke supporting skills in the body only at the first branch that actually requires their result.

Match freedom and precision to risk: use judgment for variable work, constrained patterns for preferred paths, and deterministic scripts for fragile repeated operations. Keep universally required behavior in `SKILL.md`; put branch-specific material behind a direct reference that names the exact branch that loads it. Give an ordered step a checkable completion criterion when later work could pull the agent forward too early. Use an example when it replaces prose or prevents material error, a script for repeated deterministic work, and an asset only when output uses it. Preserve one ordered workflow when sequence matters.

Treat the environment as a source of truth. Point to discoverable commands, configuration, schemas, paths, and metadata instead of caching them in prose; document only the convention, reason, or failure mode the environment does not encode. Keep rationale only when it changes judgment or makes a non-obvious guardrail generalize.

Merge rules with the same behavioral effect. Keep a second representation only for a distinct decision, authority, safety, recovery, verification, or owner boundary. Remove rationale, history, generic advice, and reference-owned procedure. Word count measures change, not quality.

Keep a dependency at its boundary and name it by exact identifier: ``Use `seda-ticket` to create tickets; persist its exact-current result.`` The caller may own triggers, inputs, freshness, integration, acceptance, authority, recovery, and stop behavior; it must not copy the dependency's procedure, resources, checks, statuses, schema, or lifecycle. Repeat only independently required safety, trust, provider, or authority rules.

Choose invocation policy from the authority and timing contract. Keep implicit invocation when natural-language routing is part of the outcome. Use `disable-model-invocation: true` only when the workflow requires an explicit user selection before material side-effect or continuing-stewardship authority can be established. Invocation policy does not replace the workflow's authority checks. When supported, keep equivalent host metadata, such as OpenAI `policy.allow_implicit_invocation`, consistent with that decision.

## Prove the candidate

Define the smallest proof before acting:

- `structural`: check applicable schema, metadata, paths, references, packaging, routing, and deterministic invariants;
- `baseline`: record pre-change behavior for a correction or equivalence claim; it cannot accept the final candidate;
- `forward`: use the smallest fresh no-context raw goal only for material uncertainty in selection, authority, safety, state, branching, or output;
- `final`: reread the exact final candidate and rerun only structural or forward proof affected by the change.

Match proof to the control shape. For a lightweight skill, first prove that its few invariants cause the intended behavioral delta and that the native result closes the outcome; do not require workflow-shaped scenarios that the skill intentionally does not own. For a workflow, prove the material transitions, stale or partial states, authority boundaries, and recovery paths that can change the result.

When the candidate, governing instructions, operation, or acceptance criteria change, mark affected evidence stale and rerun the applicable proof.

For behavior-preserving compression, compare old and new with the same raw goal, repository candidate, authority, and stop condition. Hide the expected answer. Deny credentials and mutation unless a disposable scenario authorizes them. Add an independent reviewer only when consequence or ambiguity requires it.

Do not create a prompt-evaluation harness to justify wording. Follow the repository policy for persistent evaluations and deterministic tests. Count delegated investigations, fresh sessions, reviewers, retries, and package checks as one proof scope. If that scope grows materially, ask whether to simplify, defer, or continue.

Before issuing a validation verdict, classify every applicable capability and proof obligation as `proved`, `defect`, `evidence gap`, or `not applicable`. A defect changes the verdict; it does not end validation. Report every material defect and evidence gap. Return `VERIFIED` only when every required structural and behavioral check passes against the exact candidate. Return `CHANGES_REQUIRED` for a proved defect and `INSUFFICIENT_EVIDENCE` for a material proof gap. Do not fix the candidate.

When `yo-slop` is available and the candidate needs a prose pass, use it only after behavior is settled. Preserve exact identifiers, deliberate guardrails, output schemas, and capability boundaries, then reread and revalidate the resulting candidate; prose cleanup is not behavior proof.

## Integrate and report

When mutation is authorized, keep host metadata and affected package, release, catalog, and router surfaces consistent. Preserve unrelated work. For a provider-capable skill, propagate the complete applicable repository safety contract into its independently installed owner; never add a shared provider runtime without an architecture decision. Send accepted durable project decisions to their knowledge owner when the repository authorizes that destination.

Report operation, exact candidate, control shape, authority, boundary, changed files, capability dispositions, checks, behavioral evidence or gaps, and final `source | installed | active | published` state. For material compression, include before-and-after counts. Install, activate, synchronize, publish, or hand off only with separate authority.
