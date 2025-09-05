from core.strings import SPACE
from data.source import Source

# source: see ./data for origina and cleaned versions

A = "computer science longest common substring two more strings longest string substring all them there may be more than one longest common substring applications include data deduplication plagiarism detection"

B = "longest common subsequence lcs longest subsequence common all sequences set sequences often just two sequences it differs from longest common substring unlike substrings subsequences are not required occupy consecutive positions within original sequences"

a_words = str(A).split(SPACE)

b_words = str(B).split(SPACE)

source = Source(a_words, b_words)
