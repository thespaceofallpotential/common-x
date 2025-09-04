import { IRange } from "./Range.ts";

export const SPACE = " ";
export const COMMA = ",";
export const COMMA_SEPARATOR = ", ";
export const COLON_SEPARATOR = "; ";
export const NEW_LINE = "\n";

export type Position = Readonly<number>;
export type Length = Readonly<number>;

export type Word = Readonly<string>;
export type Token = Readonly<number>;

export type TypeArray<T extends Token | Word> = Readonly<Array<T>>;
export type TypeSet<T extends Token | Word> = Set<T>;

export type PositionArray<T extends Token | Word> = { p: Position; ta: TypeArray<T> };

export type TPositionMap<T extends Token | Word> = Map<T, Position>;

export type PositionVector = {
    p: Position;
    l: Length;
};

export interface IReader<T extends Token | Word> {
    get(p: Position): T;
}

export const positionTypeMap = <T extends Token | Word>(r: IRange<T>): IReader<T> => ({ get: (p: Position): T => r.ra[p - r.position] });

// export type PositionNext<T extends Token | Word> = [Position, T | undefined];
// export const i_next_t = 1;

// export type CommonSequence<T extends Token | Word> = {
//     i: [ati: number, bti: number][];
//     t: T[];
//     w: string[];
//     s: string;
// };

// not yet... :D
// bound adjacency map: qualitative structural index (form-based as opposed to spatial space-based)
// bound adjacency map: -- think generalised suffix-tree, but rather granular adjacency -- so less (redundant) duplication
// bound adjacency map/ qualitative structural index (form-based index) : --do you see what this is yet?! ;)
// export type BoundAdjacencyMap<T extends Token | Word> = Map<T, Array<PositionNext<T>>>;
// export type PositionNextMap<T extends Token | Word> = BoundAdjacencyMap<T>;

export type PositionPair = { a: Set<Position>; b: Set<Position> };

export type Report = Map<string, PositionPair>;
