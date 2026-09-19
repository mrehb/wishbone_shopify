import * as React from 'react';
export interface StatFooterItem { label: string; value: string }
export interface StatProps {
  /** Two-digit panel number, e.g. "01". Rendered in volt. */
  index?: string;
  label: string;
  value: React.ReactNode;
  unit?: string;
  note?: string;
  footer?: StatFooterItem[];
  /** Usually a DotMatrix or DotBars. */
  children?: React.ReactNode;
  style?: React.CSSProperties;
}
export declare function Stat(props: StatProps): JSX.Element;
