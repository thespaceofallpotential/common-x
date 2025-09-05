from data.example_1_source import source

from batch.processor_factory import ProcessorTypes
from core.commonality import CommonSequence
from utils.runner import Runner

processor_type = ProcessorTypes.BRUTE_FORCE

runner = Runner[str, CommonSequence](source, processor_type)
