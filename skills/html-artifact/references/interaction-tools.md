# Reuse interaction capabilities

Read when an artifact needs behaviour beyond its existing controls. Tailwind supplies styling; `aria-*`, `data-*`, `open:`, `disabled:`, `dark:` and responsive variants express state without JavaScript style choreography. Keep complete utility strings in the source so both browser and build-time compilers can discover them.

## Pick the smallest adequate owner

| Need | First useful owner | Do not recreate |
| --- | --- | --- |
| Disclosure, modal, popover, selection input | Native `details`, `dialog`, popover and form controls, styled with Tailwind | Disclosure state, top-layer placement or modal focus containment when the browser already provides it. |
| Existing view, filter or finite carousel contract | Shipped QP asset or adequate host component | A second copy of tested artifact-specific behaviour. |
| Several linked transient values and reactive DOM bindings | Alpine when no suitable host runtime exists | A home-grown reactive/event-binding framework. Load once, only when selected. |
| Complex widget: combobox, data grid, drag/drop or virtualisation | A maintained component designed for that behaviour and compatible with the delivery | Keyboard, focus, scrolling and interaction machinery merely to avoid a dependency. |
| React/Vue host already using Headless UI | Reuse its appropriate headless component | A second framework or a duplicate widget owner. |
| Existing code or a selected plugin needs jQuery | Reuse the host copy, or load the optional pinned CDN build | A second copy of jQuery; jQuery core alone is not a complete accessible widget. |

Tailwind Plus **Elements** is a separate plain-HTML JavaScript component library, not part of Tailwind CSS. Use only with appropriate licence and redistribution rights; do not bundle customer-only code into the public QP package. Headless UI targets React/Vue; do not add either framework just for an ordinary HTML document. These are selection anchors, not an exhaustive allowlist.

## Keep the integration small

Choose one owner per control. Verify the actual API, maintenance, accessibility behaviour, licence and browser target at selection. Reuse an existing dependency when adequate; otherwise pin the selected package and follow the artifact delivery policy. Preserve useful styling freedom. Library adoption should remove hard custom work, not add a parallel implementation behind another wrapper.

For standalone documents, [optional CDN links](optional-cdn-links.md) holds exact ready-to-copy URLs for jQuery, Alpine, Plot and D3. Copy the selected entry only; Mermaid already has a conditional renderer asset. The base does not load these optional libraries.

For Alpine, use ordinary in-memory `x-data` state, declarative events and bindings; persistence plugins are not part of the default. Treat directive expressions as authored code, never interpolated source data. Use text binding rather than raw HTML injection. Its standard build evaluates expressions; use its supported CSP build when the host policy requires it, not a weakened host policy.

Keep content readable when a runtime fails and show controls only when their implementation is ready. Test the behaviour users need—keyboard/focus, the relevant state transition, reset, print and reload—not the dependency's internal calls. Do not assume a library name proves accessibility or no-save behaviour.

## Native specimen: no additional JavaScript

Use only for supporting detail that can be disclosed; critical limitations remain visible. Restyle freely. The browser owns opening and keyboard activation, Tailwind owns appearance.

```html
<details class="rounded-md border p-4 open:bg-[Canvas]">
  <summary class="cursor-pointer font-semibold">How this conclusion was checked</summary>
  <p class="mt-3">Replace with source-supported evidence and its limits.</p>
</details>
```

Sources: [Tailwind state variants](https://tailwindcss.com/docs/hover-focus-and-other-states), [Tailwind Plus Elements](https://tailwindcss.com/blog/vanilla-js-support-for-tailwind-plus), [Headless UI](https://headlessui.com/), [Alpine start](https://alpinejs.dev/start-here), [Alpine CSP](https://alpinejs.dev/advanced/csp), [Alpine Persist](https://alpinejs.dev/plugins/persist), [jQuery core](https://jquery.com/).
