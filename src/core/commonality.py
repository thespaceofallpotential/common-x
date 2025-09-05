from typing import Dict, List, Tuple, cast
from core.sequence import Sequence
from core.types import values_str


class CommonSequence[T]:
    a_position: int
    b_position: int

    values: List[T]

    def __init__(self, a_position: int, b_position: int, values: List[T] | None = None):
        self.a_position = a_position
        self.b_position = b_position

        self.values = values if values else []

    def __repr__(self) -> str:
        return f"a:{self.a_position} b:{self.b_position}, v:{values_str(cast(List[str], self.values))}"


type CommonSequences[T] = Dict[int, CommonSequence]


class BatchSequences[C]:
    ai: int
    bi: int

    items: List[C]

    def __init__(self, ai: int, bi: int, items: List[C]):
        self.ai = ai
        self.bi = bi

        self.items = items

    def __repr__(self) -> str:
        return f"ai:{self.ai} bi:{self.bi}, c: --[{str.join(': ', list(map(lambda item: f'{item}', self.items)))}]-- "


class CommonPoint[T]:
    a_position: int
    b_position: int

    value: T

    def __init__(self, ap: int, bp: int, value: T) -> None:
        self.a_position = ap
        self.b_position = bp

        self.value = value


type CommonPoints[T] = List[CommonPoint]


class CommonalityResult[T]:
    a_sequences: List[Sequence]
    b_sequences: List[Sequence]

    common: CommonSequence | None

    def __init__(
        self,
        a_sequences: List[Sequence],
        b_sequences: List[Sequence],
        common: CommonSequence | None,
    ) -> None:
        self.a_sequences = a_sequences
        self.b_sequences = b_sequences

        self.common = common


type CommonalityResult2[T] = Tuple[
    List[Sequence], List[Sequence], CommonSequence | None
]
