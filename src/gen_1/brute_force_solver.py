from core.solver import Solver
from core.commonality import CommonSequence
from core.memo import Memo
from core.sequence import Sequence


# BruteForceSolver

# The brute force solver: unchecked/unbound enumeration of possibility-space


class BruteForceSolver[T](Solver[T, CommonSequence]):
    def process(self, a: Sequence, b: Sequence):
        memo = Memo(self.items)

        for i_a, a_value in enumerate(a.values):
            for i_b, b_value in enumerate(b.values):
                memo.record(a.position + i_a, b.position + i_b, a_value, b_value)

                self.step()

            memo.next()

        return self
