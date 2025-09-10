from typing import Dict

from core.strings import EMPTY
from sanitisation.sanitisation_regex import SanitisationTypes


class Fetched:
    i_start: int = 0
    i_end: int = 0
    value: str = EMPTY

    def __repr__(self) -> str:
        return f"s:{self.i_start} e:{self.i_end} v:{self.value}"


class QualityClass:
    structured_sanitisation: Dict[SanitisationTypes, str]

    def __init__(self) -> None:
        self.structured_sanitisation = {}

    def is_structured(self):
        return len(self.structured_sanitisation) > 0


class PositiveVector:
    i: int
    length: int

    def __init__(self, i: int, length: int) -> None:
        self.i = i
        self.length = length
