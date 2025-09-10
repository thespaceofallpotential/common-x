# import re

# from core.strings import ASTERISK, COMMA, EMPTY, EXCLAMATION, NEWLINE, SPACE
# from core.types import safe_index
# from sanitisation.curation_helpers import (
#     ElementMap,
# )
# from sanitisation.character_analyser import to_character_list2
# from sanitisation.elemental_curator import ElementalCurator
# from utils.timer import Timer


# # def map_contents(
# #     curator: ElementalCurator, contents: list[str]
# # ) -> list[list[PositiveVector]]:
# #     items: list[list[PositiveVector]] = []

# #     length = len(contents)

# #     timer = Timer(True)

# #     assessor = curator.structured_assessor()

# #     curator.culture.structured

# #     for i, content in enumerate(contents):
# #         print("progress [%d%%]\r" % ((i + 1) / length * 100), end="")
# #         # print(f"progress {i} [%d%%]\r" % ((i + 1) / length * 100), end="")

# #         pattern = r"\[|\{"

# #         matches = re.finditer(pattern, content)

# #         for match in matches:
# #             print(match.start(), match.group())

# #         vectors = get_positive_vectors(content, assessor)

# #         items.append(vectors)

# #     print(f"\nt:{timer.end()}")

# #     return items


# def map_content_elements(
#     curator: ElementalCurator, contents: list[str]
# ) -> list[ElementMap]:
#     items: list[ElementMap] = []

#     length = len(contents)

#     timer = Timer(True)

#     # assessor = curator.()

#     for i, content in enumerate(contents):
#         print("progress [%d%%]\r" % ((i + 1) / length * 100), end="")
#         # print(f"progress {i} [%d%%]\r" % ((i + 1) / length * 100), end="")

#         element_list = list(set(content))
#         element_list.sort()

#         elements = str.join("", element_list)

#         # vectors = get_positive_vectors(elements, assessor)

#         # items.append(ElementMap(element_list, vectors, content))

#     print(f"\nt:{timer.end()}")

#     return items


# def map_content_elements2(
#     curator: ElementalCurator, contents: list[str]
# ) -> list[ElementMap]:
#     items: list[ElementMap] = []

#     length = len(contents)

#     timer = Timer(True)

#     assessor = curator.structured_assessor()

#     for i, content in enumerate(contents):
#         print("progress [%d%%]\r" % ((i + 1) / length * 100), end="")
#         # print(f"progress {i} [%d%%]\r" % ((i + 1) / length * 100), end="")

#         temp: dict[str, list[int]] = {}

#         character = "["

#         pattern = r"\[|\{"

#         matches = re.finditer(pattern, content)

#         for match in matches:
#             print(match.start(), match.group())

#         i_i = safe_index(content, character)

#         while i_i > -1 and i_i < len(content):
#             current = temp.get(character)

#             if current is None:
#                 temp[character] = [i_i]
#             else:
#                 temp[character].append(i_i)

#             i_i = safe_index(content, character, i_i + 1)

#             print(i_i)

#         for i_i, character in enumerate(content):
#             if character == "[":
#                 current = temp.get(character)

#                 if current is None:
#                     temp[character] = [i_i]
#                     continue

#                 temp[character].append(i_i)

#         translations = str.maketrans(
#             {
#                 COMMA: EMPTY,
#                 # PERIOD: SPACE,
#                 # NEWLINE: SPACE,
#                 ASTERISK: EMPTY,
#                 EXCLAMATION: EMPTY,
#                 ":": SPACE,
#                 ";": SPACE,
#                 "<": SPACE,
#                 ">": SPACE,
#                 '"': EMPTY,
#                 "'": EMPTY,
#                 "-": SPACE,
#                 "–": SPACE,
#                 "—": SPACE,
#                 "(": EMPTY,
#                 ")": EMPTY,
#                 "?": EMPTY,
#                 "#": EMPTY,
#                 "$": EMPTY,
#                 "&": SPACE,
#                 "+": SPACE,
#                 "/": SPACE,
#                 "=": SPACE,
#                 "|": SPACE,
#                 "{": EMPTY,
#                 "}": EMPTY,
#                 "[": EMPTY,
#                 "]": EMPTY,
#                 "\\": SPACE,
#             }
#         )

#         content = re.sub("({{< rawhtml >}})(.*?)({{< /rawhtml >}})", SPACE, content)

#         word_list = content.translate(translations).replace(r"( {2,})", " ").split()

#         # word_list = re.sub(r"[^\w\s]", SPACE, content).replace(r"( {2,})", " ").split()

#         unique_words = set(word_list)

#         unique_word_list = list(unique_words)

#         unique_word_list.sort()

#         characters = to_character_list2(unique_word_list)

#         character_set = set(characters)

#         character_set.add(" ")
#         character_set.add(NEWLINE)

#         filtered = list(filter(lambda x: x in character_set, list(content)))

#         filtered_v = str.join("", filtered)

#         element_list = list(set(content))

#         element_list.sort()

#         elements = str.join("", element_list)

#         vectors = get_positive_vectors(elements, assessor)

#         items.append(ElementMap(element_list, vectors, content))

#     print(f"\nt:{timer.end()}")

#     return items
