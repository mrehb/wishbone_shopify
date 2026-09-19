import * as React from 'react';
export interface FieldProps { label: string; type?: string; value?: string; placeholder?: string; error?: string; multiline?: boolean; onChange?: (v: string) => void; style?: React.CSSProperties }
export function Field(props: FieldProps): JSX.Element;
