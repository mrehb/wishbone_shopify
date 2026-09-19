import * as React from 'react';
export interface Spec {
  label: string;
  /** Print "—" when the value is unknown. Never invent a measurement. */
  value: React.ReactNode;
  unit?: string;
  note?: string;
  levels?: number[];
  footer?: { label: string; value: string }[];
}
export interface SpecPanelProps { specs?: Spec[]; style?: React.CSSProperties }
export declare function SpecPanel(props: SpecPanelProps): JSX.Element;
