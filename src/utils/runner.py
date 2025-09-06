from core.processor_factory import ProcessorFactory, ProcessorTypes
from core.processor import IProcessor
from core.sequence import Sequence
from utils.custom_exception import CustomException


class Runner[T, C]:
    processor: IProcessor[T, C]

    def run(self, a: Sequence, b: Sequence, processor_type: ProcessorTypes):
        factory = ProcessorFactory()

        processor = factory.build(processor_type)

        if not processor:
            raise CustomException("processor factory")

        self.processor = processor

        processor.process(a, b)

    def print(self):
        print(self.processor)

        for c in self.processor.items:
            print(c)

    def run_and_print(self, a: Sequence, b: Sequence, processor_type: ProcessorTypes):
        self.run(a, b, processor_type)
        self.print()


def run_and_print(a: Sequence, b: Sequence, processor_type: ProcessorTypes):
    runner = Runner()

    runner.run_and_print(a, b, processor_type)
