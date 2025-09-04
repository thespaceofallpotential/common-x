import { describeWordRanges } from "../../core/Report.ts";
import { aWr, bWr } from "../../core/Source.ts";
import { PositiveProjectionSolver } from "../solvers/PositiveProjectionSolver.ts";

// ProjectionSolver: approximation, hallucination, anomalous

console.log(`\nPositive Projection Solver`);

const projection = new PositiveProjectionSolver(aWr, bWr);

projection.process();

describeWordRanges(projection.cra, projection.cost);
