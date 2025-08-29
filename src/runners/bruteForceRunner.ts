import { describeWordRanges } from "../core/Report.ts";
import { aWr, bWr } from "../core/Source.ts";
import { BruteForceSolver } from "../solvers/BruteForceSolver.ts";

// BruteForceSolver

console.log(`\nBrute-Force Solver`);

const brute = new BruteForceSolver(aWr, bWr);

brute.process();

describeWordRanges(brute.cra, brute.cost);
