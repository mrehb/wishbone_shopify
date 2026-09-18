---
name: wishbone-design
description: Use this skill to generate well-branded interfaces and assets for Wishbone Golf (wishbone.golf), either for production or throwaway prototypes/mocks. Contains the brand's colours, type, geometry, logo assets, voice rules and UI kit components, all derived from the live Shopify store.
user-invocable: true
---

Read `readme.md` in this skill first, then explore the other files.

Wishbone is **dark-first**: ink `#1f1f21` is the ground, volt `#e3fc02` is the only action colour,
and the brights carry ink type only — white on volt is unreadable (1.15:1). Geometry is square
(radius 0, pills at 40 the one exception), borders are hairlines, and **nothing casts a shadow**.
Type is Oswald 500 uppercase headings over Figtree 500 body.

If creating visual artifacts (slides, mocks, throwaway prototypes), copy assets out and produce
static HTML. If working on production code, that production code is the Shopify theme at
`github.com/mrehb/wishbone_shopify` — read the rules here and match `theme/config/settings_data.json`.

If invoked without guidance, ask what they want to build, then act as an expert designer for this
brand. Note for anything customer-facing: the store is live and selling, so changes reach customers
only through a draft theme the owner publishes by hand.
