import re

from sanitisation.stopwords import StopwordRemover
from core.strings import EMPTY, SPACE


class SanitiserOptions:
    stopwords: str


class Sanitiser:
    options: SanitiserOptions | None

    def __init__(self, options: SanitiserOptions | None) -> None:
        self.options = options

    def sanitise(self, content: str) -> str:
        content = content.lower()
        content = re.sub(r"/[']/g", EMPTY, content)
        content = re.sub(r"/[^\w\s]|_/g", EMPTY, content) # TODO: hmm, not working yet. check python docs
        content = re.sub(r"/(\s{2,})/g", SPACE, content)

        if self.options and self.options.stopwords:
            stopword_remover = StopwordRemover()

            content = stopword_remover.process(content, self.options.stopwords)

        return content
