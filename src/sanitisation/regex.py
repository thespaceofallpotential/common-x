import abc
from enum import Enum
import re
from typing import Callable


class FragmentTypes(Enum):
    NONE = 0

    FIRST = 1
    START = 2
    MIDDLE = 3
    END = 4
    LAST = 5
    END_BEFORE = 6

    ALL = 10
    BODY = 11


class StructuredRegexFragments:
    first: str | None
    start: str | None
    middle: str | None
    end: str | None
    last: str | None
    end_before: str | None
    all: str | None
    body: str | None
    transform: Callable[..., str] | None = None

    def __init__(
        self,
        first: str | None = None,
        start: str | None = None,
        middle: str | None = None,
        end: str | None = None,
        last: str | None = None,
        end_before: str | None = None,
        all: str | None = None,
        body: str | None = None,
        transform: Callable[..., str] | None = None,
    ) -> None:
        self.first = first
        self.start = start
        self.middle = middle
        self.end = end
        self.last = last
        self.end_before = end_before
        self.all = all
        self.body = body
        self.transform = transform


class IRegex(metaclass=abc.ABCMeta):
    pattern: str
    positive: bool


class BasicRegex(IRegex):
    def __init__(self, regex: str, positive: bool = True) -> None:
        self.pattern = regex
        self.positive = positive

    def __repr__(self) -> str:
        return f"r:{self.pattern} p:{self.positive}"


class StructuredRegex(BasicRegex):
    fragments: StructuredRegexFragments  # Dict[FragmentTypes, str]

    fixed_index: int | None

    def __init__(
        self,
        pattern: str,
        fragments: StructuredRegexFragments | None = None,
        fixed_index: int | None = None,
        positive: bool = True,
    ) -> None:
        super().__init__(pattern, positive)

        self.fragments = (
            fragments if fragments is not None else StructuredRegexFragments()
        )

        self.fixed_index = fixed_index

        self.__initialise()

    def __initialise(self):
        start = self.fragments.start

        if start is not None:
            self.fragments.first = start[0:1]

    def is_index_ok(self, i: int):
        return self.fixed_index is None or self.fixed_index == i

    def get_fragment_pattern(self):
        fragments = self.fragments

        if (
            fragments.start is not None
            and fragments.middle is not None
            and fragments.end is not None
        ):
            return f"{re.escape(fragments.start)}|{re.escape(fragments.middle)}|{re.escape(fragments.end)}"

        if fragments.start is not None and fragments.end is not None:
            return f"{re.escape(fragments.start)}|{re.escape(fragments.end)}"

        return None

    def __repr__(self) -> str:
        def parts() -> str:
            return f"{self.fragments}"

        return f"r:{self.pattern} fi:{self.fixed_index} p:{self.positive} {parts()}".strip()
