from typing import List
from batch.processor import Processor
from batch.file import File
from batch.file_domain import FileDomain
from batch.processor_factory import ProcessorFactory, ProcessorTypes
from core.commonality import CommonSequence
from data.example_1_source import source

processor_type = ProcessorTypes.BRUTE_FORCE

files: List[File] = [File("a", source.a_words), File("b", source.b_words)]

file_domain = FileDomain(files)

factory = ProcessorFactory(processor_type)

processor = Processor[str, CommonSequence](file_domain, factory)

processor.process()

print(f"{processor.sink.items}")
