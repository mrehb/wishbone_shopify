import React from 'react';

// What actually arrives. Trivial to build, disproportionately effective on a
// considered purchase — and it pre-empts half of all support contacts.
export function InTheBox({ index = '03', items = [], note, style }) {
  return (
    <section style={style}>
      <div style={{ fontFamily: 'var(--font-mono)', fontSize: 11, letterSpacing: '0.18em', textTransform: 'uppercase', color: 'var(--text-muted)' }}>
        <b style={{ color: 'var(--color-volt)', fontWeight: 400 }}>{index}</b>&nbsp;&nbsp;In the box
      </div>
      <ul style={{ listStyle: 'none', padding: 0, margin: '16px 0 0' }}>
        {items.map((it) => (
          <li key={it.name} style={{ display: 'flex', justifyContent: 'space-between', gap: 14, padding: '11px 0', borderBottom: '1px solid var(--color-border)', fontSize: 14 }}>
            <span>{it.name}</span>
            <span style={{ fontFamily: 'var(--font-mono)', color: 'var(--text-muted)', whiteSpace: 'nowrap' }}>{it.qty || '1 ×'}</span>
          </li>
        ))}
      </ul>
      {note && <p style={{ color: 'var(--text-muted)', fontSize: 13, marginTop: 12 }}>{note}</p>}
    </section>
  );
}
