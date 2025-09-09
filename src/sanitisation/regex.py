import abc
from enum import Enum

from core.strings import EMPTY, SPACE


class RegexTypes(Enum):
    NONE = 0
    BASIC = 1
    STRUCTURED = 2


class IRegex(metaclass=abc.ABCMeta):
    pattern: str
    type: RegexTypes
    positive: bool


class BasicRegex(IRegex):
    def __init__(self, regex: str, positive: bool = True) -> None:
        self.pattern = regex
        self.positive = positive

        self.type = RegexTypes.BASIC

    def __repr__(self) -> str:
        return f"r:{self.pattern} p:{self.positive}"


class StructuredRegex(BasicRegex):
    keys: dict[str, str]

    def __init__(
        self,
        pattern: str,
        positive: bool = True,
        start: str | None = None,
        mid: str | None = None,
        end: str | None = None,
        body: str | None = None,
    ) -> None:
        super().__init__(pattern, positive)

        self.keys = {}

        if start:
            self.keys["start"] = start
            self.keys["first"] = start[0:1]

        if mid:
            self.keys["mid"] = mid

        if end:
            self.keys["end"] = end

        if body:
            self.keys["body"] = body

        self.type = RegexTypes.STRUCTURED

    def __repr__(self) -> str:
        def parts() -> str:
            return f"{self.keys}"

        return f"r:{self.pattern} p:{self.positive} {parts()}".strip()
