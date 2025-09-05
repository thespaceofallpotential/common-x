from typing import cast
from batch.file_domain import FileDomain
from batch.processor_factory import ProcessorFactory
from core.sink import Sink
from core.options import Options
from core.processable import AbstractProcessable
from core.commonality import BatchSequences
from utils.custom_exception import CustomException


class Processor[T, C]:
    options: Options | None

    file_domain: FileDomain

    processor_factory: ProcessorFactory

    processor: AbstractProcessable[T, C]

    sink: Sink

    def __init__(
        self,
        file_domain: FileDomain,
        processable_factory: ProcessorFactory,
        options: Options | None = None,
    ) -> None:
        self.file_domain = file_domain
        self.options = options
        self.processor_factory = processable_factory

        self.sink = Sink[BatchSequences[C]]()

    def process(self):
        position = 0

        length = len(self.file_domain)

        for i_a in range(length):
            a = self.file_domain.get_file(position)

            for i_b in range(length):
                if i_a >= i_b:
                    continue

                b = self.file_domain.get_file(i_b)

                processor = self.processor_factory.build()

                if not processor:
                    raise CustomException(
                        f"{self.__class__}: not implemented exception"
                    )

                processor.process(a.sequence, b.sequence)

                self.sink.add(BatchSequences(i_a, i_b, cast(list[C], processor.items)))
