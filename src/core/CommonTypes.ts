import { IRange } from "./Range.ts";
import { Position, Token, Word } from "./Types.ts";

export type CommonRange<T extends Token | Word> = {
    a: Position;
    b: Position;
    ra: T[];
};

export type CommonPoint<T extends Token | Word> = [ap: Position, bp: Position, v: T];
export type CommonPoints<T extends Token | Word> = CommonPoint<T>[];

export type DivideDismissConquer<T extends Token | Word> = [a: IRange<T>[], b: IRange<T>[], CommonRange<T> | undefined];
