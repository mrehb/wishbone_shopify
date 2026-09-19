import React from 'react';

// Fully round in v2 — the soft geometry means the pill is now consistent, not an exception.
export function VariantPill({ children, selected = false, unavailable = false, onClick, style }) {
  return (
    <span role="radio" aria-checked={selected} aria-disabled={unavailable} onClick={unavailable ? undefined : onClick}
      style={{
        display: 'inline-block', padding: '9px 20px', fontSize: 14, fontFamily: 'var(--font-mono)',
        letterSpacing: '0.1em', borderRadius: 'var(--radius-pill)',
        border: `1px solid ${selected ? 'var(--color-volt)' : 'var(--color-border-strong)'}`,
        background: selected ? 'var(--color-volt)' : 'transparent',
        color: selected ? 'var(--color-carbon)' : 'var(--color-white)',
        opacity: unavailable ? 0.35 : 1, textDecoration: unavailable ? 'line-through' : 'none',
        cursor: unavailable ? 'not-allowed' : 'pointer', userSelect: 'none', ...style,
      }}>{children}</span>
  );
}
