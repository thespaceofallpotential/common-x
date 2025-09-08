import abc
from enum import Enum

from sanitisation.analysis import Analysis


class AnalyserType(Enum):
    NONE = 0
    CHARACTER = 1
    WORD = 2
    PHRASE = 3


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
