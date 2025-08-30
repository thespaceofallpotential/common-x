import { describeWordRanges } from "../../core/Report.ts";
import { aWr, bWr } from "../../core/Source.ts";
import { Word } from "../../core/Types.ts";
import { DeductiveResolver } from "../solvers/DeductiveResolver.ts";

// DeductiveSolver: idiomatic divide & dismiss, organic: unknown special-domain creativity/ insight

console.log(`\nDeductive Resolver`);

const elemetary = new DeductiveResolver<Word>();

elemetary.process(aWr, bWr);

describeWordRanges(elemetary.cra, elemetary.cost);
