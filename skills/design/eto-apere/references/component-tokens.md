# Component Tokens

Component-specific tokens referencing semantic layer.

## Button Tokens

```css
:root {
  /* Default (Primary) */
  --button-bg: var(--color-primary);
  --button-fg: var(--color-primary-foreground);
  --button-bg-hover: var(--color-primary-hover);
  --button-bg-active: var(--color-primary-active);

  /* Secondary */
  --button-secondary-bg: var(--color-secondary);
  --button-secondary-fg: var(--color-secondary-foreground);
  --button-secondary-bg-hover: var(--color-secondary-hover);

  /* Outline */
  --button-outline-border: var(--color-border);
  --button-outline-fg: var(--color-foreground);
  --button-outline-bg-hover: var(--color-accent);

  /* Ghost */
  --button-ghost-fg: var(--color-foreground);
  --button-ghost-bg-hover: var(--color-accent);

  /* Destructive */
  --button-destructive-bg: var(--color-destructive);
  --button-destructive-fg: var(--color-destructive-foreground);
  --button-destructive-bg-hover: var(--color-destructive-hover);

  /* Sizing */
  --button-padding-x: var(--space-4);
  --button-padding-y: var(--space-2);
  --button-padding-x-sm: var(--space-3);
  --button-padding-y-sm: var(--space-1-5);
  --button-padding-x-lg: var(--space-6);
  --button-padding-y-lg: var(--space-3);

  /* Shape */
  --button-radius: var(--radius-md);
  --button-font-size: var(--font-size-sm);
  --button-font-weight: var(--font-weight-medium);
}
```

## Input Tokens

```css
:root {
  /* Background & Border */
  --input-bg: var(--color-background);
  --input-border: var(--color-input);
  --input-fg: var(--color-foreground);

  /* Placeholder */
  --input-placeholder: var(--color-muted-foreground);

  /* Focus */
  --input-border-focus: var(--color-ring);
  --input-ring-focus: var(--color-ring);

  /* Error */
  --input-border-error: var(--color-error);
  --input-fg-error: var(--color-error);

  /* Disabled */
  --input-bg-disabled: var(--color-muted);
  --input-fg-disabled: var(--color-muted-foreground);

  /* Sizing */
  --input-padding-x: var(--space-3);
  --input-padding-y: var(--space-2);
  --input-radius: var(--radius-md);
  --input-font-size: var(--font-size-sm);
}
```

## Card Tokens

```css
:root {
  /* Background & Border */
  --card-bg: var(--color-card);
  --card-fg: var(--color-card-foreground);
  --card-border: var(--color-border);

  /* Shadow */
  --card-shadow: var(--shadow-default);
  --card-shadow-hover: var(--shadow-md);

  /* Spacing */
  --card-padding: var(--space-6);
  --card-padding-sm: var(--space-4);
  --card-gap: var(--space-4);

  /* Shape */
  --card-radius: var(--radius-lg);
}
```

## Badge Tokens

```css
:root {
  /* Default */
  --badge-bg: var(--color-primary);
  --badge-fg: var(--color-primary-foreground);

  /* Secondary */
  --badge-secondary-bg: var(--color-secondary);
  --badge-secondary-fg: var(--color-secondary-foreground);

  /* Outline */
  --badge-outline-border: var(--color-border);
  --badge-outline-fg: var(--color-foreground);

  /* Destructive */
  --badge-destructive-bg: var(--color-destructive);
  --badge-destructive-fg: var(--color-destructive-foreground);

  /* Sizing */
  --badge-padding-x: var(--space-2-5);
  --badge-padding-y: var(--space-0-5);
  --badge-radius: var(--radius-full);
  --badge-font-size: var(--font-size-xs);
}
```

## Alert Tokens

```css
:root {
  /* Default */
  --alert-bg: var(--color-background);
  --alert-fg: var(--color-foreground);
  --alert-border: var(--color-border);

  /* Destructive */
  --alert-destructive-bg: var(--color-destructive);
  --alert-destructive-fg: var(--color-destructive-foreground);

  /* Spacing */
  --alert-padding: var(--space-4);
  --alert-radius: var(--radius-lg);
}
```

## Dialog/Modal Tokens

```css
:root {
  /* Overlay */
  --dialog-overlay-bg: rgb(0 0 0 / 0.5);

  /* Content */
  --dialog-bg: var(--color-background);
  --dialog-fg: var(--color-foreground);
  --dialog-border: var(--color-border);
  --dialog-shadow: var(--shadow-lg);

  /* Spacing */
  --dialog-padding: var(--space-6);
  --dialog-radius: var(--radius-lg);
  --dialog-max-width: 32rem;
}
```

## Table Tokens

```css
:root {
  /* Header */
  --table-header-bg: var(--color-muted);
  --table-header-fg: var(--color-muted-foreground);

  /* Body */
  --table-row-bg: var(--color-background);
  --table-row-bg-hover: var(--color-muted);
  --table-row-fg: var(--color-foreground);

  /* Border */
  --table-border: var(--color-border);

  /* Spacing */
  --table-cell-padding-x: var(--space-4);
  --table-cell-padding-y: var(--space-3);
}
```

## Usage Example

```css
.button {
  background: var(--button-bg);
  color: var(--button-fg);
  padding: var(--button-padding-y) var(--button-padding-x);
  border-radius: var(--button-radius);
  font-size: var(--button-font-size);
  font-weight: var(--button-font-weight);
  transition: background var(--duration-fast);
}

.button:hover {
  background: var(--button-bg-hover);
}

.button.secondary {
  background: var(--button-secondary-bg);
  color: var(--button-secondary-fg);
}
```

## Slide Tokens

`eto-apere` owns these declarations; `slides` consumes them without inventing fallback values.

```css
:root {
  --slide-bg: var(--color-background);
  --slide-bg-surface: var(--color-surface);
  --slide-bg-gradient: var(--gradient-primary);
  --slide-foreground: var(--color-primary-foreground);
  --slide-foreground-muted: var(--color-gray-200);
  --slide-border: var(--color-gray-300);
  --slide-padding: var(--spacing-section);
  --slide-title-size: var(--font-size-6xl);
  --slide-heading-size: var(--font-size-4xl);
  --slide-body-size: var(--font-size-lg);
}
```
