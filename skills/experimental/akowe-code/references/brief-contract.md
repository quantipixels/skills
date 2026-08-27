# Code Craft Brief contract

The brief is a bounded implementation aid, not a catalogue dump, architecture packet, review verdict, or implementation plan.

Return:

```text
Code Craft Brief
Candidate: <exact commit/tree/snapshot or supplied content identity>
Stack: <language/framework/runtime and material versions>
Evidence cutoff: <date/time and relevant source identities>
Architecture constraints: <exact-current constraints that affect this task, or none>
Project/local craft: <record identities used, or none>

DO
- <candidate-specific expert direction>

DON'T
- <candidate-triggered known-bad direction>

Complexity risks
- <state-space/control-flow/ownership issue, or none>

Proof seams
- <material invariant → cheapest stable proof owner>

Research
- <direct primary-source claim and citation, durable iwadi result, none, or evidence gap>

Exceptions and limits
- <material exception, unresolved version/stack boundary, or none>
```

## Selection quality

A good brief is:

- exact-candidate and exact-stack specific;
- small enough to hold in working memory;
- balanced between positive idiom and concrete failure avoidance;
- compatible with repository architecture and public contracts;
- explicit about version-sensitive facts;
- useful before implementation and still meaningful after a complete implementation rewrite.

Remove an item when it is merely formatting, a deterministic tool concern, a duplicate of another active item, a personal preference without consequence, or advice unrelated to the touched seam.

When the candidate is already strong, say so. `No material craft change` is a valid result.
