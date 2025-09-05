from core.processor_factory import ProcessorFactory, ProcessorTypes
from core.processor import IProcessor
from data.source import Source
from utils.custom_exception import CustomException


class Runner[T, C]:
    factory: ProcessorFactory[T, C]

    source: Source

    processor: IProcessor[T, C]

    def __init__(self, source: Source, processor_type: ProcessorTypes) -> None:
        self.factory = ProcessorFactory(processor_type)
        self.source = source

    def run(self):
        processor = self.factory.build()

        if not processor:
            raise CustomException("processor factory")

        self.processor = processor

        a = self.source.a_words
        b = self.source.b_words

        processor.process(a, b)

    def print(self):
        print(self.processor)

        for c in self.processor.items:
            print(c)

    def run_and_print(self):
        self.run()
        self.print()
