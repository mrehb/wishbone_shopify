import React from 'react';

// The single rounded element in the system (radius 40). Model and option selectors only.
export function VariantPill({ children, selected = false, unavailable = false, onClick, style }) {
  return (
    <span role="radio" aria-checked={selected} aria-disabled={unavailable} onClick={unavailable ? undefined : onClick}
      style={{
        display: 'inline-block', padding: '9px 20px', fontSize: 14,
        borderRadius: 'var(--radius-pill)',
        border: `1px solid ${selected ? 'var(--color-white)' : 'var(--color-border)'}`,
        background: selected ? 'var(--color-white)' : 'transparent',
        color: selected ? 'var(--color-ink)' : 'var(--color-white)',
        opacity: unavailable ? 0.4 : 1,
        textDecoration: unavailable ? 'line-through' : 'none',
        cursor: unavailable ? 'not-allowed' : 'pointer', userSelect: 'none', ...style,
      }}>{children}</span>
  );
}
