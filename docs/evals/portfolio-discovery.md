# Evaluation plan: portfolio discovery surface

Decision evidence for whether QP's public portfolio is hard to select because of **descriptions/routing presentation**, **the number of simultaneously visible owners**, or neither.

This file is evaluator-owned, not runtime skill guidance. It does not choose a target skill count, define a permanent profile, or authorize folding/removing an owner.

## Decision

Choose the smallest intervention that materially improves correct first-owner selection without hiding independently useful outcomes or increasing adjacent-owner mistakes.

The candidate interventions are ordered because later ones cost more:

1. current full surface;
2. same full surface with outcome-first discovery treatment;
3. reduced/profiled surface only if the first two arms show that visibility count remains the binding problem.

Do not jump to arm 3 because a raw count feels high.

## Measures

Record per case:

- selected first owner;
- whether the correct owner was selected without router detour when obvious;
- nearest wrong owner, if any;
- number of public-owner transitions proposed before the requested outcome;
- whether an independently useful owner was hidden/unavailable in the treatment;
- material explanation or selection overhead when observable; and
- host/model/candidate identity.

Do not turn token count or response length into the primary quality metric. The outcome is correct, economical ownership.

## Arm A — current surface

Use the exact-current installed/public QP surface with canonical names and current descriptions. Do not inject `alarina` unless the scenario itself genuinely calls for routing.

## Arm B — outcome-first presentation

Use the same complete portfolio and the same skill bodies. Change only the discovery projection for the evaluator/temporary host fixture:

- lead with the plain English owned outcome/failure mode;
- retain the canonical Yorùbá skill name as the identifier;
- do not add new semantic triggers or broaden authority;
- do not hide Experimental skills merely because they are experimental;
- distinguish direct-user-only activation where the exact skill metadata requires it.

Generate this projection from exact-current frontmatter/outcomes for each run rather than maintaining a second static catalogue in the repository.

If arm B materially closes the selection gap, prefer improving the real discovery projection over packaging profiles.

## Arm C — reduced/profiled candidate

Run only when A/B evidence still shows simultaneous visibility is a material selection problem.

Construct the candidate from the measured scenario population, not a preselected number such as 12. Record every excluded owner and which eligible scenario would reveal that exclusion as harmful. The reduced surface fails if it improves common routing by making a distinct legitimate outcome undiscoverable without an explicit acceptable fallback.

A profile is an installation/discovery mechanism, not permission to merge skill semantics. Source owners may remain independent even when a profile hides them by default.

## Core scenario set

Use fresh contexts. These cases intentionally cover both obvious owners and close neighbours.

| ID | User intent | Expected first owner | Closest wrong route |
| --- | --- | --- | --- |
| D1 | Implement a bounded code fix with proof | `alaga` | `atunwo`, `se-triage` |
| D2 | Review a supplied code candidate for defects/verdict | `atunwo` | `alaga`, `wo-pr` |
| D3 | Simplify a working software system without changing behavior | `pare` | `architect`, `alaga` |
| D4 | Decide whether a reported engineering issue is valid/in-scope | `se-triage` | `root-cause`, `alaga` |
| D5 | Find the causal mechanism behind an observed failure | `root-cause` | `se-triage`, `alaga` |
| D6 | Resolve a consequential user choice with dependent branches | `arojinle` | `atona`, `architect` |
| D7 | Shape and maintain a material initiative plan | `atona` | `seda-spec`, `arojinle` |
| D8 | Produce high-trust research for a material claim | `iwadi` | ordinary web lookup, `irinse` |
| D9 | Show supplied/current relationships visually | `fihanmi` | `html-artifact`, `slides` |
| D10 | Produce a standalone browser projection of supplied material | `html-artifact` | `fihanmi`, `slides` |
| D11 | Commit/push and publish the current branch as a PR | `seda-pr` | `wo-pr`, `alaga` |
| D12 | Babysit an open PR/stack through checks and feedback | `wo-pr` | `seda-pr`, `atunwo` |
| D13 | Clarify conflicting project/domain terminology | `amose` | `arojinle`, ordinary lookup |
| D14 | Produce an implementation-independent behavior contract | `seda-spec` | `architect`, `seda-ticket` |
| D15 | Design a consequential module/interface/system structure | `architect` | `pare`, `alaga` |
| D16 | Explicitly supervise the whole task across owners | `pepeye` | `atona`, `alarina` |

Add a case only when a real recurring owner collision or distinct public outcome is not discriminated by the current set. Do not expand to one row per skill for coverage theatre.

## Router cases

These test whether the router is used only when routing itself is useful:

- **R1 obvious owner:** "Review this code candidate and give me the defect verdict." Passing behavior selects `atunwo` directly rather than routing through `alarina`.
- **R2 genuine ambiguity:** "I have a reported production problem, existing logs, and I'm not sure whether I need validation, diagnosis, or a fix." Passing behavior may use `alarina` or directly distinguish the relevant owners without replaying settled work.
- **R3 inventory:** "What QP skills are available for this repository?" Passing behavior uses `alarina` inventory.

## Evidence log

No fresh-context model runner is available in the current authoring environment. These rows therefore establish a decision corpus, not a result.

| Arm | Host / model | Candidate | Result | Notes |
| --- | --- | --- | --- | --- |
| A | — | — | NOT_RUN | Fresh-context discovery evidence required |
| B | — | — | NOT_RUN | Temporary outcome-first projection not yet exercised |
| C | — | — | BLOCKED | Run only if A/B show residual visibility-count cost |

## Decision rule

- A healthy → keep the current public surface; do not add profile machinery.
- B materially better than A → improve discovery descriptions/projection; keep the full owner set visible.
- B still materially weak and C improves selection without hiding legitimate outcomes → implement the smallest host-compatible profile/manifest mechanism.
- C improves common cases only by suppressing distinct legitimate outcomes → reject that profile shape and revisit discovery/routing evidence instead.

Packaging/folding remains a later decision. This experiment cannot by itself prove that two owners should merge.
