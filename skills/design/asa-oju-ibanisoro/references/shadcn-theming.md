# shadcn/ui theming and customization

Use this reference after the UI library and the `eto-apere` token result are confirmed. This skill owns runtime theme behavior and component consumption; it does not define token values or a parallel Tailwind mapping.

## Configure runtime themes

For a Next.js application that already uses `next-themes`, connect the approved theme selectors through one provider:

```tsx
"use client"

import * as React from "react"
import { ThemeProvider as NextThemesProvider } from "next-themes"

export function ThemeProvider({
  children,
  ...props
}: React.ComponentProps<typeof NextThemesProvider>) {
  return <NextThemesProvider {...props}>{children}</NextThemesProvider>
}
```

Use the provider in the application layout with the project-approved default and system-preference behavior. Implement a labeled theme control with the selected component library, preserve keyboard operation, and avoid a flash of the wrong theme.

For another framework, apply the same approved selector without introducing new token values. Store a user preference only when the product contract requires persistence, and use `prefers-color-scheme` only as the defined fallback.

## Consume semantic utilities

Use the semantic utilities returned by `eto-apere`:

```tsx
<Button className="bg-primary text-primary-foreground">
  Continue
</Button>

<Card className="border-border bg-card text-card-foreground">
  Account details
</Card>
```

Add a component variant only when it represents stable application behavior. Compose approved semantic utilities instead of raw colors or a new token layer:

```tsx
const buttonVariants = cva("inline-flex items-center justify-center", {
  variants: {
    variant: {
      default: "bg-primary text-primary-foreground hover:bg-primary/90",
      destructive:
        "bg-destructive text-destructive-foreground hover:bg-destructive/90",
      outline: "border border-input bg-background hover:bg-accent",
    },
  },
})
```

Verify every supported theme for contrast, focus visibility, component states, hydration behavior, and the absence of raw color or spacing values in the changed components.
