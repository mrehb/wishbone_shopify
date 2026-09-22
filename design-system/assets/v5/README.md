# v5/ — brand direction assets (proposal, not approved)

Everything here is made from **real Product Bay images**. Nothing is generated.

| What | Source | How |
|---|---|---|
| `*.webp` cut-outs | Product Bay studio photos (TWO, THREE) and renders (ONE, EON, NEO) | trimmed; ONE renders separated from white by exact colour-to-alpha; EON's baked render shadow ramped out |
| `detail-*.webp` | crops of the same full-resolution files | the EON grip, the ONE badge (dot on the e), THREE hub and sleeve |
| `*-dots.svg` | dot portraits | each dot sized by the cut-out's coverage in that cell |
| `shots/` | finished product images | `tools/render-v5-shots.py` — field, light pool, floor, dot texture, Wishbone Dot name, real product, contact shadow |
| `shots/anchors.json` | callout positions | measured on each cut-out, carried through the render |

Regenerate: `python3 -m venv .venv && .venv/bin/pip install pillow pymupdf`, then
`.venv/bin/python tools/render-v5-shots.py` and `python3 tools/build-brand-v5.py`.

Wishbone Dot, the round 5×7 display face, is `tools/dotmatrix.py`.
