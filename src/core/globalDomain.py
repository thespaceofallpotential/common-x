from core.types import TPositionMap


class GlobalDomain:
    words: set[str]

    values: list[str]

    wordPositionMap: TPositionMap[str]

    def __init__(self, words: set[str]) -> None:
        self.words = words

        self.values = list(words)  # TODO: sort

        self.wordPositionMap = dict()

        for i, value in enumerate(self.values):
            self.wordPositionMap[value] = i

    def toWords(self, tokens: list[int]) -> list[str]:
        return list(map(lambda t: self.values[t], tokens))

    def toTokens(self, words: list[str]) -> list[int]:
        return list(map(lambda w: self.wordPositionMap[w], words))
