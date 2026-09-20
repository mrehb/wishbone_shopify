import React, { useEffect, useRef } from 'react';

// The dot accent, reduced to one job: a product silhouette where there is no photograph yet.
// 5px dots on a 2px pitch, ink on paper, paper on the ink band; the hardware's green is lime.
export function Dots({ grid, cols, rows, hot = [], size, gap, tone = 'ink', style }) {
  const ref = useRef(null);
  useEffect(() => {
    const c = ref.current; if (!c) return;
    const css = getComputedStyle(document.documentElement);
    const S = size || parseFloat(css.getPropertyValue('--dot-size')) || 5;
    const G = gap != null ? gap : (parseFloat(css.getPropertyValue('--dot-gap')) || 2);
    const lime = css.getPropertyValue('--lime').trim() || '#cbe832';
    const rgb = tone === 'paper' ? '250,250,250' : '15,16,20';
    const step = S + G, w = cols * step - G, h = rows * step - G, dpr = window.devicePixelRatio || 1;
    c.width = w * dpr; c.height = h * dpr; c.style.width = w + 'px'; c.style.height = h + 'px';
    const x = c.getContext('2d'); x.scale(dpr, dpr); x.clearRect(0, 0, w, h);
    const isHot = typeof hot === 'function' ? hot : (i) => hot.includes(i);
    for (let i = 0; i < grid.length; i++) {
      const v = grid[i]; if (v <= 0.02) continue;
      const cx = (i % cols) * step + S / 2, cy = Math.floor(i / cols) * step + S / 2;
      x.beginPath(); x.arc(cx, cy, (S / 2) * Math.min(1, 0.35 + v * 0.65), 0, Math.PI * 2);
      x.fillStyle = isHot(i, v) ? lime : `rgba(${rgb},${(0.15 + v * 0.85).toFixed(3)})`;
      x.fill();
    }
  }, [grid, cols, rows, hot, size, gap, tone]);
  return <canvas ref={ref} aria-hidden="true" style={{ display: 'block', maxWidth: '100%', ...style }} />;
}
