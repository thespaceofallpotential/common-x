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
    "\t",
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

    # TODO: sort this...
    
    translated = re.sub(r"( ){2,}", " ", translated)
    translated = re.sub(r"\.", r"\n", translated)
    translated = re.sub(r"( ){1,}(\n|\\n)( ){1,}", r"\n", translated)
    translated = re.sub(r"(\n|\\n){2,}", r"\n", translated)
    # translated = re.sub(r"(\n|\\n)( ){1,}(\n|\\n)", r"\n", translated)
    translated = re.sub(r"(\n|\\n)(\d){1,}(\n|\\n)", r"\n", translated)
    translated = re.sub(r"(\n )", "\n", translated)
    # translated = re.sub(r"( ){2,}", " ", translated)

    return translated.strip()
