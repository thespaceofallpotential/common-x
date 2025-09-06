from typing import List
from batch.ordered_domain import OrderedDomain
from core.sequence import Sequence
from data.file import File
from data.source_helper import SourceHelper
from sanitisation.sanitiser import SanitiserOptions
from sanitisation.sanitiser_factory import build_sanitiser
from sanitisation.string_helpers import to_words


class Source:
    __helper: SourceHelper

    __files: List[File]

    def __init__(self, helper: SourceHelper) -> None:
        self.__helper = helper

        self.__files = self.__helper.get_files()

    def get_sanitised(self):
        stopwords_file = self.__helper.get_file("stopwords.txt")

        sanitiser_options = SanitiserOptions(stopwords_file.content)

        sanitiser = build_sanitiser(sanitiser_options)

        sanitised = list(map(lambda x: sanitiser.sanitise(x.content), self.__files))

        return sanitised

    def get_sequences(self, sanitised: List[str] | None = None) -> List[Sequence]:
        if not sanitised:
            sanitised = self.get_sanitised()

        return list(map(lambda x: Sequence(to_words(x)), sanitised))


class Source2:
    a_words: Sequence
    b_words: Sequence

    ordered_domain: OrderedDomain

    a_tokens: Sequence
    b_tokens: Sequence

    def __init__(self, a_words: List[str], b_words: List[str]) -> None:
        self.a_words = Sequence(a_words)

        self.b_words = Sequence(b_words)

        a_word_elements = self.a_words.elements

        b_word_elements = self.b_words.elements

        self.ordered_domain = OrderedDomain(a_word_elements.union(b_word_elements))

        a_tokens = self.ordered_domain.to_tokens(self.a_words.values)

        b_tokens = self.ordered_domain.to_tokens(self.b_words.values)

        self.a_tokens = Sequence(a_tokens)

        self.b_tokens = Sequence(b_tokens)
