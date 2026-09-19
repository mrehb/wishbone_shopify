import React from 'react';

// Three or four facts, stated as values. Not badges, not guarantees, not icons —
// the brand's credibility comes from numbers it can prove.
export function TrustRow({ items = [], style }) {
  return (
    <div style={{
      display: 'grid', gridTemplateColumns: `repeat(auto-fit,minmax(170px,1fr))`, gap: 'var(--grid-gap)',
      borderTop: '1px solid var(--color-border)', borderBottom: '1px solid var(--color-border)',
      padding: '22px 0', ...style,
    }}>
      {items.map((it) => (
        <div key={it.label}>
          <div style={{ fontFamily: 'var(--font-mono)', fontSize: 10.5, letterSpacing: '0.16em', textTransform: 'uppercase', color: 'var(--text-muted)' }}>{it.label}</div>
          <div style={{ fontFamily: 'var(--font-mono)', fontSize: 21, marginTop: 7, color: it.value === '—' ? 'var(--text-muted)' : 'var(--color-white)' }}>{it.value}</div>
          {it.note && <div style={{ fontSize: 13, color: 'var(--text-muted)', marginTop: 5 }}>{it.note}</div>}
        </div>
      ))}
    </div>
  );
}
