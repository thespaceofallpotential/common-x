from typing import List
from data.file import File
from formulation.sanitisation.sanitiser import (
    ISanitiser,
    SanitiserKind,
    SanitiserOptions,
    SanitiserResult,
)
from utils.progress import TimedProgress


def sanitise_contents(
    sanitiser: ISanitiser, contents: list[str]
) -> List[SanitiserResult]:
    items: List[SanitiserResult] = []

    length = len(contents)

    progress = TimedProgress("sanitise content", length)

    for i, content in enumerate(contents):
        progress.update(i)

        result = sanitiser.sanitise(content, i)

        items.append(result)

    progress.complete()

    return items


def sanitise_files(sanitiser: ISanitiser, files: List[File]) -> List[SanitiserResult]:
    items: List[SanitiserResult] = []

    progress = TimedProgress("sanitisation", len(files))

    for i, file in enumerate(files):
        progress.update(i)

        result = sanitiser.sanitise(file.content)

        items.append(result)

    progress.complete()

    return items


def get_basic_options(stopwords: str) -> SanitiserOptions:
    options = SanitiserOptions(stopwords)

    options.sanitiser_kind = SanitiserKind.BASIC

    return options


def get_stopword_options(stopwords: str) -> SanitiserOptions:
    options = SanitiserOptions(stopwords)

    options.sanitiser_kind = SanitiserKind.STOPWORD

    return options
