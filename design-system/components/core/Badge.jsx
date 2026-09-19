import React from 'react';

const kinds = {
  live:    { label: 'Live',       fg: 'var(--color-volt)',  dot: true,  border: 'var(--color-border)' },
  best:    { label: 'Best seller', fg: 'var(--color-carbon)', bg: 'var(--color-volt)' },
  soldout: { label: 'Sold out',   fg: 'var(--text-muted)',  border: 'var(--color-border)' },
  spare:   { label: 'Spare part', fg: 'var(--color-white)', border: 'var(--color-border-strong)' },
};

// v2: mono caps chip. Only "best" is a fill — everything else is a hairline.
export function Badge({ kind = 'best', children, style }) {
  const k = kinds[kind] || kinds.best;
  return (
    <span style={{
      display: 'inline-flex', alignItems: 'center', gap: 7,
      background: k.bg || 'transparent', color: k.fg,
      border: `1px solid ${k.bg ? 'transparent' : k.border}`,
      fontFamily: 'var(--font-mono)', fontSize: 11, letterSpacing: '0.16em', textTransform: 'uppercase',
      padding: '5px 11px', borderRadius: 'var(--radius-chip)', ...style,
    }}>
      {k.dot && <i style={{ width: 6, height: 6, borderRadius: '50%', background: 'var(--color-volt)' }} />}
      {children || k.label}
    </span>
  );
}
