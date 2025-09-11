import re

from formulation.sanitisation.sanitiser import (
    ISanitiser,
    SanitiserOptions,
    SanitiserResult,
)
from formulation.analysis.curation_helpers import StructuredPatternMap
from formulation.analysis.elemental_curator import ElementalCurator
from formulation.sanitisation.regex_transforms import (
    SPACE_TRANSLATIONS,
    BLANK_TRANSLATIONS,
    regex_transform,
)
from formulation.sanitisation.stopwords import StopwordRemover


class MarkdownSanitiser(ISanitiser):
    options: SanitiserOptions

    curator: ElementalCurator

    def __init__(self, curator: ElementalCurator, options: SanitiserOptions) -> None:
        self.curator = curator
        self.options = options

    def sanitise(self, content: str, i: int | None = None) -> SanitiserResult:
        curator = self.curator

        ordered_keys = list(curator.structured_regex_order)

        structured_pattern_map = StructuredPatternMap()

        if i is not None:
            curator.structured_pattern_maps[i] = structured_pattern_map

        original = content

        result = SanitiserResult()

        for structured_sanitisation_key in ordered_keys:
            structured_regex = curator.culture.get_structured_regex(
                structured_sanitisation_key
            )

            pattern = structured_regex.pattern
            fragments = structured_regex.fragments

            if pattern is None:
                continue

            matches = re.finditer(pattern, content)

            for match in matches:
                i_m = match.start()
                group = match.group()

                is_index_ok = (
                    structured_regex.fixed_index is None
                    or structured_regex.is_index_ok(i_m)
                )

                if not is_index_ok:
                    continue

                structured_pattern_map.add(group, i_m)

                if fragments.transform is None:
                    continue

                replacement = fragments.transform(group)

                content = content.replace(group, replacement)

                # i_r = safe_index(content, group)

                # if i_r > -1:
                #     print("here")

        content = regex_transform(content, SPACE_TRANSLATIONS, BLANK_TRANSLATIONS)

        if content == original:
            c_e = set(list(content))
            o_e = set(list(original))
            diff = c_e.symmetric_difference(o_e)
            if len(diff) > 0:
                print("here")

        if self.options.stopwords is not None:
            stopword_remover = StopwordRemover()

            content = stopword_remover.process(content, self.options.stopwords)

        result.content = content

        return result

        # character_analysis = content_analysis_runner(AnalyserType.CHARACTER, contents)

        # character_list = to_character_list(character_analysis)

        # characters = set(character_list)

        # print("curate & collect")

        # curator = curate_and_collect(characters)

        # print("sanitise")

        # # mapped = map_contents(curator, contents)
        # # maps = map_content_elements2(curator, contents)

        # sanitised = sanitise_contents(curator, contents)
