import abc
from enum import Enum

from core.strings import EMPTY
from utils.custom_exception import CustomException


class SanitiserKind(Enum):
    NONE = 0
    BASIC = 1
    MARKDOWN = 2

    STOPWORD = 10


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


class SanitiserResult:
    content: str = EMPTY
    frontmatter: str | None = None


class ISanitiser(metaclass=abc.ABCMeta):
    options: SanitiserOptions

    def __init__(self, options: SanitiserOptions) -> None:
        self.options = options

    @abc.abstractmethod
    def sanitise(self, content: str, i: int | None = None) -> SanitiserResult:
        raise CustomException("NOT IMPLEMENTED")
