from typing import List

# from batch.file_domain import FileDomain
from core.sequence import Sequence
from core.sink import Sink, sink_factory
from core.processor import IProcessor
from batch.batch import Batch
from core.processor_factory import ProcessorFactory, ProcessorTypes


class BatchEngine[T, C]:
    def process(
        self,
        sequences: List[Sequence],
        processor: IProcessor[T, C],
        sink: Sink[Batch[C]],
    ):
        length = len(sequences)

        for i_a in range(length):
            a = sequences[i_a]

            for i_b in range(length):
                if i_a >= i_b:
                    # only process a pair once
                    # no same file comparisons for now
                    continue

                b = sequences[i_b]

                processor.process(a, b)

                batch = processor.get_batch(i_a, i_b)

                sink.add(batch)


def batch_runner[C](
    processor_type: ProcessorTypes,
    sequences: List[Sequence],
    sink: Sink[Batch[C]],
):
    factory = ProcessorFactory(processor_type)

    processor = factory.build()

    engine = BatchEngine()

    engine.process(sequences, processor, sink)


def batch_run_and_print(processor_type: ProcessorTypes, sequences: List[Sequence]):
    sink = sink_factory()

    batch_runner(processor_type, sequences, sink)

    print(f"{sink.items}")
