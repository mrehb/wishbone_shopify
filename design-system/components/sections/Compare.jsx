import React from 'react';
import { Eyebrow } from '../primitives/Eyebrow.jsx';
import { Display } from '../primitives/Display.jsx';
import { Photo } from '../primitives/Silhouette.jsx';
import { Price } from '../primitives/Price.jsx';
import { Button } from '../primitives/Button.jsx';

// All five models side by side. The highlighted column carries a 2px lime rule at the top.
export function Compare({ n = '03', eyebrow = 'Compare', lines = ['Five trolleys.', 'One frame idea.'], models = [], rows = [], highlight }) {
  return (
    <section className="band band--mist"><div className="container" style={{ display: 'grid', gap: 40 }}>
      <div style={{ display: 'grid', gap: 20 }}><Eyebrow n={n}>{eyebrow}</Eyebrow><Display lines={lines} /></div>
      <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 14 }}>
        <thead><tr>
          <th style={{ width: '16%' }} />
          {models.map((m) => <th key={m.id} style={{ padding: '0 12px 16px', borderTop: `2px solid ${m.id === highlight ? 'var(--lime)' : 'transparent'}`, textAlign: 'left', fontWeight: 400 }}>
            <Photo src={m.src} model={m.id} ratio={1} style={{ background: 'transparent', marginBottom: 12 }} />
            <div className="label">{m.id}</div><div className="grey" style={{ fontSize: 13 }}>{m.type}</div><Price value={m.price} from size="14px" style={{ display: 'block', marginTop: 6 }} />
          </th>)}
        </tr></thead>
        <tbody>{rows.map((r) => (
          <tr key={r.label} style={{ borderTop: 'var(--hair-w) solid var(--hair)' }}>
            <th className="label grey" style={{ textAlign: 'left', fontWeight: 'var(--w-ui)', padding: '14px 0' }}>{r.label}</th>
            {models.map((m) => { const v = r.values[m.id]; return <td key={m.id} className="num" style={{ padding: '14px 12px', color: v == null ? 'var(--grey)' : undefined }}>{v == null ? '—' : v}</td>; })}
          </tr>))}
          <tr style={{ borderTop: 'var(--hair-w) solid var(--hair)' }}><td /> {models.map((m) => <td key={m.id} style={{ padding: '20px 12px 0' }}><Button kind={m.id === highlight ? 'lime' : 'outline'} arrow style={{ padding: '10px 14px' }}>View</Button></td>)}</tr>
        </tbody>
      </table>
    </div></section>
  );
}
