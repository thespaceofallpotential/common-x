from typing import List, Set
from core.types import TPositionMap


class GlobalDomain:
    words: Set[str]

    values: List[str]

    wordPositionMap: TPositionMap[str]

    def __init__(self, words: Set[str]) -> None:
        self.words = words

        self.values = list(words)  # TODO: sort

        self.wordPositionMap = dict()

        for i, value in enumerate(self.values):
            self.wordPositionMap[value] = i

    def toWords(self, tokens: List[int]) -> List[str]:
        return list(map(lambda t: self.values[t], tokens))

    def toTokens(self, words: List[str]) -> List[int]:
        return list(map(lambda w: self.wordPositionMap[w], words))
