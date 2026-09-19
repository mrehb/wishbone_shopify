# Tile · Board

The only container and the only layout. A page is a **Board** — a strict grid of equal columns —
and everything on it is a **Tile**: same surface, 24px radius, 24px padding, a `NN LABEL` header
in the top-left, and a one-pixel lighter top edge so it reads as an object under the lamp.

There are no other boxes. No cards inside tiles, no bordered sections, no bands, no hero that is
not a tile spanning columns. If something cannot be expressed as a tile on the board, it does not
belong on the page.

Number tiles in reading order and keep the numbers stable per page — they are addresses. A tile
whose data is live (stock, status, a running total) gets `hot`, which adds the lime dot; nothing
else on the tile may be lime except the value that matters.
