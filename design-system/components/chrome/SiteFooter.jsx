import React from 'react';

export function SiteFooter({ style }) {
  const col = { display: 'flex', flexDirection: 'column', gap: 9, fontSize: 13.5 };
  const head = { fontFamily: 'var(--font-mono)', fontSize: 11, letterSpacing: '0.18em', textTransform: 'uppercase', color: 'var(--text-muted)' };
  const link = { color: 'var(--color-white)', textDecoration: 'none', opacity: 0.8 };
  return (
    <footer style={{ borderTop: '1px solid var(--color-border)', padding: '44px 24px 30px', ...style }}>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(170px,1fr))', gap: 'var(--grid-gap)' }}>
        <div style={col}>
          <img src="../../assets/wishbone-wordmark.png" alt="Wishbone Golf" style={{ width: 150 }} />
          <span style={{ color: 'var(--text-muted)' }}>Birthed in Britain.</span>
        </div>
        <div style={col}><span style={head}>Shop</span>
          <a style={link} href="#">All trolleys</a><a style={link} href="#">Electric</a><a style={link} href="#">Spare parts</a></div>
        <div style={col}><span style={head}>Support</span>
          <a style={link} href="#">Contact</a><a style={link} href="#">Shipping</a><a style={link} href="#">Returns</a></div>
        <div style={col}><span style={head}>Legal</span>
          <a style={link} href="#">Privacy policy</a><a style={link} href="#">Terms of service</a><a style={link} href="#">Cookie preferences</a></div>
      </div>
    </footer>
  );
}
