import re
from formulation.sanitisation.sanitiser import (
    ISanitiser,
    SanitiserOptions,
    SanitiserResult,
)
from formulation.sanitisation.stopwords import StopwordRemover


class BasicSanitiser(ISanitiser):
    options: SanitiserOptions

    def __init__(self, options: SanitiserOptions) -> None:
        self.options = options

    def sanitise(self, content: str, i: int | None = None) -> SanitiserResult:
        result = SanitiserResult()

        content = re.sub(r"\.|\,", r"", content)

        if self.options.stopwords is not None:
            stopword_remover = StopwordRemover()

            if self.options.regex_stopwords:
                content = stopword_remover.process_regex(
                    content, self.options.stopwords
                )
            else:
                content = stopword_remover.process(content, self.options.stopwords)

        result.content = content

        return result
