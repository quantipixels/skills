# Corpus analysis

Load this reference only when the evidence unit is a bounded multi-session corpus. Keep the common causal method, recommendation standard, and final judgment in `SKILL.md`.

## Pin the corpus

Pin the time range, session roots, repositories, inclusion and exclusion rules, selection method, and requested output before drawing conclusions.

When the corpus comes from persisted local Codex or Claude Code history, read [local session evidence](local-session-evidence.md) before sampling. Use its adapter only for deterministic inventory/normalization and structural evidence signals; eligibility, owner selection quality, incremental value, causal reconstruction, and portfolio judgment remain semantic work here or with Kọ Skill.

Inventory the corpus before sampling. Distinguish a user task, root session, resumed or copied history, rollout file, and subagent rollout. Do not treat rollout count as task count, first-to-last span as labour time, or repeated transcript content as independent evidence.

For a large corpus, use deterministic extraction for counts and metadata, then read the smallest representative and risk-weighted sample that can answer the question. Record the population, sample, exclusions, and evidence gaps.

## Reconstruct bounded causal records

Reconstruct bounded causal records for the sampled sessions. Do not invent one global timeline or infer the same contract across different tasks. Include contrasting successful or uneventful records when they can disprove a claimed pattern.

Call a pattern repeated only when the same material mechanism appears in at least two independent root sessions. Report its supporting records, eligible denominator when known, counterevidence, and coverage limit. Keep a single incident labeled as an incident even when it produced many subagent rollouts or repeated recovery attempts.

Normalize corpus counts to the pinned unit and report the numerator, denominator, and exclusions when they matter. Use counts and elapsed time only when the record supports them.

### Experimental opportunity evidence

When the corpus is being used to evaluate Experimental skills, Àyẹ̀wò owns reconstruction of historical opportunity and use. Separate opportunity from invocation.

For each root session and experiment in scope, classify only when evidence supports it:

- `ELIGIBLE_SELECTED` — the experiment was installed/active/discoverable, its owned result was materially needed, and it was selected;
- `ELIGIBLE_MISSED` — the experiment was installed/active/discoverable and its owned result was materially needed, but it was not selected;
- `MIS_TRIGGERED` — it was selected without the owned result being materially needed or outside its intent/authority/cost boundary;
- `INELIGIBLE` — the owned result was not needed;
- `UNAVAILABLE` — the result was needed but the skill was not installed/active/discoverable or a named capability blocked it; or
- `UNCERTAIN` — evidence cannot responsibly establish opportunity or availability.

For `ELIGIBLE_SELECTED`, record what materially changed because the experiment ran, its incremental cost, and whether it preserved the stable owner's lifecycle/result/authority. For `ELIGIBLE_MISSED`, identify the observed consequence only when the record supports it—for example duplicated specialist work, weaker evidence, rework, or a later correction. Do not invent counterfactual time/token savings.

Raw invocation count is never the denominator. A rare experiment may be healthy with very few uses if it was selected in the few genuinely eligible sessions. Conversely, frequent invocation can be negative evidence when it is repeatedly mis-triggered or adds no independent value.

Do not manufacture experiment invocations during real user work to improve sample size. The corpus observes natural eligible opportunities; temporary controlled steering comparisons belong to skill evaluation only when selection behavior remains materially uncertain.

Produce a compact evidence packet that another owner can consume without reconstructing the corpus:

```text
Experimental use evidence

Skill:
Corpus/population:
Source | installed | active | published boundary:
Eligible opportunities:
Selected:
Missed:
Mis-triggered:
Unavailable:
Observed incremental value:
Observed cost:
Boundary-health evidence:
Counterevidence:
Coverage/evidence gaps:
```

This packet is historical evidence, not a promotion/removal verdict. `ko-skill` may consume it when a portfolio disposition is requested.

### Stable-skill improvement evidence

When real-use history is being used to improve an already-stable skill, Àyẹ̀wò owns reconstruction and returns a compact packet rather than drafting the skill change itself.

For every material repeated failure mechanism, distinguish the smallest cause supported by the historical record:

- `CONTRACT_MISSING` — the active skill lacked a behavior-bearing rule/boundary that the repeated cases needed;
- `CONTRACT_AMBIGUOUS` — the active rule plausibly supported more than one consequential behavior and the ambiguity contributed to the failure;
- `CLEAR_RULE_VIOLATED` — the active skill already required the correct behavior but the agent did not follow it;
- `SELECTION_MISROUTED` — the wrong owner was selected or the right owner was not discoverable when needed;
- `TOOL_OR_ENVIRONMENT_GAP` — the skill contract was adequate but a host/tool/environment capability prevented the intended behavior;
- `REASONABLE_VARIANCE_OR_OBSOLETE` — the observed choice was reasonable under the then-current contract or later requirements made it obsolete; or
- `NOT_IMPLICATED` — the skill did not materially cause the observed failure.

Do not convert `CLEAR_RULE_VIOLATED`, `TOOL_OR_ENVIRONMENT_GAP`, or ordinary model variance into another skill instruction merely because the incident was costly. A stable-skill edit is earned when evidence shows a reusable owner-contract deficiency—normally `CONTRACT_MISSING`, `CONTRACT_AMBIGUOUS`, or a repeated selection boundary defect—or when one severe owner-wide failure is enough under Kọ Skill's normal admission rule.

Return this packet when Kọ Skill or another authoring decision needs the historical evidence:

```text
Stable skill improvement evidence

Skill:
Corpus/population:
Source | installed | active | published boundary:
Repeated failure mechanism:
Independent supporting root sessions:
User corrections / recovery evidence:
Current-contract assessment: <classification + exact active rule/evidence>
Selection / adjacent-owner evidence:
Observed consequence / recovery cost:
Counterevidence / healthy cases:
Smallest plausible owning change:
Proof needed after change:
Coverage/evidence gaps:
```

The packet is evidence, not an edit instruction or verdict. Kọ Skill decides whether the smallest justified response is `NO_CHANGE`, selection/discovery repair, host/tool repair, instruction clarification, reference/resource change, owner-boundary change, or another task-native disposition.

## Report the corpus

Return the executive verdict, population and unit definitions, inventory and sampling ledger, repeated-pattern matrix with independent supporting records and counterevidence, representative causal chains, ranked frictions, effective recoveries, recommendation assessment, rejected recommendations, and residual limits.

When Experimental evaluation is in scope, also return the opportunity evidence packet per experiment. Do not infer promotion, narrowing, folding, replacement, or removal from invocation counts; leave portfolio-shape judgment to `ko-skill` unless that judgment is explicitly part of a broader authorized workflow.

When stable-skill improvement is in scope, return the stable-skill improvement packet for each skill whose contract/selection boundary is materially implicated. Preserve `NO_CHANGE` evidence when the current contract was adequate; do not report only problematic sessions.

When the corpus spans projects, include one dossier for every normalized project in the population, not only sampled or problematic projects. Each dossier must state:

- aliases and evidence coverage;
- outcomes and verified current state;
- user actions and decisions;
- effective work;
- failures, inefficiencies, and gaps;
- applicable lessons;
- recommendations and no-change findings;
- counterevidence; and
- limits.

Classify each durable decision or lesson as implemented, still applicable, superseded, or unresolved, and name its owning project document, skill, test, or workflow when known. Link aggregate patterns to their project dossiers; do not use the aggregate to replace project-level analysis.

When skill corrections are authorized, distinguish source, installed, published, and active states.
