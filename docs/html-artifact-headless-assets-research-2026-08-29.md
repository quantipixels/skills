# Headless assets for standalone HTML artifacts

Date: 29 August 2026

Question: What reusable headless components or dependencies should `html-artifact` add beyond its visual foundation, theme control, report control, and carousel control?

Decision updates:

- Later on 29 August 2026, the owner explicitly chose package standardization without waiting for a second consumer. The resulting implementation adds the bounded `collection-filter-control.html` candidate and strengthens responsive semantic-table containment in `visual-foundation.css`.
- On 30 August 2026, the owner made explicit theme switching the standalone default and required a back-to-top control when page length or navigation justifies it. The control uses a native fragment link with a small keyboard-focus enhancement and defaults to a bottom-right floating icon.

The evidence and alternatives below remain the research basis for these decisions.

## Current recommendation

Add the bounded, conditional collection filter chosen in the decision update. Include explicit theme switching by default. Include the native back-to-top control when page length or navigation makes it useful. The current package otherwise covers the repeated standalone-artifact seams for which this repository has evidence. Prefer native HTML and small artifact-specific enhancement for the remaining evaluated patterns. Keep two focused build-time dependencies available by policy, not vendored as package assets:

- Mermaid for a diagram whose source is trusted and whose static SVG is materially clearer than prose.
- Observable Plot for a chart whose transforms or marks would be error-prone to implement directly.

No other local asset currently clears its admission gate. Tabs have substantial correctness requirements, but the repository has no current consumer and therefore no recurrence evidence.

This decision preserves the accepted bounded-open dependency policy: capability comes before technology, dependencies remain replaceable and reproducibly identified, and essential meaning survives failure.

## Evidence in this repository

At the research cutoff, the package contained four assets: `visual-foundation.css`, `theme-control.html`, `report-control.html`, and `carousel-control.html`. The generated HTML consumer inspected at that cutoff, [`agent-session-issue-map-2026-08-18.html`](agent-session-issue-map-2026-08-18.html), contained:

- five passive `.pill` metadata labels;
- one semantic table inside the existing `data-table-wrap` overflow treatment;
- five native `<details>` disclosures served by `report-control.html`; and
- one bespoke single-select filter group using `button[aria-pressed]` to hide cards by `data-status`.

The filter has no live result-count announcement. There are no current tabs, dialogs, popovers, tooltips, Mermaid diagrams, or charts. A deleted historical prototype is not current recurrence evidence.

## Disposition by capability

| Capability | Disposition | Exact capability and recurring risk | Runtime, trust, fallback, and maintenance |
| --- | --- | --- | --- |
| Pills, badges, and chips | Native HTML/CSS guidance | A passive badge is text, commonly a `<span>` or list item. An actionable chip must use the native element that matches its function: link, button, checkbox, or radio. Do not invent one generic `chip` role. Text or shape must carry status meaning in addition to color. | No runtime. Static text remains readable without CSS. Use `role="status"` only for a changing advisory message because the role is a polite, atomic live region, not a badge decoration. Maintenance is negligible. [WCAG use of color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color), [ARIA `status`](https://www.w3.org/TR/wai-aria/#status), [APG button pattern](https://www.w3.org/WAI/ARIA/apg/patterns/button/) |
| Static and responsive tables | Native HTML/CSS guidance; existing foundation is sufficient | Use `<table>`, `<caption>`, `<th>`, and `<td>`. Add `scope` for simple row/column headers and `id`/`headers` for genuinely complex associations. Keep the table in its own overflow container; do not convert cells into visually stacked cards that erase header relationships. | No runtime. The table remains the fallback. A table may scroll in two dimensions, but its cells and adjacent controls still need to reflow; containing the scroll prevents the whole page from becoming the scrolling surface. Maintenance is low. [WAI tables tutorial](https://www.w3.org/WAI/tutorials/tables/), [WAI table tips](https://www.w3.org/WAI/tutorials/tables/tips/), [WCAG reflow guidance](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) |
| Sortable table | Native progressive enhancement; defer a reusable asset | Put a native `<button>` in each sortable `<th>`. Set `aria-sort` only on the active header and move/update it after every sort. Use explicit typed sort keys and a stable comparator; visible text parsing is unsafe for localized dates, numbers, units, and mixed values. | If script fails, retain the original complete table and source order. Printing should retain all rows and disclose the effective sort when it changes interpretation. Maintenance is moderate because comparator, locale, null ordering, stable ordering, and state announcements can change meaning. The APG example is illustrative, not production code. [APG sortable table example](https://www.w3.org/WAI/ARIA/apg/patterns/table/examples/sortable-table/), [APG scope and cautions](https://www.w3.org/WAI/ARIA/apg/about/introduction/) |
| Filterable collection or table | Conditional local asset, `ACCEPTED BY OWNER` | The narrow asset owns single-select filter buttons, `aria-pressed`, component-scoped targets, an “all” state, zero-results text, and a polite result-count update. It does not own domain predicates or infer filter categories. | Progressive enhancement only: all supplied items stay present and visible before initialization, after script failure, and in print. Treat labels as translatable data. Maintenance is low to moderate while the contract stays single-select; text search, compound filters, URL state, or pagination should trigger a new decision. Native buttons already provide keyboard activation; a result count uses the ARIA `status` live-region semantics. [APG button pattern](https://www.w3.org/WAI/ARIA/apg/patterns/button/), [ARIA `status`](https://www.w3.org/TR/wai-aria/#status) |
| Tabs | Defer a reusable local asset | A correct tab set needs `tablist`, `tab`, and `tabpanel` relationships; one selected tab; roving `tabindex`; arrow, Home, and End behavior; a deliberate automatic/manual activation choice; and focus placement for panel content. Hidden panels also complicate fragments, printing, and complete reading order. | If later justified, enhance only after load so all panels remain visible without script, reveal every panel for print, and make fragment targets select and expose their panel. Maintenance is moderate because keyboard and focus behavior is a composite-widget contract. No current consumer justifies the asset. [APG tabs pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/), [APG keyboard-interface practice](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/) |
| Segmented controls | Native HTML guidance | Use a labeled native radio group for one mutually exclusive value. Use toggle buttons with stable labels and `aria-pressed` for independent on/off choices. Use tabs only when the controls select associated panels. The visual pill shape does not determine semantics. | No component runtime beyond any artifact-specific view update. Native radios retain keyboard behavior without script. If view filtering fails, show all content. Maintenance is low. [APG radio pattern](https://www.w3.org/WAI/ARIA/apg/patterns/radio/), [APG button pattern](https://www.w3.org/WAI/ARIA/apg/patterns/button/) |
| Disclosures and accordions | Native HTML guidance; existing report control is sufficient | Use `<details><summary>…</summary>…</details>` for document disclosure. The `name` attribute can create an exclusive group without script, though an always-readable opening section is preferable for reports. Keep real heading structure outside or alongside the summary when the document hierarchy needs it. | No runtime for basic disclosure. Unsupported or failed enhancement leaves content in document order; `report-control.html` already handles deep-link ancestors and selected print expansion. Maintenance is low. [MDN `<details>` reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details), [APG accordion pattern](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/) |
| Back to top | Progressively enhanced native control after a length or navigation trigger | Use a fragment link to an existing opening landmark or heading. Keep it last in document order and present it as a bottom-right floating icon by default. Make the target programmatically focusable so keyboard focus follows the visual return. Do not create a second opening or intercept native navigation merely to host the control. | The link still scrolls without JavaScript. A translatable `aria-label` gives the icon its accessible name, and a small enhancement aligns keyboard focus with the destination. Hide the control in print. Maintenance is negligible while the contract remains one local fragment target. |
| Tooltips | Reject a bundled asset | Prefer visible text, `aria-describedby`, or a disclosure. A custom tooltip must appear for keyboard focus and hover, remain hoverable and persistent, dismiss on Escape, keep focus on its trigger, and contain no interactive descendants. The APG tooltip pattern still lacks task-force consensus. | Essential meaning must never depend on the tooltip. Failure fallback is visible adjacent help. Maintenance and assistive-technology test cost are high relative to the small document benefit. [APG tooltip pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/), [WCAG content on hover or focus](https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus) |
| Popovers | Native HTML guidance for rare non-modal use; no asset | Declarative `popover` plus `popovertarget` provides light-dismiss behavior, Escape handling, focus-order integration, focus return, and implicit invoker relationships. The content still needs suitable semantics and a deliberate focus model. A disclosure or in-page section is usually clearer for a read-only projection. | No library, but feature support is part of the viewer environment. Keep essential content visible or linked when the API is unavailable; do not hide the only copy before enhancement succeeds. Browser behavior lowers maintenance, while authored positioning and fallback retain moderate test cost. [MDN Popover API guidance](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using) |
| Dialogs | Native `<dialog>` guidance for exceptional use; no asset | `showModal()` supplies modality, inert background content, focus containment, Escape close, and focus return. The author must still choose initial focus, label the dialog, provide a visible close action, and account for long structured content. Those decisions are content-specific and resist a safe generic wrapper. | Failure fallback is the same content in normal document flow or a direct in-page link. Maintenance is moderate; modal content also obscures the source context, so it is seldom justified in a standalone report. [WAI native-dialog technique H102](https://www.w3.org/WAI/WCAG22/Techniques/html/H102), [APG modal-dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) |
| Mermaid diagrams | Focused build-time dependency; do not bundle a viewer runtime | Pin Mermaid and render trusted diagram source to inline SVG during artifact generation. Supply `accTitle` and `accDescr`; Mermaid emits `<title>`, `<desc>`, `aria-labelledby`, `aria-describedby`, and an `aria-roledescription`. Keep a visible explanation and, when useful, the source in a disclosure. | The delivered artifact needs no Mermaid runtime or network. If rendering fails, retain the prose/source fallback and mark the diagram unavailable. Runtime rendering expands the trust and patch boundary: Mermaid assigns input trust to the integrator, `strict` disables HTML/clicks by default, and recent advisories affected bundled releases. Freshness cost is high for a viewer runtime and moderate for a pinned build tool. [Mermaid usage and security levels](https://mermaid.js.org/config/usage.html), [Mermaid accessibility](https://mermaid.js.org/config/accessibility.html), [2026 CSS-injection advisory](https://github.com/mermaid-js/mermaid/security/advisories/GHSA-87f9-hvmw-gh4p), [bundled DOMPurify advisory](https://github.com/mermaid-js/mermaid/security/advisories/GHSA-m4gq-x24j-jpmf) |
| Charts | Native SVG/HTML first; focused build-time Observable Plot when justified | Use prose or a compact table when it communicates the relationship. For a material chart, Observable Plot produces an SVG or HTML figure and exposes top-level and per-mark ARIA labels/descriptions. Authors must supply meaningful descriptions because those options default to `null`. Preserve the exact data, units, transform configuration, and a semantic table or textual conclusion. | Pre-render and serialize the result so the viewer needs no JavaScript. If rendering fails, retain the table and conclusion. Plot can also run from local UMD files with D3, but that bundled runtime is justified only for material interaction. Freshness cost is moderate because Plot and D3 identities, transforms, and accessibility output must be pinned and retested. [Observable Plot accessibility](https://observablehq.com/plot/features/accessibility), [Observable Plot local/offline use](https://observablehq.com/plot/getting-started) |
| Canvas charts and generic data grids | Reject as defaults; defer exceptional runtime use | Chart.js delegates accessibility to the author because canvas pixels are not available to screen readers. Grid.js and simple-datatables provide sort/search/pagination capabilities, but the official material reviewed does not establish an end-user accessibility contract sufficient for this package. A full data grid also introduces composite focus, pagination, source-of-truth, and transformation behavior closer to an application. | Keep the semantic table/data and conclusion as the fallback. If an artifact genuinely needs spreadsheet-like navigation or large-data operations, treat it as an explicit focused runtime dependency with concrete keyboard, screen-reader, offline, and failure proof—or reconsider whether the output has crossed into production-app scope. Maintenance is high. [Chart.js accessibility](https://www.chartjs.org/docs/latest/general/accessibility.html), [Grid.js source repository](https://github.com/grid-js/gridjs), [simple-datatables official README](https://github.com/fiduswriter/simple-datatables/blob/main/README.md) |

## Admission gate applied to the local asset

The asset was admitted through the owner's explicit standardization decision, not merely to clean up the existing bespoke script. Its contract must continue to satisfy these statements:

1. At least two independent artifact consumers need the same single-select collection filtering behavior, or the owner explicitly chooses package standardization without recurrence evidence.
2. The input/output seam is deterministic: supplied control value plus supplied item category produces a visible subset and an exact count.
3. The asset owns only presentation state. The source owner supplies categories, predicates, labels, and any meaning attached to the subset.
4. All content is visible without JavaScript and in print. A zero-result state and polite result count are available after enhancement.
5. Keyboard, focus, narrow-viewport, no-script, print, and invalid-configuration checks pass on each consumer.

Do not extend the same asset to free-text search, multi-filter query composition, sorting, pagination, or URL serialization without fresh evidence. Those features create different state and semantic-transformation contracts.

## Dependency delivery rules

For Mermaid or Observable Plot, prefer this delivery shape:

```text
Delivery shape: Single HTML
Runtime code: None
Runtime data: Static
Evidence: Embedded or Mixed
```

Pin the build dependency and preserve the source/configuration needed to reproduce semantic transformations. Treat supplied text and data as untrusted. Mermaid source must be trusted or constrained before rendering; do not enable `loose` or `antiscript` security to recover clickable HTML in a standalone report. Do not use a CDN in an offline-capable artifact. Generated SVG never replaces a visible explanation or data fallback for a complex relationship.

If interaction makes a viewer runtime necessary, ship an exact local bundle, disclose its identity and data access, and keep the base content usable. Remote runtime code is a poor default because network success, execution trust, and disclosure of non-public content are separate risks.

## Freshness and evidence limits

This review used official material current on 29 August 2026. The Mermaid documentation identified version 11.17.2. The Observable Plot documentation identified version 0.6.17. Those numbers are evidence-cutoff markers, not an allowlist or a requirement to adopt those exact releases.

The APG is informative guidance, not a normative standard or production component library. Its examples can still have browser and assistive-technology support gaps. Any future asset based on an APG example needs artifact-specific proof.

No official Grid.js or simple-datatables accessibility support statement was located. Source-level automated accessibility tooling in a dependency does not prove the keyboard and screen-reader behavior of a concrete generated table. This gap is why neither library is a retained candidate.

The repository has only one current generated consumer, so it cannot establish recurrence for tabs, sort controls, tooltips, dialogs, diagrams, or charts. The recommendation should be revisited after another independent artifact needs the same behavior or after a real artifact exposes a failure that native guidance cannot contain.

## Primary sources checked

- [HTML Standard](https://html.spec.whatwg.org/)
- [ARIA in HTML](https://www.w3.org/TR/html-aria/)
- [WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria/)
- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [WAI tables tutorial](https://www.w3.org/WAI/tutorials/tables/)
- [MDN `<details>` reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
- [MDN `<dialog>` reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
- [MDN Popover API guidance](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using)
- [Mermaid official documentation and security advisories](https://mermaid.js.org/config/usage.html)
- [Observable Plot official documentation](https://observablehq.com/plot/getting-started)
- [Chart.js official accessibility and integration documentation](https://www.chartjs.org/docs/latest/general/accessibility.html)
- [Grid.js official source repository](https://github.com/grid-js/gridjs)
- [simple-datatables official documentation and source repository](https://github.com/fiduswriter/simple-datatables)
