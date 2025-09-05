from typing import TypeVar
from core.source import Source
from data.example_1_source import a_words
from data.example_1_source import b_words

from gen_1.solvers.brute_force_solver import BruteForceSolver
from gen_1.solvers.cultivated_solver import CultivatedSolver

from gen_1.solvers.deductive_resolver import DeductiveResolver
from gen_1.solvers.positive_projection_solver import PositiveProjectionSolver

source = Source(a_words, b_words)  # words <-> tokens

a = source.a_words  # or token ranges

b = source.b_words

T = TypeVar("T", int, str)

# solvers

# brute-force solver

print(BruteForceSolver)

brute = BruteForceSolver(a, b)

brute.process()

for c in brute.common_ranges:
    print(c)

# cultivted solver: search-free "grown" solution; growth from curated parts/ cultivated environment

print(CultivatedSolver)

cultivated = CultivatedSolver(a, b)

cultivated.process()

for c in cultivated.common_ranges:
    print(c)

# deductive resolver: knowledge-free "whittled" solution; iterative elimination of negative-space

print(DeductiveResolver)

deductive = DeductiveResolver()

deductive.process(a, b)

for c in deductive.common_ranges:
    print(c)

# positive projecttion  solver

print(PositiveProjectionSolver)

projection = PositiveProjectionSolver(a, b)

projection.process()

for c in projection.common_ranges:
    print(c)
