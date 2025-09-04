import { IRange } from "./Range.ts";
import { Token, Word } from "./Types.ts";

export interface ISolver<T extends Token | Word> {
    readonly cost: number;

    process(): ISolver<T>;
}

export abstract class Solver<T extends Token | Word> implements ISolver<T> {
    readonly a: IRange<T>;
    readonly b: IRange<T>;

    cost: number = 0;

    constructor(a: IRange<T>, b: IRange<T>) {
        this.a = a;
        this.b = b;
    }

    public abstract process(): ISolver<T>;

    step = (value: number = 1) => {
        this.cost += value;
    };
}
