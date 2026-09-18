import React from 'react';

// Square field, 1px hairline at 55%, label above — never placeholder-as-label.
// Errors are stated in words; colour alone is never the signal.
export function Input({ label, placeholder, value, error, type = 'text', onChange, style }) {
  const id = label ? `wb-${label.replace(/\s+/g, '-').toLowerCase()}` : undefined;
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 6, ...style }}>
      {label && <label htmlFor={id} style={{ fontSize: 12, color: 'var(--text-muted)' }}>{label}</label>}
      <input id={id} type={type} placeholder={placeholder} value={value} onChange={onChange}
        aria-invalid={!!error}
        style={{
          fontFamily: 'var(--font-body)', fontSize: 14, color: 'var(--color-white)',
          background: 'transparent', padding: '12px 14px', borderRadius: 'var(--radius)',
          border: `1px solid ${error ? 'var(--color-error)' : 'var(--color-border)'}`, outline: 'none',
        }} />
      {error && <span style={{ color: 'var(--color-error)', fontSize: 13 }}>{error}</span>}
    </div>
  );
}
