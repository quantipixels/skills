---
name: html-artifact
description: Create or update one standalone, checked HTML/CSS/JavaScript artifact, including reports, visualizations, prototypes, demos, and bounded interactive tools. Use when the requested result is one self-contained browser artifact; do not use for production application changes, multi-page sites, backend integration, deployment, or reusable component libraries.
---

# HTML Artifact

Craft one requested standalone HTML artifact that communicates, explores, or demonstrates a bounded subject. The artifact may be a durable evidence record, data story, visualization, prototype, demo, or interface specimen. Production applications, multi-page sites, backend integrations, deployment, and reusable component libraries are separate outcomes.

For a materially complex artifact, an owning task may request a host-provided subagent to construct the complete artifact and perform its artifact-local checks after the purpose, audience, path, inputs, required behavior, and acceptance checks are fixed. The owning task retains claim or decision authority and final artifact acceptance. Keep simple artifacts and small updates local.

## 1. Build the artifact

Use the requested or existing path. Otherwise, store a durable record at `.qp/report/<YYYY-MM-DD>-<kind>-<slug>.html`; store another artifact at `.qp/<kind>/<YYYY-MM-DD>-<slug>.html`. Use a short `kind` such as `review`, `investigation`, `data`, `prototype`, `demo`, or `visualization`.

Follow the supplied audience and active user or repository writing rules. If none apply, use clear, direct, accurate technical prose. Keep precise technical terms. Give unfamiliar terms enough context for the reader to understand them. Add a concise explanation or example when necessary. Include a short glossary when recurring critical terms or artifact-specific meanings need shared definitions. Define each glossary term once in plain language. Explain an isolated term beside its first relevant use when a separate glossary would add noise.

Choose the structure, visual design, and interaction that best serve the requested purpose. Use semantic HTML, responsive CSS, and JavaScript when behavior needs it. Add code diffs, tables, graphs, diagrams, or controls only when they improve the artifact. Keep the artifact self-contained by default. Use remote scripts, fonts, or assets only when the request needs them, and identify any required network dependency.

For an evidence record, base factual claims on supplied or cited evidence. Preserve material distinctions between facts, analysis, decisions, assumptions, and open questions. Keep a short dated revision log only when a material update needs a durable reason; record what changed and why without repeating the artifact's content.

For a prototype, demo, or interface specimen, make assumptions and synthetic data recognizable. Model only the requested flows and states. Do not present the artifact as production architecture, complete behavior, or an approved product decision.

## 2. Check and return it

Check that the file exists, has usable semantic HTML, satisfies the requested content and behavior, and has no obvious broken local links or controls. For an interactive artifact, exercise its key controls and relevant keyboard paths. Render and inspect the artifact when the user requests visual proof or when its layout, responsive behavior, or interaction makes rendering useful. Keep a simple static record's checks light.

State any relevant check limitation. Return the full path or link and the checks performed.
