from enum import Enum
from typing import cast
from utils.custom_exception import CustomException

from core.processable import AbstractProcessable
from gen_1.solvers.brute_force_solver import BruteForceSolver
from gen_1.solvers.constituient_solver import ConstituientSolver
from gen_1.solvers.cultivated_solver import CultivatedSolver
from gen_1.solvers.deductive_resolver import DeductiveResolver
from gen_1.solvers.positive_projection_solver import PositiveProjectionSolver


class ProcessorTypes(Enum):
    BRUTE_FORCE = 1
    CONSTITUENT = 2
    CULTIVATED = 3
    DEDUCTIVE = 4
    POSITIVE_PROJECTION = 5


class ProcessorFactory[T, C]:
    processor_type: ProcessorTypes

    def __init__(self, processor_type: ProcessorTypes) -> None:
        self.processor_type = processor_type

    def build(self) -> AbstractProcessable[T, C]:
        match self.processor_type.value:
            case 1:
                return cast(AbstractProcessable[T, C], BruteForceSolver[T]())
            case 2:
                return cast(AbstractProcessable[T, C], ConstituientSolver[T]())
            case 3:
                return cast(AbstractProcessable[T, C], CultivatedSolver[T]())
            case 4:
                return cast(AbstractProcessable[T, C], DeductiveResolver[T]())
            case 5:
                return cast(AbstractProcessable[T, C], PositiveProjectionSolver[T]())

        raise CustomException(f"processor factory: {type} not implemented error")
