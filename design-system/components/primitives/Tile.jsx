import React from 'react';

// THE container. Every component in the system is a Tile or lives inside one.
// Same surface, same radius, same padding, same numbered label, same top-light edge.
export function Tile({ n, label, span = 1, hot = false, children, style }) {
  return (
    <section style={{
      gridColumn: `span ${span}`, background: 'var(--tile)', borderRadius: 'var(--r-tile)',
      padding: 'var(--pad)', boxShadow: 'inset 0 1px 0 var(--tile-edge)',
      display: 'flex', flexDirection: 'column', gap: 14, minWidth: 0, ...style,
    }}>
      {(n || label) && (
        <div className="label" style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          {n && <b>{n}</b>}<span>{label}</span>
          {hot && <i style={{ width: 6, height: 6, borderRadius: '50%', background: 'var(--lime)', marginLeft: 'auto' }} />}
        </div>
      )}
      {children}
    </section>
  );
}

// The page: a strict grid of tiles. This is the only layout container.
export function Board({ children, cols = 3, style }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: `repeat(${cols}, minmax(0,1fr))`, gap: 'var(--grid-gap)', ...style }}>
      {children}
    </div>
  );
}
