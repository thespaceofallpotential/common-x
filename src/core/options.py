from core.range import Range


class Options:
    halt: bool | None

    minimumSequenceLength: int = 0

    def sufficient[T](self, range: Range) -> bool:
        return range.length >= self.minimumSequenceLength
