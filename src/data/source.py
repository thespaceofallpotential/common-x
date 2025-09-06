from typing import List
from core.sequence import Sequence
from data.file import File, are_ok
from data.source_helper import SourceHelper
from sanitisation.sanitiser import SanitiserOptions
from sanitisation.sanitiser_factory import build_sanitiser
from sanitisation.string_helpers import to_words
from sanitisation.sanitiser_helpers import sanitise_files
from utils.io_helper import ScanOptions


class Source:
    __helper: SourceHelper

    __files: List[File]

    def __init__(self, helper: SourceHelper) -> None:
        self.__helper = helper

        self.__files = self.__helper.get_files()

    def get_sanitised(self):
        stopwords_file = self.__helper.get_file("../stopwords.txt")

        sanitiser_options = SanitiserOptions(stopwords_file.content)

        sanitiser = build_sanitiser(sanitiser_options)

        sanitise_files(sanitiser, self.__files)

        sanitised = are_ok(self.__files)

        return sanitised

    def get_sequences(self, sanitised: List[File] | None = None) -> List[Sequence]:
        if not sanitised:
            sanitised = self.get_sanitised()

        return list(map(lambda x: Sequence(to_words(x.content)), sanitised))

    def list_file_paths(self, options: ScanOptions):
        paths = self.__helper.file_helper.get_file_paths(options)

        for path in paths:
            print(path)
