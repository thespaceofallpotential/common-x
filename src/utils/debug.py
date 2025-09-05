from core.vector import vectors_str
from core.sequence import Sequence, sequence_values_str

IS_ACTIVE = False


def debug_vectors(a: Sequence, b: Sequence, override: bool = False):
    if override or IS_ACTIVE:
        print(vectors_str(a, b))


def debug_values(a: Sequence, b: Sequence, override: bool = False):
    if override or IS_ACTIVE:
        print(f"{sequence_values_str(a)} | {sequence_values_str(b)}")
