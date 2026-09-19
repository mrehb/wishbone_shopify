import * as React from 'react';
export interface TileProps {
  /** Two-digit index in reading order: "01". */
  n?: string;
  label?: string;
  /** Grid columns to span: 1, 2 or 3. */
  span?: 1 | 2 | 3;
  /** Adds a lime live dot to the label row. */
  hot?: boolean;
  children?: React.ReactNode;
  style?: React.CSSProperties;
}
export declare function Tile(props: TileProps): JSX.Element;
export interface BoardProps { children?: React.ReactNode; cols?: 1 | 2 | 3; style?: React.CSSProperties }
export declare function Board(props: BoardProps): JSX.Element;
