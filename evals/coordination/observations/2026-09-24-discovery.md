# C19: supplied-guidance discovery comparison

## Decision and limits

**Result: inconclusive; no demonstrated candidate advantage.** Keep the discovery changes on their stated design rationale, without claiming measured improvement. Both settled-work outputs met the declared acceptance. The baseline discovery brief also met acceptance; the candidate discovery run was interrupted without a final artifact. No replacement run was launched.

This was a finite advisory review of text artifacts, not installed-host discovery, implemented software or human preference. Four fresh workers were assigned, one per arm/task, with requested `gpt-6-luna` and high reasoning, no inherited conversation, at most eight read calls, and no external actions or writes. Exact served-model metadata, read counts and cost telemetry were not independently captured. Read restrictions used assignments, not filesystem sandboxing. The reviewing parent knew the arms and was not human-calibrated.

Sources were frozen before execution: baseline `3d7d8357`, candidate `6bbc1bb2`. Each supplied subset contained Atọ́nà's entrypoint, initiative, ideation, progressive-shaping and decomposition references, plus Àdánwò and Àròjinlẹ̀ entrypoints. Other referenced resources were unavailable by design. [Actor tasks](../actors/C19-discovery-outcomes.md) and [private acceptance](../reviewers/C19-discovery-outcomes.md) were committed in `a2057c8f`; criteria preceded actor execution. These synthetic cases reflect a user concern, not observed production frequency. The candidate does not include the subsequent Ọ̀rọ̀ ownership refactor.

| Task | Baseline | Candidate | Evidence |
| --- | --- | --- | --- |
| Unclear direction | Pass, advisory | Interrupted, unassessed | Baseline gives three mechanisms, owner walkthrough evidence and conditional next directions, without invented findings. Candidate recovered status: read Atọ́nà, no final artifact. |
| Settled work | Pass, advisory | Pass, advisory | Both return two dependent tickets covering persistence, arrival/overdue behavior and shop access, with no reopened discovery or publication. |

The parent sent a request to conclude the delayed candidate discovery run, then interrupted it and requested recovery of any existing artifact only. The worker reported none. This intervention is a run limitation, not evidence that the instructions fail. The three completed outputs are preserved below. No broad efficacy claim or routine model campaign follows from this sample.

## Baseline: unclear direction

> **Opportunity and evidence boundary:** Help small independent repair shops spend less time chasing customers and parts. Two owners are willing to walk through their work, but no workflow has been observed or measured. The shop types and main sources of delay are still unknown; demand for software is unconfirmed.
>
> **Possible directions, not decisions:**
>
> - **Make customer follow-up predictable:** Set clear owners and timings for approvals and updates, using a simple routine first. Pursue this if customer replies and repeated status checks consume the most time.
> - **Check parts and job readiness earlier:** Confirm critical parts and customer approval before promising a repair slot; schedule around what is ready. Pursue this if late parts or reshuffling leave repair capacity idle.
> - **Coordinate purchasing across shops:** Try joint sourcing or pooled orders for frequently shared parts. Pursue this only if owners have enough overlap in parts, suppliers, and timing to outweigh coordination and inventory burdens.
>
> **What to learn next:** In each owner walkthrough, trace a few recent jobs from intake to handback. Record where work waited, who had the next action, how often someone followed up, and the minutes spent on customer contact, parts sourcing, waiting, and rescheduling. Compare the patterns across shops before choosing a direction.
>
> If approval delays dominate, focus on the follow-up routine. If parts searches dominate and requests overlap, explore shared purchasing. If jobs stall after scheduling, test readiness checks and sequencing. If causes differ by shop, choose a narrower workflow to improve first.
>
> **Question for you:** What should count as the first meaningful improvement: fewer staff minutes spent chasing per job, shorter time to complete a repair, or something else?

## Baseline: settled work

### 1. Record and reopen a parts order

**What it delivers:** An operator can create a parts order with a supplier reference and expected arrival date, then reopen it with both values intact.

**Context:** Use the existing persistence and shop-access mechanisms.

**Acceptance and proof:** Create and reopen an order; verify its reference and date are unchanged. Verify an operator from another shop cannot view or edit it.

**Depends on:** None  
**State:** Open

### 2. Track arrivals and overdue orders

**What it delivers:** An operator can mark an order arrived and see unarrived orders whose expected arrival date is before today in overdue results.

**Context:** Apply existing shop access to arrival updates and overdue results.

**Acceptance and proof:** Verify an arrived order no longer appears in overdue results; an unarrived order dated before today does. Verify another shop’s operator cannot view or edit the order.

**Depends on:** 1  
**State:** Open

**Startable frontier:** 1

## Candidate: settled work

### 1. Record and manage shop parts orders

**What it delivers:** Operators can create and reopen a parts order with its supplier reference and expected arrival date intact, then mark it arrived.

**Context:** Use the existing persistence and shop-access mechanisms.

**Acceptance and proof:** Create an order, reopen it, and confirm its reference and date are intact. Mark it arrived and confirm the order reflects that status. An operator from another shop cannot view or edit it.

**Depends on:** None  
**State:** Open

### 2. See overdue shop parts orders

**What it delivers:** Operators can identify their shop’s unarrived orders whose expected arrival date is before today.

**Acceptance and proof:** Confirm an unarrived order dated before today appears in overdue results; an arrived order and an order dated today do not. An operator from another shop cannot see these results.

**Depends on:** 1 Done  
**State:** Open

**Startable frontier:** Ticket 1.
