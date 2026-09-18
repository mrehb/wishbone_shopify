import * as React from 'react';
export interface VariantPillProps {
  children?: React.ReactNode;
  selected?: boolean;
  /** Shown struck through at 40 % — never removed from the list. */
  unavailable?: boolean;
  onClick?: React.MouseEventHandler<HTMLSpanElement>;
  style?: React.CSSProperties;
}
export declare function VariantPill(props: VariantPillProps): JSX.Element;
