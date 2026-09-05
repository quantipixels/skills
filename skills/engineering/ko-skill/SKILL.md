---
name: ko-skill
description: Author, revise, or validate one portable agent skill, or audit a bounded skill portfolio. Focus on one owned outcome, deep-module composition, the smallest adequate capability/resource placement, selectively loaded expert depth, and proportionate proof.
---

# Kọ Skill

Create, revise, or validate one exact skill. Mutation requires explicit authority; validation and portfolio audit are read-only. Never infer installation, activation, synchronization, publication, provider, or other external mutation authority from source changes. For a bounded portfolio audit, read [portfolio audit](references/portfolio-audit.md).

## 1. Own one outcome

Read the candidate package plus affected repository/host instructions and integration metadata. Pin the operation, exact candidate, desired outcome, triggers, exclusions, authority, adjacent owners, and relevant `source | installed | active | published` evidence.

Grow capability depth faster than public surface area. A public skill must own an independently useful result, authority/artifact/acceptance boundary, failure mode, or reusable steering contract **and** make direct selection/use materially simpler than keeping the capability behind an existing owner. Do not remove a useful lightweight steering contract merely because a capable model can perform the underlying act.

Do not optimize for fewer owners/resources/stages. Fold only when the smaller shape preserves a coherent outcome without braiding independently useful results, authority/acceptance boundaries, lifecycle/state, or distinct reasons to change.

Frame the owner at the natural level of its outcome. Generalize the mechanism, never the authority. Protect the **material decision surface**: compression/folding/generalization must not turn an owned constraint, evidence requirement, authority boundary, or consequential choice into unlabeled model inference.

Curate frameworks **into** reasoning. Preserve a named model, standard, concept, or mature capability when its vocabulary, conceptual structure, authority, durable problem fit, or retrieval value materially improves this owner's judgment. State the skill-relevant subset/boundary directly; a name imports neither the whole methodology nor a closed ecosystem.

Use the smallest control shape that preserves correctness: `lightweight` when consequential invariants can directly produce the result; `workflow` when ordered stages, durable/external state, stale/partial recovery, multiple actors/candidates, or distinct side-effect authorities genuinely control correctness. Do not add lifecycle/status/receipts/schemas merely because the outcome is important.

### Admit a public owner only when the identity earns its surface

Before adding, re-exposing, or promoting a public owner, apply hard gates in this order:

1. **Independent result:** the capability produces a result, authority/completion boundary, or reusable steering contract that is useful without another owner's lifecycle around it.
2. **Existing-owner fit:** no current owner can absorb the capability coherently through guidance, a selective reference, native capability, or internal path without weakening that owner's outcome or authority boundary.
3. **Selection value:** the separate name makes a realistic user/agent choice materially simpler than keeping the capability behind the nearest owner.
4. **Boundary proof:** at least one realistic positive case and the closest plausible negative/adjacent-owner case support the proposed trigger and ownership boundary. A stable owner needs evidence proportionate to its routing risk; an Experimental owner may test a credible public-identity hypothesis, but missing real-use evidence remains explicit and cannot justify promotion.

If the capability is useful but the public identity has not earned selection value, keep or fold the capability behind its natural owner. If a distinct outcome is credible but recurrence/public-identity value remains unproved, use the repository's Experimental disposition rather than pretending maturity. Do not choose a target number of skills first and then force owners to fit it.

When an Experimental skill's maturity or public identity is itself being changed—promote, keep experimental, narrow, fold, replace, or remove—read [experimental skill disposition](references/experimental-disposition.md). Do not infer recurrence, selection frequency, or incremental value from source structure when that disposition requires real-use evidence.

### Admit only behavior-bearing instruction

A capable agent's default behavior is not automatically desired behavior. Keep an instruction only when its trigger, failure prevented, forced behavioral difference, value, and recurring cost justify default context.

Prefer replacing/sharpening existing guidance over appending another rule. Before adding a paragraph/reference/public owner, try one precise invariant, discriminating question, or strong `Good / Bad` boundary. Use a selective reference only when branch-specific non-obvious judgment would otherwise burden the hot path.

### Evaluate proposals without rubric theatre

When several credible capability/architecture/portfolio options remain and at least two independent criteria can materially change the choice, make the comparison explicit:

1. apply hard gates first—authority, accepted behavior, safety/security/privacy, compatibility, required accessibility, owner boundaries, and explicit non-goals cannot be averaged away;
2. derive only decision-changing criteria from the owned outcome, such as gap closure, agent leverage, architecture fit, decision-surface effect, reuse, evidence integrity, portability/maintenance, or runtime cost;
3. compare the strongest credible alternatives and material counterevidence;
4. use a grade/score only when it clarifies comparison and never as a substitute for the decisive reason; and
5. return a task-native disposition such as `ADOPT | ADAPT | FOLD | INCUBATE | DEFER | REJECT | NEEDS_EVIDENCE`, plus the proof/revisit trigger when uncertainty remains.

Keep verdict/evidence status, confidence, comparative grade, readiness, and disposition distinct. Do not create a universal portfolio scorecard or numeric confidence without a meaningful model.

## 2. Compose and place capability

Treat skills as deep modules. Pass only bounded input, current evidence/identity, authority, and caller-owned acceptance another owner needs. The callee retains native procedure, resources, proof, persistence/representation mechanics, and result. Supporting owners/references must not originate or redefine consumer semantics, lifecycle, freshness, priorities, verdicts, acceptance, or authority.

Do not project semantic units one-to-one onto operational containers unless the destination contract requires it. Requirements/tickets/phases/proof obligations/capability boundaries describe meaning; commits/candidates/branches/PRs/tests/browser runs/sessions are chosen for integration/review/rollback/ownership/release/evidence value.

Write for a capable agent. State semantic behavior, invariants, authority, and completion. Leave ordinary search, shell/filesystem work, Git, editing, tool discovery, and host-specific delegation mechanics adaptable. Prescribe isolation only when bounded independent/noisy work must leave primary context to protect focus/continuity/independent observation.

Before adding/retaining commands, references, scripts, templates, data, assets, libraries, or another public owner, read [capability and resource placement](references/resource-placement.md). Use [reference quality](references/reference-quality.md) for substantial expert depth, [script boundary](references/script-boundary.md) when executable code still appears necessary, and [knowledge catalogues](references/knowledge-catalogues.md) only when maintained researched knowledge is itself part of the useful outcome.

Keep one canonical semantic contract across hosts. Host manifests/rules/hooks/adapters should be the thinnest projection required by loader semantics and mechanically checked when drift would be consequential. Name modes only when behavior/authority truly differs. Cross-skill references use exact frontmatter `name` triggers in backticks.

For human-facing artifacts, match proof to the owned result: representation/document structure does not earn browser/UI assurance unless rendered behavior itself materially controls acceptance.

## 3. Prove the exact candidate

Use the smallest evidence that can falsify the changed contract. Structural/package validation is baseline; add realistic forward behavior only when selection, authority, safety, state, branching, composition, resource choice, or output remains materially uncertain. Re-run only proof invalidated by later changes.

For compression/consolidation/framework/reference removal/ownership moves/domain generalization, compare the same realistic bounded goal before/after when material uncertainty remains. Prove removed material was not uniquely behavior-bearing **and** the new shape does not enlarge the material decision surface or lose useful conceptual/retrieval anchors.

For model-steering changes with material uncertainty, compare the same bounded task/candidate/context under the prior/no contract and changed contract. Verify intended behavioral delta plus preserved correctness, safety, authority, and output. Keep temporary steering proof temporary unless recurring stable risk earns regression coverage.

When a proposed change to a stable skill is justified from historical multi-session behavior rather than one current task, use `ayewo-igba-ise` to reconstruct the bounded corpus and return its stable-skill improvement evidence packet. If Àyẹ̀wò has already supplied a valid bounded historical evidence packet, consume it directly and **do not invoke Àyẹ̀wò again to reconstruct the same corpus**. If Kọ is the user-selected entrypoint and the historical packet does not yet exist, compose `ayewo-igba-ise` internally, receive the packet, then continue the requested authoring/disposition workflow without requiring a second user invocation. Treat the packet as evidence, not an edit instruction. A clear active rule that agents violated, a host/tool gap, or ordinary model variance does not earn another instruction by itself; prefer the actual selection, host/tool, or execution owner unless the corpus establishes a reusable missing/ambiguous contract or owner-boundary defect.

Do not claim saved LOC/tokens/cost/latency/time/quality without an observed comparable baseline. Structural reduction is simplification evidence, never acceptance.

For validation classify material obligations as `proved | defect | evidence gap | not applicable`. Return `VERIFIED` only when required proof passes against the exact candidate, `CHANGES_REQUIRED` for a proved defect, and `INSUFFICIENT_EVIDENCE` for a material proof gap. Validation does not authorize repair.

## 4. Integrate and report

With mutation authority, reconcile only affected metadata/manifests/routes, direct resource links, deterministic tests/CI, and release surfaces. Preserve unrelated work.

Report the exact candidate, owned outcome/control shape, material owner/capability/resource changes, decision-surface effects, proof/gaps, relevant external state, and disposition/revisit condition when a comparative evaluation controlled the change.
