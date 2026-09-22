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

Three frames, generated 2026-09-22 on **GPT Image 2.5 (flare, max)** through the Higgsfield
connector. Each was made from the real photograph of the state it shows and checked side by side
against it. Prompts, job ids and references are in `../../tools/three-generated.json`.

| File | Shot | Made from |
|---|---|---|
| `three-boot.jpg` | 3 · boot | DSCF2332, the folded studio shot |
| `three-colourways-course.jpg` | 7 · Black / Lime and Black / White on the course | both DSCF2323s + course photo 014A2245 |
| `three-bag-stand.jpg` | 8 · stand bag | DSCF2329, the cart-bag studio shot, bag swapped |

Everything else on the page is real: studio photographs from Product Bay and frames from the
product film in `../three/`.

**Lesson from the first attempt (2026-09-20, withdrawn):** all eight shots were generated from one
unfolded photograph, so the model had to invent the fold and invented it wrong. Check Product Bay
for a real photograph of the state first; there are six angles per colourway and a 4K film.

**None of this is approved.** The store is live and nothing here has been published to it.
