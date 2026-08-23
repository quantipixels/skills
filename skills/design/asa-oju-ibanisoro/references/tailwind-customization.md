# Tailwind CSS customization

Use this reference to consume an approved `eto-apere` token result in application-owned Tailwind utilities and variants. Do not define a competing palette, type scale, spacing scale, radius system, or semantic-token map here.

## Consume supplied tokens

For Tailwind CSS 4, expose approved CSS variables through `@theme` aliases only when the project needs utility names that its token output does not already provide:

```css
@import "tailwindcss";

@theme {
  --color-brand: var(--color-primary);
  --font-display: var(--font-heading);
  --spacing-section: var(--layout-section-gap);
}
```

For Tailwind CSS 3, map the same supplied variables in `tailwind.config.ts`. Do not copy their resolved values into configuration.

## Add application utilities

Add a utility only for repeated application behavior that tokens do not express:

```css
@utility content-auto {
  content-visibility: auto;
}

@utility tab-* {
  tab-size: var(--tab-size-*);
}
```

Use custom variants for application state or theme selectors already present in the approved contract:

```css
@custom-variant theme-midnight (&:where([data-theme="midnight"] *));
@custom-variant aria-checked (&[aria-checked="true"]);
@custom-variant required (&:required);
```

Keep component classes and layout rules in application layers. Use semantic utilities supplied by the token mapping instead of raw colors or one-off spacing values.
