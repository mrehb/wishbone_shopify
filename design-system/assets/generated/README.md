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
