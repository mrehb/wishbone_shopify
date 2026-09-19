import React from 'react';

// Text input as a pill. Same shape as everything else that can be pressed.
export function Field({ label, placeholder, value, error, type = 'text', onChange, style }) {
  const id = label ? 'f-' + label.replace(/\W+/g, '-').toLowerCase() : undefined;
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 8, ...style }}>
      {label && <label htmlFor={id} className="label">{label}</label>}
      <input id={id} type={type} placeholder={placeholder} value={value} onChange={onChange} aria-invalid={!!error}
        style={{
          fontFamily: 'var(--font)', fontSize: 'var(--fs-body)', color: 'var(--white)', background: 'transparent',
          padding: '13px 18px', borderRadius: 'var(--r-pill)', outline: 'none',
          border: `1px solid ${error ? 'var(--lime)' : 'rgb(255 255 255 / .28)'}`,
        }} />
      {error && <span style={{ fontSize: 'var(--fs-label)', letterSpacing: '0.06em', color: 'var(--white)' }}>
        <span className="lime">▸ </span>{error}</span>}
    </div>
  );
}
