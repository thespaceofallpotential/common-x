import { IOptions } from "./Options.ts";
import { IRange, IRanges } from "./Range.ts";
import { splitOnNewLine } from "./RangeSplit.ts";
import { Token, Word } from "./Types.ts";

export default interface IResolver<T extends Token | Word> {
    readonly cost: number;

    process(aR: IRange<T>, bR: IRange<T>, d: number): IResolver<T>;

    processRanges(aRa: IRanges<T>, bRa: IRanges<T>, d: number): void;

    processContent(aR: IRange<T>, bR: IRange<T>, d: number, newLine: T): void;
}

export abstract class Resolver<T extends Token | Word> implements IResolver<T> {
    protected readonly options: IOptions | undefined;

    protected readonly sufficient: ((r: IRange<T>) => boolean) | undefined;

    cost: number = 0;

    constructor(options?: IOptions) {
        if (options) {
            this.sufficient = options.sufficient;

            this.options = options;
        }
    }

    public abstract process(aR: IRange<T>, bR: IRange<T>, d: number): IResolver<T>;

    public processRanges = (aRa: IRanges<T>, bRa: IRanges<T>, d: number): void => {
        const { process: process } = this;

        for (let ai = 0; ai < aRa.length; ai++) {
            for (let bi = 0; bi < bRa.length; bi++) {
                process(aRa[ai], bRa[bi], d + 1);
            }
        }
    };

    public processContent = (aR: IRange<T>, bR: IRange<T>, d: number, newLine: T): void => {
        const aRa = splitOnNewLine(aR, newLine);
        const bRa = splitOnNewLine(bR, newLine);

        this.processRanges(aRa, bRa, d);
    };

    step = (value: number = 1) => {
        this.cost += value;
    };
}
