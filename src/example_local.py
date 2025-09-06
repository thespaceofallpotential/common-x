from data.source import Source
from data.source_helper import SourceHelper
from core.domains import WordDomain
from utils.io_helper import ScanOptions

helper = SourceHelper("data/local/aeim")

options = ScanOptions(helper.file_helper.root, ext=".md", relative=True, recursive=True)

print("add all")

helper.add_all(options)

file_count = len(helper.relative_paths)

source = Source(helper)

# source.list_file_paths(relative=True)

# source.list_file_paths

print("get sequences")

sequences = source.get_sequences()

sequence_count = len(sequences)

print("word domain")

word_domain = WordDomain(sequences)

word_count = len(word_domain.values)

print(f"{file_count} {sequence_count} {word_count}")

# 5331 5331 291817
# TODO: need to get word count down (sanitisation issue)


# print(word_domain.values)

# sanitised = source.get_sanitised()

# a = "computer science longest common substring two more strings longest string substring all them there may be more than one longest common substring applications include data deduplication plagiarism detection"
# b = "longest common subsequence lcs longest subsequence common all sequences set sequences often just two sequences it differs from longest common substring unlike substrings subsequences are not required occupy consecutive positions within original sequences"

# sequences = source.get_sequences()
