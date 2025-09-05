from batch.file_domain import FileDomain
from batch.processor_factory import ProcessorFactory
from core.sink import Sink
from core.options import Options


class Processor[T]:
    options: Options | None

    file_domain: FileDomain

    processor_factory: ProcessorFactory

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

    def process(self):
        position = 0

        length = len(self.file_domain)

        for i_a in range(length):
            a = self.file_domain.get_file(position)

            for i_b in range(length):
                if i_a == i_b:
                    continue

                b = self.file_domain.get_file(i_b)

                processor = self.processor_factory.build()

                if not processor:
                    continue

                processor.process(a.sequence, b.sequence)

                self.sink.add(processor.items)
