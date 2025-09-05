from typing import Dict, List, Tuple, cast
from core.range import Range
from core.types import values_str


class CommonRange[T]:
    a_position: int
    b_position: int

    values: List[T]

    def __init__(self, a_position: int, b_position: int, values: List[T] | None = None):
        self.a_position = a_position
        self.b_position = b_position

        self.values = values if values else []

    def __repr__(self) -> str:
        return f"a:{self.a_position} b:{self.b_position}, v:{values_str(cast(List[str], self.values))}"


type CommonRanges[T] = Dict[int, CommonRange]


class CommonPoint[T]:
    a_position: int
    b_position: int

    value: T

    def __init__(self, ap: int, bp: int, value: T) -> None:
        self.a_position = ap
        self.b_position = bp

        self.value = value


type CommonPoints[T] = List[CommonPoint]


class CommonalityResult[T]:
    a_ranges: List[Range]
    b_ranges: List[Range]

    common: CommonRange | None

    def __init__(
        self,
        a_ranges: List[Range],
        b_ranges: List[Range],
        common: CommonRange | None,
    ) -> None:
        self.a_ranges = a_ranges
        self.b_ranges = b_ranges

        self.common = common


type CommonalityResult2[T] = Tuple[List[Range], List[Range], CommonRange | None]
