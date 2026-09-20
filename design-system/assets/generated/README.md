# generated/

AI-generated product imagery for pages the photography does not cover yet.

Rules, so a generated frame is never mistaken for a photograph:
- **Reference the real studio PNG** for geometry, proportion and colourway on every generation.
  The trolley is a real object; its frame, wheel count and colour are not open to interpretation.
- **Never generate a spec.** If a frame implies a dimension, a weight or a material, it must match
  `tools/three-assets.json`.
- **Name the file for its shot**, e.g. `three-fold-03.png`, and record it in
  `tools/three-generated.json` so `tools/build-three-page.py` picks it up.
- **Keep a provenance line** in `tools/three-generated.json`: the model, the date and the prompt.
- Anything going to a customer-facing page needs the owner's sign-off first. The store is live.

## What is here

Fifteen frames, generated 2026-09-20 on **GPT Image 2.5** through the Higgsfield connector,
every one conditioned on the real studio PNG. Prompts, job ids and references are in
`../../tools/three-generated.json`.

| Files | Shot |
|---|---|
| `three-fold-01…05.jpg` | 1 · the fold, as a sequence |
| `three-cube-hero.jpg` (+ `three-cube-alt-01/02.jpg`) | 2 · the folded cube |
| `three-boot.jpg` | 3 · boot |
| `three-organizer.jpg` | 4 · Smart Organizer, top-down |
| `three-wheel-off.jpg` | 5 · wheel off |
| `three-footbrake.jpg` | 6 · footbrake |
| `three-colourways-course.jpg` | 7 · Black / Lime and Black / White on the course |
| `three-bag-stand.jpg`, `three-bag-cart.jpg` | 8 · bag compatibility, a crossfade pair |

The two `-alt-` cubes are the other two takes of shot 2, kept so the owner can pick a different
hero. They are not placed on the page.

**None of this is approved.** The store is live and nothing here has been published to it.
