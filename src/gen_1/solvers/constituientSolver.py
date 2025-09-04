from typing import List, TypeVar
from core import solver
from core.range import Range
from core.symmetricIndex import toSymmetricIndex
from core.types import CommonPoint

T = TypeVar("T", int, str)

# ConstituientSolver: structureless mass of the solution-relative general-domain

class ConstituientSolver[T](solver.AbstractSolver):
    commonPoints: List[CommonPoint] = []

    def __init__(self, a: Range, b: Range):
        super().__init__(a, b)

    def process(self) -> solver.AbstractSolver:

        items = self.commonPoints
        a = self.a
        b = self.b

        commonSet = a.elements.intersection(b.elements)

        aXValuePositionMap = toSymmetricIndex(a.values, commonSet)
        bXValuePositionMap = toSymmetricIndex(b.values, commonSet)

        commonValues = list[T](commonSet)

        for value in commonValues:

            aPositions = aXValuePositionMap.get(value)
            bPositions = bXValuePositionMap.get(value)

            if not aPositions or not bPositions:
                continue

            for ap in aPositions:
                for bp in bPositions:

                    common = CommonPoint(ap, bp, value)

                    items.append(common)

                    self.step()

        return self
