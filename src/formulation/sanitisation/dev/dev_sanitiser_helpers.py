from typing import List
from data.file import File, FileState
from formulation.sanitisation.sanitiser import ISanitiser
from core.strings import SPACE
from formulation.sanitisation.common import ISanitiser
from utils.progress import TimedProgress


def strip_numbers(x: str) -> str:
    return str.join(
        SPACE,
        list(
            filter(
                lambda y: not (y.isnumeric() or any(char.isdigit() for char in x)),
                x.split(SPACE),
            )
        ),
    )


def only_numbers(x: str) -> list[str]:
    return list(filter(lambda y: y.isnumeric(), x.split(SPACE)))


def sanitise_file(sanitiser: ISanitiser, file: File):
    result = sanitiser.sanitise(file.content)

    file.state = FileState.OK

    words = result.content.split(SPACE)

    if file.state == FileState.OK:
        large = list(filter(lambda x: len(x) > 100, words))

        if len(large) > 0:
            # print(large)
            file.state = FileState.ERROR
            file.large = large

    numbers = only_numbers(result.content)

    if len(numbers) > 5:
        file.state = FileState.ERROR
        file.numbers = numbers

    content = strip_numbers(result.content)

    file.content = content


def sanitise_files(sanitiser: ISanitiser, files: List[File]):
    progress = TimedProgress("sanitisation", len(files))

    for i, file in enumerate(files):
        progress.update(i)

        sanitiser.sanitise(file.content)

        # sanitise_file(sanitiser, file)

    progress.complete()
