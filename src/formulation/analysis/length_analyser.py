from typing import List

from formulation.analysis.analyser import Analyser
from formulation.analysis.analysis import Analysis


class LengthAnalyser(Analyser[int]):
    def process(self, content: set):
        self.item = len(content)


def get_length(items: List[Analysis[int]]) -> List[int]:
    return list(map(lambda x: x.item, items))
