from typing import Dict, List

from core.commonality import CommonSequence
from core.sink import Sink


class Memo[T](Sink[CommonSequence]):
    prior: Dict[int, CommonSequence]

    current: Dict[int, CommonSequence]

    def __init__(self, items: List[CommonSequence]) -> None:
        super().__init__()

        self.items = items

        self.prior = {}
        self.current = {}

    def record(self, ai: int, bi: int, a_value: T, b_value: T):
        if a_value != b_value:
            return

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
            x = CommonSequence(ai, bi, values=[a_value])

            self.items.append(x)

            current[bi] = x

        if not update(bi, a_value):
            create(ai, bi, a_value)

    def next(self):
        self.prior = self.current

        self.current = {}
