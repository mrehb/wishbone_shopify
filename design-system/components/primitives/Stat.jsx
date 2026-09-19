import React from 'react';

// A number and what it is. Manrope 300 at 44px over a 12px label. Unknown prints — and says so.
export function Stat({ value, unit, label, note }) {
  const unknown = value == null || value === '' || value === '—';
  return (
    <div style={{ display: 'grid', gap: 8, padding: '8px 0' }}>
      <div className="num" style={{ fontSize: 'var(--fs-stat)', fontWeight: 'var(--w-display)', lineHeight: 1, letterSpacing: '-.01em' }}>
        {unknown ? '—' : value}{!unknown && unit && <span style={{ fontSize: '.5em', marginLeft: 4, color: 'var(--grey)' }}>{unit}</span>}
      </div>
      <div className="label grey">{label}</div>
      {(note || unknown) && <div className="grey" style={{ fontSize: 13 }}>{unknown ? 'not yet measured' : note}</div>}
    </div>
  );
}

// A row of stats separated by hairlines, as in the reference's 2,000+ / 520 / 248 / 1.85s line.
export function StatRow({ items = [] }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: `repeat(${items.length}, 1fr)` }}>
      {items.map((it, i) => (
        <div key={i} style={{ padding: '0 24px', borderLeft: i ? 'var(--hair-w) solid var(--hair)' : 0, textAlign: 'center' }}><Stat {...it} /></div>
      ))}
    </div>
  );
}
