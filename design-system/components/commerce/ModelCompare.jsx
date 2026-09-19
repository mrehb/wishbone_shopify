import React from 'react';

// Five models, three manual and two electric. Small enough to compare in one table —
// which is exactly why the store should, instead of making people open five tabs.
export function ModelCompare({ models = [], rows = [], highlight, style }) {
  const cell = { padding: '13px 14px', borderBottom: '1px solid var(--color-border)', fontSize: 14, whiteSpace: 'nowrap' };
  const mono = { fontFamily: 'var(--font-mono)' };
  return (
    <div style={{ overflowX: 'auto', ...style }}>
      <table style={{ width: '100%', borderCollapse: 'collapse', minWidth: 560 }}>
        <thead>
          <tr>
            <th style={{ ...cell, ...mono, fontSize: 11, letterSpacing: '0.18em', textTransform: 'uppercase', color: 'var(--text-muted)', textAlign: 'left', fontWeight: 400 }}>Model</th>
            {models.map((m) => (
              <th key={m.id} style={{ ...cell, textAlign: 'left', fontFamily: 'var(--font-display)', fontWeight: 500, fontSize: 17,
                color: m.id === highlight ? 'var(--color-volt)' : 'var(--color-white)' }}>{m.id}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((r) => (
            <tr key={r.label}>
              <td style={{ ...cell, ...mono, fontSize: 11, letterSpacing: '0.16em', textTransform: 'uppercase', color: 'var(--text-muted)' }}>{r.label}</td>
              {models.map((m) => {
                const v = r.values[m.id];
                return <td key={m.id} style={{ ...cell, ...mono, color: v === '—' || v === undefined ? 'var(--text-muted)' : 'var(--color-white)' }}>{v === undefined ? '—' : v}</td>;
              })}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
