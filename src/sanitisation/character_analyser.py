from typing import List

from core.sequence import Sequence
from sanitisation.analyser import Analyser
from sanitisation.analysis import Analysis


class CharacterAnalyser(Analyser):
    def process(self, content: set):
        self.item = Sequence(list(content))


def get_elements(items: List[Analysis[Sequence]]) -> List[set]:
    return list(map(lambda x: x.item.elements, items))
