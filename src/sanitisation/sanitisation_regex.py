from enum import Enum
import re
from typing import Dict


class SanitisationTypes(Enum):
    NONE = 0
    WS = 1
    D = 2


RE_WS = r"[\w\s]"  # [a-zA-Z0-9_]

RE_D = r"[\d]"  # [0-9]

RE_A = r"[']"  # apostrophe

RE_U = r"[_]"  # underscore

RE_N = r"\n"  # new line

RE_W = r"(\s{2,})"  # whitespace

RE_F = r"^(-{3})"  # frontmatter (open/ close)

RE_FC = r"[\n](-{3})"  # frontmatter close

RE_P = r"[\. ]"  # period space

RE_MIO = r"(\[{2}])"  # markdown internal link open
RE_MIC = r"(\]{2}])"  # markdown internal link open

# don't need/ want regex for a bunch of this....
# time for zzz...


def re_match(r: str, x: str) -> bool:
    return bool(re.match(r, x))


sanitisation_regex_map: Dict[SanitisationTypes, str] = {
    SanitisationTypes.WS: RE_WS,
    SanitisationTypes.D: RE_D,
}
