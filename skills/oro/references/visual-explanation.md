# Visual explanation

Lead with the smallest faithful specimen, then state its decisive consequence. Use supplied evidence and label observed implementation, proposed design and illustrative examples distinctly.

Choose the form from the reader's question: pseudocode for decision branches, a call tree for nesting, a sequence view for cross-component order, a component/file map for ownership, types/signatures for caller contracts, a state diagram for allowed transitions, or an exact/conceptual diff for change. Prose is enough for a simple fact.

Preserve execution semantics. Distinguish synchronous calls, queues, callbacks, transactions and external effects where they matter; a call tree does not prove one stack, runtime order or atomicity. Mark inferred/proposed edges and unresolved dispatch. Keep real symbols and paths without fabricating inventory.

Label a behavioral or structural sketch **Conceptual change**. Exact diffs retain actual paths, lines and order. Keep before/after views comparable, and show the whole block when omitted context would hide ownership or sequencing.

Place each specimen beside the explanation, evidence or consequence it supports. Rendering cannot supply a missing requirement or conclusion. Use `html-artifact` for portable HTML and the installed presentation capability for a deck; preserve the requested format and existing living artifact.
