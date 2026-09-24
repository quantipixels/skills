# Expressive HTML Artifact toolkit

This change standardises reusable meaning and reliable mechanics, not page appearance. Start with `skills/html-artifact/SKILL.md`; choose the relationship in the visual toolbox, then load only the matching semantic contract, recipe and controls.

## What ships

- Tailwind-first authoring with an offline-safe base and an explicit connected-development switch.
- Conditional, strict-mode Mermaid integration; flowchart, sequence, state and ER specimens; optional quantitative Plot guidance.
- One view selector for details, comparisons and finite steps; category plus text filtering; a carousel that no longer writes URL state.
- Five semantic document contracts, an optional compact manifest with safe JSON serialization, and a read-only structural checker.
- Oro resource-selection guidance and Ayewo artifact-history mining with a Keep Variable result.

Existing report-control, source composition, code-change review and living/live references remain part of the skill. The report guidance is reconciled with the new filter contract. The unrelated TDD proposals and repository-wide retirement work are outside this PR.

## Use the base

Copy `skills/html-artifact/assets/base.html` and replace illustrative content/metadata. Its portable mode makes no Tailwind network request. With a local Tailwind v4 compiler, import Tailwind, point source detection at the artifact and inline the generated CSS. Custom CSS is welcome for expression and semantic visualisations. Do not claim uncompiled utilities work.

For non-sensitive, connected development output, set the root `data-artifact-delivery="connected"`. The base loads pinned `@tailwindcss/browser@4.3.3`. This is not a production-CDN recommendation; private/offline outputs remain compiled/embedded or native CSS.

For Mermaid, put source in a labelled figure with `pre.mermaid`, a sibling `div[data-diagram-output]`, `p[data-diagram-status]` and an explanatory caption. Include `assets/renderer-control.html` after the figures. It loads Mermaid 12.0.0 only in connected mode and only when diagrams exist. Render before hiding a diagram in a panel. Portable output should embed locally rendered SVG; retained source is a truthful fallback, not a claim that a finished diagram exists.

Mermaid 12 requires ES2024-capable browsers (Safari 17.4+) and Node 22.12+ for tooling. Its default layout differs from v11. Do not invent compatibility from the pin; the real-package browser test covers the bundled recipes separately from loader stubs.

## No saved reader state

Controls update the open page only. No storage, cookies, saved URL selections, feedback capture, exports or approval forms are added. Explicit anchor navigation is still supported; previous/next does not rewrite the URL. Persistence requires a separate explicit user request, lifetime, destination and reset contract. Author-maintained living HTML is not a permission to save reader choices.

## Run the proof

```sh
python3 tests/test_html_artifact.py
python3 -m pip install playwright==1.57.0
python3 -m playwright install chromium
python3 tests/test_html_artifact_browser.py
python3 skills/html-artifact/scripts/verify_artifact.py report.html --json
```

The browser suite normally opens a real local file. Restricted environments may set `QP_TEST_TRANSPORT=content`; that runs real Chromium DOM/CSS/control checks but explicitly skips navigation/reload and stronger renderer cases. Do not report those skips as successful end-to-end delivery.

For real pinned dependencies, install `@tailwindcss/browser@4.3.3` and `mermaid@12.0.0` into disposable developer state, then set `QP_RENDERER_PACKAGES` to its node_modules directory. The browser test routes CDN module URLs to those exact local packages and exercises all four recipes plus Tailwind styling. This establishes package/API compatibility, not CDN availability. The dedicated CI workflow installs the exact packages and executes this path.

The checker rejects definite structural defects and emits review warnings for ambiguous runtime/state references. It does not execute JavaScript, assess design, prove factual truth or certify accessibility/privacy. Model-effectiveness cases in `evals/html-artifact/` remain separate, opt-in and unexecuted until actually run.

## Deliberate simplifications

One view control replaces separate detail/stepper/compare implementations. Native inputs plus a domain-owned function replace a generic model engine. Plot is a conditional recipe rather than another default runtime. Report behaviour remains a small optional asset. No rigid house palette/layout, unconditional manifest, global artifact generator, new skill identity or local-history telemetry is introduced.

Primary references: [Tailwind Play CDN](https://tailwindcss.com/docs/installation/play-cdn), [Tailwind CLI](https://tailwindcss.com/docs/installation/tailwind-cli), [Mermaid usage](https://mermaid.js.org/config/usage.html), [Mermaid 12 release](https://github.com/mermaid-js/mermaid/releases/tag/mermaid%4012.0.0).
