from batch.batch_engine import batch_run_and_print
from batch.processor_factory import ProcessorTypes

from example_1_source import source as example_1_source
from data.source import get_sequences


sequences = get_sequences(example_1_source)


batch_run_and_print(ProcessorTypes.BRUTE_FORCE, sequences)

batch_run_and_print(ProcessorTypes.CONSTITUENT, sequences)

batch_run_and_print(ProcessorTypes.CULTIVATED, sequences)

batch_run_and_print(ProcessorTypes.DEDUCTIVE, sequences)

batch_run_and_print(ProcessorTypes.POSITIVE_PROJECTION, sequences)
