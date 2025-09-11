from typing import Dict

from core.strings import CLOSE_CALLOUT, EMPTY, FRONTMATTER, NEWLINE, OPEN_CALLOUT
from formulation.sanitisation.regex import (
    IRegex,
    StructuredRegex,
    StructuredRegexFragments,
)
from formulation.sanitisation.sanitisation_types import SanitisationTypes


def build_structured_regex_map() -> Dict[SanitisationTypes, IRegex]:
    # MARKDOWN FRONTMATTER
    #
    structured_frontmatter_pattern = r"^(---\n)((.|\s)*?)(\n---)"

    def transform_frontmatter(x: str) -> str:
        return str.join(NEWLINE, list(map(lambda x: EMPTY, x.split(NEWLINE))))

    stuctured_frontmatter_fragments = StructuredRegexFragments(
        start=f"{FRONTMATTER}{NEWLINE}",
        end=f"{NEWLINE}{FRONTMATTER}",
        transform=transform_frontmatter,
    )

    # MARKDOWN CALLOUT
    #
    structured_callout_pattern = r"^(\> \[\!)((.|\s)*?)(\])[^(+|-)]?"

    def transform_callout(x: str) -> str:
        return EMPTY

    stuctured_callout_fragments = StructuredRegexFragments(
        start=f"{OPEN_CALLOUT}",
        end=f"{CLOSE_CALLOUT}",
        transform=transform_callout,
    )

    # MARKDOWN INTERNAL
    #
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
    #
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
    #
    structured_raw_html = r"({{< rawhtml >}})(.*?)({{< /rawhtml >}})"

    def transform_raw_html(x: str) -> str:
        return EMPTY

    structured_raw_html_fragments = StructuredRegexFragments(
        start="{{< rawhtml >}}", end="{{< /rawhtml >}}", transform=transform_raw_html
    )

    # STRUCTURED REGEX
    #
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
        SanitisationTypes.STRUCTURED_FRONTMATTER: structured_frontmatter,
        SanitisationTypes.STRUCTURED_CALLOUT: structured_callout,
        SanitisationTypes.STRUCTURED_MARKDOWN_INTERNAL_LINK: structured_markdown_internal,
        SanitisationTypes.STRUCTURED_MARKDOWN_EXTERNAL_LINK: structured_markdown_external,
        SanitisationTypes.STRUCTURED_RAWHTML: structured_rawhtml,
    }


structured_regex_map = build_structured_regex_map()

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
