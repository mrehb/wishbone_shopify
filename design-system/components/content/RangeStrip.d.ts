import * as React from 'react';
export interface RangeModel { id: string; electric?: boolean; price?: string; href?: string }
export interface RangeStripProps { models?: RangeModel[]; style?: React.CSSProperties }
export declare function RangeStrip(props: RangeStripProps): JSX.Element;
