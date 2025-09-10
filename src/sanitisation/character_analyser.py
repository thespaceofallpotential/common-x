from typing import List

from core.sequence import Sequence
from sanitisation.analyser import Analyser
from sanitisation.analysis import Analysis


class CharacterAnalyser(Analyser):
    def process(self, content: set):
        self.item = Sequence(list(content))


def get_elements(items: List[Analysis[Sequence]]) -> List[set]:
    return list(map(lambda x: x.item.elements, items))


def to_character_list(items: list[Analysis]):
    character_sets = get_elements(items)

    characters = set()

    for x in character_sets:
        characters = characters.union(x)

    character_list = list(characters)

    character_list.sort()

    return character_list


def to_character_list2(words: list[str]):
    characters = set()

    for word in words:
        characters = characters.union(set(list(word)))

    character_list = list(characters)

    character_list.sort()

    return character_list
