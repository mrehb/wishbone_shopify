import React from 'react';
import { Tile } from '../primitives/Tile.jsx';

// Five models, one table. Unknowns are "—", the viewed model is lime.
export function CompareTile({ n, models = [], rows = [], highlight, span = 3 }) {
  const td = { padding: '11px 12px', borderBottom: '1px solid var(--tile-line)', whiteSpace: 'nowrap', textAlign: 'left' };
  return (
    <Tile n={n} label="Compare" span={span}>
      <div style={{ overflowX: 'auto' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse', minWidth: 560 }}>
          <thead><tr>
            <th className="label" style={{ ...td, fontWeight: 400 }}>model</th>
            {models.map((m) => <th key={m.id} style={{ ...td, fontSize: 'var(--fs-lead)', fontWeight: 400, color: m.id === highlight ? 'var(--lime)' : 'var(--white)' }}>{m.id}</th>)}
          </tr></thead>
          <tbody>{rows.map((r) => (
            <tr key={r.label}>
              <td className="label" style={td}>{r.label}</td>
              {models.map((m) => { const v = r.values[m.id]; const unk = v == null || v === '—';
                return <td key={m.id} style={{ ...td, color: unk ? 'var(--grey)' : 'var(--white)' }}>{unk ? '—' : v}</td>; })}
            </tr>))}
          </tbody>
        </table>
      </div>
    </Tile>
  );
}
