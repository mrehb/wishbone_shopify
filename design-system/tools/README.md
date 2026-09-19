# tools

Generators. Each reads the real files under `design-system/` and writes one self-contained HTML
page, so nothing published can drift from the system.

| script | output | publish as |
|---|---|---|
| `build-v3.py` | the whole store as a board, rendered from the component source | *Wishbone v3 — Instrument* |
| `build-brandbook.py` | the 12-chapter brand book, set in the system | *Wishbone Golf — Brand Book v3.0* |

```bash
python3 design-system/tools/build-v3.py
python3 design-system/tools/build-brandbook.py
~/.claude/bin/artifact /tmp/wb/kit/<file>.html --title "…" --project wishbone
```

The v2 generators (`build-overview.py`, `build-library.py`) were removed with v2.
