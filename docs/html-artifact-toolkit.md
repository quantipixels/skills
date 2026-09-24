# Expressive HTML Artifact toolkit

This change standardises reusable meaning and reliable mechanics, not page appearance. Start with `skills/html-artifact/SKILL.md`; choose the relationship in the visual toolbox, then load only the matching semantic contract, recipe and controls.

## What ships

- Tailwind-backed base and jQuery controls with pinned CDN loading by default; explicit embedded/host alternatives.
- Conditional, strict-mode Mermaid integration; flowchart, sequence, state and ER specimens; optional quantitative Plot guidance.
- One view selector for details, comparisons and finite steps; category plus text filtering; a carousel that no longer writes URL state.
- Five semantic document contracts, an optional compact manifest with safe JSON serialization, and a read-only structural checker.
- Oro resource-selection guidance and Ayewo artifact-history mining with a Keep Variable result.

Existing report-control, source composition, code-change review and living/live references remain part of the skill. The report guidance is reconciled with the new filter contract. The unrelated TDD proposals and repository-wide retirement work are outside this PR.

## Use the base

Copy `skills/html-artifact/assets/base.html` and replace illustrative content/metadata. It links jQuery 4.0.0 and loads `@tailwindcss/browser@4.3.3` by default. Control assets use jQuery for DOM work and Tailwind for layout, spacing, responsive behaviour, selected/disabled states and typography. Plain CSS retains print population, focus, reduced-motion and semantic fallback guarantees. The renderer uses `@apply` on its stable generated-output wrapper. The theme control drives Tailwind's `dark:` variant. The QP mark is inline for single-file delivery, based on `assets/brand.svg`; built-in controls include inline SVG icons and visible or accessible labels. The footer credits QP Skills.

Use `data-artifact-delivery="host"` with an existing application runtime, removing the jQuery CDN tag when the host supplies it. Select `portable` only for a no-runtime-network requirement: remove CDN tags, embed jQuery and compiled Tailwind CSS, including asset classes and `type="text/tailwindcss"` directives. Do not maintain a second bespoke styling vocabulary. A deployed application should use its normal production build.

For added behaviour, use `references/interaction-tools.md`: native browser capabilities first when sufficient, existing compatible widgets where available, or a focused library for a real gap. `references/optional-cdn-links.md` caches exact static-site URLs for Alpine 3.17.4, Observable Plot 0.6.17 and D3 7.9.0; copy only what the artifact uses. Mermaid's CDN import is already in its conditional renderer asset. Tailwind Plus Elements is separate licensed software; Headless UI fits existing React/Vue hosts.

For Mermaid, put source in a labelled figure with `pre.mermaid`, a sibling `div[data-diagram-output]`, `p[data-diagram-status]` and an explanatory caption. Include `assets/renderer-control.html` after the figures. It loads Mermaid 12.0.0 only in connected mode and only when diagrams exist. Render before hiding a diagram in a panel. Portable output should embed locally rendered SVG; retained source is a truthful fallback, not a claim that a finished diagram exists.

Mermaid 12 requires ES2024-capable browsers (Safari 17.4+) and Node 22.12+ for tooling. Its default layout differs from v11. Do not infer compatibility from the pin; inspect rendered diagrams in the target browser.

## No saved reader state

Controls update the open page only. No storage, cookies, saved URL selections, feedback capture, exports or approval forms are added. Explicit anchor navigation is still supported; previous/next does not rewrite the URL. Persistence requires a separate explicit user request, lifetime, destination and reset contract. Author-maintained living HTML is not a permission to save reader choices.

## Run the proof

```sh
python3 skills/html-artifact/scripts/verify_artifact.py report.html --json
```

Open the artifact in the target browser to inspect layout, controls, printing, and any Mermaid output. A successful structural check does not establish runtime compatibility or visual quality.

The checker rejects definite structural defects and emits review warnings for ambiguous runtime/state references. It does not execute JavaScript, assess design, prove factual truth or certify accessibility/privacy. Model-effectiveness cases in `evals/html-artifact/` remain separate, opt-in and unexecuted until actually run.

## Deliberate simplifications

One view control replaces separate detail/stepper/compare implementations. Native inputs plus a domain-owned function replace a generic model engine. Plot is a conditional recipe rather than another default runtime. Report behaviour remains a small optional asset. No rigid house palette/layout, unconditional manifest, global artifact generator, new skill identity or local-history telemetry is introduced.

Primary references: [Tailwind Play CDN](https://tailwindcss.com/docs/installation/play-cdn), [Tailwind CLI](https://tailwindcss.com/docs/installation/tailwind-cli), [Mermaid usage](https://mermaid.js.org/config/usage.html), [Mermaid 12 release](https://github.com/mermaid-js/mermaid/releases/tag/mermaid%4012.0.0).
