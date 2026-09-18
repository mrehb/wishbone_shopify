import React from 'react';

export function SiteFooter({ style }) {
  const col = { display: 'flex', flexDirection: 'column', gap: 8, fontSize: 13 };
  const link = { color: 'var(--text-muted)', textDecoration: 'none' };
  return (
    <footer style={{ background: 'var(--color-ink)', borderTop: '1px solid var(--color-border-soft)', padding: '40px 24px', ...style }}>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(170px,1fr))', gap: 'var(--grid-gap)' }}>
        <div style={col}>
          <img src="../../assets/wishbone-wordmark.png" alt="Wishbone Golf" style={{ width: 160 }} />
          <span style={{ color: 'var(--text-muted)' }}>Birthed in Britain.</span>
        </div>
        <div style={col}><b style={{ textTransform: 'uppercase', fontFamily: 'var(--font-heading)', fontWeight: 500 }}>Shop</b>
          <a style={link} href="#">All trolleys</a><a style={link} href="#">Spare parts</a><a style={link} href="#">Accessories</a></div>
        <div style={col}><b style={{ textTransform: 'uppercase', fontFamily: 'var(--font-heading)', fontWeight: 500 }}>Support</b>
          <a style={link} href="#">Contact</a><a style={link} href="#">Shipping</a><a style={link} href="#">Returns</a></div>
        <div style={col}><b style={{ textTransform: 'uppercase', fontFamily: 'var(--font-heading)', fontWeight: 500 }}>Legal</b>
          <a style={link} href="#">Privacy policy</a><a style={link} href="#">Terms of service</a><a style={link} href="#">Cookie preferences</a></div>
      </div>
    </footer>
  );
}
