from typing import List


class Sink[T]:
    items: List[T]

    def __init__(self) -> None:
        self.items = []

    def add(self, item: T):
        self.items.append(item)

    def add_all(self, items: List[T]):
        self.items.extend(items)


def sink_factory[T]() -> Sink[T]:
    return Sink[T]()
