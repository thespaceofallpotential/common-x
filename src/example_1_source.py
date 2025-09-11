from data.source import Source
from data.source_helper import SourceHelper
from formulation.sanitisation.sanitiser_helpers import get_basic_options

helper = SourceHelper("data/example_1")

helper.add("a.txt")
helper.add("b.txt")

source = Source(helper)

stopwords_file = source.helper.get_file("stopwords.txt")

sanitiser_options = get_basic_options(stopwords_file.content)

# sanitised = source.get_sanitised()

# a = "computer science longest common substring two more strings longest string substring all them there may be more than one longest common substring applications include data deduplication plagiarism detection"
# b = "longest common subsequence lcs longest subsequence common all sequences set sequences often just two sequences it differs from longest common substring unlike substrings subsequences are not required occupy consecutive positions within original sequences"

# sequences = source.get_sequences()
