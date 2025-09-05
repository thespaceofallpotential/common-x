from typing import List
from core.global_domain import GlobalDomain
from core.range import Range
from data.example1Source import A


class Source:
    aWordRange: Range
    bWordRange: Range

    globalDomain: GlobalDomain

    aTokenRange: Range
    bTokenRange: Range

    def __init__(self, aWords: List[str], bWords: List[str]) -> None:
        self.aWordRange = Range(aWords)

        self.bWordRange = Range(bWords)

        aWordSet = self.aWordRange.elements

        bWordSet = self.bWordRange.elements

        self.globalDomain = GlobalDomain(aWordSet.union(bWordSet))

        aTokens = self.globalDomain.toTokens(self.aWordRange.values)

        bTokens = self.globalDomain.toTokens(self.bWordRange.values)

        self.aTokenRange = Range(aTokens)

        self.bTokenRange = Range(bTokens)
