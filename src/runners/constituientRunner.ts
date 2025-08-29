import { aWr, bWr } from "../core/Source.ts";
import { ConstituientSolver } from "../solvers/ConstituientSolver.ts";

// ConstituientSolver: structureless mass of the solution relative general-domain

console.log(`\nConstituient Solver`);

const constituient = new ConstituientSolver(aWr, bWr);

constituient.process();

console.log(`c:${constituient.cPa.length} (positive) -- cost:${constituient.cost}`);
