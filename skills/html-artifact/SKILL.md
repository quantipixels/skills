---
name: html-artifact
description: Translate supplied content, evidence, decisions, diagrams, or design specifications into one checked, highly visual, portable HTML artifact or bounded linked variant set. Use for reports, visualizations, prototypes, demos, and interactive tools whose source material and intended behavior are already provided; do not use to originate product or editorial design, content strategy, recommendations, production applications, general multi-page sites, backend integrations, deployment, or reusable component libraries.
---

# HTML Artifact

Translate supplied material into one requested portable browser artifact. Own artifact composition, visual encoding, implementation, accessibility, resilience, and checks. Do not originate the source content, product or editorial design, candidate set, comparison criteria, recommendation, or product and architecture decisions. A small linked set of supplied variants may count as one artifact. Production applications, general multi-page sites, backend integrations, deployment, and reusable component libraries are separate outcomes.

## 1. Set the contract

Use the requested or existing path. Otherwise, store a durable record at `.qp/report/<YYYY-MM-DD>-<kind>-<slug>.html`; store another artifact at `.qp/<kind>/<YYYY-MM-DD>-<slug>.html`.

Follow a supplied audience when present. Otherwise, write for an unfamiliar third party with no prior knowledge of the topic, its origin, or its terminology. Make the artifact stand alone by stating its supplied purpose, scope, and context and by explaining supplied terms and relationships as needed. Use direct technical prose only to label, connect, or clarify the supplied material without changing its meaning. If accurate orientation needs missing context, identify that input gap instead of inferring it.

Follow the supplied content, design specification, and active writing rules. Keep the artifact's narrative, evidence, data, labels, fallback content, custom styles, and artifact-specific behavior in its HTML. Use a bounded companion bundle only under the supplied-variant or local-resource rules.

Preserve distinctions between facts, analysis, decisions, assumptions, and open questions. Base factual claims on supplied or cited evidence. When material content, design, behavior, or authority is missing, identify the input gap instead of inventing it. Do not infer an actor, owner, direction, causal link, sequence, or system boundary merely because a visual syntax expects one; use a neutral event or annotation, or show the gap. Another owning task must supply or explicitly authorize those choices before this skill renders them.

Load branch guidance only when it applies:

- For an evidence report, living report, or candidate comparison, read and follow [report patterns](references/report-patterns.md).
- For a supplied prototype, demo, interface specimen, or design-variant set, read and follow [prototype patterns](references/prototype-patterns.md).

Do not load either branch for a simple visualization or bounded tool that does not need it.

## 2. Communicate visually

Use Tailwind through its browser CDN for layout and primary styling, pinned to an exact available release. Embed enough fallback CSS for readable flow, typography, spacing, tables, code, focus, and print when the CDN fails. If offline fidelity, confidentiality, or a restrictive content-security policy prohibits a runtime CDN, vendor generated CSS or pre-render the approved dependency and disclose the exception.

Encode the supplied argument visually rather than adding decoration. Lead with supplied conclusions, evidence, status, and risks when they exist. Choose comparison cards, annotated diagrams, timelines, matrices, charts, or compact metrics by information shape and reading effort; this presentation choice does not authorize new claims or design concepts. Do not turn qualitative judgments into precise-looking charts without a supplied scale and source. Give each material visual a text summary or accessible data representation; retain chart values and units in a table, list, or embedded data block.

Choose the visual system by information shape:

- Use Mermaid through an exact-version CDN only when the supplied material defines the relevant nodes, edges, direction, and ownership for a call graph, dependency, flow, state, or sequence. Keep `securityLevel: 'strict'`, add an accessible title and description, and retain the source or an adjacent text summary.
- Use semantic `div` elements and inline SVG for editorial or spatial explanations such as mass diagrams, cross-sections, layered anatomy, physical layout, and collapse animation. Give meaningful SVGs a text alternative and hide decorative SVGs.
- Combine both when the report needs graph relationships and editorial visuals. Do not force either tool onto the wrong information shape.

When the supplied material gives ordered events but not their relationships, render a neutral timeline or numbered event cards. Do not add arrowheads, participant lifelines, edges, or directional language to make the events graph-shaped.

Render code, configuration, schema, and structured-text changes with semantic HTML and embedded CSS, not a third-party diff library. Choose split or unified form by reading task. Show `+` and `−` markers, accessible labels, non-color cues, and high-contrast colors. Highlight the smallest useful inline change, handle long lines without page overflow, and retain the source patch or before-and-after text.

Implement supplied interaction, or add only presentation controls needed to navigate or reveal the same material. Keep a complete reading order without interaction, preserve keyboard operation and visible focus, respect `prefers-reduced-motion`, and do not encode meaning by color alone.

## 3. Apply the resource policy

Classify each dependency:

1. **Embedded or local:** Use for material content, evidence, custom CSS, fallback rendering, artifact-specific JavaScript, and sensitive assets. Embed small resources. Use adjacent files only when the user accepts a companion bundle; otherwise summarize or link and disclose the limitation.
2. **User-provided remote:** Use only when the user supplied or approved it and its access terms and availability fit the artifact. Do not copy protected content without authority. Keep a fallback label or summary.
3. **External enhancement:** Use only when it materially improves the artifact and local generation is impractical. Tailwind and Mermaid qualify for their defined uses. Fonts, tracking, telemetry, decorative remote images, and diff renderers do not qualify by default.

For every external enhancement, pin an exact version; record its name, version, URL, purpose, and fallback in the artifact; prefer an official distribution or reputable CDN; and add published integrity metadata without inventing a digest. Send no repository content, credentials, evidence, or user data to the provider. Do not add analytics, cookies, authenticated requests, remote HTML fragments, or executable user content. Treat external text, diagram definitions, patches, and configuration as untrusted and insert text with safe DOM APIs.

The artifact must remain readable and expose its conclusions, material evidence, navigation, diff source, and before-and-after meaning when an external enhancement fails. It is self-contained only when the HTML carries the complete communication and useful fallback.

Show one status near the title:

- **Offline-ready:** the artifact loads no runtime network resource.
- **Network-enhanced:** the HTML is complete offline, but a disclosed runtime resource changes presentation or behavior. Use this status even when the embedded fallback is fully readable.
- **Companion bundle:** adjacent approved files are required; list them and do not describe the HTML alone as self-contained.

## 4. Verify proportionately

Check structure, required content, links, controls, resources, and fallbacks. Use the lightest method that can disprove the requested behavior. Smoke-test the primary action and one relevant state or failure path. Use full browser/UI verification only for design-focused work, explicit visual-proof requests, or browser-dependent acceptance criteria. Parse Mermaid and inspect its fallback; render it only when layout matters. Inspect representative diff changes and overflow.

Report only the independent labels completed:

- **Structure checked:** content, links, policy, and fallbacks were inspected.
- **Function smoke checked:** primary behavior and one relevant state or failure path were exercised.
- **UI checked:** relevant browser states and viewports were inspected.

Verification does not prove the artifact's factual claims or product assumptions.

## 5. Deliver the entry point

Return the direct absolute path or host-rendered link; for a bundle, return its index first. Do not add an opener script unless the user requests one or a repeated cross-platform workflow requires it.

Add a temporary preview URL only when tested browser behavior requires HTTP, and state that it is transport rather than an artifact dependency. If preview fails, return the durable files, blocker, and completed checks without claiming success.

Return the portability status, verification labels, checks, limitations, network needs, and external-resource disclosure. For a report, also return its lifecycle.
