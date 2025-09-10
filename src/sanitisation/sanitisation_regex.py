from enum import Enum
from typing import Dict

import re

from core.strings import FRONTMATTER
from sanitisation.regex import (
    BasicRegex,
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

    structured_whitespace_fragments: TFragments = {
        FragmentTypes.START: r"\s",
        FragmentTypes.BODY: r"\s",
        FragmentTypes.END_BEFORE: r"[^\s]",
    }

    structured_whitespace_fragments2 = StructuredRegexFragments(
        start=r"\s",
        body=r"\s",
        end_before=r"[^\s]",
    )

    # STRUCTURED_FRONTMATTER = r"^---[^-]"  # structured: frontmatter (open/ close)

    # STRUCTURED_FRONTMATTER_CLOSE = r"\n---[^-]"  # structured: frontmatter close

    structured_period_space = r"\. "  # structured: period space

    structured_period_space_fragments: TFragments = {
        FragmentTypes.START: r"\.",
        FragmentTypes.END: r" ",
    }

    structured_period_space_fragments2 = StructuredRegexFragments(
        start=r"\.",
        end=r" ",
    )

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

    stuctured_frontmatter_fragments2 = StructuredRegexFragments(
        start=FRONTMATTER,
        end=FRONTMATTER,
    )

    structured_markdown_internal_link = r"(\[\[)[^\[\]]+(\]\])"

    structured_markdown_internal_linke_fragments: TFragments = {
        FragmentTypes.START: "[[",
        FragmentTypes.END: "]]",
    }

    structured_markdown_internal_linke_fragments2 = StructuredRegexFragments(
        start="[[",
        end="]]",
    )

    structured_markdown_external_link = r"\[[^\[\]\(\)]+\]\([^\[\]\(\)]+\)"

    structured_markdown_external_link_fragments: TFragments = {
        FragmentTypes.START: "[]",
        FragmentTypes.MIDDLE: "](",
        FragmentTypes.END: ")",
    }

    structured_markdown_external_link_fragments2 = StructuredRegexFragments(
        start="[]",
        middle="](",
        end=")",
    )

    structured_whitespace = StructuredRegex(
        structured_whitepace, structured_whitespace_fragments2
    )

    structured_period_space = StructuredRegex(
        structured_period_space, structured_period_space_fragments2
    )

    structured_frontmatter = StructuredRegex(
        structured_frontmatter, stuctured_frontmatter_fragments2, fixed_index=0
    )

    structured_markdown_internal = StructuredRegex(
        structured_markdown_internal_link,
        structured_markdown_internal_linke_fragments2,
    )

    structured_markdown_external = StructuredRegex(
        structured_markdown_external_link,
        structured_markdown_external_link_fragments2,
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
