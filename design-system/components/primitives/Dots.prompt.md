# Dots

The only way anything graphic is drawn. Charts, gauges, silhouettes, progress, icons — all a grid
of 6px dots on a 3px gap. White for the signal, grey-dim for the empty grid, **lime for the one
value that matters**. There are no SVG icons, no images-as-graphics, no illustrations.

Generators cover the recurring cases: `bars` for quantities, `ring` for a percentage, `line` for
a trend, `steps` for progress, `wave` for a hero pulse. Product silhouettes are a grid sampled
from the real photograph's luminance — never hand-drawn.

Never scale the pitch to fit: if a grid does not fit, use fewer columns. Never use dots as a
background pattern — a dot grid always means *this is data*.
