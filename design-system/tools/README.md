# tools

- `build-v4.py` — renders the v4 "Studio" system as one page from the real component source, to
  `/tmp/wb/kit/wishbone-v4.html`. Publish with `~/.claude/bin/artifact`.
- `build-brandbook.py` — the brand book, one self-contained HTML, to
  `/tmp/wb/kit/wishbone-brand-book.html`.

- `build-three-page.py` — the Wishbone CUBE three product landing page, built from the real
  Product Bay record (product 9054916) and the six course photographs, to
  `/tmp/wb/kit/wishbone-cube-three.html`. It reads six derived detail crops from
  `/tmp/wb/pb/details_b64.json` (regenerate those from the 2048px studio PNG if the
  photography changes) and embeds them; everything else is referenced from the Product Bay CDN.

All three read `tokens/*.css`, `components/**/*.jsx` and `guidelines/*.html`; change those, not the
outputs. Neither needs a browser; JSX is compiled in the reader's browser by @babel/standalone.
