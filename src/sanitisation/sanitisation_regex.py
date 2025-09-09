from enum import Enum
from typing import Dict

import re

from core.strings import FRONTMATTER
from sanitisation.regex import BasicRegex, IRegex, StructuredRegex


class SanitisationTypes(Enum):
    NONE = 0

    WS = 1
    D = 2
    NL = 3
    U = 4

    A = 10

    S_W = 20
    S_P = 21

    S_FM = 30

    S_MIL = 31
    S_MEL = 32


RE_WS = r"[\w\s]"  # positive: [a-zA-Z0-9_]

RE_D = r"[\d]"  # positive: [0-9]

RE_NL = r"\n"  # positive: new line

RE_U = r"[_]"  # positive? underscore

RE_A = r"[']"  # negative: apostrophe

RE_S_W = r"(\s{2,})"  # structured: whitespace

RE_S_F = r"^---[^-]"  # structured: frontmatter (open/ close)

RE_S_FC = r"\n---[^-]"  # structured: frontmatter close

RE_S_P = r"\. "  # structured: period space

RE_S_MIO = r"\[\["  # structured: markdown internal link open
RE_S_MIC = r"\]\]"  # structured: markdown internal link open

RE_S_FM = r"^---[^-]+\n---(\n)"

RE_S_MI = r"(\[\[)[^\[\]]+(\]\])"

RE_S_ME = r"\[[^\[\]\(\)]+\]\([^\[\]\(\)]+\)"


# don't need/ want regex for a bunch of this....
# time for zzz...


def re_match(r: str, x: str, positive: bool = True) -> bool:
    return bool(re.match(r, x)) and positive


sanitisation_regex_map: Dict[SanitisationTypes, IRegex] = {
    SanitisationTypes.WS: BasicRegex(RE_WS),
    SanitisationTypes.D: BasicRegex(RE_D),
    SanitisationTypes.NL: BasicRegex(RE_NL),
    SanitisationTypes.U: BasicRegex(RE_U),
    SanitisationTypes.A: BasicRegex(RE_A, positive=False),
    SanitisationTypes.S_W: StructuredRegex(RE_S_W, body=r"\s"),
    SanitisationTypes.S_FM: StructuredRegex(
        RE_S_FM, start=FRONTMATTER, end=FRONTMATTER
    ),
    SanitisationTypes.S_MIL: StructuredRegex(RE_S_MI, start="[[", end="]]"),
    SanitisationTypes.S_MEL: StructuredRegex(RE_S_ME, start="[]", mid="](", end=")"),
}
