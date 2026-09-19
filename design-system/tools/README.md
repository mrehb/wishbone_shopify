# tools

- `build-v4.py` — renders the v4 "Studio" system as one page from the real component source, to
  `/tmp/wb/kit/wishbone-v4.html`. Publish with `~/.claude/bin/artifact`.
- `build-brandbook.py` — the brand book, one self-contained HTML, to
  `/tmp/wb/kit/wishbone-brand-book.html`.

Both read `tokens/*.css`, `components/**/*.jsx` and `guidelines/*.html`; change those, not the
outputs. Neither needs a browser; JSX is compiled in the reader's browser by @babel/standalone.
