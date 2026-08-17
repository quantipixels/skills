# React UI component libraries

Use this reference when a React interface needs a component-library decision. This is a local inventory maintained for this skill; it is not a runtime dependency.

## Required decision gate

Before creating or adding React components:

1. Inspect `package.json`, lockfiles, `components.json`, imports, theme files, and existing component directories.
2. If a library is already present, tell the user which one you found and ask whether to reuse it.
3. If none is present, ask: **“Which UI component library should I use for this project?”**
4. Offer the choices below plus **None — build custom components**. If the user delegates the choice, recommend one using the project stack, accessibility needs, ownership model, design-system fit, theming, performance, and maintenance horizon.
5. Record the decision before implementation. Do not silently add a competing library or install packages without authorization.

## Library inventory

| Library | Working model | Best fit / decision signal |
| --- | --- | --- |
| Untitled UI React | Tailwind CSS, React Aria, TypeScript; copy-owned components with free and paid tiers | Tailwind teams wanting a broad, design-system-oriented collection and Figma alignment |
| shadcn/ui | Copy-owned components built around Tailwind CSS and Radix UI | Teams that want maximum source control and customization |
| Tailwind Plus | Premium code collection from the Tailwind team for HTML, React, and Vue | Teams wanting polished Tailwind layouts and are comfortable with paid access |
| Kibo UI | Open registry of composable React components that fills gaps around shadcn/ui | Projects needing niche or advanced components alongside shadcn/ui |
| React Aria Components | Unstyled React components focused on accessibility, internationalization, and interaction behavior | Teams building a custom visual system with strong accessibility requirements |
| Material UI (MUI) | Comprehensive, opinionated implementation of Google Material Design | Enterprise or data-heavy applications that benefit from a mature, broad system |
| Reshaped | React component library and design system centered on composition, accessibility, and developer experience | Teams wanting a professionally crafted general-purpose system |
| AlignUI | Tailwind CSS and partially Radix-based React components with Figma alignment | Teams seeking a Tailwind-oriented library with a broad component set |
| Base UI | Unstyled accessible React primitives for custom design systems | Teams that need behavior and accessibility primitives without prescribed styling |
| Tailark | Marketing blocks and templates built on shadcn/ui | Marketing sites that need ready-made sections rather than a full application system |
| HeroUI | Tailwind CSS and React Aria-based React library | Teams wanting a lightweight, accessible, customizable styled library |
| Mantine UI | Broad React component and hooks collection with theming and dark-mode support | Product teams prioritizing breadth and developer experience |
| daisyUI | Tailwind plugin using semantic component class names and themes | Tailwind projects that prefer concise classes and theme presets |
| Ant Design | Enterprise-focused React library with a large component and data-visualization surface | Complex back-office, admin, and data-heavy applications |

These are decision signals, not mandates. Confirm current compatibility, licensing, accessibility behavior, bundle impact, and maintenance status before adopting a library.

## Output

Record:

- detected libraries and evidence;
- the user-confirmed library or custom decision;
- why it fits the stack and product;
- integration and theming constraints;
- migration or lock-in risks;
- the components to use first.

### Source note

Inventory synthesized from the user-provided Untitled UI article, reviewed 2026-08-10:

https://www.untitledui.com/blog/react-component-libraries
