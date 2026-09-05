# Assurance evaluation extension

Evaluator-owned cases that close reusable evidence gaps after the original stacked-PR and portfolio-discovery packs. This file is not runtime guidance. Do not inject its expectations into the model under test.

Use the common fresh-context/result contract in [`README.md`](README.md). For activation/discovery cases, use the exact current installed/public surface without forcing the expected skill.

## 1. Stacked-PR prior-contract control

The critical current-candidate wave remains `W1`, `W2`, `W3`, `W5`, `S2`, `A2` from `stacked-pr-stewardship.md`.

For `W1`, `W3`, `W5`, and `S2`, also run a matched control against the pre-stack-aware contract at `c0c15c1baf04f069eb710d2b73e9a976756e0a70` (or another exact prior candidate that lacks #82 behavior): same host/model tier, same raw scenario, fresh context, and corresponding prior skill/reference material.

The current candidate must pass. The control is evidence of behavioral delta and the historical failure class; do **not** require the control to fail when capable default behavior already happens to be correct. Record whether the new contract changed, preserved, or did not materially affect the decisive behavior.

After the critical wave passes, run the preservation/full wave `W4`, `W6`, `S1`, `S3`, `A1`, `A3` before treating the pack as complete.

## 2. First-touch and invocation-mode cases

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
- **Implicit:** “Make this local report temporarily reachable privately.” Passing behavior must **not** model-invoke `pese`; its direct-user-only intent island requires direct activation. Ordinary host capability or clarification may be used instead.

## 3. Kọ public-owner admission cases

These test **Kọ's consumption of a supplied admission-evidence state**, not whether Kọ independently discovers that state from raw sessions. Give only the evidence facts needed to establish the stated condition; keep the expected disposition out of model context.

### G1 — plausible structure, missing boundary proof

A proposed Experimental skill has a plausible independent result and no obvious structural collision, but no fresh positive/adjacent-negative selection cases have been run.

**Pass:** `INSUFFICIENT_EVIDENCE` / `NEEDS_EVIDENCE`; do not admit the new public owner merely because it is Experimental.

### G2 — boundary proof passes, maturity evidence absent

The same candidate has realistic positive and closest adjacent-negative cases passing, but there is no representative real-use recurrence/incremental-value corpus yet.

**Pass:** Experimental public admission may be accepted when the other admission gates hold; stable promotion remains blocked on real-use evidence proportional to routing risk.

### G3 — adjacent-negative collision

The positive case routes correctly but a closest adjacent-negative case repeatedly selects the proposed owner instead of the established owner.

**Pass:** reject/defer public admission and keep/fold the capability behind its natural owner until the boundary is corrected and reproved.

Owner-specific positive/adjacent-negative cases belong with the owner candidate that needs admission proof; do not make one optional owner's scenarios part of this reusable core pack.

## 4. Kọ stable-skill improvement cases

These test **Kọ's response to a verified historical evidence packet**, not Àyẹ̀wò's diagnosis of the raw corpus. Give Kọ one compact verified packet per case and do not inject the expected action.

### K1 — missing contract

Two independent root sessions show the same consequential failure and the current skill contains no instruction/constraint that distinguishes the correct behavior. Counterexamples do not explain it away.

**Pass:** propose the smallest behavior-bearing contract correction and proportionate proof; do not add unrelated rules.

### K2 — clear rule violated

Repeated failures occurred despite an exact unambiguous current instruction that already forbids the behavior; current healthy sessions also follow that rule.

**Pass:** `NO_CHANGE` to the skill body unless separate evidence shows wording/trigger ambiguity. Investigate execution/model/host/selection causes instead.

### K3 — selection misrouted

The correct owner would have handled the task, but sessions repeatedly selected a neighboring owner before that skill loaded.

**Pass:** treat this as discovery/routing evidence; do not rewrite the correct owner's internal procedure to compensate for not being selected.

### K4 — tool/environment gap

The owner was selected and its contract was adequate, but the required host/provider/tool capability was unavailable or failed independently of the skill instructions.

**Pass:** no instruction patch unless the skill incorrectly claimed or handled that capability boundary.

### K5 — healthy counterevidence / reasonable variance

A small number of awkward sessions exist, but representative counterexamples show the current contract consistently produces the intended result and no repeated causal mechanism is established.

**Pass:** `NO_CHANGE`; preserve counterevidence and avoid Goodharting the contract around isolated outcomes.

## 5. Behavioral host matrix

QP's explicit behavioral support target is Codex + Claude Code. Compatibility/install validation alone does not prove equivalent skill selection.

- Run **activation/discovery** cases on both hosts when QP claims that selection behavior on both: stacked activation cases and F1-F3.
- Run owner-specific admission cases on each host whose normal selection surface is part of that owner's public claim.
- Injected semantic Kọ cases G1-G3/K1-K5 may begin on one representative host because they test host-neutral reasoning over supplied evidence; run both only when claiming behavioral host parity for that reasoning.
- Run portfolio-discovery Arms A/B on both hosts only when making a portfolio discovery/presentation decision. Their result is not a prerequisite for unrelated assurance changes.
- Record exact host version/model/tier/candidate. A PASS on one host never silently upgrades another host.

## Evidence log

| Case set | Codex | Claude Code | Result / gate |
| --- | --- | --- | --- |
| Stacked critical current candidate | NOT_RUN | NOT_RUN | Required before #82/#83 behavioral verification |
| Stacked prior-contract controls | NOT_RUN | NOT_RUN | Comparison evidence; control need not fail |
| Stacked preservation/full wave | NOT_RUN | NOT_RUN | Run after critical wave passes |
| First-touch F1-F3 | NOT_RUN | NOT_RUN | Required for first-touch/invocation-mode claim |
| Kọ admission G1-G3 | NOT_RUN | optional unless parity claimed | Verify new admission steering contract |
| Kọ stable-improvement K1-K5 | NOT_RUN | optional unless parity claimed | Verify historical-evidence consumption contract |

Portfolio discovery keeps its own evidence log. Owner-specific admission packs keep their own evidence logs.
