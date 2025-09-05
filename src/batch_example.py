from batch.batch_engine import batch_run_and_print
from core.processor_factory import ProcessorTypes
from data.example_1_source import source

sequences = [source.a_words, source.b_words]

batch_run_and_print(ProcessorTypes.BRUTE_FORCE, sequences)

batch_run_and_print(ProcessorTypes.CONSTITUENT, sequences)

batch_run_and_print(ProcessorTypes.CULTIVATED, sequences)

batch_run_and_print(ProcessorTypes.DEDUCTIVE, sequences)

batch_run_and_print(ProcessorTypes.POSITIVE_PROJECTION, sequences)
