from batch.processor import Processor
from batch.file import File
from batch.file_domain import FileDomain
from batch.processor_factory import ProcessorFactory, ProcessorTypes
from core.commonality import CommonSequence
from data.example_1_source import source

processor_type = ProcessorTypes.BRUTE_FORCE  # solver/ processor type

files = [File("a", source.a_words), File("b", source.b_words)]

# file_domain = FileDomain(files)

factory = ProcessorFactory(processor_type)

# first type argument is value type [str | int] (word | token)
# second type argument is record type [CommonSequence | CommonPoint]
#
# > only constituent solver uses common point for the time being...
# > (but can check check solver class for hint @ ./src/gen_1/solvers/*)
processor = Processor[str, CommonSequence](files, factory)

processor.process()

print(f"{processor.sink.items}")
