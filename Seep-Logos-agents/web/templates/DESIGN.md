# Design System: Seep Logos — Web Visual Standard

## 1. Overview & Creative North Star

**Creative North Star: "Seep" — 世界が染み込む空間**

This design system embodies the philosophy of **Seep (浸透)**: the boundary between the fictional world and reality is not a wall, but a breath. The viewer is drawn in without noticing. We reject "web-native" layouts in favor of **cinematic editorial verticality**—the user is not browsing information, they are uncovering a world.

**The single immersion test:** Before any visual decision, ask: *Does this help the viewer disappear into the world, or does it remind them they are looking at a website?* If the latter, reject it.

**Studio identity is spatial, not chromatic.** Seep Logos has no universal accent color. Our identity is expressed through darkness, intentional silence, and the quality of emergence—light appearing from void. Accent colors belong to each IP.

---

## 2. Colors & Surface Philosophy

The palette is built on depth and controlled illumination. Background is not a flat color—it is a void from which light emerges.

### Studio Defaults (IP-Agnostic)

| Token | Value | Description |
|---|---|---|
| `background` | `#080810` | Deep night. Blue-black void. The base of all immersion. |
| `surface` | `#0f0f17` | Section background. Slightly lifted from background. |
| `surface_container` | `#1a1a2a` | Cards, panels. Closest layer to the viewer. |
| `on_surface` | `#e8e3da` | Primary text. Warm white—never cold. |
| `on_surface_dim` | `#888899` | Secondary text. Captions, dates, metadata. |
| `on_surface_muted` | `#555566` | Labels, tags, inactive states. |

### IP-Specific Accent (Define Per Project)

```
--accent: [IP-specific value]
--accent-glow: [IP-specific value at 30% opacity]
```

**Do not define a studio-wide accent.** Choose based on the IP's emotional truth:

| Accent family | Emotional register | Example IPs |
|---|---|---|
| Gold `#c8b87a`–`#d4a843` | Epic, historical, weight | Dark fantasy, historical |
| Cyan `#00e5cc` | Sci-fi, mechanical, precision | Tech, mecha |
| Purple + Hot Pink `#6c3fd5` + `#ff6b9d` | Pop, character-driven | Gacha, cute |
| None (monochrome) | Minimal, teaser, editorial | Announcement sites |

### The "No-Line" Rule

**Explicit prohibition:** Do not use 1px solid borders to define sections.
- Separate content through **background shifts** between surface tokens.
- If a container edge is absolutely required for accessibility, use `rgba(255,255,255,0.08)`.
- A hard border is a **seam**. A seam breaks immersion.

---

## 3. Typography

Typography is the voice of the world. We use a **three-layer system** that separates narrative voice, functional voice, and technical voice.

| Layer | Font | Use cases |
|---|---|---|
| **Narrative voice** | Georgia, Yu Mincho, Hiragino Mincho (Serif) | Hero titles, chapter headings, world-lore text, anything meant to be *read as story* |
| **Functional voice** | -apple-system, Helvetica Neue (Sans-serif) | Navigation, buttons, card headings, UI labels |
| **Technical voice** | monospace (Courier New) | Dates, tags, numbering, metadata, code |

**The rule:** Every piece of text belongs to exactly one layer. Never mix layers within a single element. Never use Serif for UI labels. Never use monospace for narrative text unless it is an intentional world-aesthetic choice.

### Scale & Spacing

| Element | Size | Letter-spacing |
|---|---|---|
| Hero title | `clamp(2rem, 8vw, 6rem)` | Normal to slightly tight |
| Section heading | `clamp(1.4rem, 3vw, 2.8rem)` | Normal |
| Body | `15–16px` | Normal |
| Labels & tags | `9–11px` | `0.2–0.6em` (uppercase recommended) |

---

## 4. Elevation & Depth

Elevation is an **atmospheric effect**, not a structural one. We do not use drop shadows. Depth is created by tonal layering.

**The Depth Stack:**
- *Lowest:* `background` (`#080810`) — the void beneath everything
- *Mid:* `surface` (`#0f0f17`) — the general page body
- *High:* `surface_container` (`#1a1a2a`) — interactive elements, cards

**Ambient glow (floating elements only):** `box-shadow: 0 0 40px rgba(accent, 0.15)`. This mimics light wrapping around objects in a dark room. Use sparingly—maximum one element per section.

**Ghost border fallback:** If a container edge is required, use `1px solid rgba(255,255,255,0.08)`. Never 100% opaque.

---

## 5. Components

### Buttons

| Type | Style |
|---|---|
| Primary | Rectangular (`border-radius: 0`). Background: `accent`. Text: dark. Hover: outer glow `0 0 15px rgba(accent, 0.4)`. |
| Secondary | No background. Ghost border `rgba(255,255,255,0.15)`. Text: `accent`. |
| Tertiary | Text only in `on_surface_dim`. Hover: underline expands from center. |

**Roundedness:** `0px` for all serious/epic IP aesthetics. `8–12px` only for pop/character-driven IPs (K-pattern equivalent).

### Cards & Information Panels

- **Forbid divider lines** within cards.
- Separate internal sections with vertical white space (`40–80px`).
- Hover: `background` shifts to `surface_container`, optional scale `1.02`.
- Never scale beyond `1.03`—larger scales break the spatial hierarchy.

### Decorative Separators

Instead of lines, use a 1px tall gradient fading to `0%` opacity at both ends. Optional: a 4px `accent`-colored diamond at center. This is a signature element of the N and P patterns.

### Scroll Navigation

Vertical progress indicators on the right edge: `accent` color for active state, `surface_container` for track. Chapter-based. Used in chapter-scroll and dual-column patterns.

---

## 6. Animation

Animation is the **physical law of this world**. Timing communicates weight and deliberateness.

### Timing Reference

| Duration | Feel | Use |
|---|---|---|
| `0.2s` | Sharp, decisive, mechanical | Micro-interactions, toggle states |
| `0.4s` | Responsive, light | Button hovers, quick feedback |
| `0.7s` | Considered, breathing | Section reveals (default) |
| `0.9s` | Weighty, ceremonial | Hero entrances, major transitions |

**Default range for game/anime IPs: `0.7–0.9s`.** The world does not rush.

### Scroll Reveal (Standard)

```css
/* Apply to all major content blocks */
initial:  opacity: 0; transform: translateY(20px);
final:    opacity: 1; transform: translateY(0);
duration: 0.7s–0.9s;
easing:   ease  or  cubic-bezier(0.4, 0, 0.2, 1);
delay:    stagger 0.1s–0.8s between elements
trigger:  IntersectionObserver (do not re-animate on scroll-up)
```

### Hover Effects

- Border color transition: `0.2–0.3s ease`
- Glow: `box-shadow 0.3s ease`
- Scale (if used): `transform 0.3s ease`, max `scale(1.02)`

### Prohibitions

- No bounce / spring animations (`cubic-bezier` with overshoot values)
- No simultaneous animation on all elements—**static elements give moving elements meaning**
- No autoplay animations that loop indefinitely on hero sections

---

## 7. Silence & Negative Space

Negative space is a **primary design element**, not empty space.

- Section gaps: `60–100px` minimum. This is the breath between chapters.
- Text margins: Proportional to the weight of the words. A lone sentence in wide space carries more weight than a paragraph surrounded by content.
- Hero internal space communicates the scale of the world. Filling the hero is a mistake.

**The Seep principle:** A boundary that is felt but not seen. Space is how we achieve this.

---

## 8. Do's and Don'ts

### Do:
- **Do** use intentional asymmetry. Overlap character art across two surface layers to break the grid feel.
- **Do** stagger reveal animations. Content uncovering in sequence feels like a story being told.
- **Do** use Serif (Georgia) for any text meant to be experienced as narrative, even at small sizes.
- **Do** let the footer remain in the world. A "normal" footer breaks immersion at the final moment.
- **Do** choose accent color from the IP's emotional truth, not from what "looks cool."

### Don't:
- **Don't** use white backgrounds or light grey backgrounds. They destroy immersion unconditionally.
- **Don't** use pure white (`#ffffff`) for text. Use `on_surface` (`#e8e3da`)—warm white stays in the world.
- **Don't** use drop shadows. They look cheap in a high-end dark theme. Use tonal layering and ambient glow.
- **Don't** animate everything. When all elements move, nothing moves.
- **Don't** use rounded corners unless the IP explicitly requires warmth and approachability.
- **Don't** use more than two font families on a single page.
- **Don't** fix an accent color in a shared template. Accent belongs to the IP, not the studio.
- **Don't** use Bootstrap-style generic components. Every component should feel like it belongs to this world.

---

## 9. Agent Prompt Guide

When an AI agent is building a page using this design system:

1. **Start with darkness.** Background is `#080810`. Do not negotiate this.
2. **The accent color must be provided by the project brief.** If not provided, ask. Do not invent one.
3. **Typography is a three-layer decision.** Identify which layer each text element belongs to before assigning a font.
4. **Test immersion, not aesthetics.** The question is not "does this look good" but "does this disappear the viewer into the world."
5. **Silence is intentional.** Do not fill space. Space is the breath of the Seep philosophy.
6. **Reference patterns in `web/templates/`** for structural precedents. Pattern A/N/O/P are the primary editorial references.
7. **When in doubt, do less.** A restrained choice that maintains atmosphere beats a bold choice that breaks it.

---

*Seep Logos Creative Studio | Web Visual Standard v1.0 | 2026-04-04*
*Values extracted from: pattern-A, A_2, N, O, P | Governed by: `docs/visual-style-guide.md` (philosophy)*
