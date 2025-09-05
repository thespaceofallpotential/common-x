from typing import TypeVar
from core.source import Source
from data.example1Source import aWords
from data.example1Source import bWords

from gen_1.solvers.brute_force_solver import BruteForceSolver
from gen_1.solvers.cultivated_solver import CultivatedSolver

from gen_1.solvers.deductive_resolver import DeductiveResolver
from gen_1.solvers.positive_projection_solver import PositiveProjectionSolver

source = Source(aWords, bWords)  # words <-> tokens

a = source.aWordRange  # or token ranges

b = source.bWordRange

T = TypeVar("T", int, str)

# solvers

# brute-force solver

print(BruteForceSolver)

brute = BruteForceSolver(a, b)

brute.process()

for c in brute.commonRanges:
    print(c)

# cultivted solver: search-free "grown" solution; growth from curated parts/ cultivated environment

print(CultivatedSolver)

cultivated = CultivatedSolver(a, b)

cultivated.process()

for c in cultivated.commonRanges:
    print(c)

# deductive resolver: knowledge-free "whittled" solution; iterative elimination of negative-space

print(DeductiveResolver)

deductive = DeductiveResolver()

deductive.process(a, b)

for c in deductive.commonRanges:
    print(c)

# positive projecttion  solver

print(PositiveProjectionSolver)

projection = PositiveProjectionSolver(a, b)

projection.process()

for c in projection.commonRanges:
    print(c)
