import React from 'react';

const kinds = {
  bestseller: { label: 'Best seller', bg: 'var(--color-volt)', fg: 'var(--color-ink)' },
  new:        { label: 'New',         bg: 'var(--color-cyan)', fg: 'var(--color-ink)' },
  soldout:    { label: 'Sold out',    bg: 'transparent',       fg: 'var(--text-muted)', border: '1px solid var(--color-border-soft)' },
  spare:      { label: 'Spare part',  bg: 'transparent',       fg: 'var(--color-white)', border: '1px solid var(--color-border)' },
};

export function Badge({ kind = 'bestseller', children, style }) {
  const k = kinds[kind] || kinds.bestseller;
  return (
    <span style={{
      display: 'inline-block', background: k.bg, color: k.fg, border: k.border || 'none',
      fontSize: 11, letterSpacing: '0.16rem', textTransform: 'uppercase',
      padding: '5px 10px', borderRadius: 'var(--radius)', ...style,
    }}>{children || k.label}</span>
  );
}
