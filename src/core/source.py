from typing import List
from core.global_domain import GlobalDomain
from core.sequence import Sequence


class Source:
    a_words: Sequence
    b_words: Sequence

    global_domain: GlobalDomain

    a_tokens: Sequence
    b_tokens: Sequence

    def __init__(self, a_words: List[str], b_words: List[str]) -> None:
        self.a_words = Sequence(a_words)

        self.b_words = Sequence(b_words)

        a_word_elements = self.a_words.elements

        b_word_elements = self.b_words.elements

        self.global_domain = GlobalDomain(a_word_elements.union(b_word_elements))

        a_tokens = self.global_domain.to_tokens(self.a_words.values)

        b_tokens = self.global_domain.to_tokens(self.b_words.values)

        self.a_tokens = Sequence(a_tokens)

        self.b_tokens = Sequence(b_tokens)
