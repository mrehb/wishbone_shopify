# Wishbone Golf — Brand Kit

**Version 1.0 — 19 September 2026.**

This kit is *derived*, not invented. Everything marked **Observed** was read out of the live
store on 19 September 2026 — theme settings, logo files, product data and the brand's own
copy. Everything marked **Proposed** is a rule written to make the observed system usable
and consistent; those are the parts to argue with.

Sources: `theme/config/settings_data.json`, `theme/assets/base.css`, `theme/templates/index.json`,
the Shopify Files logos, and wishbone.golf itself.

---

## 1. The brand in one line

> **Birthed in Britain, Wishbone Golf merges exquisite design with unwavering quality.**
> — the brand's own words, homepage, *WE ARE WISHBONE*

**Observed** — the full homepage statement: *"Our Wishbone Trolley — crafted from ultra-light
aircraft-grade aluminum — frees you from bulk. Effortless folding, magnetic attachments, and
sealed bearings keep you rolling smoothly. Focus on your game; Wishbone Golf will handle the rest."*

**Proposed** — the three things every piece of Wishbone communication should carry:

| Pillar | What it means | Evidence it is true |
|---|---|---|
| **Engineered light** | Aircraft-grade aluminium, no bulk | The frame, the fold, the weight |
| **No nonsense** | Simple to use, nothing decorative | *"A full powered, simple 'no nonsense' electric cart"* — EON copy |
| **British design** | Design-led, quality as a given | *"Birthed in Britain"* |

## 2. Product architecture and naming

**Observed.** Models are single words in **ALL CAPS**, never numbers-as-digits:

| Model | Type | Price (EUR) |
|---|---|---|
| **ONE** | Manual 3-wheel trolley | — |
| **TWO** | Manual trolley | 199 |
| **THREE** | Manual trolley | 249 |
| **NEO** | Electric trolley | — |
| **EON** | Electric trolley, flagship | 799 |

Spare parts follow `Component (MODEL)` — *Rear Wheel Right (ONE)*, *Fast Charger (NEO & EON)*,
*Lithium Battery 27+ Holes (NEO & EON)*. 27 products live, one vendor: **Wishbone**.

**Proposed rules**

- In prose: **Wishbone ONE**, **Wishbone EON** — brand first, model in caps.
- Never "Wishbone One", "wishbone eon", "EON trolley by Wishbone".
- The company is **Wishbone Golf**; the product family is **Wishbone**.
- One product-type vendor field — anything published as *My Store* is a data error, not a brand.

## 3. Logo

**Observed.** Two marks exist, both PNG with transparency, both white-on-transparent:

| Asset | File | Size | Use |
|---|---|---|---|
| Wordmark | `WISHBONE_GOLF_NEGATIVE.png` | 800 × 64 | Site header, at 200 px wide |
| Monogram | `wb_logo.png` | 600 × 307 | Favicon |

The **wordmark** is a wide monoline geometric sans, rounded terminals, all caps, with *GOLF*
set vertically at the right edge and a ™. The **monogram** is a lowercase `wb` ligature whose
`b` bowl is cut by a quarter-circle in lime.

Local copies: [`assets/WISHBONE_GOLF_NEGATIVE.png`](assets/WISHBONE_GOLF_NEGATIVE.png),
[`assets/wb_logo.png`](assets/wb_logo.png).

**Proposed rules**

- **Clear space** = the height of the `W` on all four sides. Nothing enters it.
- **Minimum width** — wordmark 120 px on screen, 30 mm in print; monogram 24 px.
- **Backgrounds** — the marks are white, so: ink (#1F1F21), photography dark enough to keep
  the mark legible, or Volt/Cyan panels. Never on white, never on mid-grey, never on busy
  photography.
- **Don't** — recolour, outline, add effects, stretch, rotate, box it in, set the wordmark
  and monogram side by side, or rebuild *GOLF* in another typeface.

**Missing, and worth commissioning** — a positive (ink-on-light) version of both marks, and
an SVG of each. Today a light-background placement is impossible without someone
improvising, which is how brands drift.

## 4. Colour

**Observed** — the five theme colour schemes reduce to four colours:

| Name | Hex | Role |
|---|---|---|
| **Ink** | `#1F1F21` | The ground. Default background of the brand. |
| **White** | `#FFFFFF` | Type and marks on ink; occasional light surface (scheme-3). |
| **Volt** | `#E3FC02` | The action colour — primary buttons. |
| **Cyan** | `#00FCED` | Secondary accent panel (scheme-5). |

Colour schemes in use: 1 = ink + Volt buttons · 2 = ink + white buttons (cards) · 3 = white +
ink buttons · 4 = Volt panel · 5 = Cyan panel.

**Proposed ratio** — roughly 70 % ink, 20 % white, 10 % Volt. Cyan is a guest: one element per
page at most, never next to Volt at equal size.

### Accessibility — the rule that matters

Measured contrast ratios (WCAG 2.1):

| Pair | Ratio | Verdict |
|---|---|---|
| White on Ink | 16.45 | Pass |
| Volt on Ink | 14.25 | Pass |
| Cyan on Ink | 12.65 | Pass |
| Ink on Volt | 14.25 | Pass |
| Ink on Cyan | 12.65 | Pass |
| **White on Volt** | **1.15** | **Fails — unreadable** |
| **Volt on White** | **1.15** | **Fails — unreadable** |
| **Cyan on White** | **1.30** | **Fails — unreadable** |

**The rule: the brights only ever meet ink.** Volt and Cyan carry ink type; they never carry
white type, and they never sit as type on white. This is already how the theme is configured
(`button_label` on Volt is `#1f1f21`) — the rule just makes it deliberate.

### The three greens problem

There are currently **three different greens** in the brand:

| Where | Hex | Note |
|---|---|---|
| Theme buttons | `#E3FC02` | Acid yellow-green |
| Logo monogram | `#C8D645` | Muted olive lime |
| Product hardware, as photographed | ≈ `#B4FA6E` | Physical part, lighting-dependent |

They read as three different brands in a row. **Decision needed:** pick one Wishbone green,
then bring the logo file and (where possible) the hardware finish to it. My recommendation is
to keep **Volt `#E3FC02`** as the digital brand green — it is the one customers meet most, it
is the highest-contrast of the three on ink, and it is the only one already wired into every
theme scheme — and to reissue the monogram with the `b` cut in Volt.

## 5. Typography

**Observed** — `type_header_font: oswald_n5`, `type_body_font: figtree_n5`, heading scale 140 %,
body scale 100 %, root `1rem = 10px`.

| Role | Family | Weight | Size |
|---|---|---|---|
| Display (`.h0`) | Oswald | 500 | 72.8 px |
| H1 | Oswald | 500 | 56 px desktop / 42 px mobile |
| H2 | Oswald | 500 | 33.6 px / 28 px |
| H3 | Oswald | 500 | 25.2 px |
| H4 | Oswald | 500 | 21 px |
| H5 | Oswald | 500 | 18.2 px |
| Body | Figtree | 500 | 15 px |
| Bold body | Figtree | 700 | 15 px |
| Caption / eyebrow | Figtree | 500 | 10–12 px, uppercase, tracked 0.13–0.16 rem |

**Proposed rules**

- Headings are **Oswald 500, uppercase** — condensed, tight, declarative. The brand's own
  headline *WE ARE WISHBONE* is the model.
- Body is **Figtree 500**, never lighter. Bold is 700, used for emphasis, not for subheads —
  subheads are Oswald.
- Two families, four weights, nothing else. No Oswald below 18 px; no Figtree above 24 px.
- Sentence-length headlines get sentence case; short statements get caps. Never mix inside one
  heading.

## 6. Geometry and surfaces

**Observed**, and unusually consistent — this is the strongest part of the existing system:

| Property | Value | What it means |
|---|---|---|
| Corner radius | **0** on buttons, cards, inputs, media | Everything is square |
| Variant pills | radius 40 | The single deliberate exception |
| Borders | 1 px, 55 % opacity on inputs and pills | Hairlines, never heavy rules |
| Shadows | opacity 0 everywhere | **The brand has no shadows** |
| Page width | 1600 px | Wide, generous |
| Section spacing | 52 px | |
| Grid gutters | 40 × 40 px | |
| Hover effects | none | |
| Scroll animation | reveal on scroll, on | |

**Proposed** — treat "square, hairline, flat, no shadow" as a hard rule. Any new component
that arrives with a radius, a drop shadow or a gradient is off-brand, whatever it looks like
in isolation.

## 7. Photography

**Observed**, from the EON hero: matte black product, low three-quarter angle, lit from the
side, against a dark graphite wall on a concrete floor. The green hardware accents are the only
colour in frame. Dominant tones are near-black and dark teal-grey.

**Proposed rules**

- **Dark ground, always.** Graphite, concrete, asphalt, dusk. Never a white studio sweep,
  never bright grass under midday sun.
- **The product is the hero**, shot low and close enough to read the engineering — the fold,
  the bearings, the wheel profile.
- **One colour accent per frame** — the green on the hardware. No props competing for it.
- **People** are hands and stance, not faces and lifestyle. The game, not the clubhouse.
- **Don't** — flat-lay on white, heavy filters, lens flare, stock golfers laughing.

## 8. Voice

**Observed** — short declaratives, concrete nouns, one idea per sentence. *"A full powered,
simple 'no nonsense' electric cart."* *"Focus on your game; Wishbone Golf will handle the rest."*

**Proposed**

| Do | Don't |
|---|---|
| Name the material — *aircraft-grade aluminium, sealed bearings* | Reach for *innovative, premium, game-changing* |
| Lead with what it does for the round | Lead with the company's feelings about itself |
| Say the number — 27+ holes, 799 € | Say *long-lasting*, *affordable* |
| One idea per sentence | Stack three clauses and a semicolon |
| British spelling — *aluminium*, *colour* | Mixed US/UK in the same sentence |

Note: the homepage currently says *"aluminum"* (US) inside otherwise British copy. Pick one —
given *"Birthed in Britain"*, British spelling is the consistent choice.

## 9. Where the kit lives in the theme

The kit is not a PDF that rots — every value above has an address:

| Kit section | File / setting |
|---|---|
| Colour | `theme/config/settings_data.json` → `current.color_schemes.scheme-1…5` |
| Typography | `current.type_header_font`, `type_body_font`, `heading_scale`, `body_scale` |
| Type scale | `theme/assets/base.css` (h1–h6 blocks) |
| Geometry | `current.buttons_radius`, `card_corner_radius`, `inputs_radius`, `*_shadow_opacity` |
| Logo | `current.logo`, `current.logo_width`, `current.favicon` |
| Homepage copy | `theme/templates/index.json` |

Changing a brand value means changing it there, pulling, and committing — so the kit and the
store cannot silently disagree.

## 10. Decisions for the owner

1. **Which green is *the* green?** (Recommendation: Volt `#E3FC02`, reissue the monogram to match.)
2. **Commission positive (dark-on-light) and SVG versions** of both marks?
3. **Is Cyan `#00FCED` part of the brand**, or a leftover from the Ride theme demo? It appears in
   scheme-5 but nowhere on the homepage.
4. **Spelling**: *aluminium* or *aluminum* — and fix the homepage to match.
5. **Vendor field** — one product is published under vendor *My Store*. Fix to *Wishbone*.
6. Do you want this kit extended into **templates** (social post sizes, email header, packaging
   insert, spec-sheet layout), or is the system enough?
