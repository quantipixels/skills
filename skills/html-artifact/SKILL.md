---
name: html-artifact
description: Visualize supplied results, reports, analysis, data, decisions, designs, or behavior as one accessible, portable HTML artifact or bounded linked variant set. Request missing source material when needed for a truthful, useful visual explanation. Exclude originating analysis, design, decisions, or recommendations and building production applications, general sites, backend integrations, deployments, or reusable libraries.
---

# HTML Artifact

Turn supplied material into one portable visual explanation or bounded variant set. Own composition, implementation, accessibility, and resilience without changing its meaning or making its decisions. Do not turn an agent result into a styled dump of paragraphs, tables, or logs.

## 1. Set the contract

Use the requested or existing path. Otherwise, store a durable record at `.qp/report/<YYYY-MM-DD>-<kind>-<slug>.html`; store another artifact at `.qp/<kind>/<YYYY-MM-DD>-<slug>.html`.

Follow the supplied audience; otherwise write for a layperson with no prior context or subject knowledge. Make the artifact stand alone: state what it is about, why it matters, what happened or was learned, and what the reader should notice or do. Explain necessary terms and acronyms at first use. Keep content, fallback, styles, and behavior in the HTML.

Keep facts, analysis, decisions, assumptions, and open questions distinct. Before implementation, check whether the supplied material contains the context, definitions, analysis, evidence, relationships, data, and visual assets needed for a truthful and useful artifact. Request the smallest missing information or analysis from the owning task or user when it can materially improve the result. Continue with a labeled input gap only when the missing item does not undermine the artifact or cannot be obtained. Do not originate missing analysis or invent an actor, owner, direction, causal link, sequence, boundary, candidate, criterion, or recommendation to satisfy a visual form.

Load branch guidance only when it applies:

- For an evidence report, living report, or candidate comparison, read and follow [report patterns](references/report-patterns.md).
- For a supplied prototype, demo, interface specimen, or design-variant set, read and follow [prototype patterns](references/prototype-patterns.md).

Do not load either branch for a simple visualization or bounded tool. If required branch guidance cannot be read, report the blocker instead of approximating it.

## 2. Render the material visually

Encode the supplied argument instead of decorating it. Lead with supplied conclusions, evidence, status, and risks. A substantial artifact needs a central visual representation that makes its main relationship or result easier to understand than prose alone. If the material cannot support one, request the missing structure or report the visual limitation instead of filling the page with text.

Do not default to paragraphs or tables. Use short prose only to orient or interpret a visual. Use a table only for exact mappings or repeated-field comparison that is materially easier to scan in rows and columns. Choose timelines, state or flow maps, annotated comparisons, spatial diagrams, charts, card systems, carousels, or another fitting composition from the information shape. Give no qualitative judgment false precision without a supplied scale and source. Give every material visual a text summary or accessible data representation that retains chart values and units.

Choose the visual system by information shape:

- Use Mermaid only when supplied nodes, edges, direction, and ownership define a graph, flow, state, or sequence. Add an accessible title and description and retain source or a text summary.
- Use semantic HTML and inline SVG for editorial or spatial explanations; give meaningful SVGs text alternatives and hide decorative SVGs.
- Combine them only for mixed information shapes.

Keep ordered events neutral when evidence defines no relationship: show `09:00 received` and `09:05 validated` as numbered cards, not arrows, lifelines, actors, or directional claims.

Render supplied code, configuration, schema, or text changes with semantic HTML and embedded CSS, not a diff library. Use accessible `+` and `−` labels, non-color cues, high contrast, inline highlights, overflow-safe lines, and source text.

Implement supplied interaction, or add only presentation controls needed to navigate or reveal the same material. When multiple supplied designs, prototypes, screens, or visual variants are best inspected one at a time, use the carousel contract in [prototype patterns](references/prototype-patterns.md) and embed the bundled [carousel control](assets/carousel-control.html). Keep a complete reading order without interaction, preserve keyboard operation and visible focus, respect `prefers-reduced-motion`, and do not encode meaning by color alone.

Keep outcomes, decisions, current status, material evidence, risks, and next actions visible. Put logs, provenance, superseded detail, and other secondary information that the audience does not need upfront in collapsed semantic `<details>` accordions with clear `<summary>` labels. Do not collapse a blocker, warning, required action, or the only accessible representation of material content.

Embed the bundled [visual foundation](assets/visual-foundation.css) and [theme control](assets/theme-control.html) in every artifact. They supply behavior and resilience only; choose the artifact's visual direction from its material.

## 3. Apply resource and portability rules

Classify each dependency:

1. **Embedded or local:** Use for material content, evidence, fallback, artifact code, and sensitive assets. Embed small resources; use adjacent files only in an accepted companion bundle.
2. **User-provided remote:** Require supplied or approved access and copying authority, plus a fallback label or summary.
3. **External enhancement:** Require material benefit and impractical local generation. Tailwind and Mermaid qualify as defined; fonts, telemetry, decorative remote images, and diff renderers do not by default.

Use Tailwind through an exact-version browser CDN for primary styling when permitted, with fallback CSS for readable flow, typography, spacing, tables, code, focus, and print. For confidentiality, offline fidelity, or restrictive content security, vendor or pre-render generated CSS and disclose the exception. Use Mermaid through an exact-version CDN with `securityLevel: 'strict'` only for defined graph shapes.

For each external enhancement, record its name, exact version, URL, purpose, and fallback; prefer an official or reputable distribution; and use published integrity metadata without inventing a digest. Send no repository content, credentials, evidence, or user data. Add no analytics, cookies, authenticated requests, remote HTML, or executable user content. Insert untrusted text, diagrams, patches, and configuration as text, never markup:

```js
element.textContent = untrustedText;
// Never: element.innerHTML = untrustedText;
```

When an enhancement fails, retain readable conclusions, evidence, navigation, diff source, and before-and-after meaning. Call the HTML self-contained only when it carries the complete communication and fallback.

Show one status near the title:

- **Offline-ready:** the artifact loads no runtime network resource.
- **Network-enhanced:** the HTML is complete offline, but a disclosed runtime resource changes presentation or behavior.
- **Companion bundle:** adjacent approved files are required; list them and do not describe the HTML alone as self-contained.

## 4. Deliver

Do not verify the artifact unless the user explicitly requests verification. Do not run a browser or UI check as part of this skill.

Return the direct absolute path or host-rendered link, with a bundle index first. Add no opener script unless requested or repeatedly needed. Use a temporary preview URL only when requested non-UI testing requires HTTP; identify it as transport, not a dependency. If preview fails, return durable files, blocker, and completed requested checks without claiming success.

Return portability status, limitations, network needs, and external-resource disclosure. For a report, also return lifecycle, coverage disposition, and unresolved input gaps.
