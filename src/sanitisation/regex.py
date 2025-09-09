import abc
from enum import Enum
from typing import Dict


class RegexTypes(Enum):
    NONE = 0
    BASIC = 1
    STRUCTURED = 2


class FragmentTypes(Enum):
    NONE = 0

    FIRST = 1
    START = 2
    MIDDLE = 3
    END = 4
    LAST = 5

    ALL = 10
    BODY = 11


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
    keys: Dict[FragmentTypes, str]

    def __init__(
        self,
        pattern: str,
        keys: Dict[FragmentTypes, str] | None = None,
        positive: bool = True,
    ) -> None:
        super().__init__(pattern, positive)

        self.keys = keys if keys is not None else {}

        self.type = RegexTypes.STRUCTURED

        self.__initialise()

    def __initialise(self):
        start = self.keys.get(FragmentTypes.START)

        if start:
            self.keys[FragmentTypes.FIRST] = start[0:1]

    def __repr__(self) -> str:
        def parts() -> str:
            return f"{self.keys}"

        return f"r:{self.pattern} p:{self.positive} {parts()}".strip()
