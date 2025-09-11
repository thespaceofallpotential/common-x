from core.strings import EMPTY


class Fetched:
    i_start: int = 0
    i_end: int = 0
    value: str = EMPTY

    def __repr__(self) -> str:
        return f"s:{self.i_start} e:{self.i_end} v:{self.value}"
