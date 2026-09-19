# Wishbone Golf — Brand Kit

**Version 4.0 "Studio" — 19 September 2026.** Supersedes v3.0, v2.0 and v1.0 of the same day.

The owner reviewed v3 and asked for a change of direction against a new reference — a white,
product-led page with a light geometric sans, hairlines, one dark band and a lime button used
once: "too many dots, everything a bit too dark, I don't want the dotted font in every aspect."

---

## 0. The direction

One fact decides it: **the store photographs every product on pure white.** A dark site fights every
photograph; a white one lets them sit. v4 is white.

| | v4 |
|---|---|
| Ground | paper `#FFFFFF` alternating with mist `#F4F4F5`; ink `#0F1014` at most once per page |
| Type | **Manrope** — 300 caps for headlines, 400 body, 500 labels, 600 for the price |
| The dot accent | **DotGothic16 for the numbered eyebrow only**; dot silhouettes for parts without a photo |
| Accent | **Lime `#A8FF4A`** — a surface on paper (one button per view, tag, 2px rule); text only on ink |
| Line | the hairline `#E4E4E7` |
| Geometry | radius 0, no shadows; depth is a band change |
| Layout | full-bleed bands on a 1200px / 12-column container, two-half bands split 5 : 7 |

## 1. Colour

| token | value | use |
|---|---|---|
| paper | `#FFFFFF` | the page |
| mist | `#F4F4F5` | alternate band; the frame behind every product photo |
| ink | `#0F1014` | text; the one dark band |
| grey | `#6B7075` | secondary text (5.0:1) |
| hairline | `#E4E4E7` | tables, stats, fields, footer |
| lime | `#A8FF4A` | the accent — hue 89°, the hardware's green (settled in v3) |

Ink on paper 18.6:1 · ink on lime 15.5:1 · lime on ink 15.5:1 · **lime on paper 1.2:1 — never as
text.** No red: an error is a 2px lime line under the field and a plain sentence.

## 2. Type

Manrope (Google Fonts, OFL). Hero 56 / display 40 / small 28 at weight 300, upper case, 2% tracking,
one statement per line each ending in a full stop. Body 15/1.6. Label 12 caps, 0.16em, weight 500.
Price weight 600. **DotGothic16** at 12px, smoothing off, for the eyebrow `01  THE LINEUP` and
nothing else.

## 3. Bands

96px padding (56 mobile, 40 for strips). Paper and mist alternate; consecutive paper bands are
divided by a hairline; the ink band appears once, for the technology feature. Text 5 columns,
image 7. One lime button per view: the purchase.

## 4. Photography

The store's white-studio shots, in a mist frame, `mix-blend-mode: multiply` so the object sits on
the band. No text over photographs, no dark backdrops, no retouched green. Fifteen parts and the NEO
have no photograph and draw their model's dot silhouette until they do.

## 5. Components

Primitives: Eyebrow, Display, Button (lime / ink / outline / text), Stat + StatRow, Field
(underline), Tag, Price, Dots, Silhouette + Photo. Sections: Hero, Stats, Lineup, Feature (paper /
mist / ink), Trust, Inquiry, Buy, Specs, Compare, Parts, Faq. Chrome: Header, Footer. All in
`design-system/components`, all built on the real catalogue.

## 6. Open

Fold size and weight unmeasured; photographs for fifteen parts and the NEO; SVG masters; ™ vs ®;
"aluminum" → "aluminium"; vendor "My Store"; the theme still runs v1.

---

# Appendix — v3.0 "Instrument" (superseded)

**Version 3.0 "Instrument" — 19 September 2026.** Supersedes v2.0 and v1.0 of the same day.

The owner reviewed v2 and rejected it as not consistent enough. v3 is a from-scratch rebuild from
the two references — the DeerFlow dashboard the owner chose as the direction, and the Wishbone
product itself — with the one constraint that the accent stays green.

---

## 0. The principle: one of everything

| | v3 has exactly one |
|---|---|
| Typeface | **DotGothic16** — a 16px dot-matrix bitmap face, at every size, for every string |
| Container | **the Tile** — 24px radius, 24px padding, numbered label, 1px top-light edge |
| Layout | **the Board** — 3 / 2 / 1 columns, 16px gap; every page is a board of tiles |
| Graphic device | **Dots** — 6px on a 3px pitch; charts, gauges, progress, photo-sampled silhouettes |
| Rounded element | **the Pill** — button, ghost, tag, status, select, field |
| Ground | `#0F1014` under **one lamp**, top-left, `#F2D2AB` |
| Accent | **Lime `#A8FF4A`** |

Two radii (24 / 999). Two text colours (white `#FAFAFA` / grey `#8E9298`). One accent. No red —
attention is lime and an error is a lime-marked instruction. No shadows, no gradients on surfaces,
no icons, no second typeface, no other box.

## 1. Why v2 failed

v2 kept three typefaces (Space Grotesk, Figtree, Share Tech Mono), five radii (20 / 16 / 10 / 8 /
999), an error red, a "card / raised" grey ladder, and used the dot matrix as a garnish on
components that were otherwise a generic dark e-commerce UI. The reference is coherent because it
has one type voice, one tile, and one way of drawing anything. v2 had several of each.

It also called two different colours "the green": volt `#E3FC02` and the logo's `#C8D645` are both
**hue 66° — yellow-greens** — while the trolleys' hardware photographs at **hue 90°, green**.

## 2. The green, settled

The product cannot be repainted, so the brand green is the product's. **Lime `#A8FF4A`** (h89 s100
l65): contrast 15.45:1 on the ground, 15.45:1 for ground-coloured text on lime, 1.18:1 for white on
lime — so lime always carries ground text, never white. The monogram is recut with its
quarter-circle in lime (`assets/wishbone-monogram-lime.png`); v1's olive cut and v2's volt cut are
retired. `charcoal-lime`, the colourway, is now literally the accent colour.

## 3. Type

**DotGothic16** (Fontworks, SIL OFL, Google Fonts). One weight. Sizes are multiples of its 16px
grid so the dots stay crisp: **12** label · **16** body · **20** lead · **32** h · **48** readout ·
**64** display · **96** hero. Labels 12px, tracked 0.14em, uppercase. Font smoothing off.

Rule: the brand writes short. Product copy, labels, values, headings — all DotGothic16. Long legal
text (policies, checkout) is Shopify-controlled and falls back to the system mono; that is the only
place a second face appears, and it is not a brand surface.

Fallback stack: `'DotGothic16', 'VT323', ui-monospace, monospace`.

## 4. The Tile and the Board

Every page — home, product, collection, cart, account — is a **Board**: a grid of 3 columns above
900px, 2 above 600, 1 below, with a 16px gap on a 1200px page. Everything on it is a **Tile**: `#111214`
surface, 24px radius, 24px padding, a `NN LABEL` header top-left, a 1px `rgb(255 255 255 / .06)`
inset top edge so it reads as an object under the lamp. Tiles span 1, 2 or 3 columns. Tiles whose
data is live carry a lime dot in the label row.

There is no other container. No cards inside tiles, no bands, no full-bleed hero, no bordered
sections.

## 5. Dots

6px dots on a 3px gap. White for the signal (`#FAFAFA`), dim (`rgb(250 250 250 / .22)`) for the
empty grid, lime for the one value that matters. Generators: `bars`, `ring`, `line`, `steps`,
`wave`. Product silhouettes are sampled from the real photograph's luminance — the EON's is; the
other four models use a procedural outline **only until they are photographed**, then are sampled
the same way. Never hand-draw a product; never use dots as a background.

## 6. Pill and Field

The single rounded element. **button** (lime fill, ground text — the purchase), **ghost**
(outline), **tag** (grey chip), **status** (chip with a dot: grey idle / lime live), **select**
(radio for models and colourways: white fill when on). **Field** is a pill-shaped input; its error
state is a lime border and a `▸` instruction line — there is no red.

## 7. Light and photography

One warm lamp, high and to the left, in the page wash (`radial-gradient(130% 80% at 0% 0%,
rgb(242 210 171 / .2), transparent 62%)`) and in every photograph. Matte black product, low
three-quarter angle, concrete / graphite / dusk, the hardware green the only colour in frame.
The lamp is the only atmosphere: no shadows, no gradients on tiles, no glow behind the lime.

## 8. Voice — unchanged

Report the value, then stop. Numbers are addresses (`01 … n`, reading order). Unknown prints `—`
with *not yet measured*. Statements may end with the cursor `_` — hero and footer only. Models in
caps; parts keep `Component (MODEL)` in full. British spelling; no superlatives, exclamation marks
or emoji.

## 9. Components (19)

**Primitives** — Tile + Board, Dots (+ bars, ring, line, steps, wave), Pill, Field, Readout,
Silhouettes.
**Tiles** — HeroTile, RangeTile, CompatTile, BuyTile, SpecTile, CompareTile, ProductTile,
PartTile, FaqTile, BoxTile, TrustTile.
**Chrome** — TopBar, FootBar.

Every tile is the same Tile. Every graphic is Dots. Every pressable thing is a Pill.

## 10. Where it lives

`design-system/tokens/*.css` (source of truth) · `docs/brand/tokens.css` + `tokens.json`
(portable) · `design-system/components/{primitives,tiles,chrome}` · `design-system/guidelines/`
(8 specimen cards) · `design-system/assets/` (wordmark, monogram-lime) · Claude Design project
*Wishbone Golf Design System* · generator `tools/build-v3.py`.

## 11. Open

1. Fold size and weight — unmeasured; readouts print `—`.
2. Photograph ONE, TWO, THREE, NEO to §7 so their silhouettes can be sampled.
3. Positive + SVG marks.
4. The Shopify theme still runs v1.
5. The brand book (`tools/build-brandbook.py`) still describes v2 and must be regenerated for v3.
6. "aluminum" → "aluminium"; one product under vendor *My Store*.

---

## Appendix — v2.0 and v1.0, as recorded



v1.0 documented the brand as it was found on the live store. v2.0 is a **rebrand**, commissioned by
the owner with one constraint: *keep the green as the accent, change everything else.* What follows
is the new system; §12 records what v1 said, so the change is auditable rather than silent.

The full system — tokens, components, specimen cards — is in
[`../../design-system/`](../../design-system/) and pushed to the Claude Design project
*Wishbone Golf Design System*.

---

## 0. What changed in v2, in one table

| | v1.0 (as-found) | v2.0 (this) |
|---|---|---|
| Ground | `#1F1F21` cold ink | **`#0F1014` carbon** + warm top-left wash |
| Accent | volt `#E3FC02` **+ cyan** `#00FCED` | **volt only** |
| Monogram accent | olive `#C8D645` | **volt** — mark reissued |
| Geometry | radius 0; pills the exception | **20px cards / 10px controls**; pills consistent |
| Display face | Oswald 500 UPPERCASE | **Space Grotesk 500**, sentence case |
| Body face | Figtree 500 | Figtree 400/500 (unchanged) |
| Values & labels | body type | **Share Tech Mono** readouts |
| Signature device | — | **dot matrix** |
| Volt share | 10 % | **4 %** |
| Page / section / gutter | 1600 / 52 / 40 | **1440 / 72 / 20** |
| Shadows | none | **none** (unchanged) |

**Why the green stayed:** the hardware is physically green. A website can be repainted; a fleet of
trolleys cannot. Everything else was free to move, and did.

**Why the corners flipped:** the reference direction the owner chose is built on soft, object-like
panels. v1's square rule and that softness cannot both be the signature — so the square went.

---

## 1. Ground and colour

| Token | Hex | Role |
|---|---|---|
| Carbon | `#0F1014` | The page. Warm near-black, never neutral grey. |
| Card | `#16171B` | Panels. |
| Raised | `#1E2026` | Inputs, wells, hover surfaces. |
| **Volt** | `#E3FC02` | The only accent. One element per screen. |
| White | `#FAFAFA` | Type. |
| Muted | `#8E9298` | Secondary type. |
| Warm light | `#F2D2AB` | A *lighting* value — photography and the page wash. Never a UI fill. |
| Error | `#FF6B6B` | Errors only. Never a second accent. |

**Retired:** cyan `#00FCED` (a Ride-theme leftover that never appeared on the storefront) and the
monogram's olive `#C8D645` (the mark now carries volt). The three-greens problem is closed.

**The rule, unchanged from v1:** volt carries **carbon** type. White on volt measures 1.15:1 and is
unreadable; volt never appears as type on white. Proportion moves to roughly **78 / 18 / 4** — with
the whole page dark and soft, a single volt element carries further. If two volt things are visible
at once, one of them is wrong.

## 2. Type — three faces, one job each

| Face | Job | Sizes |
|---|---|---|
| **Space Grotesk** 500/700 | Says what a thing is | display 68 · h1 48 · h2 32 · h3 23 · h4 18 |
| **Figtree** 400/500/700 | Explains it | body 15 · small 13 |
| **Share Tech Mono** | Reports a value | readout 44 · label 11, tracked 0.18em, uppercase |

Display type is sentence case — the uppercase went with Oswald. Labels and readouts are mono caps.
A number set in body type is a missed opportunity; prose set in mono is unreadable.

## 3. Geometry — soft, layered, still flat

Cards 20px · controls 10px · media 16px · chips 8px · pills full. Borders are hairlines:
`rgb(255 255 255 / .08)` on cards, `.24` on anything selectable.

**Still no drop shadows.** Depth comes from the surface steps (carbon → card → raised) and the warm
wash. A gradient may light a scene; it may never fill a component.

Layout: 1440px page, 72px between sections, 20px grid gutters. Cards sit closer together and groups
sit further apart, so a panel cluster reads as one instrument.

## 4. The dot matrix — the signature device

Every quantity, chart, progress state and product silhouette is drawn as a grid of dots: white at
18–92 % opacity for the body of the data, volt for the part that matters. Dot 5px, gap 3px.

Silhouettes are generated by sampling a real product photograph's luminance, so the dotted EON is
the actual EON, not an illustration of one. `DotMatrix` and `DotBars` ship in the design system.

**Never use it as texture or background pattern.** A dot grid always means *this is data*; the
moment it decorates, the device stops working.

## 5. Light and photography

One warm source `#F2D2AB` raking from the top-left, falling to black — in photography and as the
page's fixed background wash.

Matte black product, low three-quarter angle, close enough to read the engineering: the fold, the
bearings, the wheel profile. Concrete, graphite, asphalt, dusk. The green hardware is the only
colour in frame. People are hands and stance, not faces.

Never: white studio sweeps, flat-lays, bright grass at midday, cool blue-grey grading, stock golfers.

## 6. Voice — unchanged, and now the brand looks like it

> **Birthed in Britain, Wishbone Golf merges exquisite design with unwavering quality.**

Report the value, then stop. *"Range · 27+ holes."* *"799 €."* Short declaratives, concrete nouns,
one idea per sentence, British spelling, no superlatives, no exclamation marks, no emoji.

Panels are numbered `01`, `02`, `03` in reading order — addresses, not decoration. **If a value is
unknown, print `—`.** Inventing a spec is the one thing that breaks a brand built on numbers as proof.

Naming is unchanged: **Wishbone ONE**, **Wishbone EON**; the company is **Wishbone Golf**; spare
parts keep `Component (MODEL)` in full.

## 7. Marks

- **Wordmark** `assets/wishbone-wordmark.png` — 800 × 64, white on transparent. Header 180px in v2
  (the status line above carries some weight). Min 120px screen / 30 mm print. Clear space = the
  height of the W. Carbon, dark photography or a volt panel only.
- **Monogram** `assets/wishbone-monogram-volt.png` — **reissued**: the `b` bowl now carries volt.
  The v1 original is kept at `assets/wishbone-monogram.png` for reference.
- **Still missing:** a positive (ink-on-light) version and an SVG of each. Worth commissioning now
  that the colour is settled.

## 8. Product architecture — unchanged

| Model | Type | Price |
|---|---|---|
| **ONE** | Manual 3-wheel trolley | — |
| **TWO** | Manual trolley | 199 € |
| **THREE** | Manual trolley | 249 € |
| **NEO** | Electric trolley | — |
| **EON** | Electric trolley, flagship | 799 € |

27 products live, one vendor: Wishbone. Spare parts follow `Component (MODEL)`.

## 9. Where this lives

| Piece | Path |
|---|---|
| Tokens | `docs/brand/tokens.css` · `tokens.json` · `design-system/tokens/*.css` |
| Components | `design-system/components/{core,commerce,chrome}` |
| Specimen cards | `design-system/guidelines/*.html` |
| Marks | `docs/brand/assets/` · `design-system/assets/` |
| Live theme | `theme/` — **still v1**, see below |

## 10. What has not been done

**The Shopify theme still runs v1.** This kit is the target, not the storefront. Nothing reaches
customers until a draft theme is built from it and published by hand — the guard hook and
`bin/wb`'s draft-first design both still hold.

Sequenced, the theme work is: tokens into `config/settings_data.json` → type via the theme's font
settings (Space Grotesk and Share Tech Mono are both on Google Fonts, Figtree is already loaded) →
radius and spacing settings → new sections for `SpecPanel` and dot-matrix heroes → photography.

## 11. Decisions still open

1. **Fold size and weight are missing from the catalogue.** A telemetry brand needs them; panels
   print `—` until they exist.
2. **Positive + SVG marks** to commission.
3. **"aluminum" → "aluminium"** on the homepage.
4. One product is published under vendor *My Store* instead of *Wishbone*.
5. Whether the wordmark itself should eventually be redrawn — it is a v1-era logotype in a
   monoline face, and it is the one element v2 did not touch.

## 12. What v1.0 recorded (for audit)

v1.0 documented the as-found store: ink `#1F1F21` ground, volt + cyan, Oswald 500 uppercase over
Figtree 500, radius 0 everywhere with variant pills at 40 as the sole exception, 1600 / 52 / 40
layout, no shadows, and photography already dark and low-angle. Everything above supersedes it
except the voice, the naming rules, the product architecture and the no-shadow rule, which carried
over unchanged.

The extraction that produced v1 — theme settings, contrast measurements, catalogue — is unchanged
and still the evidence base; only the design decisions moved.
