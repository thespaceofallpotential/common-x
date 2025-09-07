from example_1_source import source
from core.processor_factory import ProcessorTypes
from utils.runner import run_and_print


sequences = source.get_sequences()

a, b = sequences

# all solvers ./gen_1/*

# brute-force solver
# > basic naieve
run_and_print(a, b, ProcessorTypes.BRUTE_FORCE)

# constituent solver
# > structure-less approximation
run_and_print(a, b, ProcessorTypes.CONSTITUENT)

# cultivted solver
# > search-free "grown" solution; growth from curated parts/ cultivated environment
run_and_print(a, b, ProcessorTypes.CULTIVATED)

# deductive resolver
# > knowledge-free "whittled" solution; iterative elimination of negative-space
run_and_print(a, b, ProcessorTypes.DEDUCTIVE)

# positive projection solver
# > partial optimisation, to illustrate "hallucination space"
run_and_print(a, b, ProcessorTypes.POSITIVE_PROJECTION)
