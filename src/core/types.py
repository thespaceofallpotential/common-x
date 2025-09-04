from core.range import Range


type TPositionMap[T] = dict[T, int]


class CommonRange[T]:
    aPosition: int
    bPosition: int

    values: list[T]

    def __init__(self, aPosition: int, bPosition: int, values: list[T] | None = None):
        self.aPosition = aPosition
        self.bPosition = bPosition

        self.values = values if values else []

    def __repr__(self) -> str:
        return f"a:{self.aPosition} b:{self.bPosition}, v:{self.values})"


type CommonRanges = dict[int, CommonRange]


class CommonalityResult[T]:
    aRanges: list[Range[T]]
    bRanges: list[Range[T]]

    common: CommonRange[T] | None

    def __init__(
        self,
        aRanges: list[Range[T]],
        bRanges: list[Range[T]],
        common: CommonRange[T] | None,
    ) -> None:
        self.aRanges = aRanges
        self.bRanges = bRanges
        self.common = common


type CommonalityResult2[T] = tuple[list[Range[T]], list[Range[T]], CommonRange[T] | None]

# export type CommonPoint<T extends Token | Word> = [ap: Position, bp: Position, v: T];
# export type CommonPoints<T extends Token | Word> = CommonPoint<T>[];

# export type DivideDismissConquer<T extends Token | Word> = [a: IRange<T>[], b: IRange<T>[], CommonRange<T> | undefined];
