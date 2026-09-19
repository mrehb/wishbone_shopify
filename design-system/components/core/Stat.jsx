import React from 'react';

// A telemetry readout: numbered label, the value in mono, supporting pairs underneath.
export function Stat({ index, label, value, unit, note, footer = [], children, style }) {
  return (
    <div style={{
      background: 'var(--surface-card)', border: '1px solid var(--color-border)',
      borderRadius: 'var(--radius-card)', padding: '18px 20px', ...style,
    }}>
      <div style={{ fontFamily: 'var(--font-mono)', fontSize: 11, letterSpacing: '0.18em', textTransform: 'uppercase', color: 'var(--text-muted)' }}>
        {index && <b style={{ color: 'var(--color-volt)', fontWeight: 400 }}>{index}&nbsp;&nbsp;</b>}{label}
      </div>
      <div style={{ display: 'flex', alignItems: 'baseline', gap: 8, marginTop: 14 }}>
        <span style={{ fontFamily: 'var(--font-mono)', fontSize: 44, lineHeight: 1, letterSpacing: '0.02em' }}>{value}</span>
        {unit && <span style={{ color: 'var(--text-muted)', fontSize: 13 }}>{unit}</span>}
      </div>
      {note && <div style={{ color: 'var(--text-muted)', fontSize: 13, marginTop: 6 }}>{note}</div>}
      {children && <div style={{ marginTop: 14 }}>{children}</div>}
      {footer.length > 0 && (
        <div style={{ display: 'flex', gap: 22, marginTop: 16 }}>
          {footer.map((f) => (
            <div key={f.label}>
              <div style={{ fontFamily: 'var(--font-mono)', fontSize: 10, letterSpacing: '0.16em', textTransform: 'uppercase', color: 'var(--text-muted)' }}>{f.label}</div>
              <div style={{ fontFamily: 'var(--font-mono)', fontSize: 17 }}>{f.value}</div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
