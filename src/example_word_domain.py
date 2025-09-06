from example_1_source import source
from core.domains import WordDomain


sequences = source.get_sequences()

word_domain = WordDomain(sequences)

print(word_domain.values)
