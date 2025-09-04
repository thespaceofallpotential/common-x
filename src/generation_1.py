from typing import TypeVar
from core.reporting import commonPartitionString
from core.source import Source
from data.example1Source import aWords
from data.example1Source import bWords

from gen_1.solvers.bruteForceSolver import BruteForceSolver
from gen_1.solvers.cultivatedSolver import CultivatedSolver

from gen_1.solvers.deductiveResolver import DeductiveResolver
from gen_1.solvers.positiveProjectionSolver import PositiveProjectionSolver

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
    print(commonPartitionString(c))

# cultivted solver: search-free "grown" solution; growth from curated parts/ cultivated environment

print(CultivatedSolver)

cultivated = CultivatedSolver(a, b)

cultivated.process()

for c in cultivated.commonRanges:
    print(commonPartitionString(c))

# deductive resolver: knowledge-free "whittled" solution; iterative elimination of negative-space

print(DeductiveResolver)

deductive = DeductiveResolver()

deductive.process(a, b)

for c in deductive.commonRanges:
    print(commonPartitionString(c))

# positive projecttion  solver

print(PositiveProjectionSolver)

projection = PositiveProjectionSolver(a, b)

projection.process()

for c in projection.commonRanges:
    print(commonPartitionString(c))
