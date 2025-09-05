from typing import Dict, List, Set, TypeVar, cast

from core.strings import SPACE


T = TypeVar("T", int, str)


type TPositionMap[T] = Dict[T, int]


class PositionedValues[T]:
    position: int
    values: List[T]

    def __init__(self, position: int, values: List[T]):
        self.position = position
        self.values = values

    def __repr__(self) -> str:
        return f"p:{self.position} v:{values_str(cast(List[str], self.values))}"


def values_str(values: List[T]) -> str:
    return str.join(SPACE, cast(List[str], values))


def elements_str(elements: Set[T]) -> str:
    return str.join(SPACE, cast(List[str], list(elements)))


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
