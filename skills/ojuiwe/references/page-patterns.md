# Page patterns

Documents start in Markdown. Use the bundled generator for their HTML reading view; edit and commit the source, regenerate on demand. Fenced extensions add optional depth, tabs, charts, timelines and callouts without maintaining a second document. Syntax is in [document pages](document-pages.md).

| Pattern | What helps the reader |
| --- | --- |
| Comparison | Put the same criteria side by side in a table; keep trade-offs and the deciding evidence together. |
| Plan/handoff | Milestones timeline, dependencies/data flow, inline mockup references, risky code and a risk table; distinguish done from proposed. |
| Code review | Exact diff with notes beside the changed lines, severity in words and jump links to findings. Retain real file paths/lines. |
| Annotated diff | Pair each consequential hunk with its effect and evidence; preserve context and distinguish a sketch from an exact patch. |
| Boxes and arrows | Modules, entry points and the hot path; label inferred edges and asynchronous handoffs. Use source fences or an inlined generated SVG. |
| PR tour | Motivation, before/after, file-by-file reasons and where a reviewer should focus; link the actual patch. |
| Design reference | Copyable token values and component sizes/states in a contact sheet; keep labels and implementation references visible. |
| Explainer | TL;DR, a working example, optional details, tabbed code samples, glossary and FAQ; each part answers a reader question. |
| Report | A finding beside small charts, source revision, units and limits; light structure instead of decorative dashboards. |
| Incident report | Minute-by-minute timeline, log excerpts, impact, recovery proof and follow-up task list. |

Hand-built HTML fits the patterns Markdown cannot express:

- **Prototype:** a few linked screens with real motion; sliders for duration/easing when tuning is the question. State what is simulated.
- **Interactive diagram:** inline SVG with clickable steps revealing execution, timings and failure paths; preserve a readable text view.
- **Deck:** one `section` per slide, arrow-key navigation, meaningful motion and a complete print view.
- **Custom editor:** a small triage board, flag chooser or prompt tuner for a hard-to-describe task. Always end with export/copy that turns choices into text to paste back or commit. Keep choices transient until that explicit action.

Use jump links and a heading index for navigation, native collapsibles for optional depth and keyboard tabs for alternate views. Keep options visible together when choosing between them. Adapt the QP layout and density to the material; a pattern is not a quota or a template to fill.
