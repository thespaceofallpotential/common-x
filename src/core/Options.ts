import { IRange } from "./Range.ts";
import { Token, Word } from "./Types.ts";

export interface IOptions {
    halt: boolean | undefined;

    minimumSequenceLength: number;

    sufficient: (<T extends Token | Word>(r: IRange<T>) => boolean) | undefined;
}

export class Options implements IOptions {
    halt: boolean | undefined = false;

    minimumSequenceLength: number = 0;

    sufficient = <T extends Token | Word>(r: IRange<T>) => r.length >= this.minimumSequenceLength;
}
