# QP design tokens

QP's mark supplies white ink, round eyes and the red smile `#d52e1e`. Use crisp neutral or slightly cool greys and a sparse red accent. No warm off-whites, beige, cream, sand, tan, coral, terracotta or orange palette, and no copied product tokens. Layout, density and type may adapt to the reader.

| Token | Light | Dark |
| --- | --- | --- |
| `--qp-bg` | `#ffffff` | `#0b0d10` |
| `--qp-surface` | `#f4f5f7` | `#15181d` |
| `--qp-fg` | `#0e1116` | `#f2f4f7` |
| `--qp-muted` | `#565d68` | `#9aa1ab` |
| `--qp-border` | `#d9dce1` | `#2a2f36` |
| `--qp-accent` | `#d52e1e` | `#ff5b4d` |
| `--qp-accent-strong` | `#a8221a` | `#ff8174` |
| `--qp-success` | `#1a7f4b` | `#3fbf7f` |
| `--qp-warning` | `#b26b00` | `#e0a030` |
| `--qp-danger` | `#c0182b` | `#ff6b7a` |
| `--qp-chart-1` | `#d52e1e` | `#ff5b4d` |
| `--qp-chart-2` | `#2f6fb0` | `#75ade8` |
| `--qp-chart-3` | `#1f8a7a` | `#57c7b5` |
| `--qp-chart-4` | `#3b4a5c` | `#99adc7` |
| `--qp-chart-5` | `#6b4fbf` | `#af92ee` |
| `--qp-chart-6` | `#b26b00` | `#e0a030` |

Chart order is red, blue, teal, slate, purple, amber; dark variants keep those hues. Use the system UI sans stack and `ui-monospace`, no webfonts. Radius is 6px, borders 1px, spacing follows an 8px rhythm. The stylesheet in [base.html](../assets/base.html) is the executable token source; the generator reuses it.

SIGIDI owns `--background`/`--foreground`. Use those for page background/text and retain QP's accent, status and chart colours. The host's light/dark mode selects the matching QP tokens without moving its stylesheet. Standalone pages follow system mode and offer a transient toggle.

Body text requires 4.5:1; large text, focus and meaningful graphical UI require 3:1. Check text on both background and surface in each mode. Warning/chart colours can mark symbols or large UI when they do not reach body contrast; status labels stay in the foreground colour and also say pass/caution/fail. Decorative borders do not carry status. Recheck actual colours in a host or adapted palette.
