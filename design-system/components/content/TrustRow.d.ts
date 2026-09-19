import * as React from 'react';
export interface TrustItem { label: string; value: string; note?: string }
export interface TrustRowProps { items?: TrustItem[]; style?: React.CSSProperties }
export declare function TrustRow(props: TrustRowProps): JSX.Element;
