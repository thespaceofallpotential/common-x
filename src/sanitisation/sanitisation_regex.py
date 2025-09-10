from enum import Enum
from typing import Dict

import re

from core.strings import CLOSE_CALLOUT, EMPTY, FRONTMATTER, NEWLINE, OPEN_CALLOUT, SPACE
from sanitisation.regex import (
    FragmentTypes,
    IRegex,
    StructuredRegex,
    StructuredRegexFragments,
)

type TFragments = Dict[FragmentTypes, str]


class SanitisationTypes(Enum):
    NONE = 0

    WHITESPACE = 1
    DIGIT = 2
    NEWLINE = 3
    UNDERSCORE = 4

    APOSTROPHE = 10

    STRUCTURED_WHITESPACE = 20
    STRUCTURED_PERIOD_SPACE = 21

    STRUCTURED_FRONTMATTER = 30
    STRUCTURED_CALLOUT = 31

    STRUCTURED_MARKDOWN_INTERNAL_LINK = 31
    STRUCTURED_MARKDOWN_EXTERNAL_LINK = 32

    STRUCTURED_RAWHTML = 33


def re_match(r: str, x: str, positive: bool = True) -> bool:
    return bool(re.match(r, x)) and positive


def build_sanitisation_map() -> Dict[SanitisationTypes, IRegex]:
    # whitespace = r"[\w\s]"  # positive: [a-zA-Z0-9_]
    # digits = r"[\d]"  # positive: [0-9]
    # newline = r"\n"  # positive: new line
    # underscore = r"[_]"  # positive? underscore
    # apostrophe = r"[']"  # negative: apostrophe
    # structured_whitepace = r"(\s{2,})"  # structured: whitespace
    # structured_whitespace_fragments: TFragments = {
    #     FragmentTypes.START: r"\s",
    #     FragmentTypes.BODY: r"\s",
    #     FragmentTypes.END_BEFORE: r"[^\s]",
    # }
    # structured_whitespace_fragments2 = StructuredRegexFragments(
    #     start=r"\s",
    #     body=r"\s",
    #     end_before=r"[^\s]",
    # )
    # STRUCTURED_FRONTMATTER = r"^---[^-]"  # structured: frontmatter (open/ close)
    # STRUCTURED_FRONTMATTER_CLOSE = r"\n---[^-]"  # structured: frontmatter close
    # structured_period_space = r"\. "  # structured: period space
    # structured_period_space_fragments: TFragments = {
    #     FragmentTypes.START: r"\.",
    #     FragmentTypes.END: r" ",
    # }
    # structured_period_space_fragments2 = StructuredRegexFragments(
    #     start=r"\.",
    #     end=r" ",
    # )
    # -----------------

    # FRONTMATTER

    # structured_frontmatter = r"^---\n[^(---)]+\n---(\n)"

    structured_frontmatter_pattern = r"^(---\n)((.|\s)*?)(\n---)"

    def transform_frontmatter(x: str) -> str:
        return str.join(NEWLINE, list(map(lambda x: EMPTY, x.split(NEWLINE))))

    stuctured_frontmatter_fragments = StructuredRegexFragments(
        start=f"{FRONTMATTER}{NEWLINE}",
        end=f"{NEWLINE}{FRONTMATTER}",
        transform=transform_frontmatter,
    )

    # MARKDOWN CALLOUT

    structured_callout_pattern = r"^(\> \[\!)((.|\s)*?)(\])[^(+|-)]?"

    def transform_callout(x: str) -> str:
        return EMPTY

    stuctured_callout_fragments = StructuredRegexFragments(
        start=f"{OPEN_CALLOUT}",
        end=f"{CLOSE_CALLOUT}",
        transform=transform_callout,
    )

    # MARKDOWN INTERNAL

    structured_markdown_internal_pattern = r"(\[\[)[^\[\]]+(\]\])"

    def transform_markdown_internal(x: str) -> str:
        x = x[2:]
        x = x[0:-2]

        if "|" in x:
            x = x.split("|")[1]

        return x

    structured_markdown_internal_link_fragments = StructuredRegexFragments(
        start="[[", end="]]", transform=transform_markdown_internal
    )

    # MARKDOWN EXTERNAL

    # structured_markdown_external_link = r"\[[^\[\]\(\)]+\]\([^\[\]\(\)]+\)"
    structured_markdown_external_pattern = (
        r"(\[)[^( )]?((.|\n)*?)([^\[]\]\()((.|\n)*?)(\))"
    )
    # structured_markdown_external_link = r"(\[)[^( )]?((.|\n|[^\(])*?)(\]\()((.|\n)*?)(\))"

    def transform_markdown_external(x: str) -> str:
        x = x[0:2]
        x = x[0:-2]

        if "|" in x:
            x = x.split("|")[1]

        return x

    structured_markdown_external_link_fragments = StructuredRegexFragments(
        start="[", middle="](", end=")", transform=transform_markdown_external
    )

    # MARKDOWN_RAW HTML

    structured_raw_html = r"({{< rawhtml >}})(.*?)({{< /rawhtml >}})"

    def transform_raw_html(x: str) -> str:
        return EMPTY

    structured_raw_html_fragments = StructuredRegexFragments(
        start="{{< rawhtml >}}", end="{{< /rawhtml >}}", transform=transform_raw_html
    )

    structured_frontmatter = StructuredRegex(
        structured_frontmatter_pattern, stuctured_frontmatter_fragments, fixed_index=0
    )

    structured_callout = StructuredRegex(
        structured_callout_pattern, stuctured_callout_fragments, fixed_index=0
    )

    structured_markdown_internal = StructuredRegex(
        structured_markdown_internal_pattern,
        structured_markdown_internal_link_fragments,
    )

    structured_markdown_external = StructuredRegex(
        structured_markdown_external_pattern,
        structured_markdown_external_link_fragments,
    )

    structured_rawhtml = StructuredRegex(
        structured_raw_html, structured_raw_html_fragments
    )

    return {
        # SanitisationTypes.WHITESPACE: BasicRegex(whitespace),
        # SanitisationTypes.DIGIT: BasicRegex(digits),
        # SanitisationTypes.NEWLINE: BasicRegex(newline),
        # SanitisationTypes.UNDERSCORE: BasicRegex(underscore),
        # SanitisationTypes.APOSTROPHE: BasicRegex(apostrophe, False),
        # SanitisationTypes.STRUCTURED_WHITESPACE: structured_whitespace,
        # SanitisationTypes.STRUCTURED_PERIOD_SPACE: structured_period_space,
        SanitisationTypes.STRUCTURED_FRONTMATTER: structured_frontmatter,
        SanitisationTypes.STRUCTURED_CALLOUT: structured_callout,
        SanitisationTypes.STRUCTURED_MARKDOWN_INTERNAL_LINK: structured_markdown_internal,
        SanitisationTypes.STRUCTURED_MARKDOWN_EXTERNAL_LINK: structured_markdown_external,
        SanitisationTypes.STRUCTURED_RAWHTML: structured_rawhtml,
    }


sanitisation_regex_map = build_sanitisation_map()

space_translations = [
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

blank_translations = [
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


def transform(content: str, spaced: list[str], blanked: list[str]):
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


# translations = str.maketrans(
#     {
#         COMMA: EMPTY,
#         # PERIOD: SPACE,
#         # NEWLINE: SPACE,
#         ASTERISK: EMPTY,
#         EXCLAMATION: EMPTY,
#         ":": SPACE,
#         ";": SPACE,
#         "<": SPACE,
#         ">": SPACE,
#         '"': EMPTY,
#         "'": EMPTY,
#         "-": SPACE,
#         "–": SPACE,
#         "—": SPACE,
#         "(": EMPTY,
#         ")": EMPTY,
#         "?": EMPTY,
#         "#": EMPTY,
#         "$": EMPTY,
#         "&": SPACE,
#         "+": SPACE,
#         "/": SPACE,
#         "=": SPACE,
#         "|": SPACE,
#         "{": EMPTY,
#         "}": EMPTY,
#         "[": EMPTY,
#         "]": EMPTY,
#         "\\": SPACE,
#     }
# )
