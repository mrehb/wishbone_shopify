import React from 'react';

// A model tag: `NEO`, `ONE & NEO`, `ALL`. Hairline box, 12px caps. `on` fills it lime.
export function Tag({ children, on = false, style }) {
  return <span className="label" style={{ display: 'inline-block', padding: '5px 8px', border: `1px solid ${on ? 'var(--lime)' : 'var(--hair)'}`, background: on ? 'var(--lime)' : 'transparent', color: on ? 'var(--on-lime)' : 'inherit', lineHeight: 1, ...style }}>{children}</span>;
}
