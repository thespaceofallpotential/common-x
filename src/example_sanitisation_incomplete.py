from data.source_helper import SourceHelper
from data.source import Source
from formulation.analysis.character_analyser import to_character_list
from formulation.analysis.analyser import AnalyserType
from formulation.analysis.content_analysis_engine import content_analysis_runner
from formulation.sanitisation.elemental_curator import (
    curate_and_collect,
)

from formulation.sanitisation.markdown.markdown import EXCALIDRAW_PLUGIN
from formulation.sanitisation.sanitiser import SanitiserOptions
from formulation.sanitisation.sanitiser_helpers import sanitise_contents
from formulation.sanitisation.sanitiser_factory import build_sanitiser
from utils.io_helper import ScanOptions

# textual-domain analysis: as a precoursour to intelligent sanitisation,
# using approach & methods consistent with common-x solvers

# ---
#
# 1. make it work  <--- WE ARE HERE!
# 2. make it right
#
# fucking hell, python loop performance...
#
#
# ---


def sanitise_content():
    helper = SourceHelper("data/local/aeim")

    options = ScanOptions(
        helper.file_helper.root, ext=".md", relative=True, recursive=True
    )

    helper.add_all(options)

    print(f"{len(helper.relative_paths)} files")

    source = Source(helper)

    contents = source.get_contents(excluding=[EXCALIDRAW_PLUGIN])

    character_analysis = content_analysis_runner(AnalyserType.CHARACTER, contents)

    character_list = to_character_list(character_analysis)

    characters = set(character_list)

    print(f"{characters}")

    print("curate & collect")

    curator = curate_and_collect(characters)

    stopwords_file = helper.get_file("../stopwords.txt")

    sanitiser_options = SanitiserOptions(stopwords_file.content)

    sanitiser = build_sanitiser(curator, sanitiser_options)

    sanitised = sanitise_contents(sanitiser, contents)

    sanitised_content = list(map(lambda x: x.content, sanitised))

    character_analysis2 = content_analysis_runner(
        AnalyserType.CHARACTER, sanitised_content
    )

    character_list2 = to_character_list(character_analysis2)

    characters2 = set(character_list2)

    print(f"{characters2}")

    print(f"{len(sanitised)}")

    # 1. make it work  <--- STILL HERE! ;)


sanitise_content()
