# Idea to usable product

**Outcome:** turn an unresolved product/engineering idea into a usable, evidenced product increment without forcing settled stages to replay.

## Lane

1. **`iwadi` — evidence, when missing.** Use when current external facts, prior-art comparison, framework/provider behavior, or repository evidence can materially change the direction.
2. **`arojinle` — consequential choice, when open.** Resolve a decision only when credible alternatives materially differ.
3. **`atona` — coordinated plan, when needed.** Shape the route when delivery has material dependencies, risk, sequencing, or several owners.
4. **`architect` / `seda-spec` — structure or behavior, conditionally.**
   - use `architect` when implementation would otherwise invent consequential technical structure or ownership;
   - use `seda-spec` when observable behavior/contract remains ambiguous.
5. **Independent plan review — whenever an explicit plan becomes material.** After all plan-affecting decisions are reflected in the fixed plan, review it in fresh read-only context before treating it as ready or using it to progress work. Route findings back to the nearest semantic owner, update the plan, and review materially changed plans again. If this route never needed an explicit plan, skip this stage rather than manufacturing one.
6. **`alaga` — implementation and sufficient proof.** Deliver the accepted coding outcome and return the exact candidate/result to the workflow lead.
7. **`atunwo` — independent code judgment, when required.** Use when the user/workflow requires review or risk/uncertainty makes independent evidence materially valuable.
8. **`seda-pr` — publication, only when authorized.** Create/update the PR/MR; publication does not imply merge/release authority.
9. **`ayewo-igba-ise` — terminal retrospective.** After the current product/result state is fixed, postmortem the workflow and harvest only evidence-backed reusable learning through its natural owner.

## Branches and recovery

- New evidence invalidates the chosen direction → `arojinle` (or `iwadi` first if evidence is still missing).
- Architecture/spec work changes sequencing, dependencies, proof, or ownership → refresh `atona` only where the plan changed, then return to plan review while the plan remains material.
- Plan review reopens sequencing/dependencies → `atona`; reopens architecture → `architect`; reopens observable behavior → `seda-spec`; exposes a consequential user choice → `arojinle`. Review the resulting fixed plan again before treating it as ready.
- Candidate/base changes after code review → refresh only affected `atunwo` evidence.
- Code review confirms a defect → `alaga`, then re-review only invalidated findings/evidence.
- Publication/CI exposes a concrete delivery defect → nearest causal owner, not a full workflow restart.
- Postmortem earns an existing agent-instruction improvement → route it as a separately authorized follow-on to `oro-fun-sigidi`; new skill identity or material routing/ownership changes remain proposals until the user explicitly accepts them. Other durable improvements go to explicit `amose` `.learnings` or their natural project/runtime owner. Do not rewrite the judged run while reconstructing it.

## Completion and closure

Delivery stops when the accepted product increment exists with required proof and the requested publication/integration state is accurately reported. The autonomous workflow closes only after `ayewo-igba-ise` completes and every qualifying learning is harvested or explicitly handed off; no durable learning is a valid result.
