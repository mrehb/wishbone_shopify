# Wishbone Golf — Brand Book v2.0 "Telemetry"

The full guideline is an HTML document generated from the live design system:
**`design-system/tools/build-brandbook.py`** → publish with `~/.claude/bin/artifact`.

It is generated rather than written once, so the book and the components cannot drift apart.
Regenerate after any token change:

```bash
python3 design-system/tools/build-brandbook.py
~/.claude/bin/artifact /tmp/wb/kit/wishbone-brand-book.html \
  --title "Wishbone Golf — Brand Book v2.0" --project wishbone
```

## Chapters

| # | Chapter | Covers |
|---|---------|--------|
| 01 | The brand | Statement, three pillars, architecture, the range, audience |
| 02 | Verbal identity | Voice principles, do/don't, house style, microcopy library |
| 03 | The marks | Wordmark and monogram specs, clear space, misuse, placement, what to commission |
| 04 | Colour | Palette with RGB, proportion, contrast table, states, colour off-screen |
| 05 | Typography | The three faces, licensing, specimens, scale, hierarchy, rules, fallbacks, Shopify mapping |
| 06 | Layout, grid & surfaces | Page, spacing scale, radius, panel anatomy |
| 07 | The dot matrix | Specification, how a silhouette is made, where it may and may not be used |
| 08 | Iconography | Stroke spec, minimum set to commission, interim rule |
| 09 | Photography & light | Lighting recipe, shot list, do/don't |
| 10 | Motion | Duration tokens, allowed and forbidden, reduced-motion |
| 11 | Applications | Storefront, product page, email, social, print and physical |
| 12 | Governance | Where things live, how to change them, versions, open items |

## The parts worth having in text

### Typefaces and licensing

| Face | Role | Designer | Licence |
|---|---|---|---|
| **Space Grotesk** 400/500/700 | Display — names a thing | Florian Karsten | SIL OFL 1.1 (Google Fonts) |
| **Figtree** 400/500/700 + italic | Body — explains it | Erik Kennedy | SIL OFL 1.1 (Google Fonts) |
| **Share Tech Mono** | Telemetry — reports a value | Carrois Apostrophe | SIL OFL 1.1 (Google Fonts) |

All three are open-licence: free for commercial use, self-hosting, PDF embedding, packaging and
signage. No per-seat cost. **Before a print or packaging run**, send the supplier the actual font
files plus the licence text, and re-confirm the licence on the family's page at handoff time.

The wordmark's letterforms are a bespoke logotype, not one of these three. It stays an image asset
and is never re-typeset.

### Iconography — none exists yet

Stroke only, **1.5px at 24px**, butt caps, mitre joins, 24×24 grid with 2px margin, 2px corner
radius, white at 92 % (volt only when the icon *is* the accent). Interim: one open-source 1.5px
stroke set used consistently — never two sources mixed. Never emoji or unicode glyphs as icons.

### Motion

`--motion-fast` 180ms (hover, focus) · `--motion` 320ms (panels, drawers) · `--motion-slow` 600ms
(reveal, hero) · `--ease` `cubic-bezier(.16,.84,.44,1)`. Forbidden: hover lift or scale, parallax,
auto-carousels, bounce easing, anything looping near the buy button. All motion must respect
`prefers-reduced-motion: reduce`.

### Print

Carbon prints as a 4-colour rich black, never 100 K. **Volt is outside CMYK gamut — specify a
fluorescent/bright spot ink and get a physical proof**; a process approximation reads as dull lime.
The hardware green (≈`#B4FA6E` as photographed) is never retouched toward volt.

## Open items

1. **Fold size and weight** missing from the catalogue — panels print `—` until measured.
2. **Positive (dark-on-light) and SVG versions of both marks** to commission.
3. **Icon set** to the spec above, or a documented decision to stay on an open-source set.
4. **Spot-ink proof for volt** before any print run.
5. "aluminum" → "aluminium" on the homepage.
6. One product still published under vendor *My Store*.
7. Trademark status — the wordmark shows ™; is it registered?
8. **Theme migration** — the storefront still runs v1 in full.

See [`BRAND_KIT.md`](BRAND_KIT.md) for the decisions and the evidence behind them.
