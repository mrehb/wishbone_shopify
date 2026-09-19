import * as React from 'react';
export interface DotGrid { grid: number[]; cols: number; rows: number; hot?: number[] }
export interface DotsProps extends DotGrid {
  hot?: number[] | ((index: number, value: number) => boolean);
  size?: number; gap?: number; style?: React.CSSProperties;
}
export declare function Dots(props: DotsProps): JSX.Element;
export declare function bars(levels: number[], rows?: number, hotAbove?: number): DotGrid;
export declare function ring(pct: number, radius?: number): DotGrid;
export declare function line(points: number[], rows?: number): DotGrid;
export declare function wave(cols?: number, rows?: number, phase?: number): DotGrid;
export declare function steps(n: number, done: number): DotGrid;
