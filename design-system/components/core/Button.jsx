import React, { useState } from 'react';

// v2: soft-cornered, technical. Volt fill with carbon label is the only loud button.
export function Button({ variant = 'primary', size = 'md', disabled = false, onClick, style, children }) {
  const [hover, setHover] = useState(false);
  const base = {
    fontFamily: 'var(--font-display)', fontWeight: 500, fontSize: size === 'lg' ? 16 : 14,
    letterSpacing: '0.01em', padding: size === 'lg' ? '15px 30px' : '12px 22px',
    borderRadius: 'var(--radius-control)', border: '1px solid transparent', boxShadow: 'none',
    cursor: disabled ? 'default' : 'pointer', display: 'inline-flex', alignItems: 'center', gap: 8,
    opacity: disabled ? 0.35 : 1, pointerEvents: disabled ? 'none' : 'auto',
    transition: 'background var(--motion-fast), color var(--motion-fast), border-color var(--motion-fast)',
  };
  const variants = {
    primary: { background: hover ? '#eeff4a' : 'var(--color-volt)', color: 'var(--color-carbon)' },
    ghost:   { background: hover ? 'var(--surface-raised)' : 'transparent', color: 'var(--color-white)', borderColor: 'var(--color-border-strong)' },
    quiet:   { background: 'transparent', color: 'var(--text-muted)', padding: size === 'lg' ? '15px 10px' : '12px 8px' },
  };
  return (
    <button style={{ ...base, ...(variants[variant] || variants.primary), ...style }}
      disabled={disabled} onClick={onClick}
      onMouseEnter={() => setHover(true)} onMouseLeave={() => setHover(false)}>{children}</button>
  );
}
