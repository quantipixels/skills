# Idea to usable product

**Outcome:** turn an unresolved product/engineering idea into a usable, evidenced product increment without forcing settled stages to replay.

## Lane

1. **`iwadi` — evidence, when missing.** Use when current external facts, prior-art comparison, framework/provider behavior, or repository evidence can materially change the direction.
2. **`arojinle` — consequential choice, when open.** Resolve a decision only when credible alternatives materially differ.
3. **`atona` — coordinated plan, when needed.** Shape the route when delivery has material dependencies, risk, sequencing, or several owners.
4. **`architect` / `seda-spec` — structure or behavior, conditionally.**
   - use `architect` when implementation would otherwise invent consequential technical structure or ownership;
   - use `seda-spec` when observable behavior/contract remains ambiguous.
5. **`alaga` — implementation and sufficient proof.** Deliver the accepted coding outcome and return the exact candidate/result to the workflow lead.
6. **`atunwo` — independent judgment, when required.** Use when the user/workflow requires review or risk/uncertainty makes independent evidence materially valuable.
7. **`seda-pr` — publication, only when authorized.** Create/update the PR/MR; publication does not imply merge/release authority.
8. **`ayewo-igba-ise` — terminal retrospective.** After the current product/result state is fixed, postmortem the workflow and harvest only evidence-backed reusable learning through its natural owner.

## Branches and recovery

- New evidence invalidates the chosen direction → `arojinle` (or `iwadi` first if evidence is still missing).
- Architecture/spec changes invalidate delivery assumptions → refresh `atona` only where sequencing/proof changed, then return to `alaga`.
- Candidate/base changes after review → refresh only affected `atunwo` evidence.
- Review confirms a defect → `alaga`, then re-review only invalidated findings/evidence.
- Publication/CI exposes a concrete delivery defect → nearest causal owner, not a full workflow restart.
- Postmortem earns a durable improvement → route it as a separate follow-on to `ko-skill`, explicit `amose` `.learnings`, or the natural project/runtime owner; do not rewrite the judged run while reconstructing it.

## Completion and closure

Delivery stops when the accepted product increment exists with required proof and the requested publication/integration state is accurately reported. The autonomous workflow closes only after `ayewo-igba-ise` completes and every qualifying learning is harvested or explicitly handed off; no durable learning is a valid result.
