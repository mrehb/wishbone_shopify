import React, { useState } from 'react';

// FAQ, shipping, warranty, fitting instructions. The store has none of these today —
// and a repairable product generates exactly these questions.
export function Accordion({ items = [], index = '04', title = 'Questions', style }) {
  const [open, setOpen] = useState(0);
  return (
    <section style={style}>
      <div style={{ fontFamily: 'var(--font-mono)', fontSize: 11, letterSpacing: '0.18em', textTransform: 'uppercase', color: 'var(--text-muted)' }}>
        <b style={{ color: 'var(--color-volt)', fontWeight: 400 }}>{index}</b>&nbsp;&nbsp;{title}
      </div>
      <div style={{ marginTop: 16 }}>
        {items.map((it, i) => {
          const isOpen = open === i;
          return (
            <div key={it.q} style={{ borderBottom: '1px solid var(--color-border)' }}>
              <button onClick={() => setOpen(isOpen ? -1 : i)} aria-expanded={isOpen}
                style={{
                  width: '100%', textAlign: 'left', background: 'none', border: 0, cursor: 'pointer',
                  padding: '17px 0', display: 'flex', justifyContent: 'space-between', gap: 16, alignItems: 'baseline',
                  fontFamily: 'var(--font-display)', fontWeight: 500, fontSize: 17, color: 'var(--color-white)',
                }}>
                {it.q}
                <span style={{ fontFamily: 'var(--font-mono)', color: 'var(--color-volt)', fontSize: 18, lineHeight: 1 }}>{isOpen ? '−' : '+'}</span>
              </button>
              {isOpen && (
                <div style={{ paddingBottom: 18, maxWidth: '68ch', color: 'var(--text-muted)', fontSize: 14.5 }}>{it.a}</div>
              )}
            </div>
          );
        })}
      </div>
    </section>
  );
}
