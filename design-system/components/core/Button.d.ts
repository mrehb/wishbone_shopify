import * as React from 'react';
export interface ButtonProps {
  /** primary = volt fill, carbon label · ghost = hairline outline · quiet = text only */
  variant?: 'primary' | 'ghost' | 'quiet';
  size?: 'md' | 'lg';
  disabled?: boolean;
  onClick?: React.MouseEventHandler<HTMLButtonElement>;
  style?: React.CSSProperties;
  children?: React.ReactNode;
}
export declare function Button(props: ButtonProps): JSX.Element;
