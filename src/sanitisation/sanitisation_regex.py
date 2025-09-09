from enum import Enum
from typing import Dict

import re

from core.strings import FRONTMATTER
from sanitisation.regex import BasicRegex, FragmentTypes, IRegex, StructuredRegex

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

    STRUCTURED_MARKDOWN_INTERNAL_LINK = 31
    STRUCTURED_MARKDOWN_EXTERNAL_LINK = 32


def re_match(r: str, x: str, positive: bool = True) -> bool:
    return bool(re.match(r, x)) and positive


def build_sanitisation_map() -> Dict[SanitisationTypes, IRegex]:
    whitespace = r"[\w\s]"  # positive: [a-zA-Z0-9_]

    digits = r"[\d]"  # positive: [0-9]

    newline = r"\n"  # positive: new line

    underscore = r"[_]"  # positive? underscore

    apostrophe = r"[']"  # negative: apostrophe

    structured_whitepace = r"(\s{2,})"  # structured: whitespace

    structured_whitespace_fragments: TFragments = {FragmentTypes.BODY: r"\s"}

    # STRUCTURED_FRONTMATTER = r"^---[^-]"  # structured: frontmatter (open/ close)

    # STRUCTURED_FRONTMATTER_CLOSE = r"\n---[^-]"  # structured: frontmatter close

    structured_preiod_space = r"\. "  # structured: period space

    structured_period_space_fragments: TFragments = {
        FragmentTypes.START: r"\.",
        FragmentTypes.END: r" ",
    }

    # STRUCTURED_MARKDOWN_INTERNAL_LINK_OPEN = (
    #     r"\[\["  # structured: markdown internal link open
    # )
    # STRUCTURED_MARKDOWN_INTERNAL_LINK_CLOSE = (
    #     r"\]\]"  # structured: markdown internal link open
    # )

    structured_frontmatter = r"^---[^-]+\n---(\n)"

    stuctured_frontmatter_fragments: TFragments = {
        FragmentTypes.START: FRONTMATTER,
        FragmentTypes.END: FRONTMATTER,
    }

    structured_markdown_internal_link = r"(\[\[)[^\[\]]+(\]\])"

    structured_markdown_internal_linke_fragments: TFragments = {
        FragmentTypes.START: "[[",
        FragmentTypes.END: "]]",
    }

    structured_markdown_external_link = r"\[[^\[\]\(\)]+\]\([^\[\]\(\)]+\)"

    structured_markdown_external_link_fragments: TFragments = {
        FragmentTypes.START: "[]",
        FragmentTypes.MIDDLE: "](",
        FragmentTypes.END: ")",
    }

    structured_whitespace = StructuredRegex(
        structured_whitepace, structured_whitespace_fragments
    )

    structured_period_space = StructuredRegex(
        structured_preiod_space, structured_period_space_fragments
    )

    structured_frontmatter = StructuredRegex(
        structured_frontmatter, stuctured_frontmatter_fragments
    )

    structured_markdown_internal = StructuredRegex(
        structured_markdown_internal_link,
        structured_markdown_internal_linke_fragments,
    )

    structured_markdown_external = StructuredRegex(
        structured_markdown_external_link,
        structured_markdown_external_link_fragments,
    )

    return {
        SanitisationTypes.WHITESPACE: BasicRegex(whitespace),
        SanitisationTypes.DIGIT: BasicRegex(digits),
        SanitisationTypes.NEWLINE: BasicRegex(newline),
        SanitisationTypes.UNDERSCORE: BasicRegex(underscore),
        SanitisationTypes.APOSTROPHE: BasicRegex(apostrophe, False),
        SanitisationTypes.STRUCTURED_WHITESPACE: structured_whitespace,
        SanitisationTypes.STRUCTURED_PERIOD_SPACE: structured_period_space,
        SanitisationTypes.STRUCTURED_FRONTMATTER: structured_frontmatter,
        SanitisationTypes.STRUCTURED_MARKDOWN_INTERNAL_LINK: structured_markdown_internal,
        SanitisationTypes.STRUCTURED_MARKDOWN_EXTERNAL_LINK: structured_markdown_external,
    }


sanitisation_regex_map = build_sanitisation_map()
