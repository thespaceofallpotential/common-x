from core.strings import NEWLINE, SPACE


class StopwordRemover:
    def process(self, content: str, stopwords: str) -> str:
        lines = content.split(NEWLINE)

        exclude = set(stopwords.split(NEWLINE))

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
