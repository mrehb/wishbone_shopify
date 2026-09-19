import React from 'react';

// The headline. Light Manrope, upper case, one full stop per line. `lines` is an array so the
// breaks are the author's, not the browser's. size: 'hero' | 'display' | 's'.
export function Display({ lines = [], size = 'display', as = 'h2', style }) {
  const Tag = as;
  const cls = 'display' + (size === 'hero' ? ' display--hero' : size === 's' ? ' display--s' : '');
  return <Tag className={cls} style={style}>{lines.map((l, i) => <span key={i} style={{ display: 'block' }}>{l}</span>)}</Tag>;
}
