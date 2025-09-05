from data.example_1_source import source

from core.processor_factory import ProcessorTypes
from core.commonality import CommonSequence
from utils.runner import Runner

processor_type = ProcessorTypes.DEDUCTIVE

runner = Runner[str, CommonSequence](source, processor_type)
