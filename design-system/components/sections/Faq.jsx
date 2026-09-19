import React, { useState } from 'react';
import { Eyebrow } from '../primitives/Eyebrow.jsx';
import { Display } from '../primitives/Display.jsx';

// Questions as hairline rows; one open at a time; the marker is a + that turns into a −.
export function Faq({ n = '05', eyebrow = 'Questions', lines = ['Asked often.'], items = [] }) {
  const [open, setOpen] = useState(0);
  return (
    <section className="band"><div className="container grid" style={{ alignItems: 'start' }}>
      <div style={{ gridColumn: 'span 4', display: 'grid', gap: 20 }}><Eyebrow n={n}>{eyebrow}</Eyebrow><Display lines={lines} size="s" /></div>
      <div style={{ gridColumn: '6 / span 7', borderTop: 'var(--hair-w) solid var(--hair)' }}>
        {items.map((it, i) => (
          <div key={i} style={{ borderBottom: 'var(--hair-w) solid var(--hair)' }}>
            <button onClick={() => setOpen(open === i ? -1 : i)} aria-expanded={open === i} style={{ width: '100%', display: 'flex', justifyContent: 'space-between', gap: 24, padding: '18px 0', background: 'none', border: 0, textAlign: 'left', cursor: 'pointer', fontSize: 'var(--fs-lead)', fontWeight: 'var(--w-body)' }}>
              <span>{it.q}</span><span aria-hidden="true" style={{ fontWeight: 300, fontSize: 22, lineHeight: 1 }}>{open === i ? '−' : '+'}</span>
            </button>
            {open === i && <p className="grey" style={{ padding: '0 0 20px', maxWidth: '60ch' }}>{it.a}</p>}
          </div>
        ))}
      </div>
    </div></section>
  );
}
