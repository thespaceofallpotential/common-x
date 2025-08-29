import { describeWordRanges } from "./core/Report.ts";
import { aWr, bWr } from "./core/Source.ts";
import { Word } from "./core/Types.ts";
import { BruteForceSolver } from "./solvers/BruteForceSolver.ts";
import { ConstituientSolver } from "./solvers/ConstituientSolver.ts";
import { CultivatedSolver } from "./solvers/CultivatedSolver.ts";
import { DeductiveResolver } from "./solvers/DeductiveResolver.ts";
import { ProjectionSolver } from "./solvers/ProjectionSolver.ts";

const isSummary = true;

// CultivatedSolver: organic "knowledge culture" ; middle-out/through

console.log(`CultivatedSolver`);

const culture = new CultivatedSolver(aWr, bWr);

culture.process();

describeWordRanges(culture.cra, culture.cost, isSummary);

///         ---         ///

// ConstituientSolver: structureless mass of the solution relative general-domain

console.log(`\nConstituientSolver`);

const constituient = new ConstituientSolver(aWr, bWr);

constituient.process();

console.log(`c:${constituient.cPa.length} (positive) -- cost:${constituient.cost}`);

///         ---         ///

// ProjectionSolver: approximation, hallucination, anomalous

console.log(`\nProjectionSolver`);

const projection = new ProjectionSolver(aWr, bWr);

projection.process();

describeWordRanges(projection.cra, projection.cost, isSummary);

///         ---         ///

// DeductiveSolver: idiomatic divide & dismiss, organic: unknown special-domain creativity/ insight

console.log(`\nDeductiveResolver`);

const elemetary = new DeductiveResolver<Word>();

elemetary.process(aWr, bWr);

describeWordRanges(elemetary.cra, elemetary.cost, isSummary);

///         ---         ///

// BruteForceSolver

console.log(`\nBruteForceSolver`);

const brute = new BruteForceSolver(aWr, bWr);

brute.process();

describeWordRanges(brute.cra, brute.cost, isSummary);

///         ---         ///

// LazyFakeSuffixTreeSolver

// console.log(`\nLazyFakeSuffixTreeSolver`);

// const lazyFake = new LazyFakeSuffixTreeSolver(aWr, bWr);

// lazyFake.process();

// describeWordRanges(lazyFake.cra, lazyFake.cost, false);
