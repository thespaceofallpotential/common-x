from data.example_1_source import source
from gen_1.runners.brute_force_runner import runner as gen_1_brute
from gen_1.runners.constituent_runner import runner as gen_1_constituent
from gen_1.runners.cultivated_runner import runner as gen_1_cultivated
from gen_1.runners.deductive_runner import runner as gen_1_deductive
from gen_1.runners.positive_projection_runner import runner as gen_1_projection

a = source.a_words
b = source.b_words

# brute-force solver
gen_1_brute.run_and_print(a, b)

# constituent solver
gen_1_constituent.run_and_print(a, b)

# cultivted solver: search-free "grown" solution; growth from curated parts/ cultivated environment
gen_1_cultivated.run_and_print(a, b)

# deductive resolver: knowledge-free "whittled" solution; iterative elimination of negative-space
gen_1_deductive.run_and_print(a, b)

# positive projecttion  solver
gen_1_projection.run_and_print(a, b)
