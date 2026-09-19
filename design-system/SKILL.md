---
name: wishbone-design
description: Use this skill to generate well-branded interfaces and assets for Wishbone Golf (wishbone.golf), for production or throwaway mocks. Contains the v4 "Studio" system — white bands, Manrope, one lime button, hairlines, the dot-matrix face for eyebrows only — plus logo assets, voice rules and the section library built on the real catalogue.
user-invocable: true
---

Read `readme.md` in this skill first, then explore the other files.

Wishbone v4 is a **white, product-led** system: paper and mist bands on a 1200px twelve-column
container, at most one ink band per page; **Manrope** for all type (light upper-case statement
headlines, one full stop per line); **DotGothic16 only for the numbered eyebrow**; the hairline
`#e4e4e7` as the only line; radius 0, no shadows; **lime `#a8ff4a`** as the single accent — the
purchase button once per view, small marks otherwise, never text on paper. Product photographs are
the store's white-studio shots multiplied onto mist; a missing photo becomes a dot silhouette.
Unknown values print `—`.

If creating visual artifacts, copy assets out and produce static HTML. If working on production
code, that is the Shopify theme at `github.com/mrehb/wishbone_shopify`; the store is live, so
changes reach customers only through a draft theme the owner publishes by hand.

If invoked without guidance, ask what they want to build, then act as an expert designer for this
brand.
