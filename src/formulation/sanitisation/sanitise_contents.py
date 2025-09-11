# import re

# from formulation.sanitisation.curation_helpers import (
#     StructuredPatternMap,
# )
# from formulation.sanitisation.elemental_curator import ElementalCurator
# from formulation.sanitisation.regex_transforms import (
#     transform,
#     SPACE_TRANSLATIONS,
#     BLANK_TRANSLATIONS,
# )
# from formulation.sanitisation.sanitiser import Sanitiser
# from utils.progress import TimedProgress


# def sanitise_content(
#     curator: ElementalCurator, content: str, i: int | None = None
# ) -> str:
#     ordered_keys = list(curator.structured_regex_order)

#     structured_pattern_map = StructuredPatternMap()

#     if i is not None:
#         curator.structured_pattern_maps[i] = structured_pattern_map

#     original = content

#     for structured_sanitisation_key in ordered_keys:
#         structured_regex = curator.culture.get_structured_regex(
#             structured_sanitisation_key
#         )

#         pattern = structured_regex.pattern
#         fragments = structured_regex.fragments

#         if pattern is None:
#             continue

#         matches = re.finditer(pattern, content)

#         for match in matches:
#             i_m = match.start()
#             group = match.group()

#             is_index_ok = (
#                 structured_regex.fixed_index is None
#                 or structured_regex.is_index_ok(i_m)
#             )

#             if not is_index_ok:
#                 continue

#             structured_pattern_map.add(group, i_m)

#             if fragments.transform is None:
#                 continue

#             replacement = fragments.transform(group)

#             content = content.replace(group, replacement)

#             # i_r = safe_index(content, group)

#             # if i_r > -1:
#             #     print("here")

#     content = transform(content, SPACE_TRANSLATIONS, BLANK_TRANSLATIONS)
#     # sanitised = sanitise(content, assessor)

#     if content == original:
#         c_e = set(list(content))
#         o_e = set(list(original))
#         diff = c_e.symmetric_difference(o_e)
#         if len(diff) > 0:
#             print("here")

#     return content


# def sanitise_contents(sanitiser: Sanitiser, contents: list[str]) -> list[str]:
#     items: list[str] = []

#     length = len(contents)

#     progress = TimedProgress("sanitise content", length)

#     for i, content in enumerate(contents):
#         progress.update(i)

#         content = sanitise_content(curator, content, i)

#         items.append(content)

#     progress.complete()

#     return items
