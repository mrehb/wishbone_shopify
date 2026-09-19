# Wishbone Golf — Design System v3 "Instrument"

British golf trolleys. **"Birthed in Britain, Wishbone Golf merges exquisite design with unwavering
quality."** *A full powered, simple 'no nonsense' cart.* — the brand's own words, unchanged.

**What this represents:** [wishbone.golf](https://wishbone.golf) (`k500sw-e1.myshopify.com`).
Manual **ONE / TWO / THREE**, electric **NEO / EON**, and a spare-parts catalogue that is most of
what the store sells (22 of 27 products, named `Component (MODEL)`).

## Why v3 replaced v2

v2 hedged. Three typefaces, five radii, a dot device bolted onto an otherwise generic dark UI, and
"the green" quietly meaning two different hues. It was not consistent enough to be a brand.

v3 goes back to the two references — the DeerFlow dashboard the owner chose, and the Wishbone
product itself — and takes exactly one of everything:

| | one of |
|---|---|
| Typeface | **DotGothic16** — a 16px dot-matrix bitmap face. Labels, values, headings, copy. |
| Container | **the Tile** — 24px radius, 24px padding, numbered label, 1px top-light edge |
| Layout | **the Board** — a strict 3 / 2 / 1-column grid of tiles, 16px gap. Every page. |
| Graphic device | **Dots** — 6px on a 3px pitch. Charts, gauges, silhouettes, progress. Nothing else. |
| Rounded element | **the Pill** — buttons, tags, status, selectors, fields. One shape. |
| Ground | **#0F1014** under one warm lamp, top-left (`#F2D2AB` wash) |
| Accent | **Lime #A8FF4A** — hue 89°, the hardware's actual green |
| Light | the lamp. No shadows, no gradients on tiles, no glow. |

Two radii in the whole system (tile 24, pill 999). Two text colours (white, grey). One accent.
**No red** — attention is lime, and an error is a lime-marked instruction.

### The green, settled

The theme's volt `#E3FC02` and the logo's olive `#C8D645` are both hue 66° — yellow-greens. The
trolleys' hardware photographs at hue 90° — green. Two colours had been called "the green".
The product cannot be repainted, so the brand green is the product's: `#A8FF4A`, contrast 15.5:1
on the ground. The monogram is recut with its quarter-circle in lime (`assets/wishbone-monogram-lime.png`).

## CONTENT FUNDAMENTALS

- **Report the value, then stop.** *Range · 27+ holes.* *799 €.* One idea per sentence.
- **Numbers are addresses.** Every tile is numbered `01…n` in reading order.
- **Unknown prints `—`** with *not yet measured*. Never a guess. Fold size and weight are unknown
  for every model today; the tiles say so.
- **Statements may end with the cursor** `_` — sparingly: the hero, the footer line.
- Models in caps: **Wishbone ONE**, **Wishbone EON**. Parts keep `Component (MODEL)` in full.
- British spelling. No superlatives, exclamation marks or emoji.

## VISUAL FOUNDATIONS

- **Type:** DotGothic16 at 12 / 16 / 20 / 32 / 48 / 64 / 96 — multiples of its 16px grid so the
  dots stay crisp. Labels 12px tracked 0.14em uppercase. Font smoothing off.
- **Colour:** ground `#0F1014`, tile `#111214`, white `#FAFAFA`, grey `#8E9298`, lime `#A8FF4A`.
  Lime always carries ground-coloured text. One lime element per tile; the page's lime button is
  the purchase.
- **Geometry:** tile 24px, pill 999px. Nothing else is rounded, nothing else is square.
- **Dots:** 6px / 3px. `bars`, `ring`, `line`, `steps`, `wave`, and photo-sampled silhouettes.
- **Light:** one warm lamp top-left in the page wash and in every photograph. Tiles catch it as
  a 1px top edge.
- **Motion:** dots draw in, readouts count, the cursor blinks. 160 / 320 / 640ms. Nothing lifts.

## Index

- `styles.css` · `tokens/` — colors, typography, geometry, layout, base
- `assets/` — wordmark, monogram (v1), **monogram-lime** (current)
- `guidelines/` — colour, type, tile, dots, board, marks, light, voice
- `components/primitives/` — **Tile + Board**, **Dots** (+ generators), **Pill**, **Field**,
  **Readout**, **Silhouettes** (EON sampled from its photograph)
- `components/tiles/` — HeroTile, RangeTile, CompatTile, BuyTile, SpecTile, CompareTile,
  ProductTile, PartTile, FaqTile, BoxTile, TrustTile
- `components/chrome/` — TopBar, FootBar
- `uploads/` — BRAND_KIT.md, tokens, marks · `SKILL.md` — agent entry point
- `tools/` — generators for the brand book and the library page

## Not done

The Shopify theme still runs v1. This system is the target; nothing reaches customers until a
draft theme is built from it and published by hand. Fold size and weight are still unmeasured.
Positive and SVG versions of the marks are still to commission.
