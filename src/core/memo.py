from core.commonality import CommonRange
from typing import Dict, List, TypeVar


T = TypeVar("T", int, str)


class Memo[T]:
    commonRanges: List[CommonRange]

    prior: Dict[int, CommonRange] = dict()

    current: Dict[int, CommonRange] = dict()

    def __init__(self, items: List[CommonRange]) -> None:
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
            x = CommonRange(ai, bi, values=[aValue])

            items.append(x)

            current[bi] = x

        if not update(bi, aValue):
            create(ai, bi, aValue)

    def next(self):
        self.prior = self.current

        self.current = dict()
