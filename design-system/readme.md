# Wishbone Golf — Design System v4 "Studio"

British golf trolleys. **"Birthed in Britain, Wishbone Golf merges exquisite design with unwavering
quality."** *A full powered, simple 'no nonsense' cart.* — the brand's own words, unchanged.

**What this represents:** [wishbone.golf](https://wishbone.golf) (`k500sw-e1.myshopify.com`).
Manual **ONE / TWO / THREE**, electric **NEO / EON**, and a spare-parts catalogue that is most of
what the store sells (22 of 27 products, named `Component (MODEL)`).

## Why v4 replaced v3

v3 took the dot-matrix reference literally: dark ground, dot type everywhere, dot charts in every
tile. The owner's verdict — too many dots, too dark, the dot font should not be in every aspect —
and a new reference: a white, airy, product-led page with a light geometric sans, one dark band,
hairlines, and a lime button used exactly once.

One fact settles the direction: **the store photographs every product on pure white.** A dark site
fights every photograph; a white one lets them sit. v4 is built on that.

| | v4 |
|---|---|
| Ground | **paper `#FFFFFF`**, alternating with **mist `#F4F4F5`**; **ink `#0F1014`** at most once per page |
| Type | **Manrope** 300 / 400 / 500 / 600 for everything |
| The dot accent | **DotGothic16 for the eyebrow only** (`01  THE LINEUP`), and dot **silhouettes** for parts with no photo. Nothing else |
| Accent | **Lime `#CBE832`**, hue 70°. A surface on paper (button, tag, 2px rule), text only on ink |
| Line | the **hairline** `#E4E4E7` — tables, stats, fields, footer |
| Geometry | **radius 0.** No shadows. Depth is a band change |
| Layout | full-bleed **bands** on a 1200px, 12-column container; two-half bands split 5 : 7 |
| Photography | white studio, multiplied onto mist |

### The green, settled for real

The logo olive is hue 66°. The ONE, the TWO and the THREE photograph at hue 72–73°. Only the EON
sits at 89°, and v3 and v4.0 wrongly took it as the brand. **v4.1 moves the accent to `#CBE832`,
hue 70°** — four degrees from the mark, four degrees from the hardware, 13.7:1 on ink both ways.
The logo and the interface are finally the same green.

### Red exists, but not here

`#E03828` is on the CUBE mark and on the White / Red colourway of every model. It is a **product
colour**: it appears on hardware and in colourway swatches and nowhere else. Buttons are lime,
errors are lime. The interface still has no red.

## CONTENT FUNDAMENTALS

- **Headlines are statements**, one per line, each with a full stop: *LIGHT. SIMPLE. BRITISH.*
- **Report the value, then stop.** *27+ holes.* *799,00 €.* One idea per sentence.
- **Unknown prints `—`** with *not yet measured*. Fold size and weight are unknown for every model.
- Models in caps: **Wishbone ONE**, **Wishbone EON**. Parts keep `Component (MODEL)` in full.
- British spelling. No superlatives, exclamation marks or emoji.

## VISUAL FOUNDATIONS

- **Type:** hero 56 / display 40 / s 28 at weight 300, upper case, 2% tracking. Body 15/1.6.
  Label 12 caps 0.16em at 500. Price at 600. Eyebrow 12 in DotGothic16, smoothing off.
- **Colour:** ink on paper 18.6:1, grey `#6B7075` 5.0:1, ink on lime 13.7:1. Lime is never text on
  paper. No red — an error is a lime line and a sentence.
- **Bands:** 96px padding (56 mobile, 40 for strips). Paper/mist alternate; consecutive paper bands
  get a hairline; ink once, for the technology feature. One lime button per view: the purchase.
- **Photo:** the store's white-background shot in a mist frame, `mix-blend-mode: multiply`; the
  model's dot silhouette where there is no shot.
- **Motion:** colour and opacity only. 160 / 320 / 640ms. Nothing lifts, nothing loops.

## Index

- `styles.css` · `tokens/` — colors, typography, geometry, layout, base
- `assets/` — wordmark + **wordmark-ink**, monogram-lime + **monogram-ink** (positive, for paper)
- `guidelines/` — colour, type, band, photo, dots, marks, voice, motion
- `components/primitives/` — Eyebrow, Display, Button, Stat + StatRow, Field, Tag, Price, Dots,
  Silhouette + **Photo**
- `components/sections/` — Hero, Stats, Lineup, Feature, Trust, Inquiry, Buy, Specs, Compare,
  Parts, Faq
- `components/chrome/` — Header, Footer
- `uploads/` — BRAND_KIT.md, tokens, marks · `SKILL.md` — agent entry point
- `tools/` — generators for the brand book and the library page

## Not done

The Shopify theme still runs v1. Fold size and weight are still unmeasured. Fifteen parts and the
NEO have no photograph. SVG masters of the marks are still to commission.
