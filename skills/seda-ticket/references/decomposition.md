# Ticket states, startability and checks

Use when the split must be exact: a plan needs the split inside it, tickets come from a caller's confirmed breakdown, or tickets are tracked after they are cut. It adds to the rules in `SKILL.md`.

## Work from what is settled

Use the spec and plan already in context; read the project only where an accurate boundary needs it. Do not invent a requirement. Ask only when missing authority or an ambiguity could change scope, outcome, order or ownership; settle ordinary size and order choices yourself. Keep the spec's ids and requirements in the tickets. Keep identities a caller supplied.

## Ticket boundary is meaning, not operations

A ticket does not imply a commit, branch, PR, document, proof file or agent session; the builder chooses those from integration, review, rollback and release needs. Do not split one outcome by team, layer, file type or proof activity. For a wide refactor that cannot stay green as slices, add a compatible form, move bounded groups over, then remove the old form. Name the integration check each enabling ticket serves.

Add an external prerequisite to a ticket only when a named fact, approval or resource outside the ticket set blocks starting; say who owns it. Skip guessed file paths, long snippets, generic checklists and fake dependencies.

## States

| State | Meaning | Evidence |
| --- | --- | --- |
| Open | work remains | none |
| Done | the owner's evidence proves the acceptance check | the result |
| Cancelled | removed on purpose | who decided and why |

Do not add In Progress, In Review or Blocked states; the active builder and reviewer own those. Reconcile Open to Done or Cancelled from their current results.

An Open ticket is **startable** when every ticket it depends on is Done and no external prerequisite is active; otherwise it is **blocked**. Only Done clears a dependency. A Cancelled dependency means re-plan, not unblock. The **startable frontier** is every Open ticket that is startable.

## Check before returning

Each ticket can be verified alone; dependencies are real and acyclic; acceptance is observable; the whole source scope is covered once, with no overlap; each non-vertical ticket has a necessary reason. Say which choices you inferred and which the user confirmed; do not label inferred ones confirmed. If confirmation is needed, show the affected choices and ask, then iterate. Honor a request to review the draft first.

Return the tickets in dependency order with the startable frontier. Persisting, publishing, running and review progress belong to others.
