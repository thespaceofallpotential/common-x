# from data.source import Source, get_sequences
# from data.source_helper import SourceHelper
# from core.domains import WordDomain
# from utils.io_helper import ScanOptions

# helper = SourceHelper("data/local/aeim")

# options = ScanOptions(helper.file_helper.root, ext=".md", relative=True, recursive=True)

# helper.add_all(options)

# print("set files")

# source = Source(helper)

# # source.list_file_paths(relative=True)

# # source.list_file_paths

# print("get sequences")

# sequences = get_sequences(source)

# print("word domain")

# word_domain = WordDomain(sequences)

# print(f"{len(helper.relative_paths)} {len(sequences)} {len(word_domain.values)}")

# # 5331 5331 291817
# # TODO: need to get word count down (sanitisation issue)
# #
# # 5331 5215 135703
# #   basic sanitiser frontmatter check
# # 5331 5160 123196
# #   large word
# # 5331 4932 21695
# #   more than x numbers
# # 5331 4874 20055
# #   pad new lines
# # 5331 4874 19925
# #   strip numbers
# # 5331 4892 18164
# #   strip markdown links, callouts
# # 5331 4892 13102
# #   string any isdigit

# print(word_domain.values)

# # sanitised = source.get_sanitised()

# # a = "computer science longest common substring two more strings longest string substring all them there may be more than one longest common substring applications include data deduplication plagiarism detection"
# # b = "longest common subsequence lcs longest subsequence common all sequences set sequences often just two sequences it differs from longest common substring unlike substrings subsequences are not required occupy consecutive positions within original sequences"

# # sequences = source.get_sequences()

# # print('Downloading File FooFile.txt [%d%%]\r'%i, end="")
