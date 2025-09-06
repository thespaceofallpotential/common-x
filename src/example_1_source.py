from core.strings import SPACE
from data.source import Source
from data.source_helper import SourceHelper

# source: see ./data for original & cleaned versions

A = "computer science longest common substring two more strings longest string substring all them there may be more than one longest common substring applications include data deduplication plagiarism detection"

B = "longest common subsequence lcs longest subsequence common all sequences set sequences often just two sequences it differs from longest common substring unlike substrings subsequences are not required occupy consecutive positions within original sequences"

a_words = str(A).split(SPACE)

b_words = str(B).split(SPACE)

helper = SourceHelper("data/example_1")

helper.add("a.txt")
helper.add("b.txt")

source = Source(helper)

# sanitised = source.get_sanitised()
# sequences = source.get_sequences()
