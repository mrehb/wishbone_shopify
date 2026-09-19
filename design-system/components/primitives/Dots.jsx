import React, { useEffect, useRef } from 'react';

// THE graphic device. Every chart, silhouette, icon, progress state and divider in the
// system is a grid of dots on a 6/3 pitch. Nothing is drawn any other way.
export function Dots({ grid, cols, rows, hot = [], size, gap, style }) {
  const ref = useRef(null);
  useEffect(() => {
    const c = ref.current; if (!c) return;
    const css = getComputedStyle(document.documentElement);
    const S = size || parseFloat(css.getPropertyValue('--dot')) || 6;
    const G = gap != null ? gap : (parseFloat(css.getPropertyValue('--gap')) || 3);
    const lime = css.getPropertyValue('--lime').trim() || '#a8ff4a';
    const step = S + G, w = cols * step - G, h = rows * step - G, dpr = window.devicePixelRatio || 1;
    c.width = w * dpr; c.height = h * dpr; c.style.width = w + 'px'; c.style.height = h + 'px';
    const x = c.getContext('2d'); x.scale(dpr, dpr); x.clearRect(0, 0, w, h);
    const isHot = typeof hot === 'function' ? hot : (i) => hot.includes ? hot.includes(i) : hot.has(i);
    for (let i = 0; i < grid.length; i++) {
      const v = grid[i]; if (v <= 0) continue;
      const cx = (i % cols) * step + S / 2, cy = Math.floor(i / cols) * step + S / 2;
      x.beginPath(); x.arc(cx, cy, S / 2, 0, Math.PI * 2);
      x.fillStyle = isHot(i, v) ? lime : (v >= 0.99 ? 'rgba(250,250,250,1)' : `rgba(250,250,250,${(0.22 + v * 0.78).toFixed(3)})`);
      x.fill();
    }
  }, [grid, cols, rows, hot, size, gap]);
  return <canvas ref={ref} style={{ display: 'block', maxWidth: '100%', ...style }} />;
}

// ---- generators: each returns { grid, cols, rows, hot } ready for <Dots {...} /> ----

// Vertical bars. levels 0..1 per column; the top of any column >= hotAbove is lime.
export function bars(levels, rows = 8, hotAbove = 1.01) {
  const cols = levels.length, grid = [], hot = [];
  for (let r = 0; r < rows; r++) for (let c = 0; c < cols; c++) {
    const filled = (rows - r) / rows <= levels[c] + 1e-9;
    grid.push(filled ? 1 : 0.18);
    if (filled && levels[c] >= hotAbove && r === Math.round(rows - levels[c] * rows)) hot.push(r * cols + c);
  }
  return { grid, cols, rows, hot };
}

// A ring gauge. pct 0..1 of the circumference is lit; the lit arc is lime.
export function ring(pct, radius = 7) {
  const cols = radius * 2 + 1, rows = cols, grid = [], hot = [];
  for (let r = 0; r < rows; r++) for (let c = 0; c < cols; c++) {
    const dx = c - radius, dy = r - radius, d = Math.hypot(dx, dy);
    const on = Math.abs(d - radius) < 0.7;
    grid.push(on ? 1 : 0);
    if (on) { const a = (Math.atan2(dy, dx) + Math.PI / 2 + Math.PI * 2) % (Math.PI * 2); if (a / (Math.PI * 2) <= pct) hot.push(r * cols + c); }
  }
  return { grid, cols, rows, hot };
}

// A signal line. points 0..1, one per column; drawn as a 1-dot-thick trace with a lime peak.
export function line(points, rows = 10) {
  const cols = points.length, grid = new Array(cols * rows).fill(0), hot = [];
  let peak = 0; points.forEach((p, i) => { if (p > points[peak]) peak = i; });
  points.forEach((p, c) => {
    const r = Math.round((1 - p) * (rows - 1)); grid[r * cols + c] = 1;
    if (c === peak) hot.push(r * cols + c);
  });
  return { grid, cols, rows, hot };
}

// A waveform band, decorative-only for hero tiles: symmetric around the centre row.
export function wave(cols = 40, rows = 9, phase = 0) {
  const grid = [], hot = [];
  for (let r = 0; r < rows; r++) for (let c = 0; c < cols; c++) {
    const amp = (Math.sin(c / 3.1 + phase) * 0.5 + 0.5) * (rows / 2);
    const on = Math.abs(r - (rows - 1) / 2) <= amp;
    grid.push(on ? 0.35 + 0.65 * (1 - Math.abs(r - (rows - 1) / 2) / (rows / 2)) : 0);
  }
  return { grid, cols, rows, hot };
}

// A checklist step: n steps, k done. Done steps are lime.
export function steps(n, k) {
  const cols = n * 4 - 3, rows = 1, grid = new Array(cols).fill(0.22), hot = [];
  for (let i = 0; i < n; i++) { grid[i * 4] = 1; if (i < k) hot.push(i * 4); }
  return { grid, cols, rows, hot };
}
