import re

from core.strings import EMPTY, NEWLINE, SPACE
from formulation.sanitisation.regex_multi_pattern import (
    get_pattern,
    get_structured_pattern_list,
    get_word_pattern,
)


class StopwordRemover:
    def process_regex(self, content: str, stopwords: str) -> str:
        # items = re.findall(r"(?:^| )([^\\ ])", content)

        exclude = stopwords.split(NEWLINE)

        # original = content

        for item in exclude:
            content = re.sub(get_word_pattern(item), EMPTY, content)

        # print(f"{len(original)} | {len(content)}")
        # # elements = set(map(lambda x: x, items))
        # # elements = set(items)

        # # exclude = list(filter(lambda x: x[:1] in elements, exclude))

        # pattern = get_pattern(exclude)

        # # items = get_structured_pattern_list(content, patterns)

        # # for item in items:
        # content2 = re.sub(pattern, EMPTY, original)

        # print(f"{len(original)} | {len(content)} | {len(content2)}")

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
