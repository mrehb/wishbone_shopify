---
name: wishbone-design
description: Use this skill to generate well-branded interfaces and assets for Wishbone Golf (wishbone.golf), for production or throwaway mocks. Contains the v3 "Instrument" system — one dot-matrix typeface, one tile, one dot device, one lime accent — plus logo assets, voice rules and the tile library.
user-invocable: true
---

Read `readme.md` in this skill first, then explore the other files.

Wishbone v3 is **one of everything**: DotGothic16 for all type, the Tile as the only container on
a strict Board grid, Dots (6px/3px) as the only graphic, the Pill as the only rounded element,
ground `#0f1014` under one warm lamp, and **lime `#a8ff4a`** as the only accent — always carrying
ground-coloured text. No shadows, no red, no second typeface, no other box. Tiles are numbered in
reading order; unknown values print `—`.

If creating visual artifacts, copy assets out and produce static HTML. If working on production
code, that is the Shopify theme at `github.com/mrehb/wishbone_shopify`; the store is live, so
changes reach customers only through a draft theme the owner publishes by hand.

If invoked without guidance, ask what they want to build, then act as an expert designer for this
brand.
