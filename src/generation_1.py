from data.example_1_source import source
from core.processor_factory import ProcessorTypes
from utils.runner import run_and_print

a = source.a_words
b = source.b_words

# brute-force solver
run_and_print(ProcessorTypes.BRUTE_FORCE, a, b)

# constituent solver
run_and_print(ProcessorTypes.CONSTITUENT, a, b)

# cultivted solver: search-free "grown" solution; growth from curated parts/ cultivated environment
run_and_print(ProcessorTypes.CULTIVATED, a, b)

# deductive resolver: knowledge-free "whittled" solution; iterative elimination of negative-space
run_and_print(ProcessorTypes.DEDUCTIVE, a, b)

# positive projecttion  solver
run_and_print(ProcessorTypes.POSITIVE_PROJECTION, a, b)
