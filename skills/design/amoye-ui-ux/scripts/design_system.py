#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aggregate search results and apply reasoning to one design-system recommendation.

Usage:
    from design_system import generate_design_system
    result = generate_design_system("SaaS dashboard", "My Project")
    print(result["text"])

"""

import csv
import json
import sys
import io
from core import search, DATA_DIR

# Force UTF-8 for stdout/stderr to handle emojis/box-drawing chars on Windows (cp1252 default)
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if sys.stderr.encoding and sys.stderr.encoding.lower() != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


# ============ CONFIGURATION ============
REASONING_FILE = "ui-reasoning.csv"

SEARCH_CONFIG = {
    "product": {"max_results": 1},
    "style": {"max_results": 3},
    "color": {"max_results": 2},
    "landing": {"max_results": 2},
    "typography": {"max_results": 2}
}

# ============ DESIGN DIALS (1-10) ============
# Inspired by taste-skill's DESIGN_VARIANCE / MOTION_INTENSITY / VISUAL_DENSITY
# knobs: three optional 1-10 sliders that bias the existing query-based search
# instead of replacing it. Each dial buckets into a low/mid/high tier.
DIAL_TIERS = {
    "variance": [
        (1, 3, {"label": "Centered / Minimal", "style_keywords": ["Minimalism", "Exaggerated Minimalism", "centered", "symmetric", "grid-based"]}),
        (4, 7, {"label": "Balanced / Modern", "style_keywords": ["modern", "structured", "balanced"]}),
        (8, 10, {"label": "Bold / Asymmetric", "style_keywords": ["Brutalism", "Bento Grids", "asymmetric", "experimental"]}),
    ],
    "motion": [
        (1, 3, {"label": "Subtle", "tier": "Subtle"}),
        (4, 7, {"label": "Standard", "tier": "Standard"}),
        (8, 10, {"label": "Complex", "tier": "Complex"}),
    ],
    "density": [
        (1, 3, {"label": "Spacious", "spacing": {"xs": "4px", "sm": "8px", "md": "24px", "lg": "32px", "xl": "48px", "2xl": "64px", "3xl": "96px"}}),
        (4, 7, {"label": "Standard", "spacing": {"xs": "4px", "sm": "8px", "md": "16px", "lg": "24px", "xl": "32px", "2xl": "48px", "3xl": "64px"}}),
        (8, 10, {"label": "Dense / Dashboard", "spacing": {"xs": "2px", "sm": "4px", "md": "8px", "lg": "12px", "xl": "16px", "2xl": "24px", "3xl": "32px"}}),
    ],
}


def _resolve_dial(dial_name: str, value) -> dict:
    """Bucket a 1-10 dial value into its tier config. Returns None if value is None."""
    if value is None:
        return None
    value = max(1, min(10, int(value)))
    for lo, hi, info in DIAL_TIERS[dial_name]:
        if lo <= value <= hi:
            return {**info, "value": value}
    return None


# ============ COLOR MODE RESOLUTION ============
# Style, palette and anti-patterns are resolved from separate CSVs. Without a
# shared notion of "which mode did we land on", a dark-primary style can be
# paired with a light palette and a "don't use dark mode" anti-pattern.

# Phrases in styles.csv "Light Mode ✓" / "Dark Mode ✓" that mark a style as
# dark-first rather than merely dark-capable ("✓ Full" means both work).
_DARK_PRIMARY_MARKERS = (
    "dark mode primary", "dark primary", "dark-only", "dark only",
    "dark preferred", "dark focused", "dark-first", "dark rich",
    "light mode only as exception",
)

# Query phrases that are an explicit request for a dark theme.
_DARK_QUERY_MARKERS = (
    "dark mode", "dark theme", "dark ui", "dark-mode", "darkmode",
    "night mode", "midnight", "oled",
)

# Anti-pattern clauses that contradict a resolved dark mode.
_DARK_ANTI_PATTERN_MARKERS = ("dark mode", "dark modes", "dark theme")

# Relative luminance below which a Background hex counts as a dark surface.
# #1F2937 (the lightest dark background in colors.csv) sits at ~0.026 and
# #E8ECF1 (the darkest light background) at ~0.79, so the gap is wide.
_DARK_BACKGROUND_MAX_LUMINANCE = 0.18


def _relative_luminance(hex_color: str):
    """WCAG relative luminance of a #RRGGBB string, or None if unparseable."""
    if not hex_color:
        return None
    value = hex_color.strip().lstrip("#")
    if len(value) == 3:
        value = "".join(c * 2 for c in value)
    if len(value) != 6:
        return None
    try:
        channels = [int(value[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    except ValueError:
        return None
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
              for c in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def _palette_is_dark(palette: dict) -> bool:
    """True when a colors.csv row's Background is a dark surface."""
    luminance = _relative_luminance((palette or {}).get("Background", ""))
    return luminance is not None and luminance < _DARK_BACKGROUND_MAX_LUMINANCE


def _style_is_dark_primary(style: dict) -> bool:
    """True when a styles.csv row describes itself as dark-first."""
    if not style:
        return False
    declared = "{} {}".format(
        style.get("Light Mode ✓", ""), style.get("Dark Mode ✓", "")
    ).lower()
    return any(marker in declared for marker in _DARK_PRIMARY_MARKERS)


def _query_wants_dark(query: str) -> bool:
    """True when the query explicitly asks for a dark theme."""
    lowered = (query or "").lower()
    return any(marker in lowered for marker in _DARK_QUERY_MARKERS)


def _resolve_color_mode(query: str, style: dict) -> str:
    """Resolve the mode the rest of the output has to agree with."""
    if _query_wants_dark(query) or _style_is_dark_primary(style):
        return "dark"
    return "light"


def _select_palette_for_mode(palettes: list, mode: str) -> dict:
    """Pick the highest-ranked palette matching the resolved mode.

    Only the dark case filters. Light is left on the existing "top hit wins"
    behaviour so queries that never mention a mode keep their current palette.
    Falls back to the top hit when the data has no matching ramp.
    """
    if not palettes:
        return {}
    if mode == "dark":
        for palette in palettes:
            if _palette_is_dark(palette):
                return palette
    return palettes[0]


def _filter_anti_patterns_for_mode(anti_patterns: str, mode: str) -> str:
    """Drop "avoid dark mode" advice once dark mode is the resolved answer."""
    if mode != "dark" or not anti_patterns:
        return anti_patterns
    kept = [
        clause for clause in anti_patterns.split("+")
        if not any(marker in clause.lower() for marker in _DARK_ANTI_PATTERN_MARKERS)
    ]
    return " + ".join(clause.strip() for clause in kept if clause.strip())


# ============ DESIGN SYSTEM GENERATOR ============
class DesignSystemGenerator:
    """Generates design system recommendations from aggregated searches."""

    def __init__(self):
        self.reasoning_data = self._load_reasoning()

    def _load_reasoning(self) -> list:
        """Load reasoning rules from CSV."""
        filepath = DATA_DIR / REASONING_FILE
        if not filepath.exists():
            return []
        with open(filepath, 'r', encoding='utf-8') as f:
            return list(csv.DictReader(f))

    def _multi_domain_search(self, query: str, style_priority: list = None) -> dict:
        """Execute searches across multiple domains."""
        results = {}
        for domain, config in SEARCH_CONFIG.items():
            if domain == "style" and style_priority:
                # For style, also search with priority keywords
                priority_query = " ".join(style_priority[:2]) if style_priority else query
                combined_query = f"{query} {priority_query}"
                results[domain] = search(combined_query, domain, config["max_results"])
            else:
                results[domain] = search(query, domain, config["max_results"])
        return results

    def _find_reasoning_rule(self, category: str) -> dict:
        """Find matching reasoning rule for a category."""
        category_lower = category.lower()

        # Try exact match first
        for rule in self.reasoning_data:
            if rule.get("UI_Category", "").lower() == category_lower:
                return rule

        # Try partial match
        for rule in self.reasoning_data:
            ui_cat = rule.get("UI_Category", "").lower()
            if ui_cat in category_lower or category_lower in ui_cat:
                return rule

        # Try keyword match
        for rule in self.reasoning_data:
            ui_cat = rule.get("UI_Category", "").lower()
            keywords = ui_cat.replace("/", " ").replace("-", " ").split()
            if any(kw in category_lower for kw in keywords):
                return rule

        return {}

    def _apply_reasoning(self, category: str, search_results: dict) -> dict:
        """Apply reasoning rules to search results."""
        rule = self._find_reasoning_rule(category)

        if not rule:
            return {
                "pattern": "Hero + Features + CTA",
                "style_priority": ["Minimalism", "Flat Design"],
                "color_mood": "Professional",
                "typography_mood": "Clean",
                "key_effects": "Subtle hover transitions",
                "anti_patterns": "",
                "decision_rules": {},
                "severity": "MEDIUM"
            }

        # Parse decision rules JSON
        decision_rules = {}
        try:
            decision_rules = json.loads(rule.get("Decision_Rules", "{}"))
        except json.JSONDecodeError:
            pass

        return {
            "pattern": rule.get("Recommended_Pattern", ""),
            "style_priority": [s.strip() for s in rule.get("Style_Priority", "").split("+")],
            "color_mood": rule.get("Color_Mood", ""),
            "typography_mood": rule.get("Typography_Mood", ""),
            "key_effects": rule.get("Key_Effects", ""),
            "anti_patterns": rule.get("Anti_Patterns", ""),
            "decision_rules": decision_rules,
            "severity": rule.get("Severity", "MEDIUM")
        }

    def _select_best_match(self, results: list, priority_keywords: list) -> dict:
        """Select best matching result based on priority keywords."""
        if not results:
            return {}

        if not priority_keywords:
            return results[0]

        # First: try exact style name match
        for priority in priority_keywords:
            priority_lower = priority.lower().strip()
            for result in results:
                style_name = result.get("Style Category", "").lower()
                if priority_lower in style_name or style_name in priority_lower:
                    return result

        # Second: score by keyword match in all fields
        scored = []
        for result in results:
            result_str = str(result).lower()
            score = 0
            for kw in priority_keywords:
                kw_lower = kw.lower().strip()
                # Higher score for style name match
                if kw_lower in result.get("Style Category", "").lower():
                    score += 10
                # Lower score for keyword field match
                elif kw_lower in result.get("Keywords", "").lower():
                    score += 3
                # Even lower for other field matches
                elif kw_lower in result_str:
                    score += 1
            scored.append((score, result))

        scored.sort(key=lambda x: x[0], reverse=True)
        return scored[0][1] if scored and scored[0][0] > 0 else results[0]

    def _extract_results(self, search_result: dict) -> list:
        """Extract results list from search result dict."""
        return search_result.get("results", [])

    def generate(self, query: str, project_name: str = None,
                 variance: int = None, motion: int = None, density: int = None) -> dict:
        """Generate complete design system recommendation.

        variance/motion/density are optional 1-10 dials (see DIAL_TIERS) that bias
        style selection, pull in a matching motion.csv snippet, and override the
        spacing scale, without changing behavior when left unset.
        """
        variance_info = _resolve_dial("variance", variance)
        motion_info = _resolve_dial("motion", motion)
        density_info = _resolve_dial("density", density)

        # Step 1: First search product to get category
        product_result = search(query, "product", 1)
        product_results = product_result.get("results", [])
        category = "General"
        if product_results:
            category = product_results[0].get("Product Type", "General")

        # Step 2: Get reasoning rules for this category
        reasoning = self._apply_reasoning(category, {})
        style_priority = reasoning.get("style_priority", [])

        # DESIGN_VARIANCE dial: bias style retrieval/selection toward
        # centered-minimal (low) or bold-asymmetric (high) keywords.
        effective_style_priority = style_priority
        if variance_info:
            effective_style_priority = variance_info["style_keywords"] + style_priority

        # Step 3: Multi-domain search with style priority hints
        search_results = self._multi_domain_search(query, effective_style_priority)
        search_results["product"] = product_result  # Reuse product search

        # Step 4: Select best matches from each domain using priority
        style_results = self._extract_results(search_results.get("style", {}))
        color_results = self._extract_results(search_results.get("color", {}))
        typography_results = self._extract_results(search_results.get("typography", {}))
        landing_results = self._extract_results(search_results.get("landing", {}))

        best_style = self._select_best_match(style_results, effective_style_priority)
        # Resolve the mode from the style + query first, then pick a palette that
        # agrees with it. Ranking colors independently is what let a dark-primary
        # style ship with a light background.
        color_mode = _resolve_color_mode(query, best_style)
        best_color = _select_palette_for_mode(color_results, color_mode)
        best_typography = typography_results[0] if typography_results else {}
        best_landing = landing_results[0] if landing_results else {}

        # MOTION_INTENSITY dial: pull a matching GSAP skeleton from motion.csv
        # (domain key is "gsap", not "motion" - PR #296 already owns the "motion"
        # domain for Emil Kowalski's motion-design principles, motion-principles.csv).
        motion_snippet = {}
        if motion_info:
            motion_result = search(f"{query} {motion_info['tier']}", "gsap", 5)
            motion_matches = motion_result.get("results", [])
            tiered = [m for m in motion_matches if m.get("Intensity Tier") == motion_info["tier"]]
            if tiered:
                motion_snippet = tiered[0]
            elif motion_matches:
                motion_snippet = motion_matches[0]

        # Step 5: Build final recommendation
        # Combine effects from both reasoning and style search
        style_effects = best_style.get("Effects & Animation", "")
        reasoning_effects = reasoning.get("key_effects", "")
        combined_effects = style_effects if style_effects else reasoning_effects
        search_errors = {
            domain: result["error"]
            for domain, result in search_results.items()
            if result.get("error")
        }

        return {
            "project_name": project_name or query.upper(),
            "category": category,
            "pattern": {
                "name": best_landing.get("Pattern Name", reasoning.get("pattern", "Hero + Features + CTA")),
                "sections": best_landing.get("Section Order", "Hero > Features > CTA"),
                "cta_placement": best_landing.get("Primary CTA Placement", "Above fold"),
                "color_strategy": best_landing.get("Color Strategy", ""),
                "conversion": best_landing.get("Conversion Optimization", "")
            },
            "style": {
                "name": best_style.get("Style Category", "Minimalism"),
                "type": best_style.get("Type", "General"),
                "effects": style_effects,
                "keywords": best_style.get("Keywords", ""),
                "best_for": best_style.get("Best For", ""),
                "performance": best_style.get("Performance", ""),
                "accessibility": best_style.get("Accessibility", ""),
                "light_mode": best_style.get("Light Mode ✓", ""),
                "dark_mode": best_style.get("Dark Mode ✓", ""),
            },
            "colors": {
                "primary": best_color.get("Primary", "#2563EB"),
                "on_primary": best_color.get("On Primary", ""),
                "secondary": best_color.get("Secondary", "#3B82F6"),
                "accent": best_color.get("Accent", "#F97316"),
                "background": best_color.get("Background", "#F8FAFC"),
                "foreground": best_color.get("Foreground", "#1E293B"),
                "muted": best_color.get("Muted", ""),
                "border": best_color.get("Border", ""),
                "destructive": best_color.get("Destructive", ""),
                "ring": best_color.get("Ring", ""),
                "notes": best_color.get("Notes", ""),
                # Keep aliases used by existing structured-result consumers.
                "cta": best_color.get("Accent", "#F97316"),
                "text": best_color.get("Foreground", "#1E293B"),
            },
            "typography": {
                "heading": best_typography.get("Heading Font", "Inter"),
                "body": best_typography.get("Body Font", "Inter"),
                "mood": best_typography.get("Mood/Style Keywords", reasoning.get("typography_mood", "")),
                "best_for": best_typography.get("Best For", ""),
                "google_fonts_url": best_typography.get("Google Fonts URL", ""),
                "css_import": best_typography.get("CSS Import", "")
            },
            "key_effects": combined_effects,
            "anti_patterns": _filter_anti_patterns_for_mode(
                reasoning.get("anti_patterns", ""), color_mode
            ),
            "decision_rules": reasoning.get("decision_rules", {}),
            "severity": reasoning.get("severity", "MEDIUM"),
            "dials": {
                "variance": variance_info["value"] if variance_info else None,
                "variance_label": variance_info["label"] if variance_info else None,
                "motion": motion_info["value"] if motion_info else None,
                "motion_label": motion_info["label"] if motion_info else None,
                "density": density_info["value"] if density_info else None,
                "density_label": density_info["label"] if density_info else None,
            },
            "motion_snippet": motion_snippet,
            "spacing_scale": density_info["spacing"] if density_info else None,
            "search_errors": search_errors,
        }


def format_markdown(design_system: dict) -> str:
    """Format a design-system result as Markdown."""
    project = design_system.get("project_name", "PROJECT")
    pattern = design_system.get("pattern", {})
    style = design_system.get("style", {})
    colors = design_system.get("colors", {})
    typography = design_system.get("typography", {})
    effects = design_system.get("key_effects", "")
    anti_patterns = design_system.get("anti_patterns", "")
    dials = design_system.get("dials", {})
    motion_snippet = design_system.get("motion_snippet", {})

    lines = []
    lines.append(f"## Design System: {project}")
    lines.append("")

    # Design Dials section (only if at least one dial was set)
    if any(dials.get(k) is not None for k in ("variance", "motion", "density")):
        lines.append("### Design Dials")
        if dials.get("variance") is not None:
            lines.append(f"- **Variance:** {dials['variance']}/10 — {dials['variance_label']}")
        if dials.get("motion") is not None:
            lines.append(f"- **Motion:** {dials['motion']}/10 — {dials['motion_label']}")
        if dials.get("density") is not None:
            lines.append(f"- **Density:** {dials['density']}/10 — {dials['density_label']}")
        lines.append("")

    # Pattern section
    lines.append("### Pattern")
    lines.append(f"- **Name:** {pattern.get('name', '')}")
    if pattern.get('conversion'):
        lines.append(f"- **Conversion Focus:** {pattern.get('conversion', '')}")
    if pattern.get('cta_placement'):
        lines.append(f"- **CTA Placement:** {pattern.get('cta_placement', '')}")
    if pattern.get('color_strategy'):
        lines.append(f"- **Color Strategy:** {pattern.get('color_strategy', '')}")
    lines.append(f"- **Sections:** {pattern.get('sections', '')}")
    lines.append("")

    # Style section
    lines.append("### Style")
    lines.append(f"- **Name:** {style.get('name', '')}")
    light = style.get("light_mode", "")
    dark = style.get("dark_mode", "")
    if light or dark:
        lines.append(f"- **Mode Support:** Light {light} | Dark {dark}")
    if style.get('keywords'):
        lines.append(f"- **Keywords:** {style.get('keywords', '')}")
    if style.get('best_for'):
        lines.append(f"- **Best For:** {style.get('best_for', '')}")
    if style.get('performance') or style.get('accessibility'):
        lines.append(f"- **Performance:** {style.get('performance', '')} | **Accessibility:** {style.get('accessibility', '')}")
    lines.append("")

    # Colors section (extended palette)
    lines.append("### Colors")
    lines.append("| Role | Hex | CSS Variable |")
    lines.append("|------|-----|--------------|")
    md_color_entries = [
        ("Primary",      "primary",      "--color-primary"),
        ("On Primary",   "on_primary",   "--color-on-primary"),
        ("Secondary",    "secondary",    "--color-secondary"),
        ("Accent/CTA",   "accent",       "--color-accent"),
        ("Background",   "background",   "--color-background"),
        ("Foreground",   "foreground",   "--color-foreground"),
        ("Muted",        "muted",        "--color-muted"),
        ("Border",       "border",       "--color-border"),
        ("Destructive",  "destructive",  "--color-destructive"),
        ("Ring",         "ring",         "--color-ring"),
    ]
    for label, key, css_var in md_color_entries:
        hex_val = colors.get(key, "")
        if hex_val:
            lines.append(f"| {label} | `{hex_val}` | `{css_var}` |")
    if colors.get("notes"):
        lines.append(f"\n*Notes: {colors.get('notes', '')}*")
    lines.append("")

    # Typography section
    lines.append("### Typography")
    lines.append(f"- **Heading:** {typography.get('heading', '')}")
    lines.append(f"- **Body:** {typography.get('body', '')}")
    if typography.get("mood"):
        lines.append(f"- **Mood:** {typography.get('mood', '')}")
    if typography.get("best_for"):
        lines.append(f"- **Best For:** {typography.get('best_for', '')}")
    if typography.get("google_fonts_url"):
        lines.append(f"- **Google Fonts:** {typography.get('google_fonts_url', '')}")
    if typography.get("css_import"):
        lines.append(f"- **CSS Import:**")
        lines.append(f"```css")
        lines.append(f"{typography.get('css_import', '')}")
        lines.append(f"```")
    lines.append("")

    # Key Effects section
    if effects:
        lines.append("### Key Effects")
        lines.append(f"{effects}")
        lines.append("")

    # Motion section (GSAP skeleton, only if --motion dial was set)
    if motion_snippet:
        lines.append("### Motion")
        lines.append(f"**{motion_snippet.get('Category', '')}** ({motion_snippet.get('Intensity Tier', '')}) — Trigger: {motion_snippet.get('Trigger', '')} | Duration: {motion_snippet.get('Duration', '')} | Easing: `{motion_snippet.get('Easing', '')}`")
        lines.append("```js")
        lines.append(motion_snippet.get("GSAP Snippet", ""))
        lines.append("```")
        if motion_snippet.get("Framework Notes"):
            lines.append(f"*Framework notes: {motion_snippet.get('Framework Notes', '')}*")
        motion_do = motion_snippet.get("Do", "")
        motion_dont = motion_snippet.get("Don't", "")
        if motion_do:
            lines.append(f"- ✅ {motion_do}")
        if motion_dont:
            lines.append(f"- ❌ {motion_dont}")
        lines.append("")

    # Anti-patterns section
    if anti_patterns:
        lines.append("### Avoid (Anti-patterns)")
        newline_bullet = '\n- '
        lines.append(f"- {anti_patterns.replace(' + ', newline_bullet)}")
        lines.append("")

    # Pre-Delivery Checklist section
    lines.append("### Pre-Delivery Checklist")
    lines.append("- [ ] No emojis as icons (use SVG: Heroicons/Lucide)")
    lines.append("- [ ] cursor-pointer on all clickable elements")
    lines.append("- [ ] Hover states with smooth transitions (150-300ms)")
    lines.append("- [ ] Light mode: text contrast 4.5:1 minimum")
    lines.append("- [ ] Focus states visible for keyboard nav")
    lines.append("- [ ] prefers-reduced-motion respected")
    lines.append("- [ ] Responsive: 375px, 768px, 1024px, 1440px")
    lines.append("")

    return "\n".join(lines)

# ============ MAIN ENTRY POINT ============
def generate_design_system(query: str, project_name: str = None,
                           variance: int = None, motion: int = None,
                           density: int = None) -> dict:
    """Generate one structured design recommendation and its Markdown rendering."""
    design_system = DesignSystemGenerator().generate(
        query,
        project_name,
        variance=variance,
        motion=motion,
        density=density,
    )
    return {
        "text": format_markdown(design_system),
        "design_system": design_system,
        "search_errors": design_system.get("search_errors", {}),
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate a design-system recommendation")
    parser.add_argument("query", help="Search query, for example 'SaaS dashboard'")
    parser.add_argument("--project-name", "-p", default=None, help="Project name")
    parser.add_argument("--variance", type=int, choices=range(1, 11), metavar="1-10")
    parser.add_argument("--motion", type=int, choices=range(1, 11), metavar="1-10")
    parser.add_argument("--density", type=int, choices=range(1, 11), metavar="1-10")
    args = parser.parse_args()

    result = generate_design_system(
        args.query,
        args.project_name,
        variance=args.variance,
        motion=args.motion,
        density=args.density,
    )
    print(result["text"])
