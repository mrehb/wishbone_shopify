import React, { useId } from 'react';

// An underlined field, as in the reference's inquiry form. Label above in 12px caps; the line
// is the hairline and turns ink on focus. Error is a lime line plus a plain instruction. No red.
export function Field({ label, type = 'text', value, placeholder, error, multiline = false, onChange, style }) {
  const id = useId();
  const [focus, setFocus] = React.useState(false);
  const line = error ? '2px solid var(--lime)' : focus ? '1px solid currentColor' : '1px solid var(--hair)';
  const common = { id, value, placeholder, onChange: onChange && ((e) => onChange(e.target.value)), onFocus: () => setFocus(true), onBlur: () => setFocus(false),
    style: { width: '100%', border: 0, borderBottom: line, background: 'transparent', padding: '10px 0', outline: 'none', borderRadius: 0, fontSize: 'var(--fs-body)', resize: 'vertical' } };
  return (
    <div style={{ display: 'grid', gap: 4, ...style }}>
      <label htmlFor={id} className="label grey">{label}</label>
      {multiline ? <textarea rows={3} {...common} /> : <input type={type} {...common} />}
      {error && <div style={{ fontSize: 13, marginTop: 4 }}><span aria-hidden="true" style={{ display: 'inline-block', width: 8, height: 8, background: 'var(--lime)', marginRight: 8 }} />{error}</div>}
    </div>
  );
}
