import React from 'react';
import { DotMatrix } from '../core/DotMatrix.jsx';

// Five models as five dotted silhouettes: the clearest possible answer to
// "what does Wishbone make?" — and it needs no photography to ship.
function silhouette(seed, electric) {
  const C = 30, R = 20, v = [], acc = [];
  for (let y = 0; y < R; y++) {
    for (let x = 0; x < C; x++) {
      const i = y * C + x;
      const wheel = Math.abs(Math.hypot(x - 7, y - 14) - 4) < 1.2 || Math.abs(Math.hypot(x - 24, y - 14) - 4) < 1.2;
      const frame = (y > 5 && y < 7 && x > 6 && x < 25) || (Math.abs((x - 7) * 0.5 - (y - 14)) < 0.7 && x > 6 && x < 17);
      const handle = Math.abs(x - 24) < 0.9 && y > 2 && y < 7;
      const motor = electric && Math.hypot(x - 15, y - 15) < 2.2;
      const on = wheel || frame || handle || motor;
      v.push(on ? 1 : 0);
      if (on && motor) acc.push(i);
    }
  }
  return { values: v, cols: C, rows: R, accent: acc };
}

export function RangeStrip({ models = [], style }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: `repeat(${models.length}, minmax(0,1fr))`, gap: 'var(--grid-gap)', ...style }}>
      {models.map((m, i) => {
        const s = silhouette(i, m.electric);
        return (
          <a key={m.id} href={m.href || '#'} style={{
            textDecoration: 'none', color: 'inherit', background: 'var(--surface-card)',
            border: '1px solid var(--color-border)', borderRadius: 'var(--radius-card)', padding: '18px 16px',
            display: 'flex', flexDirection: 'column', gap: 12,
          }}>
            <DotMatrix values={s.values} cols={s.cols} rows={s.rows} accent={s.accent} size={4} gap={2} />
            <div>
              <div style={{ fontFamily: 'var(--font-display)', fontWeight: 500, fontSize: 17 }}>{m.id}</div>
              <div style={{ fontFamily: 'var(--font-mono)', fontSize: 10.5, letterSpacing: '0.14em', textTransform: 'uppercase', color: 'var(--text-muted)', marginTop: 5 }}>
                {m.electric ? 'Electric' : 'Manual'}
              </div>
              <div style={{ fontFamily: 'var(--font-mono)', fontSize: 14, marginTop: 8, color: m.price ? 'var(--color-white)' : 'var(--text-muted)' }}>{m.price || '—'}</div>
            </div>
          </a>
        );
      })}
    </div>
  );
}
