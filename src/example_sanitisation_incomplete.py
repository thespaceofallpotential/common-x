from data.source_helper import SourceHelper
from data.source import Source
from formulation.analysis.character_analyser import to_character_list
from formulation.analysis.analyser import AnalyserType
from formulation.analysis.content_analysis_engine import content_analysis_runner
from formulation.analysis.elemental_curator import (
    collect_and_curate,
)

from formulation.sanitisation.markdown.markdown import EXCALIDRAW_PLUGIN
from formulation.sanitisation.sanitiser_helpers import (
    get_sanitiser_options,
    sanitise_contents,
)
from formulation.sanitisation.sanitiser_factory import build_sanitiser
from core.strings import NEWLINE
from formulation.sanitisation.sanitiser_kind import SanitiserKind
from formulation.sanitisation.sanitiser_options import SanitiserOptions
from utils.io_helper import DirectoryScanOptions

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

    helper.add_all_for(
        DirectoryScanOptions(
            helper.file_helper.root, ext=".md", relative=True, recursive=True
        )
    )

    print(f"{len(helper.relative_paths)} files")

    stopwords = helper.get_content("../stopwords.txt")

    print(f"{len(stopwords.split(NEWLINE))} stopwords")

    source = Source(helper)

    contents = source.get_contents(excluding=[EXCALIDRAW_PLUGIN])

    curator = collect_and_curate(contents)

    options = get_sanitiser_options(
        stopwords,
        SanitiserKind.MARKDOWN,
        # {"regex_stopwords": True}, # SanitiserOptions.regex_stopwords
    )

    sanitiser = build_sanitiser(curator, options)

    sanitised = sanitise_contents(sanitiser, contents)

    sanitised_content = list(map(lambda x: x.content, sanitised))

    character_analysis2 = content_analysis_runner(
        AnalyserType.CHARACTER, sanitised_content
    )

    character_list2 = to_character_list(character_analysis2)

    characters2 = set(character_list2)

    print(f"{characters2}")

    print(f"{len(sanitised)}")
    
    

    # helper.file_helper.write("sanitised.txt", str.join("\n", sanitised_content))
    # 1. make it work  <--- STILL HERE! ;)


sanitise_content()
