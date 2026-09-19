import * as React from 'react';
export interface HeroTileProps {
  n?: string; label?: string; title: string; copy?: string; cta?: string; secondary?: string;
  /** Model id: EON draws the sampled silhouette, others the outline. Omit for a waveform. */
  model?: string;
  stats?: { label: string; value: string }[]; span?: 2 | 3;
}
export declare function HeroTile(props: HeroTileProps): JSX.Element;
