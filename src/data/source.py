from typing import List

from core.sequence import Sequence
from core.strings import EMPTY
from data.file import File
from data.source_helper import SourceHelper
from formulation.sanitisation.common import SanitiserOptions
from formulation.sanitisation.string_helpers import to_words
from formulation.sanitisation.elemental_curator import (
    ElementalCurator,
    curate_and_collect,
)
from formulation.sanitisation.sanitiser import sanitise_contents
from formulation.sanitisation.sanitiser_factory import build_sanitiser
from formulation.analysis.analyser import AnalyserType
from formulation.analysis.character_analyser import to_character_list
from formulation.analysis.content_analysis_engine import content_analysis_runner
from utils.progress import TimedProgress
from utils.io_helper import ScanOptions


def parse_excluding(content: str, exclude: list[str]) -> str:
    for value in exclude:
        if value in content:
            return EMPTY

    return content


class Source:
    helper: SourceHelper

    __files: List[File]

    def __init__(self, helper: SourceHelper) -> None:
        self.helper = helper

        self.__files = self.helper.get_files()

    def get_files(self) -> List[File]:
        return self.__files

    def get_all_contents(self, lower_case: bool = True) -> list[str]:
        return self.get_contents(lower_case)

    def get_contents(
        self, lower_case: bool = True, excluding: list[str] | None = None
    ) -> list[str]:
        items: list[str] = []

        files = self.__files

        progress = TimedProgress("retrieving files", len(files))

        for i, file in enumerate(files):
            progress.update(i)

            content = file.content

            if excluding is not None:
                content = parse_excluding(content, excluding)

            if lower_case:
                content = content.lower()

            items.append(content)

        progress.complete()

        return items

    def get_textual_sequences(self):
        return list(map(lambda x: Sequence(list(x.content.lower())), self.__files))

    def list_file_paths(self, options: ScanOptions):
        paths = self.helper.file_helper.get_file_paths(options)

        for path in paths:
            print(path)


def get_sanitised_contents(
    source: Source, curator: ElementalCurator | None = None
) -> list[str]:
    stopwords_file = source.helper.get_file("../stopwords.txt")

    sanitiser_options = SanitiserOptions(stopwords_file.content)

    contents = source.get_all_contents()

    if curator is None:
        character_analysis = content_analysis_runner(AnalyserType.CHARACTER, contents)

        character_list = to_character_list(character_analysis)

        characters = set(character_list)

        print(f"{characters}")

        print("curate & collect")

        curator = curate_and_collect(characters)

    sanitiser = build_sanitiser(curator, sanitiser_options)

    results = sanitise_contents(sanitiser, contents)

    sanitised = list(map(lambda x: x.content, results))

    return sanitised


def get_sequences(
    source: Source,
    curator: ElementalCurator | None = None,
    sanitised_contents: List[str] | None = None,
) -> List[Sequence]:
    if not sanitised_contents:
        sanitised_contents = get_sanitised_contents(source, curator)

    return list(map(lambda x: Sequence(to_words(x)), sanitised_contents))
