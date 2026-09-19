import * as React from 'react';
export interface DotGrid { grid: number[]; cols: number; rows: number; hot: number[] }
export const EON_S: DotGrid; export const EON_L: DotGrid;
export function outline(electric?: boolean, cols?: number, rows?: number): DotGrid;
export function silhouette(id: string, large?: boolean): DotGrid;
export function Photo(props: { src?: string; alt?: string; model?: string; ratio?: number; tone?: 'ink' | 'paper'; large?: boolean; style?: React.CSSProperties }): JSX.Element;
