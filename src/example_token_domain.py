from typing import List
from example_1_source import source
from core.domains import TokenDomain
from core.sequence import Sequence
from data.source import get_sequences

sequences: List[Sequence[str]] = get_sequences(source)

token_domain = TokenDomain(sequences)

print(token_domain.word_position_map)

token_sequences = token_domain.to_token_sequences(sequences)

print(token_sequences)

# a_tokens = self.ordered_domain.to_tokens(self.a_words.values)

# b_tokens = self.ordered_domain.to_tokens(self.b_words.values)
