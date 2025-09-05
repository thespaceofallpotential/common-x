from core import solver
from core.partition_helpers import partitions
from core.sequence import Sequence
from core.types import T
from gen_1.solvers.brute_force_solver import BruteForceSolver


# ProjectionSolver: approximation, hallucination, anomalous


class PositiveProjectionSolver[T](solver.AbstractSequenceSolver):
    def __init__(self, a: Sequence, b: Sequence):
        super().__init__(a, b)

    def process(self) -> solver.AbstractSolver:
        a = self.a
        b = self.b

        common_set = a.elements.intersection(b.elements)

        a_sequences = partitions(a, common_set)
        b_sequences = partitions(b, common_set)

        for a_sequence in a_sequences:
            for b_sequence in b_sequences:
                brute = BruteForceSolver(a_sequence, b_sequence)

                brute.process()

                self.common_sequences.extend(brute.common_sequences)

                self.step()

        return self
