# from data.source_helper import SourceHelper
# from data.source import Source
# from formulation.analysis.character_analyser import to_character_list
# from formulation.analysis.analyser import AnalyserType
# from formulation.analysis.content_analysis_engine import content_analysis_runner
# from formulation.analysis.elemental_curator import (
#     curate_and_collect,
# )
# from formulation.sanitisation.markdown.markdown import EXCALIDRAW_PLUGIN
# from utils.io_helper import ScanOptions

# # textual-domain analysis: as a precoursour to intelligent sanitisation,
# # using approach & methods consistent with common-x solvers

# # ---
# #
# # 1. make it work  <--- WE ARE HERE!
# # 2. make it right
# #
# # fucking hell, python loop performance...
# #
# #
# # ---


# def map_content():
#     helper = SourceHelper("data/local/aeim")

#     # options = ScanOptions(helper.file_helper.root, ext=".md", relative=True, recursive=True)
#     options = ScanOptions(
#         helper.file_helper.root, ext=".md", relative=True, recursive=True
#     )

#     helper.add_all(options)

#     print(f"{len(helper.relative_paths)} files")

#     print("retrieving content...")

#     files = helper.get_files()

#     # item = next(filter(lambda x: "pdf" in x.path, files))
#     # if item is not None:
#     #     print("here")

#     print(f"content retrieved ({len(files)})")

#     print("building textual sequences")

#     source = Source(helper)

#     contents = source.get_all_contents()

#     # content exclusion

#     contents = list(filter(lambda x: EXCALIDRAW_PLUGIN not in x, contents))

#     # i_i = 0

#     # for i, x in enumerate(files):
#     #     if "pdf" in x.path:
#     #         i_i = i
#     #         break
#     # contents = list([contents[i_i]])

#     print("character analysis")

#     character_analysis = content_analysis_runner(AnalyserType.CHARACTER, contents)

#     character_list = to_character_list(character_analysis)

#     characters = set(character_list)

#     print("curate & collect")

#     curator = curate_and_collect(characters)

#     print(f"{curator}")

#     # mapped = map_contents(curator, contents)
#     # maps = map_content_elements2(curator, contents)

#     # sanitised = sanitise_contents(curator, contents)

#     # print(f"{len(sanitised)}")

#     # filtered = list(filter(lambda x: "](" in x, sanitised))

#     # character_analysis2 = content_analysis_runner(AnalyserType.CHARACTER, sanitised)

#     # character_list2 = to_character_list(character_analysis2)

#     # characters2 = set(character_list2)

#     # print(f"{len(sanitised)}")

#     # 1. make it work  <--- STILL HERE! ;)


# map_content()
