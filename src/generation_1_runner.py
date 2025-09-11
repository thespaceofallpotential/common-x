from example_1_source import source, sanitiser_options
from batch.processor_factory import ProcessorTypes
from data.source import get_sequences
from utils.runner import run_and_print


sequences = get_sequences(source, sanitiser_options=sanitiser_options)

a, b = sequences

# all solvers ./gen_1_solvers/*

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
