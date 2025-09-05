from typing import Dict, List, TypeVar

from core.commonality import CommonRange


T = TypeVar("T", int, str)


class Memo[T]:
    common_ranges: List[CommonRange]

    prior: Dict[int, CommonRange]

    current: Dict[int, CommonRange]

    def __init__(self, items: List[CommonRange]) -> None:
        self.common_ranges = items
        self.prior = {}
        self.current = {}

    def record(self, ai: int, bi: int, a_value: T, b_value: T):
        if a_value != b_value:
            return

        items = self.common_ranges
        prior = self.prior
        current = self.current

        def update(bi: int, a_value: T) -> bool:
            existing = prior.get(bi - 1)

            if not existing:
                return False

            existing.values.append(a_value)

            current[bi] = existing

            return True

        def create(ai: int, bi: int, a_value: T):
            x = CommonRange(ai, bi, values=[a_value])

            items.append(x)

            current[bi] = x

        if not update(bi, a_value):
            create(ai, bi, a_value)

    def next(self):
        self.prior = self.current

        self.current = {}
