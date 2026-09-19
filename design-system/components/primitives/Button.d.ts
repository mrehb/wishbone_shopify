import * as React from 'react';
export interface ButtonProps { kind?: 'lime' | 'ink' | 'outline' | 'text'; arrow?: boolean; disabled?: boolean; block?: boolean; href?: string; onClick?: () => void; children?: React.ReactNode; style?: React.CSSProperties }
export function Button(props: ButtonProps): JSX.Element;
