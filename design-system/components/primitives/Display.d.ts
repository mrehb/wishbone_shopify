import * as React from 'react';
export interface DisplayProps { lines: string[]; size?: 'hero' | 'display' | 's'; as?: keyof JSX.IntrinsicElements; style?: React.CSSProperties }
export function Display(props: DisplayProps): JSX.Element;
