import React, { useState } from 'react';

// Wishbone buttons: Oswald uppercase, square, no shadow, no hover transform.
// Primary is volt with INK label — the brights never carry white type.
export function Button({ variant = 'primary', size = 'md', disabled = false, onClick, style, children }) {
  const [pressed, setPressed] = useState(false);
  const base = {
    fontFamily: 'var(--font-heading)', fontWeight: 500, textTransform: 'uppercase',
    letterSpacing: '0.04em', fontSize: size === 'lg' ? 17 : 15,
    padding: size === 'lg' ? '16px 34px' : '13px 26px',
    border: 'none', borderRadius: 'var(--radius)', boxShadow: 'none',
    cursor: disabled ? 'default' : 'pointer', display: 'inline-flex', alignItems: 'center', gap: 8,
    opacity: disabled ? 0.4 : 1, pointerEvents: disabled ? 'none' : 'auto',
    transition: 'background 150ms, color 150ms',
  };
  const variants = {
    primary:   { background: pressed ? '#c9df02' : 'var(--color-volt)', color: 'var(--color-ink)' },
    secondary: { background: 'transparent', color: 'var(--color-volt)', boxShadow: 'inset 0 0 0 1px var(--color-volt)' },
    white:     { background: 'var(--color-white)', color: 'var(--color-ink)' },
    // For use ON a volt or cyan panel: invert to ink fill.
    invert:    { background: 'var(--color-ink)', color: 'var(--color-volt)' },
  };
  return (
    <button style={{ ...base, ...(variants[variant] || variants.primary), ...style }}
      disabled={disabled} onClick={onClick}
      onMouseDown={() => setPressed(true)} onMouseUp={() => setPressed(false)} onMouseLeave={() => setPressed(false)}>
      {children}
    </button>
  );
}
