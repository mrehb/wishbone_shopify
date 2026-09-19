# Wishbone Golf — Brand Book

The brand book is generated, not hand-written, so it can never drift from the tokens and
components it documents.

| | |
|---|---|
| Current version | **v4.0 "Studio"** — 19 September 2026 |
| Generator | `design-system/tools/build-brandbook.py` → `/tmp/wb/kit/wishbone-brand-book.html` |
| Published | via `~/.claude/bin/artifact` (TFF command center, project *wishbone*) |
| Written kit | [`BRAND_KIT.md`](BRAND_KIT.md) — the decisions, with v3 / v2 / v1 as appendix |
| Tokens | [`tokens.css`](tokens.css) · [`tokens.json`](tokens.json) |

## Chapters

01 The brand · 02 The direction · 03 Marks · 04 Colour · 05 Type · 06 Bands and grid ·
07 The dot accent · 08 Photography · 09 Components · 10 Voice · 11 Motion · 12 Governance

## The system in one paragraph

White page, mist frames, one dark band per page. Manrope for everything — light upper-case
statement headlines, one full stop per line. DotGothic16 for the numbered eyebrow above each
headline and nowhere else. The hairline is the only line, the radius is 0, there are no shadows.
Lime `#A8FF4A` — the hardware's green — is the purchase button, once per view, and small marks;
never text on paper. Product photographs are the store's white-studio shots multiplied onto mist;
a missing photo becomes a dot silhouette. Unknown values print an em dash.

## To regenerate

```bash
cd design-system && python3 tools/build-brandbook.py && python3 tools/build-v4.py
~/.claude/bin/artifact /tmp/wb/kit/wishbone-brand-book.html --title "Wishbone Golf brand book v4.0" --project wishbone
```
