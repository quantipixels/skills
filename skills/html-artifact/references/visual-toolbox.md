# Visual toolbox

Use this selector to avoid blank-page reinvention. Pick by the question, not by a requirement to use a renderer. One sound representation normally beats a gallery. Artistic expression remains welcome.

| Reader relationship | First useful form | Add interaction when it helps |
| --- | --- | --- |
| Who sends what, in what order? | Mermaid sequence | Guided steps beside the complete exchange. |
| Which branch or dependency matters? | Mermaid flowchart | Select a path's explanation without hiding the overview. |
| Which transitions are legal? | Mermaid state diagram | A supplied-model stepper; show current state and reset. |
| Which entities and cardinalities? | Mermaid ER | Persistent-on-screen detail selection, not saved selections. |
| How does a system fit together? | Labelled flowchart/subgraphs or inspected architecture grammar | Detail view for a selected resource; no invented edges. |
| What changed? | Aligned before/after, exact diff or timeline | Same-frame comparison or current-changes lens. |
| What proves this? | Claim/evidence/disposition table or trace view | Linked highlighting/detail selection with stable identities. |
| How much, how often, what pattern? | Table for lookup; Observable Plot for trend/distribution | Exact values on focus/tap, with an accessible table. |
| Where does measured quantity flow? | Sankey only with actual weighted flows | Details for the supplied weights; never turn topology into numbers. |
| Which independent peers need scanning? | List, table or cards | Category/text filter with result count and reset. |

Use [Mermaid recipes](mermaid-recipes.md) for the first four forms and [quantitative views](quantitative-views.md) for plots. Native HTML/SVG is often better for controlled editorial layout, cross-sections and paired code. D3 or another focused renderer earns its cost when the requested view needs data joins or bespoke interaction that simpler tools cannot express reliably. D3 is not itself an automatic graph-layout solution.

## Diagram craft

Show actual directed and labelled relationships. Choose flow orientation to fit the reading path; use lanes/subgraphs for real ownership, not decoration. Keep labels readable at the target width; split a dense graph into coherent linked views instead of shrinking it into illegibility. Put branch conditions on edges and outcomes at their destination. Legends explain unfamiliar encodings, not obvious rectangles.

A diagram with rounded nodes is still a diagram when its edges carry meaning. The failure is unrelated cards standing in for a flow, not rounded corners. Do not replace an effective visual with a graph solely to increase Mermaid use.

## Ready-made interaction

Use the single `view-control.html` asset for selection/detail, comparison and guided sequences rather than three near-identical widgets. Use the existing filter/carousel/report controls for their own contracts. Native disclosures need no additional runtime. Model demonstrations use domain-owned functions plus native labelled inputs and `output`; there is no generic model engine that should invent the domain rules.

All default state is ephemeral. No autosave, approval form, feedback collection or URL-state synchronisation comes with a recipe. The [interaction contract](interactive-projections.md) governs optional depth.
