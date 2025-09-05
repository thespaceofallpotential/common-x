from typing import List, Set
from core.types import TPositionMap


class GlobalDomain:
    words: Set[str]

    values: List[str]

    word_position_map: TPositionMap[str]

    def __init__(self, words: Set[str]) -> None:
        self.words = words

        self.values = list(words)  # TODO: sort

        self.word_position_map = {}

        for i, value in enumerate(self.values):
            self.word_position_map[value] = i

    def to_words(self, tokens: List[int]) -> List[str]:
        return list(map(lambda t: self.values[t], tokens))

    def to_tokens(self, words: List[str]) -> List[int]:
        return list(map(lambda w: self.word_position_map[w], words))
