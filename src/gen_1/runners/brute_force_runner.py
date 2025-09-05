from core.processor_factory import ProcessorTypes
from utils.runner import runner_factory

processor_type = ProcessorTypes.BRUTE_FORCE

runner = runner_factory(processor_type)
