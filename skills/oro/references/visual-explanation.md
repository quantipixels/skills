# Visual explanation

Lead with the smallest faithful specimen, then explain its decisive consequence. Use supplied evidence; distinguish observed implementation, proposed design and illustrative examples.

| Reader question | Useful form |
| --- | --- |
| How does the algorithm decide? | Pseudocode with decisive branches and failure paths. |
| Who calls whom? | A call tree for nested calls; a sequence diagram for cross-component ordering. |
| Where do state and UI responsibilities live? | A component tree with relevant state and module boundaries. |
| Where does this behavior belong? | A shallow file/responsibility map with source paths. |
| What contract do callers use? | Types or signatures showing relevant inputs, outputs and errors. |
| What changes? | A structural diff with enough unchanged context to preserve ownership and order. |
| Which states and transitions are allowed? | A state diagram with consequential guards and outcomes. |

Select forms by the question, not a quota. Prefer the host's rendered form when it improves readability; short code specimens remain useful. Prose alone is sufficient for a simple fact.

## Preserve execution semantics

Distinguish synchronous calls, queued work, callbacks, transactions and external effects when they control understanding. A call tree is not evidence of one stack, atomicity or runtime order. Mark asynchronous handoffs explicitly; use a sequence view when ordering is the point. Label proposed or inferred edges and unresolved dispatch. Retain relevant source paths or symbols without turning the view into a repository inventory.

For example, a supplied payment flow may need these separate observations:

| Boundary | Observation |
| --- | --- |
| Provider | Payment accepted. |
| Local transaction | Recording the receipt failed. |
| Retry | Must follow the supplied provider identity and reconciliation contract. |

This explains why a failure response does not establish that payment never happened. It is an illustrative model, not proof about a particular system.

## Show the change in its own shape

A conceptual diff shows a behavioral or structural delta; label it **Conceptual change**, not an exact source patch:

```diff
 publishDraft
   validateDraft
+  checkExpectedRevision
   saveRevision
-  sendNotification
+  queueNotification
```

Show the complete block when most is new, omitted context would hide ownership or order, or the reader needs a copyable target. Exact source diffs retain their real paths and lines; sketches must not fabricate them. Keep before/after views comparable in scale, detail and labels.

## Deliver for the reader

Place the specimen beside the short explanation, consequence or evidence it supports. Keep only the relevant calls, files, props, states, boundaries and alternatives. Rendering cannot supply missing requirements or conclusions.

For portable HTML, use `html-artifact`; for a presentation, use the installed presentation capability. Preserve the user's requested format, including living HTML plans. Reuse the existing document and preview where appropriate. Open only when requested or needed for render proof, following the delivery owner's policy.
