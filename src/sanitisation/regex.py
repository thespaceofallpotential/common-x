import abc

from core.strings import EMPTY, SPACE


class IRegex(metaclass=abc.ABCMeta):
    pattern: str
    type: str = EMPTY
    positive: bool


class BasicRegex(IRegex):
    def __init__(self, regex: str, positive: bool = True) -> None:
        self.pattern = regex
        self.positive = positive

        self.type = "basic"

    def __repr__(self) -> str:
        return f"r:{self.pattern} p:{self.positive}"


class StructuredRegex(BasicRegex):
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

        self.start = start
        self.mid = mid
        self.end = end
        self.body = body

        self.type = "structured"

    def __repr__(self) -> str:
        def parts() -> str:
            y: list[str] = []
            if self.start:
                y.append(f"s:{self.start}")
            if self.mid:
                y.append(f"m:{self.mid}")
            if self.end:
                y.append(f"e:{self.end}")
            if self.body:
                y.append(f"b:{self.body}")

            return str.join(SPACE, y)

        return f"r:{self.pattern} p:{self.positive} {parts()}".strip()
