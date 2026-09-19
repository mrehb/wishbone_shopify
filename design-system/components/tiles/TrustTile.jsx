import React from 'react';
import { Tile } from '../primitives/Tile.jsx';
import { Readout } from '../primitives/Readout.jsx';

// One fact, as a value. "22 spare parts listed" beats any badge.
export function TrustTile({ n, label, value, unit, note, hot = false }) {
  return (
    <Tile n={n} label={label} hot={hot}><Readout value={value} unit={unit} note={note} size="var(--fs-h)" /></Tile>
  );
}
