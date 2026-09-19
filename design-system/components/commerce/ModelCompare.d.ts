import * as React from 'react';
export interface CompareModel { id: string }
export interface CompareRow {
  label: string;
  /** Keyed by model id. Missing or "—" renders muted — never blank. */
  values: Record<string, string>;
}
export interface ModelCompareProps {
  models?: CompareModel[];
  rows?: CompareRow[];
  /** Model id shown in volt — the one the customer is currently viewing. */
  highlight?: string;
  style?: React.CSSProperties;
}
export declare function ModelCompare(props: ModelCompareProps): JSX.Element;
