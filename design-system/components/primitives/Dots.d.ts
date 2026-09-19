import * as React from 'react';
export interface DotsProps { grid: number[]; cols: number; rows: number; hot?: number[] | ((i: number, v: number) => boolean); size?: number; gap?: number; tone?: 'ink' | 'paper'; style?: React.CSSProperties }
export function Dots(props: DotsProps): JSX.Element;
