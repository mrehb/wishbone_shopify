import * as React from 'react';
export interface ButtonProps {
  /** primary = volt fill with ink label · secondary = volt hairline · white = white fill · invert = ink fill on a volt/cyan panel */
  variant?: 'primary' | 'secondary' | 'white' | 'invert';
  size?: 'md' | 'lg';
  disabled?: boolean;
  onClick?: React.MouseEventHandler<HTMLButtonElement>;
  style?: React.CSSProperties;
  children?: React.ReactNode;
}
export declare function Button(props: ButtonProps): JSX.Element;
