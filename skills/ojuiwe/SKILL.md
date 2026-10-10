---
name: ojuiwe
description: Builds a self-contained HTML page from Markdown documents or supplied material. Use when a report, plan, comparison, review or explainer needs a visual reading view, or when a prototype, editor, deck or interactive diagram needs HTML.
---

# Ojú-ìwé (page)

## Output

One HTML page, generated from a Markdown source for documents, shown inline or saved as a file.

## Needs

The content to present and its reader. If either is missing, or the request is not for a page, return to the caller and say what is missing. Preserve the supplied facts, identifiers, uncertainty and proof limits.

## Method

Use HTML when layout, a visual relationship or interaction makes the material easier to understand. Linear text can stay in Markdown. Documents are authored once in Markdown; generate the person's HTML view with [md_to_html.py](scripts/md_to_html.py). Commit the Markdown and generate HTML on demand; keep an HTML copy only when it must be shared as a file. Hand-build HTML for prototypes, custom editors, decks and interactive diagrams that Markdown cannot express.

Start from the inline QP stylesheet and mark in [base.html](assets/base.html). [QP tokens](references/design-tokens.md) are the default, including light and dark modes. Adapt layout, density and type to the report and reader; keep the palette crisp and neutral. Keep the decision beside its evidence and comparisons visible together. [Page patterns](references/page-patterns.md) guide composition; they are examples, not mandatory templates.

Use zero runtime dependencies by default: plain HTML/CSS/JS and inline SVG, with no build or webfonts. A dependency needs an explicit capability gain, a pinned version and a useful offline fallback. Kept pages inline every resource; pre-render diagrams to SVG. Chart.js and Mermaid are opt-in only. Read [dependency policy](references/dependency-policy.md) when selecting either.

Reuse the plain-JS [view/step-through](assets/view-control.html), [filter](assets/collection-filter-control.html), [carousel](assets/carousel-control.html), [tabs](assets/tabs-control.html), [collapsible](assets/collapsible-control.html), [report/print](assets/report-control.html) and [SVG chart](assets/chart-control.html) assets. The [Mermaid renderer](assets/renderer-control.html) is only for an explicitly selected connected preview. Remove unused examples and controls together.

Read [document pages](references/document-pages.md) for generation, fenced extensions and SIGIDI delivery; [code-change review](references/code-change-review.md) for exact patch views; [living and live views](references/living-and-live.md) for updates; [manifest](references/manifest.md) when machine-readable identity is needed. [Codex defaults](references/codex-defaults.md) helps when a generic layout hides the useful content.

Keep supplied text escaped, reader choices transient, and core meaning readable without scripts. A private review page loads no remote executable code. Use visible metadata, semantic reading order, keyboard/focus support, non-colour cues, reduced motion and complete print views.

## Done

[verify_artifact.py](scripts/verify_artifact.py) passes. A real browser preview in both themes shows readable content, sufficient contrast, no console errors and a `ready` line. The added controls work by click and keyboard, including reset, no-match and print where relevant. Generated documents reproduce from the same Markdown and bundled assets. State any check that could not run.

## Return

Return the HTML page or its path, the Markdown source when applicable, and verification results to the caller. It writes a working record of kind plan, report or prototype when requested, or a committed record of kind doc for a kept document.
