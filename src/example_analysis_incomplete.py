from data.source_helper import SourceHelper
from data.source import Source
from sanitisation.character_analyser import to_character_list
from sanitisation.analyser import AnalyserType
from sanitisation.content_analysis_engine import content_analysis_runner
from sanitisation.elemental_curator import (
    curate_and_collect,
    map_content_elements,
    map_content_elements2,
    map_contents,
)

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


def map_content():
    helper = SourceHelper("data/local/aeim")

    # options = ScanOptions(helper.file_helper.root, ext=".md", relative=True, recursive=True)
    options = ScanOptions(
        helper.file_helper.root, ext=".md", relative=True, recursive=False
    )

    helper.add_all(options)

    print(f"{len(helper.relative_paths)} files")

    print("retrieving content...")

    files = helper.get_files()

    i_i = 0

    for i, x in enumerate(files):
        if "pdf" in x.path:
            i_i = i
            break

    # item = next(filter(lambda x: "pdf" in x.path, files))
    # if item is not None:
    #     print("here")

    print(f"content retrieved ({len(files)})")

    print("building textual sequences")

    source = Source(helper)

    contents = source.get_content()

    contents = list([contents[i_i]])

    print("character analysis")

    character_analysis = content_analysis_runner(AnalyserType.CHARACTER, contents)

    character_list = to_character_list(character_analysis)

    characters = set(character_list)

    print("curate & collect")

    curator = curate_and_collect(characters)

    print("sanitise")

    # maps = map_contents(curator, contents)
    maps = map_content_elements2(curator, contents)

    # sanitised = sanitise_contents(curator, contents)

    print(f"{len(maps)}")

    # 1. make it work  <--- STILL HERE! ;)


map_content()
