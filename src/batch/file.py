from core.sequence import Sequence


class File[T]:
    path: str
    sequence: Sequence

    def __init__(self, path: str, sequence: Sequence) -> None:
        self.path = path
        self.sequence = sequence
