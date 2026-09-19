import * as React from 'react';
export interface DotMatrixProps {
  /** Row-major intensities, 0..1, length cols*rows. */
  values: number[];
  cols: number;
  rows: number;
  /** Indices drawn in volt, or a predicate (index, value) => boolean. */
  accent?: number[] | ((index: number, value: number) => boolean);
  size?: number;
  gap?: number;
  style?: React.CSSProperties;
}
export declare function DotMatrix(props: DotMatrixProps): JSX.Element;

export interface DotBarsProps {
  /** One level per column, 0..1. */
  levels: number[];
  height?: number;
  /** Columns at or above this level get volt tips. */
  accentAbove?: number;
  size?: number;
  gap?: number;
  style?: React.CSSProperties;
}
export declare function DotBars(props: DotBarsProps): JSX.Element;
