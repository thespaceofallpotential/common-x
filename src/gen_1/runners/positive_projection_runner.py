from core.processor_factory import ProcessorTypes
from utils.runner import runner_factory

processor_type = ProcessorTypes.POSITIVE_PROJECTION

runner = runner_factory(processor_type)
