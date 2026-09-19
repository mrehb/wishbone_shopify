import * as React from 'react';
export interface FieldProps {
  label?: string; placeholder?: string; value?: string;
  /** A sentence that says what to do. There is no red in the system — errors are lime-marked text. */
  error?: string; type?: string;
  onChange?: React.ChangeEventHandler<HTMLInputElement>; style?: React.CSSProperties;
}
export declare function Field(props: FieldProps): JSX.Element;
