from core.range import Range
from typing import Dict, List, Tuple, TypeVar

T = TypeVar("T", int, str)


type TPositionMap[T] = Dict[T, int]


class PositionedValues[T]:
    position: int
    values: List[T]

    def __init__(self, position: int, values: List[T]):
        self.position = position
        self.values = values


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


# export type PositionNext<T extends Token | Word> = [Position, T | undefined];
# export const i_next_t = 1;

# export type CommonSequence<T extends Token | Word> = {
#     i: [ati: number, bti: number][];
#     t: T[];
#     w: string[];
#     s: string;
# };

# not yet... :D
# bound adjacency map: qualitative structural index (form-based as opposed to spatial space-based)
# bound adjacency map: -- think generalised suffix-tree, but rather granular adjacency -- so less (redundant) duplication
# bound adjacency map/ qualitative structural index (form-based index) : --do you see what this is yet?! ;)
# export type BoundAdjacencyMap<T extends Token | Word> = Map<T, Array<PositionNext<T>>>;
# export type PositionNextMap<T extends Token | Word> = BoundAdjacencyMap<T>;
