class Analysis[T]:
    i: int

    item: T

    def __init__(self, i: int, item: T):
        self.i = i

        self.item = item

    def __repr__(self) -> str:
        return f"i:{self.i}, v:{self.item} "
