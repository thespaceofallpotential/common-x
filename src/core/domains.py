from typing import List, Set
from core.types import TPositionMap
from core.sequence import Sequence
from core.sequence_helpers import get_union


class WordDomain:
    words: Set[str]

    values: List[str]

    def __init__(self, sequences: List[Sequence]) -> None:
        self.words = get_union(sequences)

        self.values = list(self.words)

        self.values.sort()


class TokenDomain(WordDomain):
    word_position_map: TPositionMap[str]

    def __init__(self, sequences: List[Sequence]) -> None:
        super().__init__(sequences)

        self.word_position_map = {}

        for i, value in enumerate(self.values):
            self.word_position_map[value] = i

    def to_words(self, tokens: List[int]) -> List[str]:
        return list(map(lambda t: self.values[t], tokens))

    def to_tokens(self, words: List[str]) -> List[int]:
        return list(map(lambda w: self.word_position_map[w], words))

    def to_token_sequences(self, sequences: List[Sequence[str]]) -> List[Sequence[int]]:
        return list(map(lambda x: Sequence(self.to_tokens(x.values)), sequences))
