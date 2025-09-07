from example_1_source import source
from core.processor_factory import ProcessorTypes
from utils.runner import run_and_print


sequences = source.get_sequences()

a, b = sequences

# brute-force solver
run_and_print(a, b, ProcessorTypes.BRUTE_FORCE)

# constituent solver
run_and_print(a, b, ProcessorTypes.CONSTITUENT)

# cultivted solver: search-free "grown" solution; growth from curated parts/ cultivated environment
run_and_print(a, b, ProcessorTypes.CULTIVATED)

# deductive resolver: knowledge-free "whittled" solution; iterative elimination of negative-space
run_and_print(a, b, ProcessorTypes.DEDUCTIVE)

# positive projecttion  solver
run_and_print(a, b, ProcessorTypes.POSITIVE_PROJECTION)
