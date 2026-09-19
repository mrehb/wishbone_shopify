import React from 'react';
import { Eyebrow } from '../primitives/Eyebrow.jsx';
import { Display } from '../primitives/Display.jsx';

// A hairline table of what the product is. Unknown rows print — and say so; they are not hidden.
export function Specs({ n = '02', eyebrow = 'Specification', lines = ['What it is.'], rows = [], box = [] }) {
  return (
    <section className="band"><div className="container grid" style={{ alignItems: 'start' }}>
      <div style={{ gridColumn: 'span 4', display: 'grid', gap: 20 }}><Eyebrow n={n}>{eyebrow}</Eyebrow><Display lines={lines} size="s" />
        {box.length > 0 && <div style={{ marginTop: 16 }}><div className="label grey" style={{ marginBottom: 10 }}>In the box</div><ul style={{ listStyle: 'none', padding: 0, display: 'grid', gap: 6, fontSize: 14 }}>{box.map((b) => <li key={b.name}><span className="grey num" style={{ display: 'inline-block', width: 32 }}>{b.qty || '1 ×'}</span>{b.name}</li>)}</ul></div>}
      </div>
      <table style={{ gridColumn: '6 / span 7', width: '100%', borderCollapse: 'collapse', fontSize: 14 }}><tbody>
        {rows.map((r) => { const unknown = r.value == null || r.value === '' || r.value === '—'; return (
          <tr key={r.label} style={{ borderBottom: 'var(--hair-w) solid var(--hair)' }}>
            <th className="label grey" style={{ textAlign: 'left', fontWeight: 'var(--w-ui)', padding: '14px 0', width: '40%' }}>{r.label}</th>
            <td style={{ padding: '14px 0' }} className="num">{unknown ? <span className="grey">— <span style={{ fontSize: 12 }}>not yet measured</span></span> : r.value}</td>
          </tr>); })}
      </tbody></table>
    </div></section>
  );
}
