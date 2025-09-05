from core.strings import NEWLINE, SPACE


class StopwordRemover:
    def process(self, content: str, stopwords: str) -> str:
        lines = content.split(NEWLINE)

        exclude = set(stopwords.split(NEWLINE))

        def process_line(line: str) -> str:
            words = line.split(SPACE)

            words = filter(lambda x: x not in exclude, words)

            return str.join(SPACE, words)

        lines = list(map(lambda x: process_line(x), lines))

        return str.join(NEWLINE, lines)
