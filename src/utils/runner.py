from core.processor_factory import ProcessorFactory, ProcessorTypes
from core.processor import IProcessor
from core.sequence import Sequence
from utils.custom_exception import CustomException


class Runner[T, C]:
    factory: ProcessorFactory[T, C]

    processor: IProcessor[T, C]

    def __init__(self, processor_type: ProcessorTypes) -> None:
        self.factory = ProcessorFactory(processor_type)

    def run(self, a: Sequence, b: Sequence):
        processor = self.factory.build()

        if not processor:
            raise CustomException("processor factory")

        self.processor = processor

        processor.process(a, b)

    def print(self):
        print(self.processor)

        for c in self.processor.items:
            print(c)

    def run_and_print(self, a: Sequence, b: Sequence):
        self.run(a, b)
        self.print()


def runner_factory[T, C](processor_type: ProcessorTypes) -> Runner:
    runner = Runner[T, C](processor_type)

    return runner


def run_and_print(processor_type: ProcessorTypes, a: Sequence, b: Sequence):
    runner_factory(processor_type).run_and_print(a, b)
