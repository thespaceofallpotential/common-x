from typing import cast

from utils.custom_exception import CustomException

from batch.processor import IProcessor, ProcessorTypes

from gen_1_solvers.brute_force_solver import BruteForceSolver
from gen_1_solvers.constituient_solver import ConstituientSolver
from gen_1_solvers.cultivated_solver import CultivatedSolver
from gen_1_solvers.deductive_resolver import DeductiveResolver
from gen_1_solvers.positive_projection_solver import PositiveProjectionSolver


class ProcessorFactory[T, C]:
    def build(self, processor_type: ProcessorTypes) -> IProcessor[T, C]:
        match processor_type.value:
            case 1:
                return cast(IProcessor[T, C], BruteForceSolver[T]())
            case 2:
                return cast(IProcessor[T, C], ConstituientSolver[T]())
            case 3:
                return cast(IProcessor[T, C], CultivatedSolver[T]())
            case 4:
                return cast(IProcessor[T, C], DeductiveResolver[T]())
            case 5:
                return cast(IProcessor[T, C], PositiveProjectionSolver[T]())

        raise CustomException(f"processor factory: {type} not implemented error")
