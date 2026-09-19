import React, { useState } from 'react';
import { Tile } from '../primitives/Tile.jsx';

export function FaqTile({ n, label = 'Questions', items = [], span = 2 }) {
  const [open, setOpen] = useState(0);
  return (
    <Tile n={n} label={label} span={span}>
      <div>{items.map((it, i) => { const on = open === i; return (
        <div key={it.q} style={{ borderBottom: '1px solid var(--tile-line)' }}>
          <button onClick={() => setOpen(on ? -1 : i)} aria-expanded={on} style={{
            width: '100%', textAlign: 'left', background: 'none', border: 0, cursor: 'pointer', padding: '14px 0',
            display: 'flex', justifyContent: 'space-between', gap: 16, fontFamily: 'var(--font)', fontSize: 'var(--fs-lead)', color: 'var(--white)' }}>
            {it.q}<span className="lime">{on ? '−' : '+'}</span>
          </button>
          {on && <p className="grey" style={{ paddingBottom: 16, maxWidth: '60ch' }}>{it.a}</p>}
        </div>); })}
      </div>
    </Tile>
  );
}
