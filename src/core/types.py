from typing import Dict, TypeVar


T = TypeVar("T")

type TPositionMap[T] = Dict[T, int]


def safe_index(value: str, pattern: str, i_from: int = 0):
    try:
        return value.index(pattern, i_from)
    except:  # noqa: E722
        return -1


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
