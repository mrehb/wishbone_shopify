import React from 'react';

// The reference's press-logo row, with the words Wishbone actually has: its four proof points,
// set as tracked caps on a mist strip. Swap in press marks when there are any.
export function Trust({ items = ['Birthed in Britain', 'Aircraft-grade aluminium', 'Sealed bearings', 'Magnetic attachments', 'Folds flat'] }) {
  return (
    <section className="band band--mist band--tight"><div className="container">
      <ul className="label grey" style={{ display: 'flex', justifyContent: 'space-between', flexWrap: 'wrap', gap: 24, listStyle: 'none', padding: 0 }}>{items.map((t) => <li key={t}>{t}</li>)}</ul>
    </div></section>
  );
}
