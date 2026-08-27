# Complexity awareness

Use metrics and code shape to ask where the reader must simulate unnecessary state or control. Do not optimize a metric in isolation.

Signals:

- cyclomatic and cognitive complexity;
- nesting and boolean-expression depth;
- branch duplication;
- fan-out and collaborator count;
- mutable state count and state-space cross product;
- exception, async, transaction, process, retry, and lifecycle transitions;
- repeated conversion/wrapper layers;
- churn × complexity where history is available;
- test explosion around one behavior.

Classify the complexity:

```text
essential
→ the domain/runtime really has these states/transitions; localize it in one deep owner and keep the representation explicit.

accidental
→ the implementation introduced extra states, branches, indirection, duplication, or ownership ambiguity; reduce the representation/mechanism.
```

Do not extract tiny methods/classes/interfaces solely to lower cyclomatic complexity. Check whether the number of meaningful decisions, state combinations, or ownership boundaries actually fell.

When a full repository/candidate simplification decision is required, route the exact candidate and signals to `pare`; `irinse` may provide deterministic metric evidence but neither tool output nor a threshold is a verdict.
