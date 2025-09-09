from enum import Enum
from typing import Dict

import re


class SanitisationTypes(Enum):
    NONE = 0

    WS = 1
    D = 2
    NL = 3
    U = 4

    A = 10

    S_W = 20
    S_P = 21

    S_F = 30
    S_FC = 31

    S_MIO = 32
    S_MIC = 33


RE_WS = r"[\w\s]"  # positive: [a-zA-Z0-9_]

RE_D = r"[\d]"  # positive: [0-9]

RE_NL = r"\n"  # positive: new line

RE_U = r"[_]"  # positive? underscore

RE_A = r"[']"  # negative: apostrophe

RE_S_W = r"(\s{2,})"  # structured: whitespace

RE_S_F = r"^---"  # structured: frontmatter (open/ close)

RE_S_FC = r"\n---"  # structured: frontmatter close

RE_S_P = r"\. "  # structured: period space

RE_S_MIO = r"\[\["  # structured: markdown internal link open
RE_S_MIC = r"\]\]"  # structured: markdown internal link open

RE_S_MI = r"(\[\[)[^\[\]]+(\]\])"

RS_S_MO = r"\[[^\[\]\(\)]+\]\([^\[\]\(\)]+\)"

# don't need/ want regex for a bunch of this....
# time for zzz...


def re_match(r: str, x: str) -> bool:
    return bool(re.match(r, x))


sanitisation_regex_map: Dict[SanitisationTypes, str] = {
    SanitisationTypes.WS: RE_WS,
    SanitisationTypes.D: RE_D,
}
