import React from 'react';

// v2: raised surface, soft corners, mono label. Errors are stated in words.
export function Input({ label, placeholder, value, error, type = 'text', onChange, style }) {
  const id = label ? `wb-${label.replace(/\s+/g, '-').toLowerCase()}` : undefined;
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 7, ...style }}>
      {label && (
        <label htmlFor={id} style={{
          fontFamily: 'var(--font-mono)', fontSize: 11, letterSpacing: '0.18em',
          textTransform: 'uppercase', color: 'var(--text-muted)',
        }}>{label}</label>
      )}
      <input id={id} type={type} placeholder={placeholder} value={value} onChange={onChange} aria-invalid={!!error}
        style={{
          fontFamily: 'var(--font-body)', fontSize: 14, color: 'var(--color-white)',
          background: 'var(--surface-raised)', padding: '13px 15px',
          borderRadius: 'var(--radius-control)', outline: 'none',
          border: `1px solid ${error ? 'var(--color-error)' : 'var(--color-border-strong)'}`,
        }} />
      {error && <span style={{ color: 'var(--color-error)', fontSize: 13 }}>{error}</span>}
    </div>
  );
}
