---
name: ko-skill
description: Author or revise one portable agent skill. Focus on a narrow outcome, a clear invocation boundary, concise instructions, integrated metadata, and proportionate verification.
---

# Ko Skill

Author or revise one portable skill. Keep only the guidance an agent needs to produce the outcome reliably.

## 1. Shape the skill

Read the repository and host instructions, the target skill and its resources, and the relevant catalog and metadata. Confirm the path, mutation authority, recurring outcome, triggers, exclusions, and adjacent owners.

Revise an existing outcome owner instead of creating a competing skill. Create a skill only for a recurring outcome, decision, or failure mode that ordinary documentation does not solve. Use the requested location; ask only when it cannot be inferred.

For a behavior correction, pin and exercise the pre-fix candidate with realistic raw input when that can be done safely. Capture the observed failure or evidence gap before editing. If current behavior already satisfies the target contract, do not change the skill only to restate that contract; identify another proved behavioral benefit or leave it unchanged. Do not build an evaluation harness only to justify a wording change.

Before editing, define the minimum useful verification: direct structure checks and the smallest forward test, if any, that resolves material behavioral uncertainty. If the required proof grows materially, stop and ask whether to simplify, defer, or continue.

## 2. Write the contract

Give the skill one narrow outcome and name the adjacent behavior it excludes. Treat user-supplied constraints as the target contract. Reconcile conflicting owning rules, but do not add policies outside the request or required integration.

Write for a capable agent:

- keep only non-obvious, behavior-bearing instructions;
- put selection triggers and the bounded outcome in the description;
- match detail to risk: use flexible guidance for judgment and exact steps or scripts for fragile operations;
- keep common instructions in `SKILL.md` and move substantial conditional detail to directly linked references;
- give each conditional branch or reference one exact load trigger, and keep its rules, caveats, and failure behavior together;
- use examples only when they clarify a material boundary, prevent likely misinterpretation, or make the instruction shorter or simpler overall; use a compact Good/Bad pair for a stable contrast and one example for a stable valid form; remove prose the example makes redundant, but never compress away authoritative conditions, safety constraints, or failure behavior;
- add scripts only for repeated deterministic work and assets only when the output uses them; and
- keep each rule with one owner; reference another specialist's required result instead of copying its procedure.

Run a compression pass. Remove repeated rules, rationale, history, transcripts, generic advice, and editorial text that does not improve selection, action, safety, or verification.

## 3. Integrate it

Keep the name, description, metadata, invocation policy, and packaged surfaces consistent with the host schema. Update release metadata and any catalog or router whose inventory or flow changed. Verify unchanged surfaces without no-op edits and preserve unrelated work.

For a provider-capable skill, keep provider execution local and include every applicable repository safety rule in that independently installed skill. Do not replace native provider semantics with a shared runtime unless an architecture decision authorizes it.

## 4. Verify proportionately

Always reread changed files and directly check frontmatter, metadata, paths, references, catalog, routing, packaging, changed scripts, and the final diff as applicable.

Treat structural checks as proof only of the named structures, not agent behavior.

Use fresh no-context subagent sessions when a change creates material uncertainty about selection, authority, unsafe effects, state transitions, complex branching, or agent interpretation. Use the smallest set of realistic raw goals that can distinguish success from failure; do not create a session for every theoretical branch. Hide the expected owner, answer, and rationale. Deny provider writes, credentials, and repository mutation unless a disposable scenario explicitly authorizes them.

Add an independent reviewer only when the consequence or ambiguity justifies a second judgment. Give each producer and reviewer the exact final candidate and raw evidence, not the intended verdict. After a correction or candidate change, rerun only the affected proof against the exact final candidate.

Do not add prompt eval suites or new behavioral test cases to this repository. Existing deterministic tests can remain while their owning behavior remains.

Report the skill path, boundary, changed files, direct checks, any forward-test evidence, candidate identity, and limitations. Distinguish repository, published, installed, and active states when relevant. Install or publish only when requested.
