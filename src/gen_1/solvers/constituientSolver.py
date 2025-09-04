from core import solver
from core.symmetricIndex import toSymmetricIndex
from core.types import CommonPoint


class ConstituientSolver[T](solver.AbstractSolver):
    commonPoints: list[CommonPoint[T]] = []

    def __init__(self, a: solver.Range, b: solver.Range):
        super().__init__(a, b)

    def process(self) -> solver.AbstractSolver:

        items = self.commonPoints
        a = self.a
        b = self.b

        commonSet = a.parts.intersection(b.parts)

        aXValuePositionMap = toSymmetricIndex(a.values, commonSet)
        bXValuePositionMap = toSymmetricIndex(b.values, commonSet)

        commonValues = list(commonSet)

        for value in commonValues:

            aPositions = aXValuePositionMap.get(value)
            bPositions = bXValuePositionMap.get(value)

            if not aPositions or not bPositions:
                continue

            for ap in aPositions:
                for bp in bPositions:

                    common = CommonPoint[T](ap, bp, value)

                    items.append(common)

                    self.step()

        return self
