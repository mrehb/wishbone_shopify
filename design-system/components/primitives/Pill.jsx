import React, { useState } from 'react';

// The one rounded element. Buttons, tags, status chips and selectors are all this,
// distinguished by kind — never by a different shape.
export function Pill({ kind = 'button', on = false, hot = false, disabled = false, onClick, children, style }) {
  const [hover, setHover] = useState(false);
  const base = {
    display: 'inline-flex', alignItems: 'center', gap: 8, fontFamily: 'var(--font)', fontSize: 'var(--fs-label)',
    letterSpacing: 'var(--track-label)', textTransform: 'uppercase', lineHeight: 1,
    borderRadius: 'var(--r-pill)', border: '1px solid transparent', cursor: onClick && !disabled ? 'pointer' : 'default',
    opacity: disabled ? 0.35 : 1, pointerEvents: disabled ? 'none' : 'auto', userSelect: 'none', whiteSpace: 'nowrap',
    transition: 'background var(--t-fast), color var(--t-fast), border-color var(--t-fast)',
  };
  const kinds = {
    button: { padding: '14px 22px', fontSize: 'var(--fs-body)', letterSpacing: '0.04em', textTransform: 'none',
              background: hover ? '#c2ff7a' : 'var(--lime)', color: 'var(--on-lime)' },
    ghost:  { padding: '14px 22px', fontSize: 'var(--fs-body)', letterSpacing: '0.04em', textTransform: 'none',
              background: hover ? 'rgb(255 255 255 / .06)' : 'transparent', color: 'var(--white)', borderColor: 'rgb(255 255 255 / .28)' },
    tag:    { padding: '7px 12px', color: 'var(--grey)', borderColor: 'var(--tile-line)' },
    status: { padding: '7px 12px', color: 'var(--white)', borderColor: 'var(--tile-line)' },
    select: { padding: '9px 16px', fontSize: 'var(--fs-body)', letterSpacing: '0.06em',
              background: on ? 'var(--white)' : 'transparent', color: on ? 'var(--ground)' : 'var(--white)',
              borderColor: on ? 'var(--white)' : 'rgb(255 255 255 / .28)' },
  };
  return (
    <span role={kind === 'select' ? 'radio' : kind === 'button' || kind === 'ghost' ? 'button' : undefined}
      aria-checked={kind === 'select' ? on : undefined} aria-disabled={disabled}
      onClick={disabled ? undefined : onClick} onMouseEnter={() => setHover(true)} onMouseLeave={() => setHover(false)}
      style={{ ...base, ...kinds[kind], ...style }}>
      {(hot || kind === 'status') && <i style={{ width: 6, height: 6, borderRadius: '50%', background: hot ? 'var(--lime)' : 'var(--grey)' }} />}
      {children}
    </span>
  );
}
