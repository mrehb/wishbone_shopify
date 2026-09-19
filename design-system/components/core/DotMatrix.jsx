import React, { useEffect, useRef } from 'react';

// THE signature device of v2. Any value, silhouette or chart is drawn as a dot grid:
// data reads as instrumentation rather than decoration.
//
// values: numbers 0..1, row-major, length = cols * rows
// accent: indices (or a predicate) drawn in volt instead of white
export function DotMatrix({ values, cols, rows, accent = [], size = 5, gap = 3, style }) {
  const ref = useRef(null);
  const accentSet = Array.isArray(accent) ? new Set(accent) : accent;
  useEffect(() => {
    const c = ref.current; if (!c) return;
    const step = size + gap;
    const dpr = window.devicePixelRatio || 1;
    const w = cols * step, h = rows * step;
    c.width = w * dpr; c.height = h * dpr; c.style.width = w + 'px'; c.style.height = h + 'px';
    const ctx = c.getContext('2d'); ctx.scale(dpr, dpr); ctx.clearRect(0, 0, w, h);
    const css = getComputedStyle(document.documentElement);
    const volt = css.getPropertyValue('--color-volt').trim() || '#e3fc02';
    for (let i = 0; i < values.length; i++) {
      const v = values[i]; if (v <= 0.05) continue;
      const x = (i % cols) * step + size / 2, y = Math.floor(i / cols) * step + size / 2;
      const isAccent = typeof accentSet === 'function' ? accentSet(i, v) : accentSet.has(i);
      ctx.beginPath(); ctx.arc(x, y, Math.max(v * (size / 2), 0.4), 0, Math.PI * 2);
      ctx.fillStyle = isAccent ? volt : `rgba(250,250,250,${(0.18 + v * 0.74).toFixed(3)})`;
      ctx.fill();
    }
  }, [values, cols, rows, size, gap, accent]);
  return <canvas ref={ref} style={{ display: 'block', maxWidth: '100%', ...style }} />;
}

// Convenience: a horizontal dot bar chart. levels are 0..1, one per column.
export function DotBars({ levels, height = 8, accentAbove = 0.8, size = 5, gap = 3, style }) {
  const cols = levels.length, rows = height;
  const values = [], accent = [];
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const filled = (rows - r) / rows <= levels[c];
      const i = r * cols + c;
      values.push(filled ? 1 : 0.18);
      if (filled && levels[c] >= accentAbove && (rows - r) / rows > accentAbove - 0.2) accent.push(i);
    }
  }
  return <DotMatrix values={values} cols={cols} rows={rows} accent={accent} size={size} gap={gap} style={style} />;
}
