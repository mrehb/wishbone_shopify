import * as React from 'react';
export interface HeroStat { label: string; value: string }
export interface HeroProps {
  index?: string;
  eyebrow?: string;
  title: string;
  copy?: string;
  cta?: string;
  secondary?: string;
  /** Up to four. Unknown values pass "—". */
  stats?: HeroStat[];
  /** A photograph or a DotMatrix silhouette. */
  media?: React.ReactNode;
  style?: React.CSSProperties;
}
export declare function Hero(props: HeroProps): JSX.Element;
