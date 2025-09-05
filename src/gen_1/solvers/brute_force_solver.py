from core import solver
from core.memo import Memo
from core.sequence import Sequence


# BruteForceSolver

# The brute force solver: unbound enumeration of an entire possibility-space
#


class BruteForceSolver[T](solver.AbstractSequenceSolver):
    def __init__(self, a: Sequence, b: Sequence) -> None:
        super().__init__(a, b)

    def process(self) -> solver.AbstractSolver:
        a = self.a
        b = self.b

        memo = Memo(self.common_sequences)

        for i_a, a_value in enumerate(a.values):
            for i_b, b_value in enumerate(b.values):
                memo.record(a.position + i_a, b.position + i_b, a_value, b_value)

                self.step()

            memo.next()

        return self
