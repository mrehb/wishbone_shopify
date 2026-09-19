# tools

`build-overview.py` regenerates the HTML overview of this design system — it reads the real
files (guideline card bodies, component JSX, prompt rules, the asset PNGs) and inlines them into
one self-contained page, so the overview cannot drift from what was actually pushed.

```bash
python3 design-system/tools/build-overview.py
~/.claude/bin/artifact /tmp/wb/kit/wishbone-design-system.html \
  --title "Wishbone Design System — what shipped" --project wishbone
```

The component section pulls React from unpkg at view time and degrades to a visible message if
the viewing device is offline; the guideline cards are plain HTML and always render.

`build-library.py` renders the whole component library from source — every component with real
catalogue data, the storefront audit it was designed against, and the roadmap of what is still
missing.

```bash
python3 design-system/tools/build-library.py
~/.claude/bin/artifact /tmp/wb/kit/wishbone-library.html \
  --title "Wishbone — component library" --project wishbone
```

`build-brandbook.py` generates the 12-chapter brand book the same way.
