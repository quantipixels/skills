# QP operating architecture

QP exposes one low-cognitive-load operating surface over independently owned skills. Generic `Use QP` intent enters through `alarina`; an explicit valid owner selection bypasses routing. Every selected owner keeps its semantic outcome, authority, lifecycle, result, proof, and recovery semantics.

Engineering, Design, Productivity, and Experimental are all first-party parts of the current portfolio. Experimental marks evidence/promotion maturity, not a category-wide acceptance tax or routing exclusion. Runtime eligibility remains governed by each skill's normal trigger, intent, authority, cost, safety, evidence, and host-invocation boundaries.

Evidence cutoff: `quantipixels/skills` `ori` at `ed9ff7d84cc84cba71684caa6a5ddf340a3463c3` (`Give Experimental skills earned runtime opportunities (#58)`), 2026-08-31.

## Decision

QP consolidates the **operating surface**, not the expertise.

One independently useful outcome has one semantic owner. QP may route or execute across owners, but no router, host adapter, convenience entrypoint, or maturity group absorbs another owner's result or lifecycle.

The useful architecture is:

```text
User / host
   │
   ├── exact owner named ───────────────────────────────► exact owner
   │
   └── generic `Use QP`
            │
            ├── host supports QP Agent ─► QP Agent ─┐
            │                                       │
            └── skill-only host ────────────────────┤
                                                    ▼
                                                `alarina`
                                                    │
                                      shortest current owner/flow
                                                    │
                                                    ▼
                                             native owner results
```

## Alárinà is the QP front door

`alarina` owns generic portfolio entry and current-state routing.

- `Use QP for this` and `Use qp-skills` are routing intent, not a new execution mode.
- An explicit valid skill selection bypasses routing when that skill already owns the requested result.
- Current repository skill metadata is the inventory; Alárinà does not maintain a copied catalogue.
- Routing starts from the exact current state and does not replay settled exploration, planning, architecture, implementation, review, publication, or postmortem work.
- Every added owner must contribute an independently useful result that is actually required.
- Routing grants no extra mutation, provider, credential, publication, destructive-action, or specialist authority.
- If no QP owner materially improves the requested result, Alárinà returns `NO_ROUTE`.

## QP Agent

QP defines one optional **main-agent host adapter** for hosts that support custom agents. It provides a single QP-facing execution surface without introducing another semantic owner.

The QP Agent:

- preloads the canonical `alarina` routing contract;
- delegates generic route selection to Alárinà instead of copying route policy;
- executes or coordinates the selected owners in the host's normal context;
- passes only context/results needed by the active owner relationship;
- respects each skill's normal trigger, intent, authority, cost, safety, evidence, and host-invocation boundaries; and
- stops at the requested outcome.

It does **not** own routing policy, planning, implementation, review verdicts, publication, durable state, acceptance, proof, or a copied skill catalogue. It has no independent task lifecycle.

A host with no custom-agent support uses Alárinà or exact skills directly. The QP Agent is therefore an optional projection, not a portability dependency or shared runtime.

## Owner composition

QP has no universal task lifecycle. Route from the work's current state and add an owner only when its result is independently required.

Representative substantial software delivery may compose:

```text
shape / contract → deliver → review / prove
```

This is orientation, not a mandatory playbook. Any stage may be absent and direct invocation may begin anywhere.

Common owners include:

- initiative lifecycle: `atona`;
- material user decisions: `arojinle`;
- technical architecture: `solution-architect`;
- normative behavior: `seda-spec` when a separate behavior contract is required;
- prospective scope/minimality steering: `scope-guard` when that result is independently useful;
- delivery decomposition: `seda-ticket` when consumable slices help;
- implementation and integrated proof: `alaga`;
- candidate-pinned implementation scrutiny: `akowe` when its normal admission/cost boundary is satisfied;
- causal diagnosis: `root-cause` when competing mechanisms must be resolved before a responsible correction;
- code verdict/parity: `atunwo`;
- simplification: `pare`;
- human-led review disposition: `hitl-review`;
- browser journey proof: `dogfood` when literal user journeys and browser-dependent acceptance claims remain.

Publication, stewardship, postmortem, handoff, representation, research, and durable reconciliation are conditional owner outcomes, not automatic suffixes.

## Experimental maturity

#58 establishes the portfolio rule: Experimental skills are first-party runtime candidates whose maturity is under evaluation.

This architecture does not add a second Experimental policy. It relies on the current repository/skill contracts:

- Experimental status alone neither requires manual acceptance nor grants invocation.
- Normal trigger, intent, authority, cost, safety, evidence, and host-invocation gates decide runtime eligibility.
- A skill may deliberately require direct user activation when that is part of its own intent island.
- Experiments are never invoked merely to manufacture graduation evidence.
- One successful use does not silently redefine another owner or justify promotion.
- Promotion, keep-experimenting, narrowing/folding, replacement, or removal requires the evidence boundary owned by `ko-skill` and supplied verified real-use evidence when historical opportunity/value claims are material.

The QP Agent and Alárinà preserve these per-skill gates rather than creating a group-wide override.

## Playbook policy

QP has no first-class top-level playbook layer.

Repeated behavior belongs at the smallest surface that owns it:

- owner-specific recurring procedure → owner-local invariant/reference;
- stable cross-owner routing relationship → `alarina`;
- initiative sequencing → `atona`;
- implementation/convergence procedure → `alaga` or the relevant implementation owner;
- independently useful new outcome with its own authority/acceptance boundary → only then consider a new public skill.

Do not create feature/bug/refactor/research playbook skills merely to restate combinations current owners can derive. A shared playbook or deep module must pass the same deletion test as every seam: removing it must lose real policy, lifecycle, authority, compatibility, proof, or independently reusable judgment.

## Writing composition

`technical-writing` and `yo-slop` remain separate useful outcomes.

- `technical-writing` owns document mode, instruction structure, technical sentence clarity, and unambiguous syntax.
- `yo-slop` owns final cleanup or explicit pruning without changing facts/contract.
- Repository guidance no longer forces `technical-writing → yo-slop` as a mandatory mini-pipeline.
- Use cleanup only when that separate result is independently useful; otherwise stop when the technical-writing outcome is complete.

This applies the same architecture rule to productivity work: a commonly useful next action is not automatically a required phase.

## Design vertical

Design uses the same operating surface as the rest of QP.

`apere` remains a valid Design-domain router because broad/multi-deliverable Design work can require design-specific prerequisites, dependency order, parallelism, shared constraints, and approval boundaries. Focused Design work still goes directly to its specialist.

The Quanti Pixels redesign pilot proved one deeper stable Design capability worth promoting into existing owners rather than creating a new lifecycle owner:

```text
actual product evidence
  → freeze settled product/brand constraints
  → identify the unresolved material design question
  → explore materially different mechanisms only when the choice is genuinely open
  → select one coherent direction
  → implementation owner
  → exact rendered result
  → Amọ̀ye review against accepted direction
  → smallest material correction
  → implementation owner rerender/native proof
  → stop when material deficiencies are resolved
```

`amoye-ui-ux` owns design direction, proportional exploration, selection, and rendered design judgment. `asa-oju-ibanisoro` owns React/web implementation, native proof, applying accepted corrections, and rerendering. Neither absorbs the other's result or lifecycle.

Durable project-specific design truth discovered through selection/convergence goes to `amose` only when it is non-obvious, reusable, and confirmed. Generic UX advice, rejected taste, and one-off polish do not become project knowledge.

## Portfolio audit disposition

A bounded stable/leaf-owner audit found no broad merge/removal required by this architecture. Most current owners already satisfy the one-outcome/conditional-composition rule, so mass edits would be churn rather than consolidation.

Close boundaries reviewed as independently useful include:

- `seda-spec` / `seda-ticket` — normative behavior versus delivery decomposition;
- `scope-guard` / `alaga` / `pare` — prospective scope steering versus implementation versus read-only simplification;
- `se-triage` / `root-cause` / `alaga` — report classification versus causal diagnosis versus correction;
- `atunwo` / `pare` / `hitl-review` — code verdict/parity versus simplification versus human-led review decision;
- `seda-pr` / `wo-pr` — publication versus continuing stewardship;
- `akowe` / `ro-wo` / `iwadi` / `orisun` — candidate implementation counsel versus premise challenge versus sufficient/durable research versus exact-version upstream-source escalation;
- `alarina` / `apere` — portfolio routing versus Design-domain multi-owner decomposition;
- `technical-writing` / `yo-slop` / `salaye` — technical structure versus cleanup/pruning versus reusable plain-language explanation; and
- `html-artifact` / `prototype` / Design owner / `dogfood` — information projection versus disposable decision instrument versus actual interface work versus real-browser journey proof.

Do not consolidate toward a numerical skill target. Merge, fold, promote, replace, or remove only from exact-current ownership evidence and the applicable real-use evidence boundary.

## Global versus owner-local guidance

There is no universal QP runtime instruction file or `qp` super-skill.

Portfolio-wide invariants are projected only where needed:

- Alárinà owns generic QP entry and routing;
- repository guidance owns portfolio/maturity policy;
- a QP Agent carries only minimal host-adapter rules;
- current skill metadata remains the inventory; and
- each specialist independently preserves the authority/safety rules required for its own invocation.

Keep owner admission rules, procedure, state, proof, deep references, provider safety, outputs, and recovery with the owner. Do not centralize them into a shared runtime merely to reduce prose.

## Failure and recovery

- **Inventory drift:** current distribution/skill metadata wins; stale routing prose is a defect, not authority.
- **Already-settled work:** enter at the current owner and do not replay prior stages.
- **No useful QP owner:** Alárinà returns `NO_ROUTE`; the host may continue with ordinary capabilities.
- **Stale owner result:** the consuming owner refreshes the exact result/candidate it depends on; no coordinator reconciles copied state.
- **Long or multi-session work:** use the active semantic owner record and `handoff` only when context must move.
- **QP Agent unavailable:** use Alárinà or direct owner invocation; QP remains fully usable.
- **Experiment unsuitable/unavailable:** continue through another justified route; Experimental status itself is neither blocker nor guarantee.

## Architecture contract

```text
Candidate:
QP operating architecture / 2026-08-31 / #58-aligned migration

Critical invariants:
- Current distribution/skill metadata is the portfolio inventory.
- Generic QP intent routes through alarina.
- Explicit valid owner selection bypasses routing.
- One independently useful outcome has one semantic owner.
- Owners retain lifecycle, authority, result, proof, and recovery semantics.
- QP Agent is an execution adapter, never a semantic owner.
- Experimental runtime eligibility remains per-skill and maturity-agnostic.
- Conditional later outcomes are selected only when independently requested/needed.

Allowed directions:
- user/host → explicit current owner
- user/host → alarina → selected owner(s)
- user/host → QP Agent → alarina → selected owner(s)
- owner → supporting owner when its independent result is required
- alarina → apere when Design-domain routing itself is needed
- experimental owner/result → consumer when current contracts permit it
- owner result → amose when durable reusable project/domain truth is established

Forbidden states:
- alarina or QP Agent owning specialist lifecycle/state/acceptance/proof
- copied skill catalogue inside a host agent/coordinator
- mandatory public playbook sequence
- category membership alone granting stronger authority or forcing a detour
- routing granting mutation/provider/credential/publication authority
- caller copies of callee procedure/result schemas
- unconditional publication/postmortem/handoff/cleanup/compound stages
- consolidation to satisfy a numerical skill-count target

Complexity budget:
- no public qp-mode skill
- no shared executable orchestration runtime
- no new datastore/service/queue/protocol
- no required provider-specific host adapter
- no duplicate runtime owner catalogue

Compatibility:
- preserve all current skill names/direct invocation
- preserve current installation/distribution model
- generic Use QP discovers alarina
- hosts with no custom-agent support remain first-class
- preserve #58 Experimental runtime and evidence boundaries

Primary proof seams:
- current distribution/skill metadata → inventory
- alarina contract → current-state/direct-owner behavior
- repository validation/CI → package/link/metadata integrity
- plugin-agent validator → host projection structure/preload integrity
- QP Agent → thin-projection parity against alarina/this ADR
- Design owner contracts → rendered-convergence ownership boundary
- Experimental portfolio disposition → ko-skill + verified real-use evidence when required

Evidence cutoff:
quantipixels/skills ori @ ed9ff7d84cc84cba71684caa6a5ddf340a3463c3, 2026-08-31
```

## Rejected alternatives

**Task-wide `qp-mode` skill** — rejected because it duplicates specialist lifecycle/authority and creates another semantic owner.

**Shared executable orchestration runtime** — rejected; the host adapter is instructions plus native host skill invocation, not a service/runtime layer.

**Public playbook catalogue** — rejected because current owner contracts and routing derive the needed composition.

**Agent as semantic coordinator** — rejected. The QP Agent is a thin host execution adapter.

**Experimental as permanent quarantine** — rejected by #58. Experimental is runtime maturity/evidence status; individual skills own their own invocation gates.

**Mandatory writing cleanup** — rejected because cleanup/pruning is a separate outcome, not an inevitable stage after technical writing.

**New Design convergence owner** — rejected because the useful behavior belongs cleanly inside existing design-judgment and implementation owners.

**Mass skill consolidation** — rejected as an architecture goal. Revisit individual skills only from exact-current overlap and evidence.

## Implemented migration

This architecture is implemented through bounded changes rather than blanket edits to every skill:

- **Generic QP entrance** — Alárinà is discoverable from `Use QP` / `Use qp-skills` and remains a router only.
- **Claude Code host projection** — `agents/qp.md` plus plugin registration provide the optional QP main-agent surface without a new runtime or copied catalogue.
- **Host projection proof** — deterministic validation checks plugin-agent paths, frontmatter, names, local preloads, and per-skill model-invocation restrictions.
- **Writing composition** — repository guidance no longer forces `technical-writing → yo-slop`.
- **Design convergence** — the real Quanti Pixels redesign pilot promoted constraint freezing, proportionate mechanism-diverse exploration, exact rendered review, and Amọ̀ye/Àṣà convergence into stable Design owners.
- **No gratuitous leaf churn** — audited owners that already satisfy the architecture remain unchanged.

#58's Experimental runtime changes are preserved as the governing portfolio policy rather than duplicated or rolled back by this migration.

## Implementation proof

Repository CI is the package-integrity owner for the published candidate. The final migration requires the existing package-state/Akọsílẹ̀ checks plus the QP skill-package validator and plugin-agent validator to pass on the exact PR head.

The plugin-agent validator is deliberately per-skill: group membership is not a failure; an individual `disable-model-invocation: true` remains enforceable when a skill uses it.
