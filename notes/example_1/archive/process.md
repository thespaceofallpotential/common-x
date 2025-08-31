# common-x: example 1; process

> TODO:
> 
> note: github latex rendering seems broken on mobile/ ios?
> note: --what is the convention for naming a second variable as modified version of the first? 

---
## source: strings

Consider two *"input strings"* $A$, and $B$:-

### A
> *[data](/data/a.txt) | [meta](/data/a-meta.txt)*
>
> In computer science, a longest common substring of two or more strings is a longest string that is a substring of all of them. There may be more than one longest common substring. Applications include data deduplication and plagiarism detection.
>
> — [wikipedia: longest common substring](https://en.wikipedia.org/wiki/Longest_common_substring)

### B
> *[data](/data/b.txt) | [meta](/data/b-meta.txt)*
>
> A longest common subsequence (LCS) is the longest subsequence common to all sequences in a set of sequences (often just two sequences). It differs from the longest common substring: unlike substrings, subsequences are not required to occupy consecutive positions within the original sequences.
>
> — [wikipedia: longest common subsequence](https://en.wikipedia.org/wiki/Longest_common_subsequence)

---
## preparation: stopwords

Before processing, our input-strings $A$ and $B$ , must be *"cleaned"* *(in the sense of a "qualitative filter" on constituent words — to remove problematic analytical noise, known as "stopwords")*

> "Stop words are the words in a stop list (or stoplist or negative dictionary) which are filtered out ("stopped") before or after processing of natural language data (i.e. text) because they are deemed to have little semantic value or are otherwise insignificant for the task at hand"
>
> — [wikipedia: stopwords](https://en.wikipedia.org/wiki/Stop_word)

Let's define a list of *stopwords* $Sl$ , to be excluded from input-strings $A$ and $B$:-

$$Sl = \lbrace a, in, is, of, or, the, to, that \rbrace$$

Such that:-

$$A \to a \; |\; a = A\setminus{sl}$$

...and...

$$B \to b \; | \; b= B\setminus{sl}$$

Accordingly:-

### a
>
> computer science longest common substring two more strings longest string substring all them there may be more than one longest common substring applications include data deduplication plagiarism detection
>
> — *[a (clean)](/data/a-clean.txt) | [A (original)](/data/a.txt)*

### b
>
> longest common subsequence lcs longest subsequence common all sequences set sequences often just two sequences it differs from longest common substring unlike substrings subsequences are not required occupy consecutive positions within original sequences
>
> — *[b (clean)](/data/b-clean.txt) | [B (original)](/data/b.txt)*

