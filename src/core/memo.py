from core.types import CommonRange, CommonRanges


class Memo[T]:
    commonRanges: list[CommonRange[T]] = []

    prior: dict[int, CommonRange[T]] = dict()

    current: dict[int, CommonRange[T]] = dict()

    def __init__(self, items: list[CommonRange[T]]) -> None:
        self.commonRanges = items

    def record(self, ai: int, bi: int, aValue: T, bValue: T):
        if aValue != bValue:
            return

        items = self.commonRanges
        prior = self.prior
        current = self.current

        def update(bi: int, aValue: T) -> bool:
            existing = prior.get(bi - 1)

            if not existing:
                return False

            existing.values.append(aValue)

            current[bi] = existing

            return True

        def create(ai: int, bi: int, aValue: T):
            x = CommonRange[T](ai, bi, values=[aValue])

            items.append(x)

            current[bi] = x

        if not update(bi, aValue):
            create(ai, bi, aValue)

    def next(self):
        self.prior = self.current

        self.current = dict()
