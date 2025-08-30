import { describeWordRanges } from "../../core/Report.ts";
import { aWr, bWr } from "../../core/Source.ts";
import { CultivatedSolver } from "../solvers/CultivatedSolver.ts";

// CultivatedSolver: organic "knowledge culture" ; middle-out/through

console.log(`Cultivated Solver`);

const culture = new CultivatedSolver(aWr, bWr);

culture.process();

describeWordRanges(culture.cra, culture.cost);
