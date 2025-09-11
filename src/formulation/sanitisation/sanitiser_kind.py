from enum import Enum


class SanitiserKind(Enum):
    NONE = 0
    BASIC = 1
    MARKDOWN = 2

    STOPWORD = 10
