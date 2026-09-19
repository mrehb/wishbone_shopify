---
name: wishbone-design
description: Use this skill to generate well-branded interfaces and assets for Wishbone Golf (wishbone.golf), either for production or throwaway prototypes/mocks. Contains the v2 "Telemetry" brand system — carbon ground, volt accent, dot-matrix data device, Space Grotesk/Figtree/Share Tech Mono — plus logo assets, voice rules and UI kit components.
user-invocable: true
---

Read `readme.md` in this skill first, then explore the other files.

Wishbone v2 is **instrumentation on carbon**: `#0f1014` ground with a warm top-left wash, volt
`#e3fc02` as the single accent (always carrying carbon type — white on volt is unreadable at
1.15:1), soft geometry (20px cards, 10px controls), and **no shadows**. Three faces: Space Grotesk
says what a thing is, Figtree explains it, Share Tech Mono reports a value. The signature device is
the **dot matrix** — quantities, charts and product silhouettes drawn as dot grids. Panels are
numbered 01, 02, 03. If a value is unknown, print `—`; never invent a spec.

If creating visual artifacts (slides, mocks, throwaway prototypes), copy assets out and produce
static HTML. If working on production code, that production code is the Shopify theme at
`github.com/mrehb/wishbone_shopify` — read the rules here and match `theme/config/settings_data.json`.

If invoked without guidance, ask what they want to build, then act as an expert designer for this
brand. Note for anything customer-facing: the store is live and selling, so changes reach customers
only through a draft theme the owner publishes by hand.
