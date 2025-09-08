from data.source_helper import SourceHelper
from data.source import Source
from core.sink import sink_factory
from sanitisation.character_analyser import get_elements
from sanitisation.analyser import AnalyserType
from sanitisation.analysis_engine import analysis_runner
from utils.io_helper import ScanOptions

# textual-domain analysis: as a precoursour to intelligent sanitisation,
# using approach & methods consistent with common-x solvers


helper = SourceHelper("data/local/aeim")

options = ScanOptions(helper.file_helper.root, ext=".md", relative=True, recursive=True)

helper.add_all(options)

print(f"{len(helper.relative_paths)} files")

files = helper.get_files()

print(f"content retrieved ({len(files)})")

print("building textual sequences")

source = Source(helper)

sink = sink_factory()

contents = source.get_content()

analysis_runner(AnalyserType.CHARACTER, contents, sink)

print(f"{len(sink.items)}")

elements = get_elements(sink.items)

print("end")

# sequences = source.get_textual_sequences()

# print(f"{len(sequences)}")

# sizes = list(map(lambda x: x.size, sequences))

# sizes.sort(reverse=True)

# print(f"max: {max(sizes)}")
