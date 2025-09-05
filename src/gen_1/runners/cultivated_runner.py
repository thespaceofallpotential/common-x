from core.processor_factory import ProcessorTypes
from utils.runner import runner_factory

processor_type = ProcessorTypes.CULTIVATED

runner = runner_factory(processor_type)
