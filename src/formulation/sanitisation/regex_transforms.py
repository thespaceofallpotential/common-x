import re

from core.strings import EMPTY, SPACE


SPACE_TRANSLATIONS = [
    ":",
    ";",
    "<",
    ">",
    "-",
    "–",
    "—",
    "&",
    "+",
    "/",
    "=",
    "|",
    "\\",
    "~",
    "_",
]

BLANK_TRANSLATIONS = [
    ",",
    "*",
    "!",
    '"',
    "'",
    "(",
    ")",
    "?",
    "#",
    "$",
    "{",
    "}",
    "[",
    "]",
    "^",
    "%",
    "@",
    "`",
]


def regex_transform(content: str, spaced: list[str], blanked: list[str]):
    items: dict[str, str] = {}

    for x in spaced:
        items[x] = SPACE

    for x in blanked:
        items[x] = EMPTY

    translations = str.maketrans(items)

    translated = content.translate(translations)

    translated = re.sub(r"\.", r"\n", translated)
    translated = re.sub(r"\n( ){1,}\n", r"\n", translated)  #
    translated = re.sub(r"(\n){2,}", r"\n", translated)
    translated = re.sub(r"( ){2,}", " ", translated).strip()

    return translated
