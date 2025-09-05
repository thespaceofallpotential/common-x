from core.range import Range


class Options:
    halt: bool | None

    minimumSequenceLength: int = 0

    def sufficient(self, r: Range) -> bool:
        return r.length >= self.minimumSequenceLength
