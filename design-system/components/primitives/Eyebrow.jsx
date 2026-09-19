import React from 'react';

// The one place the dot-matrix face appears: a numbered section label.
// On paper it is ink with a 20px lime rule; on the ink band it is lime with no rule.
export function Eyebrow({ n, children, style }) {
  return <div className="eyebrow" style={style}>{n && <b>{n}</b>}{children}</div>;
}
