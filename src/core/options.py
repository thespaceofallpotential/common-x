from core.sequence import Sequence


class Options:
    halt: bool | None

    minimumSequenceLength: int = 0

    def sufficient(self, sequence: Sequence) -> bool:
        return sequence.length >= self.minimumSequenceLength
