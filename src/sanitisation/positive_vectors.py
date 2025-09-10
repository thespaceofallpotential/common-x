# from typing import Callable

# from core.strings import EMPTY

# type TStepAssessor = Callable[..., int]

# ----
# horribly slow compared to re functions...
# not possible to practically implement common-x idiomatic sanitisation in python...
# nevermind - will address seperately
# ----

# class PositiveVector:
#     i: int
#     length: int

#     def __init__(self, i: int, length: int) -> None:
#         self.i = i
#         self.length = length

#     def __repr__(self) -> str:
#         return f"i:{self.i} l:{self.length}"


# def get_positive_vectors(content: str, assessor: TStepAssessor) -> list[PositiveVector]:
#     vectors: list[PositiveVector] = []


#     current: PositiveVector | None = None

#     length = len(content)
#     i = 0

#     while i < length:
#         character = content[i]

#         step = assessor(content, i, character)

#         if step == 0:
#             current = None

#             i += 1

#             continue

#         if current is not None:
#             current.length += step

#         if current is None:
#             current = PositiveVector(i, step)

#             vectors.append(current)

#         i += step

#     return vectors


# def get_element_vectors(content: str, assessor: TStepAssessor) -> list[PositiveVector]:
#     vectors: list[PositiveVector] = []

#     current: PositiveVector | None = None

#     length = len(content)
#     i = 0

#     while i < length:
#         character = content[i]

#         step = assessor(content, i, character)

#         if step == 0:
#             current = None

#             i += 1

#             continue

#         if current is None:
#             current = PositiveVector(i, step)

#             vectors.append(current)

#         if current is not None:
#             current.length += step

#         i += step

#     return vectors


# def print_vectors(content: str, vectors: list[PositiveVector]) -> str:
#     positive_content = list(map(lambda x: content[x.i : x.i + x.length], vectors))

#     return str.join(EMPTY, positive_content)
