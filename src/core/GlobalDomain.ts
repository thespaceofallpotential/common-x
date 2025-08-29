import { TPositionMap, Token, TypeArray, TypeSet, Word } from "./Types.ts";

export interface IGlobalDomain {
    gws: TypeSet<Word>;

    gwa: TypeArray<Word>;

    wpm: TPositionMap<Word>;

    toTokens(wa: TypeArray<Word>): TypeArray<Token>;

    toWords(ta: TypeArray<Token>): TypeArray<Word>;
}

export class GlobalDomain implements IGlobalDomain {
    gws: TypeSet<Word>;

    gwa: TypeArray<Word>;

    wpm: TPositionMap<Word> = new Map();

    constructor(gws: TypeSet<Word>) {
        this.gws = gws;

        this.gwa = [...gws].sort();

        const { gwa, wpm } = this;

        for (let i = 0; i < gwa.length; i++) {
            wpm.set(gwa[i], i);
        }
    }

    toTokens = (wa: TypeArray<Word>): TypeArray<Token> => wa.map((w) => this.wpm.get(w)!);

    toWords = (ta: TypeArray<Token>): TypeArray<Word> => ta.map((t) => this.gwa[t]);
}
