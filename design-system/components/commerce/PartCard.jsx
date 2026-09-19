import React from 'react';
import { DotMatrix } from '../core/DotMatrix.jsx';

// Spare parts are the volume of this catalogue and 15 of them have no photograph.
// Rather than a grey box, an image-less part gets a dot-matrix plate carrying its
// model compatibility — honest, on-brand, and still scannable in a grid.
function plate(seed) {
  const C = 26, R = 18, v = [];
  let s = seed;
  for (let i = 0; i < C * R; i++) {
    s = (s * 9301 + 49297) % 233280;
    const x = i % C, y = Math.floor(i / C);
    const ring = Math.abs(Math.hypot(x - C / 2, y - R / 2) - 5.5) < 1.6;
    v.push(ring ? 0.9 : (s / 233280) * 0.22);
  }
  return { values: v, cols: C, rows: R };
}

export function PartCard({ title, price, fits = [], image, soldOut = false, style }) {
  const p = plate(title.length * 977);
  return (
    <article style={{
      background: 'var(--surface-card)', border: '1px solid var(--color-border)',
      borderRadius: 'var(--radius-card)', overflow: 'hidden', opacity: soldOut ? 0.6 : 1, ...style,
    }}>
      <div style={{
        aspectRatio: '4 / 3', margin: 10, borderRadius: 'var(--radius-media)',
        background: image ? `center/cover url(${image})` : 'var(--surface-raised)',
        display: 'flex', alignItems: 'center', justifyContent: 'center', overflow: 'hidden',
      }}>
        {!image && <DotMatrix values={p.values} cols={p.cols} rows={p.rows} size={4} gap={2} />}
      </div>
      <div style={{ padding: '6px 18px 18px' }}>
        <h4 style={{ fontFamily: 'var(--font-display)', fontWeight: 500, fontSize: 15.5, margin: 0, lineHeight: 1.3 }}>{title}</h4>
        <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap', margin: '10px 0 12px' }}>
          {fits.map((f) => (
            <span key={f} style={{
              fontFamily: 'var(--font-mono)', fontSize: 10, letterSpacing: '0.14em',
              padding: '3px 8px', borderRadius: 'var(--radius-chip)',
              border: '1px solid var(--color-border-strong)', color: 'var(--text-muted)',
            }}>{f}</span>
          ))}
        </div>
        <div style={{ fontFamily: 'var(--font-mono)', fontSize: 16 }}>{soldOut ? 'Sold out' : price}</div>
      </div>
    </article>
  );
}
