---
name: html-artifact
description: Visualize supplied results, reports, analysis, data, decisions, designs, or behavior as one accessible, portable HTML artifact or bounded linked variant set. Request missing source material when needed for a truthful, useful visual explanation. Exclude originating analysis, design, decisions, or recommendations and building production applications, general sites, backend integrations, deployments, or reusable libraries.
---

# HTML Artifact

Turn supplied material into one portable visual explanation or bounded variant set. Own composition, implementation, accessibility, and resilience without changing its meaning or making its decisions. Do not turn an agent result into a styled dump of paragraphs, tables, or logs.

## 1. Set the contract

Use the requested or existing path. When none is supplied, use `.qp/<kind>/<YYYY-MM-DD>-<slug>.html`.

Follow the supplied audience. Otherwise, write for a reader with no prior context or subject knowledge. Make the artifact stand alone: identify the subject, its importance, the outcome, and what the reader should notice or do. Explain terms and acronyms at first use. Match `<html lang>` and the base `dir` to the artifact language. Use semantic markup to preserve direction in mixed-direction content. Keep content, fallback, styles, and behavior in the HTML.

Keep facts, analysis, decisions, assumptions, and open questions distinct. Before implementation, check for the context, definitions, evidence, relationships, data, and assets needed for a truthful artifact. Request the smallest missing item that would materially improve the result. Continue with a labeled input gap only when the gap does not undermine the artifact or the item cannot be obtained. Never invent analysis, actors, owners, direction, causality, sequence, boundaries, candidates, criteria, or recommendations to satisfy a visual form.

For a report, follow [report patterns](references/report-patterns.md) to derive one stable contract and information direction from its `Purpose`, family, reader and use, scenario, entry resource, and context. Honor binding formats. Return one direction, not design options, report variants, or prototype behavior. Change the contract only when its purpose, format, audience, or evidence shape materially changes. State the transition before recomposing the report.

Let design skills trigger through the host's normal selection rules. Do not enumerate, route, or hardcode them here. Their results may shape presentation but cannot originate report content, decisions, options, or prototype behavior.

Load branch guidance only when it applies:

- For any report, including an evidence report, living report, or candidate comparison, read and follow its linked report guidance above.
- For a supplied prototype, demo, interface specimen, or design-variant set, read and follow [prototype patterns](references/prototype-patterns.md).

Do not load either branch for a simple visualization or bounded tool. If required branch guidance cannot be read, report the blocker instead of approximating it.

## 2. Render the material visually

Encode the supplied argument instead of decorating it. A substantial artifact needs a central visual that explains its main relationship or result better than prose alone. If the material cannot support one, request the missing structure or disclose the visual limitation. For a report, use its selected information direction for the opening, hierarchy, central representation, and evidence emphasis. Recompose a report that would still fit an unrelated subject after removing its title and subject nouns.

Do not default to paragraphs or tables. Use prose to orient or interpret a visual. Use a table only when rows and columns make exact mappings or repeated fields easier to scan. Bound its columns, keep cells overflow-safe, and replace a wide low-density table with grouped detail. Choose a timeline, state or flow map, annotated comparison, spatial diagram, chart, card system, carousel, or another form from the information shape. Do not give qualitative judgment false precision without a supplied scale and source. Give every material visual a text summary or accessible data representation with its values and units.

Choose the visual system by information shape:

- Use Mermaid only when supplied nodes, edges, direction, and ownership define a graph, flow, state, or sequence. Add an accessible title and description. Retain the source or a text summary.
- Use semantic HTML and inline SVG for editorial or spatial explanations. Give meaningful SVGs text alternatives and hide decorative SVGs.
- Combine them only for mixed information shapes.

Keep ordered events neutral when evidence defines no relationship: show `09:00 received` and `09:05 validated` as numbered cards, not arrows, lifelines, actors, or directional claims.

Render supplied code, configuration, schema, or text changes with semantic HTML and embedded CSS, not a diff library. Use accessible `+` and `−` labels, non-color cues, high contrast, inline highlights, overflow-safe lines, and source text.

Implement supplied interaction or presentation controls that only navigate or reveal the same material. For a supplied visual collection, follow [prototype patterns](references/prototype-patterns.md) and embed the [carousel control](assets/carousel-control.html). Preserve the reading order without interaction, keyboard operation, visible focus, and reduced-motion preferences. Do not encode meaning by color alone.

Keep outcomes, decisions, status, material evidence, risks, and next actions visible before supporting detail. Separate sections with enough space to scan. Put secondary logs, provenance, and superseded detail in semantic `<details>` elements with clear labels. Summarize logs, then group retained entries by a supplied boundary such as phase, date, source, or severity. Keep blockers, warnings, required actions, and sole accessible representations visible. Render long IDs, hashes, and URLs as copyable block text that wraps without changing the value.

Embed the [visual foundation](assets/visual-foundation.css) and [theme control](assets/theme-control.html) in every artifact. They provide behavior and resilience, not visual direction. Localize every visible and assistive control string, including status, fallback, and live-announcement text. Adapt directional controls to the base `dir`.

## 3. Apply resource and portability rules

Classify each dependency:

1. **Embedded or local:** Use for material content, evidence, fallback, code, and sensitive assets. Embed small resources. Use adjacent files only in an accepted companion bundle.
2. **User-provided remote:** Require supplied or approved access, copying authority, and a fallback label or summary.
3. **External enhancement:** Require material benefit when local generation is impractical. Tailwind and Mermaid qualify as defined. Fonts, telemetry, decorative remote images, and diff renderers do not by default.

When permitted, use an exact-version Tailwind browser CDN with fallback CSS for readable flow, typography, spacing, tables, code, focus, and print. For confidential, offline, or content-security-constrained material, vendor or pre-render the CSS and disclose the exception. Use an exact-version Mermaid CDN with `securityLevel: 'strict'` only for defined graph shapes.

For each external enhancement, record its name, exact version, URL, purpose, and fallback. Prefer an official or reputable distribution. Use published integrity metadata without inventing a digest. Treat remote executable resources as able to read the document. Use them only for public material or when the user approved the exact host for that content. Otherwise, vendor or pre-render them. Send no credentials. Add no analytics, cookies, authenticated requests, remote HTML, or executable user content. Insert untrusted text, diagrams, patches, and configuration as text, never markup:

```js
element.textContent = untrustedText;
// Never: element.innerHTML = untrustedText;
```

If an enhancement fails, retain readable conclusions, evidence, navigation, diff source, and before-and-after meaning. Call the HTML self-contained only when it contains the complete communication and fallback.

Show two independent statuses near the title:

- **Network:** `Offline-ready` loads no runtime network resource. `Network-enhanced` remains complete offline, but a disclosed runtime resource changes presentation or behavior.
- **Packaging:** `Single file` requires no adjacent file. `Companion bundle` requires approved adjacent files. List them and do not call the HTML alone self-contained.

## 4. Deliver

Before delivery, reread the files and run the smallest non-UI checks for references, anchors, script syntax, fallback content, and resource disclosures. Report verification as `run`, `not run`, or `incomplete`, with completed checks and gaps. Claim accessibility, portability, interaction, and visual correctness only to the extent proved. Run a browser or UI check only when the user requests it or another owning workflow requires it.

Return the absolute path or host-rendered link, with a bundle index first. Add an opener script only when requested or repeatedly needed. Use a temporary preview URL only when requested non-UI testing requires HTTP. Identify it as transport, not a dependency. If preview fails, return the files, blocker, and completed checks without claiming success.

Return network status, packaging status, verification status, limitations, and external-resource disclosure. For a report, also return lifecycle, coverage disposition, and unresolved input gaps.
