import React, { useState } from 'react';
import { Tile } from '../primitives/Tile.jsx';
import { Pill } from '../primitives/Pill.jsx';

// The purchase. Price, colourway, one lime pill, and the two facts that close a trolley sale.
const SW = { 'charcoal-black': ['#2b2b2e', '#0f1014'], 'charcoal-lime': ['#2b2b2e', '#a8ff4a'], 'charcoal-red': ['#2b2b2e', '#b3342a'], 'white-red': ['#e9e9e9', '#b3342a'] };
export function BuyTile({ n, title, price, colourways = [], delivery, parts, soldOut = false, span = 1 }) {
  const [cw, setCw] = useState(colourways[0]);
  return (
    <Tile n={n} label="Buy" span={span} hot={!soldOut}>
      <h2>{title}</h2>
      <div className="readout" style={{ fontSize: 'var(--fs-h)' }}>{price}</div>
      {colourways.length > 0 && (
        <div>
          <div className="label">colourway · <span style={{ color: 'var(--white)' }}>{cw}</span></div>
          <div style={{ display: 'flex', gap: 10, marginTop: 10 }}>
            {colourways.map((c) => { const [a, b] = SW[c] || ['#2b2b2e', '#2b2b2e']; const on = c === cw; return (
              <button key={c} aria-label={c} aria-pressed={on} onClick={() => setCw(c)} style={{
                width: 34, height: 34, padding: 0, cursor: 'pointer', borderRadius: '50%',
                background: `linear-gradient(135deg, ${a} 0 50%, ${b} 50% 100%)`,
                border: `2px solid ${on ? 'var(--lime)' : 'transparent'}`, outline: on ? 'none' : '1px solid rgb(255 255 255 / .28)', outlineOffset: -1 }} />); })}
          </div>
        </div>
      )}
      <Pill kind="button" disabled={soldOut} style={{ justifyContent: 'center' }}>{soldOut ? 'Sold out' : 'Add to cart'}</Pill>
      <dl style={{ margin: 0, display: 'grid', gap: 6 }}>
        {delivery && <div style={{ display: 'flex', gap: 12 }}><dt className="label" style={{ minWidth: 88 }}>delivery</dt><dd style={{ margin: 0 }}>{delivery}</dd></div>}
        {parts != null && <div style={{ display: 'flex', gap: 12 }}><dt className="label" style={{ minWidth: 88 }}>parts</dt><dd style={{ margin: 0 }}>{String(parts).padStart(2, '0')} listed for this model</dd></div>}
      </dl>
    </Tile>
  );
}
