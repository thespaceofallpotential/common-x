import re
from typing import List
from core.strings import (
    EMPTY,
    FRONTMATTER,
    LT,
    NEWLINE,
    OPEN_SQUARE_BRACKET,
    SPACE,
    SVG,
)
from core.types import index_withoutexception


def is_svg(x: str) -> bool:
    return x.startswith(SVG)


def is_html(x: str) -> bool:
    return x.startswith(LT) and not is_svg(x)


def is_space(x: str) -> bool:
    return x.startswith(SPACE) or x.startswith(NEWLINE)


def is_frontmatter(x: str) -> bool:
    return x.startswith(FRONTMATTER)


def has_links(x: str) -> bool:
    return x.index(OPEN_SQUARE_BRACKET) > -1


def clean_str(x: str) -> str:
    return re.sub(r"(\s{2,})", SPACE, x).strip()


def prepare_str(x: str) -> str:
    x = x.lower()

    x = re.sub(r"[']", EMPTY, x)

    x = re.sub(r"[^\w\s]|_", EMPTY, x)

    return x.strip()


def strip_new_lines(x: str) -> str:
    return re.sub(r"\n", SPACE, x).strip()


def pad_new_lines(x: str) -> str:
    return re.sub(
        r"\n", f"{SPACE}{NEWLINE}{SPACE}", x
    )  # TODO:: make this smarter: pad l,r only if necessary


def shrink_whitespace(x: str) -> str:
    return re.sub(r"(\s{2,})", SPACE, x).strip()


frontmatter_delimiter = f"{NEWLINE}{FRONTMATTER}"


def get_frontmatter(x: str) -> str:
    if not is_frontmatter(x):
        return EMPTY

    i = index_withoutexception(x, frontmatter_delimiter)

    if i < 0:
        return EMPTY

    i_end = i + len(frontmatter_delimiter)

    x = x[:i_end]

    return x


def strip_frontmatter(x: str) -> str:
    if not is_frontmatter(x):
        return x

    i = index_withoutexception(x, frontmatter_delimiter)

    i_end = i + len(frontmatter_delimiter)

    x = f"{SPACE * i_end} {x[i_end:]}"

    return x


def periods_to_new_line(x: str) -> str:
    lines = list(map(lambda y: re.sub(r"\. ", NEWLINE, y), x.split(NEWLINE)))

    return str.join(NEWLINE, lines)


def to_words(x: str) -> List[str]:
    return str(x).split(SPACE)


# const getFrontmatter = (content: string): string => {
#     const end = content.indexOf(`${NEWLINE}${FRONTMATTER}`);

#     const value = content.substring(0, end + 4);

#     return value;
# };
