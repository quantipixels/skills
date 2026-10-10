---
name: seda-ticket
description: Splits a spec or plan into tickets, each a vertical slice that delivers something checkable on its own, with acceptance check, dependencies, size and a safe landing order. Use when settled work needs to be cut into buildable pieces or handed to several agents.
---

# Seda Ticket

**Output:** an ordered set of tickets, each buildable, checkable and landable on its own, in an order where every landing leaves the project working. Working record (kind: ticket), one per ticket, numbered in landing order; reuse the set that exists for this spec. Publish to an issue tracker (GitHub Issues, Linear, Jira) only on request, with the tracker's own interface, and report the links.

**Needs:** a spec or plan with acceptance checks and no blocking open question. If the work is not settled enough to cut, return to the caller and say what is missing. Do not invent a requirement to fill a gap.

## Method

A ticket is a **vertical slice**: a thin piece that goes end to end through the layers it needs and delivers something a person or test can check alone. Do not split by layer, role or file type ("the API", "the UI", "the tests") when one slice could cross them.

A **wide refactor** is the exception: its pieces cannot each stay green as a slice. Make it one ticket, or a sequenced set across layers (add the new form, move users over in bounded groups, remove the old form), and write the reason in the ticket. An enabling piece that truly blocks later slices is allowed on the same terms.

Use [the ticket template](references/ticket-template.md): a title that states the outcome, what it delivers, its acceptance check (point at the spec's check ids), dependencies, size (rough small, medium, large; a large one usually should be cut again), and a boundary only where a wrong delivery is plausible.

Order so each ticket lands safely: dependencies first, then the slice that proves the riskiest assumption early, then the rest. Keep dependencies real and acyclic and note which can run in parallel; no fake dependencies. A boundary is about meaning, not commits or branches.

Read [decomposition](references/decomposition.md) when tickets are tracked after they are cut (Open, Done, Cancelled; startable or blocked), or when a caller supplied a confirmed breakdown.

## Done

Every acceptance check in the source is covered by some ticket, no ticket carries scope the source does not, and each ticket could be picked up by someone who has not read the others.

## Return

Return the ordered list with dependencies and the tickets that can start now.
