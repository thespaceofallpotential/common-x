from typing import List
from data.file import File, FileState
from sanitisation.sanitiser import Sanitiser
from sanitisation.markkdown_sanitiser_helper import EXCALIDRAW_PLUGIN
from core.strings import SPACE


def strip_numbers(x: str) -> str:
    return str.join(SPACE, list(filter(lambda y: not y.isnumeric(), x.split(SPACE))))


def only_numbers(x: str) -> list[str]:
    return list(filter(lambda y: y.isnumeric(), x.split(SPACE)))


def sanitise_file(sanitiser: Sanitiser, file: File):
    result = sanitiser.sanitise(file.content)

    file.state = FileState.OK

    if result.frontmatter:
        if EXCALIDRAW_PLUGIN in result.frontmatter:
            file.state = FileState.ERROR
            file.frontmatter = result.frontmatter

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


def sanitise_files(sanitiser: Sanitiser, files: List[File]):
    for file in files:
        sanitise_file(sanitiser, file)
