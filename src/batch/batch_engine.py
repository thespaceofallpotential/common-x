import math

from typing import List

# from batch.file_domain import FileDomain
from batch.batch import Batch
from batch.processor import IProcessor
from batch.processor_factory import ProcessorFactory, ProcessorTypes
from core.sequence import Sequence
from core.sink import Sink, sink_factory
from utils.progress import TimedProgress


class BatchEngine[T, C]:
    def process(
        self,
        sequences: List[Sequence],
        processor: IProcessor[T, C],
        sink: Sink[Batch[C]],
    ):
        length = len(sequences)

        total = length * length / 2
        count = 0

        progress = TimedProgress("batch", math.ceil(total))

        for i_a in range(length):
            a = sequences[i_a]

            for i_b in range(length):
                progress.update(count)

                if i_b >= i_a:
                    # only process a pair once
                    # no same file comparisons for now
                    break

                b = sequences[i_b]

                processor.process(a, b)

                batch = processor.get_batch(i_a, i_b)

                sink.add(batch)

                count += 1

        progress.complete()


def batch_runner[C](
    processor_type: ProcessorTypes,
    sequences: List[Sequence],
    sink: Sink[Batch[C]],
):
    factory = ProcessorFactory()

    processor = factory.build(processor_type)

    engine = BatchEngine()

    engine.process(sequences, processor, sink)


def batch_run_and_print(processor_type: ProcessorTypes, sequences: List[Sequence]):
    sink = sink_factory()

    batch_runner(processor_type, sequences, sink)

    print(f"{sink.items}")
