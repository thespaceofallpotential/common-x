import { DivideDismissConquer } from "./CommonTypes.ts";
import { toCommonRange } from "./helpers.ts";
import { IOptions } from "./Options.ts";
import { IRange } from "./Range.ts";
import { splitCommon, splitFrom } from "./RangeSplit.ts";
import { Token, Word } from "./Types.ts";

export const parseSplitCommon = <T extends Token | Word>(a: IRange<T>, b: IRange<T>, options?: IOptions): DivideDismissConquer<T> => {
    if (a.rs.intersection(b.rs).size === 0) return [[], [], undefined]; // fail fast

    const [aRa, bRa] = splitCommon(a, b, options);

    if (aRa.length > 1 || bRa.length > 1) return [aRa, bRa, undefined]; // stage results

    if (aRa.length === 0 || bRa.length === 0) return [[], [], undefined];

    const [aRa2, bRa2, common] = parseSplitSequence(aRa[0], bRa[0], options?.halt);

    return [aRa2, bRa2, common];
};

export const parseSplitSequence = <T extends Token | Word>(a: IRange<T>, b: IRange<T>, haltOnUnhandled: boolean = false): DivideDismissConquer<T> => {
    const [common, aSplitIndex, bSplitIndex] = toCommonRange(a, b);

    if (common) {
        if (aSplitIndex > 0) {
            const aa = splitFrom(a, aSplitIndex);

            return [[aa], [b], common]; // a is larger
        }

        if (bSplitIndex > 0) {
            const ba = splitFrom(b, bSplitIndex);

            return [[], [ba], common]; // b is larger
        }

        return [[], [], common]; // single result -> common map
    }

    const message = `err: space splitter; unhandled condition`;

    if (haltOnUnhandled) throw message;

    console.error(message);

    return [[], [], undefined];
};

export const parseCheckSequence = <T extends Token | Word>(a: IRange<T>, b: IRange<T>): DivideDismissConquer<T> => {
    const [common, aSplitIndex, bSplitIndex] = toCommonRange(a, b);

    if (common) {
        if (aSplitIndex > 0) return [[a], [b], undefined];

        if (bSplitIndex > 0) return [[a], [b], undefined];

        return [[], [], common];
    }

    return [[a], [b], undefined];
};
