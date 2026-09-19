import React from 'react';

// v2: carbon bar, mono nav, live status dot — the header reads as a device status line.
export function SiteHeader({ links = ['Trolleys', 'Electric', 'Spare parts', 'Contact'], cartCount = 0, status = 'All systems operational', style }) {
  const nav = { fontFamily: 'var(--font-mono)', fontSize: 12, letterSpacing: '0.14em', textTransform: 'uppercase' };
  return (
    <header style={{ background: 'var(--surface-page)', borderBottom: '1px solid var(--color-border)', ...style }}>
      {status && (
        <div style={{ ...nav, display: 'flex', alignItems: 'center', gap: 8, padding: '8px 24px', color: 'var(--text-muted)', borderBottom: '1px solid var(--color-border)' }}>
          <i style={{ width: 6, height: 6, borderRadius: '50%', background: 'var(--color-volt)' }} />{status}
        </div>
      )}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: 28, padding: '16px 24px' }}>
        <img src="../../assets/wishbone-wordmark.png" alt="Wishbone Golf" style={{ width: 180, maxWidth: '38%' }} />
        <nav style={{ ...nav, display: 'flex', gap: 22 }}>
          {links.map((l) => <a key={l} href="#" style={{ color: 'var(--color-white)', textDecoration: 'none' }}>{l}</a>)}
        </nav>
        <span style={{ ...nav, color: 'var(--color-volt)' }}>Cart [{String(cartCount).padStart(2, '0')}]</span>
      </div>
    </header>
  );
}
