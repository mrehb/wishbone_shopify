import * as React from 'react';
export interface PillProps {
  /** button = lime fill · ghost = outline · tag = grey chip · status = chip with dot · select = radio */
  kind?: 'button' | 'ghost' | 'tag' | 'status' | 'select';
  /** select: selected state */
  on?: boolean;
  /** lime dot (live) */
  hot?: boolean;
  disabled?: boolean;
  onClick?: React.MouseEventHandler<HTMLSpanElement>;
  children?: React.ReactNode;
  style?: React.CSSProperties;
}
export declare function Pill(props: PillProps): JSX.Element;
