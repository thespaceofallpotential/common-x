import { CommonRange, DivideDismissConquer } from "../core/CommonTypes.ts";
import { parseCheckSequence, parseSplitCommon } from "../core/FilteredRangeSplit.ts";
import { IOptions } from "../core/Options.ts";
import { IRange } from "../core/Range.ts";
import IResolver, { Resolver } from "../core/Resolver.ts";
import { Token, Word } from "../core/Types.ts";

const isCandidate = <T extends Token | Word>(a: IRange<T>, b: IRange<T>) => {
    const isSameSize = a.ra.length === b.ra.length;

    const isCommon = a.rs.symmetricDifference(b.rs).size === 0;

    return isSameSize && isCommon;
};

const divideAndDismiss = <T extends Token | Word>(aR: IRange<T>, bR: IRange<T>, options?: IOptions): DivideDismissConquer<T> => (isCandidate(aR, bR) ? parseCheckSequence(aR, bR) : parseSplitCommon(aR, bR, options));

const conquer = <T extends Token | Word>(commonMap: CommonRange<T>, cma: CommonRange<T>[]) => cma.push(commonMap);

const sufficientRemaining = <T extends Token | Word>(aRa: IRange<T>[], bRa: IRange<T>[], options?: IOptions) => (options ? aRa.find((x) => x.length > options.minimumSequenceLength) && bRa.find((x) => x.length > options.minimumSequenceLength) : aRa.length > 0 && bRa.length > 0);

/**
 * 
 */
export class DeductiveResolver<T extends Token | Word> extends Resolver<T> {
    readonly cra: CommonRange<T>[] = [];

    constructor(options?: IOptions) {
        super(options);
    }

    public override process = (aR: IRange<T>, bR: IRange<T>, d: number = 0): IResolver<T> => {
        const { cra, step, options, processRanges } = this;

        const [aRa, bRa, common] = divideAndDismiss(aR, bR, options);

        if (common) conquer(common, cra);

        if (sufficientRemaining(aRa, bRa)) processRanges(aRa, bRa, d + 1); // fractal recursion: process (ranges) -> split to sub-ranges -> processRanges -> iteratively cross-check sub-ranges -> process (sub-ranges -> ranges) |->

        step(aR.length + bR.length); // TODO: need to update this value... ballpark for now; custom data-structures will significanly reduce & custom hardware will eliminate

        return this;
    };
}
