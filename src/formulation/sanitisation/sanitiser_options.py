from formulation.sanitisation.sanitiser_kind import SanitiserKind


class SanitiserOptions:
    def __init__(self, stopwords: str | None = None) -> None:
        self.stopwords = stopwords

    clean: bool = True

    pad_new_line: bool = True

    periods_to_new_line: bool = True

    prepare: bool = True

    stopwords: str | None

    strip_frontmatter: bool = True

    strip_links: bool = True

    strip_callouts: bool = True

    strip_any_numeric: bool = True

    sanitiser_kind: SanitiserKind | None = None

    regex_stopwords: bool | None = None

    def assign(self, items: dict[str, object]):
        for key in items:
            value = items[key]

            self.__setattr__(key, value)
