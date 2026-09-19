import * as React from 'react';
export interface BoxItem { name: string; qty?: string }
export interface InTheBoxProps { index?: string; items?: BoxItem[]; note?: string; style?: React.CSSProperties }
export declare function InTheBox(props: InTheBoxProps): JSX.Element;
