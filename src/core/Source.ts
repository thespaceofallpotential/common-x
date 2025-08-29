import { A } from "../../data/a.ts";
import { B } from "../../data/b.ts";
import { GlobalDomain } from "./GlobalDomain.ts";
import { Range } from "./Range.ts";
import { SPACE, TypeArray, Word } from "./Types.ts";

export const awa = A.split(SPACE) as TypeArray<Word>;

export const bwa = B.split(SPACE) as TypeArray<Word>;

export const aWr = new Range(awa); // Range<Word>

export const bWr = new Range(bwa); // Range<Word>

export const gd = new GlobalDomain(aWr.rs.union(bWr.rs));

export const ata = gd.toTokens(aWr.ra); // as TypedArray<Token>

export const bta = gd.toTokens(bWr.ra); // as TypedArray<Token>

export const aTr = new Range(ata); // Range<Token>

export const bTr = new Range(bta); // Range<Token>
