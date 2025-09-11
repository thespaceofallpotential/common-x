from example_1_source import source
from core.domains import WordDomain
from data.source import get_sequences


sequences = get_sequences(source)

word_domain = WordDomain(sequences)

print(word_domain.values)
