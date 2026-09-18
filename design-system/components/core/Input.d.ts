import * as React from 'react';
export interface InputProps {
  label?: string;
  placeholder?: string;
  value?: string;
  /** Written in full sentences — colour is never the only signal. */
  error?: string;
  type?: string;
  onChange?: React.ChangeEventHandler<HTMLInputElement>;
  style?: React.CSSProperties;
}
export declare function Input(props: InputProps): JSX.Element;
