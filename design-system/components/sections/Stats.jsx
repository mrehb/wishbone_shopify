import React from 'react';
import { StatRow } from '../primitives/Stat.jsx';

// The band under the hero: four or five facts, hairlines between, paper.
export function Stats({ items = [{ value: '27+', unit: 'holes', label: 'range on one charge' }, { value: '5', label: 'models' }, { value: '22', label: 'spare parts listed' }, { value: '2–4', unit: 'days', label: 'delivery' }] }) {
  return <section className="band band--tight" style={{ borderBottom: 'var(--hair-w) solid var(--hair)' }}><div className="container"><StatRow items={items} /></div></section>;
}
