import React from 'react';

// One shape: a rectangle, 12px tracked caps, 14/24 padding, an arrow when it leads somewhere.
// kind: 'lime' (the purchase — one per view) | 'ink' | 'outline' | 'text'
export function Button({ kind = 'outline', arrow = false, disabled = false, children, href, onClick, style, block = false }) {
  const base = { display: block ? 'flex' : 'inline-flex', width: block ? '100%' : undefined, alignItems: 'center', justifyContent: 'center', gap: 14,
    padding: '14px 24px', border: '1px solid transparent', borderRadius: 'var(--r)', cursor: disabled ? 'default' : 'pointer',
    transition: 'background var(--t-fast) var(--ease), color var(--t-fast) var(--ease), border-color var(--t-fast) var(--ease)', ...style };
  const kinds = {
    lime: { background: 'var(--lime)', color: 'var(--on-lime)', borderColor: 'var(--lime)' },
    ink: { background: 'var(--ink)', color: '#fafafa', borderColor: 'var(--ink)' },
    outline: { background: 'transparent', color: 'inherit', borderColor: 'currentColor' },
    text: { background: 'transparent', color: 'inherit', padding: '14px 0' },
  };
  const s = { ...base, ...kinds[kind], ...(disabled ? { opacity: .38 } : null) };
  const Tag = href ? 'a' : 'button';
  return (
    <Tag className="label" href={href} onClick={disabled ? undefined : onClick} disabled={!href && disabled ? true : undefined} aria-disabled={disabled || undefined} style={s}>
      <span>{children}</span>{arrow && <span aria-hidden="true" style={{ fontWeight: 400, letterSpacing: 0 }}>→</span>}
    </Tag>
  );
}
