from typing import List, cast
from batch.file_domain import FileDomain
from batch.processor_factory import ProcessorFactory
from batch.file import File
from core.sink import Sink
from core.options import Options
from core.processable import AbstractProcessable
from core.commonality import BatchSequences
from utils.custom_exception import CustomException


class Processor[T, C]:
    options: Options | None

    files: List[File]

    processor_factory: ProcessorFactory

    processor: AbstractProcessable[T, C]

    sink: Sink

    def __init__(
        self,
        files: List[File],
        processable_factory: ProcessorFactory,
        options: Options | None = None,
    ) -> None:
        self.files = files
        self.options = options
        self.processor_factory = processable_factory

        self.sink = Sink[BatchSequences[C]]()

    def process(self):
        length = len(self.files)

        for i_a in range(length):
            a = self.files[i_a]

            for i_b in range(length):
                if i_a >= i_b:
                    # only process a pair once
                    # no same file comparisons for now
                    continue

                b = self.files[i_b]

                processor = self.processor_factory.build()

                if not processor:
                    raise CustomException(
                        f"{self.__class__}: not implemented exception"
                    )

                processor.process(a.sequence, b.sequence)

                self.sink.add(BatchSequences(i_a, i_b, cast(list[C], processor.items)))
