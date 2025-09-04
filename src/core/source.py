from core.globalDomain import GlobalDomain
from core.range import Range
from data.example1Source import A


class Source:
    aWordRange: Range[str]
    bWordRange: Range[str]

    globalDomain: GlobalDomain

    aTokenRange: Range[int]
    bTokenRange: Range[int]

    def __init__(self, aWords: list[str], bWords: list[str]) -> None:

        self.aWordRange = Range(aWords)

        self.bWordRange = Range(bWords)

        aWordSet = self.aWordRange.parts

        bWordSet = self.bWordRange.parts

        self.globalDomain = GlobalDomain(aWordSet.union(bWordSet))

        aTokens = self.globalDomain.toTokens(self.aWordRange.values)

        bTokens = self.globalDomain.toTokens(self.bWordRange.values)

        self.aTokenRange = Range(aTokens)

        self.bTokenRange = Range(bTokens)
