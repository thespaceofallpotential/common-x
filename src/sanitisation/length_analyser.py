from typing import List

from sanitisation.analyser import Analyser
from sanitisation.analysis import Analysis


class LengthAnalyser(Analyser[int]):
    def process(self, content: set):
        self.item = len(content)


def get_length(items: List[Analysis[int]]) -> List[int]:
    return list(map(lambda x: x.item, items))
