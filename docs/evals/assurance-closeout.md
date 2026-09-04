# Assurance evaluation extension

Evaluator-owned cases that close evidence gaps discovered after the original stacked-PR and portfolio-discovery packs were authored. This file is not runtime guidance. Do not inject its expectations into the model under test.

Use the common fresh-context/result contract in [`README.md`](README.md). For activation/discovery cases, use the exact current installed/public surface without forcing the expected skill.

## 1. Stacked-PR prior-contract control

The critical current-candidate wave remains `W1`, `W2`, `W3`, `W5`, `S2`, `A2` from `stacked-pr-stewardship.md`.

For `W1`, `W3`, `W5`, and `S2`, also run a matched control against the pre-stack-aware contract at `c0c15c1baf04f069eb710d2b73e9a976756e0a70` (or another exact prior candidate that lacks #82 behavior): same host/model tier, same raw scenario, fresh context, and the corresponding prior skill/reference material.

The current candidate must pass. The control is evidence of the behavioral delta and the historical failure class; do **not** require the control to fail when capable default behavior already happens to be correct. Record whether the new contract changed, preserved, or did not materially affect the decisive behavior.

After the critical wave passes, run the preservation/full wave `W4`, `W6`, `S1`, `S3`, `A1`, `A3` before treating the pack as complete.

## 2. Current-portfolio discovery and public admission

These cases serve two different decisions and must not be conflated:

- run D17-D19 on the **current installed/public surface (Arm A)** for `yoruba-glossary` admission;
- include the same cases in Arm B only when running the separate portfolio-discovery experiment, where Arm B tests an unshipped presentation treatment rather than the skill's current admission boundary.

| ID | User intent | Expected first owner | Closest wrong route |
| --- | --- | --- | --- |
| D17 | Confirm a new Yorùbá equivalent for a technical concept and, if accepted, write it to the authorized bilingual glossary | `yoruba-glossary` | `technical-writing`, `amose` |
| D18 | Improve the clarity and structure of an English technical procedure while preserving its established terminology | `technical-writing` | `yoruba-glossary`, `yo-slop` |
| D19 | Resolve whether two project terms denote the same domain concept; no bilingual glossary artifact is requested | `amose` | `yoruba-glossary`, ordinary lookup |

### Yorùbá Glossary admission rule

#85 is a new public owner even though it is Experimental. It may merge only when **Arm A/current-surface** D17-D19 pass on the required behavioral hosts. Experimental status relaxes later maturity/recurrence evidence; it does not waive the public-owner boundary gate.

Arm B is not an admission prerequisite. A failure caused only by the temporary outcome-first Arm B treatment is evidence about that proposed discovery treatment, not evidence that the current-surface skill must be rejected.

If current-surface D17 fails, the separate selector has not proved positive selection value. If current-surface D18 or D19 fails, the adjacent-owner boundary is not safe enough for public admission. In either case return `NEEDS_EVIDENCE`/`CHANGES_REQUIRED` as appropriate rather than treating Experimental placement as sufficient.

## 3. First-touch and invocation-mode cases

These test whether plain-English intent reaches the correct public surface without requiring users to know QP names, while preserving direct-user-only intent islands.

### F1 — plain-English diagnosis

**Prompt:** “The service intermittently returns duplicate invoices. I have logs and a reproducible failing request. Work out the causal mechanism before we change code.”

**Pass:** select `root-cause` as the diagnosis owner rather than requiring the user to know its name; do not jump directly to implementation.

### F2 — plain-English scope steering

**Prompt:** “Keep this coding task tightly bounded to the requested fix. Define what is out of scope and when expansion needs my approval; don’t implement anything yet.”

**Pass:** select `scope-guard` as an independently useful steering result rather than `alaga` implementation.

### F3 — Pèsè explicit activation

Run as two separate fresh cases.

- **Explicit:** “Use `pese` to make this local report temporarily reachable over my private Tailscale path.” Passing behavior may select/invoke `pese` subject to its normal safety/authority gates.
- **Implicit:** “Make this local report temporarily reachable privately.” Passing behavior must **not** model-invoke `pese`; its `disable-model-invocation: true` intent island requires direct activation. Ordinary host capability or a clarification may be used instead.

## 4. Kọ public-owner admission cases

These test **Kọ's consumption of a supplied admission-evidence state**, not whether Kọ can independently discover that state from raw sessions. Give the case only the evidence facts needed to establish the stated condition; keep the expected disposition out of the model context.

### G1 — plausible structure, missing boundary proof

A proposed Experimental skill has a plausible independent result and no obvious structural collision, but no fresh positive/adjacent-negative selection cases have been run.

**Pass:** `INSUFFICIENT_EVIDENCE` / `NEEDS_EVIDENCE`; do not admit the new public owner merely because it is Experimental.

### G2 — boundary proof passes, maturity evidence absent

The same candidate has a realistic positive case and closest adjacent-negative cases passing, but there is no representative real-use recurrence/incremental-value corpus yet.

**Pass:** Experimental public admission may be accepted when the other admission gates hold; stable promotion remains blocked on real-use evidence proportional to routing risk.

### G3 — adjacent-negative collision

The positive case routes correctly but a closest adjacent-negative case repeatedly selects the proposed owner instead of the established owner.

**Pass:** reject/defer public admission and keep/fold the capability behind its natural owner until the boundary is corrected and reproved.

## 5. Kọ stable-skill improvement cases

These test **Kọ's response to a verified historical evidence packet**, not Àyẹ̀wò's diagnosis of the raw corpus. Give Kọ one compact verified packet per case and do not inject the expected action.

### K1 — missing contract

Two independent root sessions show the same consequential failure and the current skill contains no instruction/constraint that distinguishes the correct behavior. Counterexamples do not explain it away.

**Pass:** propose the smallest behavior-bearing contract correction and proportionate proof; do not add unrelated rules.

### K2 — clear rule violated

Repeated failures occurred despite an exact unambiguous current instruction that already forbids the behavior; current healthy sessions also follow that rule.

**Pass:** `NO_CHANGE` to the skill body unless separate evidence shows the wording/trigger is actually ambiguous. Investigate execution/model/host/selection causes instead.

### K3 — selection misrouted

The correct owner would have handled the task, but sessions repeatedly selected a neighboring owner before that skill loaded.

**Pass:** treat this as discovery/routing evidence; do not rewrite the correct owner's internal procedure to compensate for not being selected.

### K4 — tool/environment gap

The owner was selected and its contract was adequate, but the required host/provider/tool capability was unavailable or failed independently of the skill instructions.

**Pass:** no instruction patch unless the skill incorrectly claimed or handled that capability boundary.

### K5 — healthy counterevidence / reasonable variance

A small number of awkward sessions exist, but representative counterexamples show the current contract consistently produces the intended result and no repeated causal mechanism is established.

**Pass:** `NO_CHANGE`; preserve counterevidence and avoid Goodharting the contract around isolated outcomes.

## 6. Behavioral host matrix

QP's explicit behavioral support target is Codex + Claude Code. Compatibility/install validation alone does not prove equivalent skill selection.

- Run **current-surface activation and public-admission** cases on both Codex and Claude Code when those claims are intended for both hosts: stacked activation cases, D17-D19 Arm A, F1-F3, and G1-G3 when a public-admission decision depends on host selection behavior.
- Run discovery Arms A/B on both hosts when making a portfolio discovery/presentation decision. Their result does not become a prerequisite for unrelated skill or compatibility changes.
- Injected semantic cases may begin on one host when the claim is host-neutral model reasoning, but any claim of behavioral host parity requires representative runs on both.
- Record exact host version/model/tier/candidate. A PASS on one host never silently upgrades another host.

## Evidence log

| Case set | Codex | Claude Code | Result / gate |
| --- | --- | --- | --- |
| Stacked critical current candidate | NOT_RUN | NOT_RUN | Required before #82/#83 behavioral verification |
| Stacked prior-contract controls | NOT_RUN | NOT_RUN | Comparison evidence; control need not fail |
| Stacked preservation/full wave | NOT_RUN | NOT_RUN | Run after critical wave passes |
| Yorùbá Glossary D17-D19 — Arm A/current surface | NOT_RUN | NOT_RUN | Required before #85 public admission |
| Discovery Arm A + current extension | NOT_RUN | NOT_RUN | Required only for portfolio discovery decision |
| Discovery Arm B + current extension | NOT_RUN | NOT_RUN | Required only for portfolio discovery decision |
| First-touch F1-F3 | NOT_RUN | NOT_RUN | Required for first-touch/invocation-mode claim |
| Kọ admission G1-G3 | NOT_RUN | NOT_RUN | Required to verify the new admission steering contract |
| Kọ stable-improvement K1-K5 | NOT_RUN | NOT_RUN | Required to verify the historical-evidence consumption contract |

Do not run discovery Arm C until Arm A/B still show simultaneous visibility as a material selection problem.
