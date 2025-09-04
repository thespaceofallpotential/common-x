from core.range import Range
from typing import Dict, List, Tuple, TypeVar

T = TypeVar("T", int, str)


type TPositionMap[T] = Dict[T, int]


class CommonRange[T]:
    aPosition: int
    bPosition: int

    values: List[T]

    def __init__(self, aPosition: int, bPosition: int, values: List[T] | None = None):
        self.aPosition = aPosition
        self.bPosition = bPosition

        self.values = values if values else []

    def __repr__(self) -> str:
        return f"a:{self.aPosition} b:{self.bPosition}, v:{self.values})"


type CommonRanges[T] = Dict[int, CommonRange]


class CommonPoint[T]:
    aPosition: int
    bPosition: int

    value: T

    def __init__(self, ap: int, bp: int, value: T) -> None:
        self.aPosition = ap
        self.bPosition = bp

        self.value = value


type CommonPoints[T] = List[CommonPoint]


class CommonalityResult[T]:
    aRanges: List[Range]
    bRanges: List[Range]

    common: CommonRange | None

    def __init__(
        self,
        aRanges: List[Range],
        bRanges: List[Range],
        common: CommonRange | None,
    ) -> None:
        self.aRanges = aRanges
        self.bRanges = bRanges

        self.common = common


type CommonalityResult2[T] = Tuple[List[Range], List[Range], CommonRange | None]

# export type CommonPoint<T extends Token | Word> = [ap: Position, bp: Position, v: T];
# export type CommonPoints<T extends Token | Word> = CommonPoint<T>[];

# export type DivideDismissConquer<T extends Token | Word> = [a: IRange<T>[], b: IRange<T>[], CommonRange<T> | undefined];
