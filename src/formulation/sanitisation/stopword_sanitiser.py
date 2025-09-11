from formulation.sanitisation.sanitiser import (
    ISanitiser,
    SanitiserOptions,
    SanitiserResult,
)
from formulation.sanitisation.stopwords import StopwordRemover


class StopwordSanitiser(ISanitiser):
    options: SanitiserOptions

    def __init__(self, options: SanitiserOptions) -> None:
        self.options = options

    def sanitise(self, content: str, i: int | None = None) -> SanitiserResult:
        result = SanitiserResult()

        if self.options.stopwords is not None:
            stopword_remover = StopwordRemover()

            content = stopword_remover.process(content, self.options.stopwords)

        result.content = content

        return result
