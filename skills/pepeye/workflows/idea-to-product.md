# Idea to usable product

**Outcome:** turn an unresolved product/engineering idea into a usable, evidenced product increment without forcing settled stages to replay.

## Lane

1. **`iwadi` — evidence, when missing.** Use when current external facts, prior-art comparison, framework/provider behavior, or repository evidence can materially change the direction.
2. **`arojinle` — consequential choice, when open.** Resolve a decision only when credible alternatives materially differ.
3. **`atona` — coordinated plan, when needed.** Shape the route when delivery has material dependencies, risk, sequencing, or several owners.
4. **`architect` / `seda-spec` — structure or behavior, conditionally.**
   - use `architect` when implementation would otherwise invent consequential technical structure or ownership;
   - use `seda-spec` when observable behavior/contract remains ambiguous.
5. **Independent plan review — whenever an explicit plan becomes material.** After plan-affecting decisions are reflected in the fixed plan, review it in fresh read-only context before treating it as ready or using it to progress work. Route findings back to the nearest semantic owner, update the plan, and review again only when the judgment boundary materially changes.
6. **`alaga` — implementation and sufficient proof.** Deliver the accepted coding outcome and return the exact candidate/result to the workflow lead.
7. **`atunwo` — independent code judgment, when required.** Use when the user/workflow requires review or risk/uncertainty makes independent evidence materially valuable.
8. **`seda-pr` — publication, only when authorized.** Create/update the PR/MR; publication does not imply merge/release authority.
9. **`ayewo-igba-ise` — terminal retrospective.** After the result state is fixed, postmortem the workflow and harvest only evidence-backed reusable learning through its natural owner.

## Capability flow

When the evidence surface is large, use cheaper workers to gather and collate it before expensive synthesis/judgment. Preserve source/code locators in the handoff.

For the current Codex preference shape:

- Luna/Terra gather repository/external evidence and normal research synthesis;
- Astra/medium produces a material plan from the compact evidence/decisions;
- fresh Astra/high premortems the fixed plan;
- Sol performs most substantive technical analysis, architecture development, diagnosis, and implementation;
- Terra normally owns prose-first artifacts, dropping to Luna for deterministic writing; and
- Astra reviews consequential candidates/decisions at acceptance boundaries rather than checking every collection step.

Use the active host policy as authority when its model names/preferences differ.

## Branches and recovery

- New evidence invalidates the chosen direction → `arojinle` (or `iwadi` first if evidence is still missing).
- Architecture/spec work changes sequencing, dependencies, proof, or ownership → refresh `atona` only where the plan changed, then return to plan review while the plan remains material.
- Plan review reopens sequencing/dependencies → `atona`; reopens architecture → `architect`; reopens observable behavior → `seda-spec`; exposes a consequential user choice → `arojinle`. Review the resulting fixed plan again before treating it as ready.
- Candidate/base changes after code review → refresh only affected `atunwo` evidence.
- Code review confirms a defect → `alaga`, then re-review only invalidated findings/evidence.
- Publication/CI exposes a concrete delivery defect → nearest causal owner, not a full workflow restart.
- Postmortem earns an agent-instruction/skill improvement → route it as a separate `oro-fun-sigidi` follow-on when the remediation scope authorizes that surface. New skill identity or material routing/ownership changes follow the same scope/evidence rule: apply when covered and justified, otherwise return a bounded handoff. Other durable improvements go to explicit `amose` `.learnings` or their natural project/runtime owner.

## Completion and closure

Delivery stops when the accepted product increment exists with required proof and the requested publication/integration state is accurately reported. The autonomous workflow closes only after `ayewo-igba-ise` completes and every qualifying learning is harvested or explicitly handed off; no durable learning is a valid result.
