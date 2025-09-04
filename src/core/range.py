class PartitionVector:
    position: int
    length: int

    def __init__(self, position: int, length: int):
        self.position = position
        self.length = length

    def getEnd(self):
        return self.position + self.length

    def __repr__(self) -> str:
        return f"p:{self.position} l:{self.length}"


class Range[T](PartitionVector):
    def __init__(
        self,
        values: list[T],
        position: int = 0,
        parts: set[T] | None = None,
    ):
        super().__init__(position, len(values))
        
        self.values = values

        self.parts = parts if parts else set(values)

    def getIndex(self, value: T, start: int = 0) -> int:
        return self.values.index(value, start)

    def __repr__(self) -> str:
        return f"p:{self.position} l:{self.length} v:{self.values} s:{self.parts=})"
