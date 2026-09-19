import React from 'react';

export function FootBar() {
  const mono = { fontSize: 'var(--fs-label)', letterSpacing: 'var(--track-label)', textTransform: 'uppercase' };
  const col = (h, items) => (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
      <span style={{ ...mono, color: 'var(--grey)' }}>{h}</span>
      {items.map((i) => <a key={i} href="#" style={{ color: 'var(--white)', textDecoration: 'none' }}>{i}</a>)}
    </div>
  );
  return (
    <footer style={{ borderTop: '1px solid var(--tile-line)', padding: '30px 0 10px', display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(160px,1fr))', gap: 20 }}>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
        <img src="../../assets/wishbone-wordmark.png" alt="Wishbone Golf" style={{ width: 150 }} />
        <span className="grey cursor">Birthed in Britain</span>
      </div>
      {col('shop', ['All trolleys', 'Electric', 'Spare parts'])}
      {col('support', ['Contact', 'Shipping', 'Returns'])}
      {col('legal', ['Privacy policy', 'Terms of service', 'Cookie preferences'])}
    </footer>
  );
}
