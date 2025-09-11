import abc

from enum import Enum

from formulation.analysis.analysis import Analysis


class AnalyserType(Enum):
    NONE = 0
    LENGTH = 1
    CHARACTER = 2
    WORD = 3
    PHRASE = 4


class IAnalyser(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def process(self, content: str):
        pass

    @abc.abstractmethod
    def get_analysis(self, i: int) -> Analysis:
        pass


class Analyser[T](IAnalyser, metaclass=abc.ABCMeta):
    item: T | None

    @abc.abstractmethod
    def process(self, content: str):
        pass

    def get_analysis(self, i: int) -> Analysis:
        analysis = Analysis(i, self.item)

        self.item = None

        return analysis

    def __repr__(self) -> str:
        return f"{self.__class__}"
