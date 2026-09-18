# Wishbone Golf — Design System

British golf trolleys. **"Birthed in Britain, Wishbone Golf merges exquisite design with unwavering
quality."** Operating principle, in the brand's own words: *a full powered, simple 'no nonsense' cart.*

**What this represents:** the live Shopify storefront [wishbone.golf](https://wishbone.golf)
(`k500sw-e1.myshopify.com`, theme "Wishbone" #187794981188, built on Shopify's *Ride* theme,
en-AT / EUR). Product families: manual trolleys **ONE / TWO / THREE**, electric **NEO / EON**, plus
accessories and a deep spare-parts catalogue (27 products live).

**Sources:** extracted 2026-09-19 from the live theme's `settings_data.json` and `base.css`, the
storefront's own copy, the product catalogue, and the logo PNGs in Shopify Files. No Figma file
exists. Raw extracts are in `uploads/` (`BRAND_KIT.md`, `tokens.css`, `tokens.json`, logos).
Everything here is derived from the live store, not invented — where a rule was written rather than
observed, `BRAND_KIT.md` labels it **Proposed**.

## CONTENT FUNDAMENTALS

- **Tone:** engineered, understated, British. Technical without being cold.
- **Rhythm:** state the material, state the number, stop. *"Crafted from ultra-light aircraft-grade
  aluminium."* *"27+ holes on one charge."*
- **Sentences:** short, one idea each. Concrete nouns over adjectives. **No superlatives, no
  exclamation marks, no emoji.**
- **Casing:** headings uppercase (Oswald 500). Body and button labels sentence case.
- **Naming:** models are single words in caps — **Wishbone ONE**, **Wishbone EON**, never
  "Wishbone One". The company is **Wishbone Golf**; the product family is **Wishbone**. Spare parts
  keep their `Component (MODEL)` form in full — that parenthesis is how customers find the right part.
- **Spelling:** British. The homepage currently says "aluminum" inside otherwise British copy — a
  known inconsistency, see Decisions.

## VISUAL FOUNDATIONS

- **Colour:** ink `#1f1f21` is the ground — this is a dark-first brand, not a white one. White is
  type. Volt `#e3fc02` is the only action colour. Cyan `#00fced` is a guest accent. Roughly
  70 / 20 / 10 ink / white / volt.
- **The colour rule that matters:** the brights only ever meet ink. White on volt measures **1.15:1**
  and is unreadable; cyan on white is 1.30:1. Volt and cyan always carry ink type, and never appear
  as type on white. The live theme is already wired this way.
- **Type:** two families. **Oswald 500 uppercase** headings at a 140 % scale (display 72.8px → h5
  18.2px); **Figtree 500** body at 15px, 700 for emphasis only. Captions 11px, tracked 0.16rem, caps.
  Subheads are Oswald, never bold Figtree.
- **Geometry — the signature trait: SQUARE.** Radius 0 on buttons, cards, inputs and media. Variant
  pills at radius 40 are the single deliberate exception. Borders are 1px hairlines at 55 %.
- **Shadows: none.** Every surface in the theme ships shadow opacity 0. Anything arriving with a
  radius, a drop shadow or a gradient is off-brand however good it looks in isolation.
- **Layout:** 1600px page, 52px between sections, 40 × 40px grid gutters, text left-aligned.
  Breakpoints 480 / 750 / 990 / 1400.
- **Motion:** reveal on scroll, and nothing else. The theme disables hover effects entirely — no
  lift, no scale, no image zoom.
- **Imagery:** dark ground always — graphite, concrete, asphalt, dusk. Matte black product shot low
  and close enough to read the engineering (the fold, the bearings, the wheel profile). One colour
  accent per frame: the green on the hardware. People are hands and stance, not faces. Never a white
  studio sweep, never bright grass at midday, never stock golfers laughing.

## ICONOGRAPHY & MARKS

- `assets/wishbone-wordmark.png` — 800 × 64, white on transparent, *GOLF* set vertically with a ™.
  Header use at 200px; minimum 120px on screen, 30 mm print. Clear space = the height of the W.
- `assets/wishbone-monogram.png` — 600 × 307 `wb` ligature, currently the favicon. Minimum 24px.
- Both marks are **white only**, so they live on ink, dark photography or a volt/cyan panel — never
  on white or mid-grey. **Missing: a positive (ink-on-light) version and an SVG of each.** Until those
  exist, light-background placements get improvised, which is how brands drift. FLAGGED.
- No icon set ships with the theme. If icons are needed, use a 1.5px stroke set and keep them square-
  cornered; replace with the theme's own SVGs when available.

## DECISIONS OPEN WITH THE OWNER

1. **Which green is *the* green?** Three are live: theme buttons `#e3fc02`, logo monogram `#c8d645`,
   hardware as photographed ≈`#b4fa6e`. Recommendation: standardise on volt `#e3fc02` and reissue the
   monogram to match. This system assumes volt until told otherwise.
2. **Commission positive + SVG marks.**
3. **Is cyan brand or leftover?** It sits in the theme's scheme-5 but appears nowhere on the homepage.
4. **aluminium / aluminum** — pick one and fix the homepage.
5. One product is published under vendor *My Store* instead of *Wishbone*.

## Index

- `styles.css` — global entry (imports everything below)
- `tokens/` — `colors.css`, `typography.css` (+Google Fonts), `geometry.css`, `layout.css`, `base.css`
- `assets/` — wordmark, monogram
- `guidelines/` — colour, type, brand and geometry specimen cards
- `components/core/` — Button, Input, Badge, VariantPill
- `components/commerce/` — ProductCard
- `components/chrome/` — SiteHeader, NewsletterBand, SiteFooter
- `uploads/` — the raw extraction: `BRAND_KIT.md`, tokens, logos
- `SKILL.md` — agent skill entry point

Kept in step with the storefront from `/workspace/wishbone` in the brand cell on devbox: the theme is
version-controlled at `github.com/mrehb/wishbone_shopify`, so every token here has an address in
`theme/config/settings_data.json` and the two cannot silently disagree.
