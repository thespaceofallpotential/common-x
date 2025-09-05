from batch.batch_engine import batch_runner
from core.processor_factory import ProcessorTypes
from data.example_1_source import source
from core.sink import sink_factory

processor_type = ProcessorTypes.BRUTE_FORCE  # solver/ processor type

sequences = [source.a_words, source.b_words]

sink = sink_factory()

batch_runner(processor_type, sequences, sink)

print(f"{sink.items}")
