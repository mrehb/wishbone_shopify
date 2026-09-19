import React from 'react';

// Money, the store's way: 799,00 € — comma decimal, space, euro sign. `from` prefixes "From".
export function Price({ value, from = false, compare, size = 'var(--fs-lead)', style }) {
  const unknown = value == null || value === '' || value === '—';
  return (
    <span className="num" style={{ fontSize: size, fontWeight: 'var(--w-strong)', ...style }}>
      {from && !unknown && <span className="label grey" style={{ marginRight: 8, fontWeight: 'var(--w-ui)' }}>from</span>}
      {unknown ? '—' : value}
      {compare && !unknown && <span className="grey" style={{ textDecoration: 'line-through', fontWeight: 'var(--w-body)', marginLeft: 10, fontSize: '.8em' }}>{compare}</span>}
    </span>
  );
}
