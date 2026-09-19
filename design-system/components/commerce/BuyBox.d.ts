import * as React from 'react';
export interface BuyBoxProps {
  title: string;
  price: string;
  /** Struck-through former price. Use only for a genuine reduction. */
  was?: string;
  badge?: 'live' | 'best' | 'soldout' | 'spare';
  stock?: 'in' | 'out';
  delivery?: string;
  /** e.g. "14 parts listed for the NEO" — the repairability promise, stated as a number. */
  partsNote?: string;
  /** Variant controls — usually a ColorwaySelector. */
  children?: React.ReactNode;
  style?: React.CSSProperties;
}
export declare function BuyBox(props: BuyBoxProps): JSX.Element;
