# Prototype Patterns

Read this file only when supplied designs or behavior specifications must become a prototype, demo, interface specimen, or variant set.

Render only supplied designs, flows, states, and behavior. Do not invent a design or variant to complete a set. Keep supplied assumptions and synthetic data recognizable. Show a clear non-production status; a successful render is not production readiness or product approval.

## Present a visual collection

When multiple supplied designs, prototypes, screens, or visual variants are best inspected one at a time, embed [`../assets/carousel-control.html`](../assets/carousel-control.html) and adapt its neutral markup to the supplied items. Select exactly one bundled control composition: compact glyphs, visible labels, or overlay glyphs. Keep its accessible names, stable labels, direct links, keyboard behavior, no-autoplay rule, no-script fallback, live announcement, and narrow-viewport resilience. Use a simultaneous comparison instead when side-by-side differences are the purpose.

## Keep variants stable

Label supplied variants sequentially as **Variant A, B, C** or **Variant 1, 2, 3**. Use one scheme and supplied or neutral descriptors. Do not add evaluative labels. After sharing links, keep labels and paths immutable: do not renumber survivors or reuse a retired label; give a newly supplied design the next unused label. Preserve a retired direct link with a small tombstone page or index entry when needed.

When each page or view must show one design, give each variant a direct link plus persistent previous, next, and index links:

- Prefer one HTML file with stable fragment or query links when each selected route reliably shows only its variant. Keep a no-script index.
- Use one index plus sibling HTML files for strict isolation, JavaScript-free direct links, or independent review. Use relative links, keep shared context and comparison criteria in the index, and classify the result as a companion bundle. This does not authorize a general multi-page site.

Good: `index.html` links to `variant-a.html`, `variant-b.html`, and `variant-c.html`, each with one neutral design and persistent navigation. Bad: one page stacks designs that require isolated views, labels them `first`, `other`, and `final`, and exposes no durable variant link.

For a variant bundle, return the index first and then direct links to each variant under the shared delivery rules.
