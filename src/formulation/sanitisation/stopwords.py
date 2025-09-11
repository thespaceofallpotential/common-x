import re

from core.strings import EMPTY, NEWLINE, SPACE
from formulation.sanitisation.regex_multi_pattern import (
    get_pattern,
    get_structured_pattern_list,
)


class StopwordRemover:
    def process_regex(self, content: str, stopwords: str) -> str:
        exclude = stopwords.split(NEWLINE)

        patterns = get_pattern(exclude)

        items = get_structured_pattern_list(content, patterns)

        for item in items:
            content = re.sub(item, EMPTY, content)

        return content

    def process(self, content: str, stopwords: str) -> str:
        exclude = set(stopwords.split(NEWLINE))

        lines = content.split(NEWLINE)

        def process_line(line: str) -> str:
            words = line.split(SPACE)

            words = filter(lambda x: x not in exclude, words)

            return str.join(SPACE, words)

        lines = list(map(process_line, lines))

        return str.join(NEWLINE, lines)


def remove_stopwords(x: str, stopwords: str) -> str:
    stopword_remover = StopwordRemover()

    x = stopword_remover.process(x, stopwords)

    return x
