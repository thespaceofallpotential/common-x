from core.sink import sink_factory
from data.source_helper import SourceHelper
from data.source import Source
from sanitisation.character_analyser import get_elements
from sanitisation.analyser import AnalyserType
from sanitisation.analysis_engine import analysis_runner
from sanitisation.qualitative_sequence import QualitativeSequence
from sanitisation.elemental_culture import curate_elements
from sanitisation.elemental_sanitisers import BasicElementalSanitiser
from utils.timer import Timer
from utils.io_helper import ScanOptions

# textual-domain analysis: as a precoursour to intelligent sanitisation,
# using approach & methods consistent with common-x solvers


helper = SourceHelper("data/local/aeim")

options = ScanOptions(helper.file_helper.root, ext=".md", relative=True, recursive=True)

helper.add_all(options)

print(f"{len(helper.relative_paths)} files")

print("retrieving content...")

files = helper.get_files()

print(f"content retrieved ({len(files)})")

print("building textual sequences")

source = Source(helper)

sink = sink_factory()

contents = source.get_content()

analysis_runner(AnalyserType.CHARACTER, contents, sink)

print(f"{len(sink.items)}")

elements = get_elements(sink.items)

print(f"union ({len(elements)})")

all_elements = set()

for x in elements:
    all_elements = all_elements.union(x)


all_element_list = list(all_elements)

all_element_list.sort()

# ws = list(filter(lambda x: re.sub(r"[^\w\s]|_", EMPTY, x), all_characters))

sequence = QualitativeSequence(all_element_list)

print("curate")

culture = curate_elements(sequence.elements)

sanitiser = BasicElementalSanitiser(culture)

print("build sanitiser")

sanitiser.build()

print("sanitise")

all_sanitised: list[str] = []

length = len(contents)

timer = Timer()

timer.start()

for i, content in enumerate(contents):
    print(f"{'progress [%d%%]\r'}" % ((i + 1) / length * 100), end="")

    sanitised = sanitiser.sanitise(content)

    all_sanitised.append(sanitised)

print(f"\nt:{timer.end()}")

print("end")

# sequences = source.get_textual_sequences()

# print(f"{len(sequences)}")

# sizes = list(map(lambda x: x.size, sequences))

# sizes.sort(reverse=True)

# print(f"max: {max(sizes)}")
