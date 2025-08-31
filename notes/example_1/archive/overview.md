## example 1 overview
> *on complexity*

Both *"subset problems"* and *"intersection problems"* reduce to *"finding things in spaces"* (see [background](/notes/background.md) for introduction to subset and intersection problems)*
)

> *simplifying: — the larger the space, the more complex/ difficult the challenge (of finding what is sought)*

The complexity of a common-substring problem is typically framed in terms of big-O notation, which captures the relationship between the size of inputs, and the corresponding product-space, which for common-x problems generally, is $O(n^{2})$

Specifically, given:-

$$n = |a| = 28$$

...and...

$$m = |b| = 33$$

Subsequently, the area of the *"problem-space"* of *"example 1"* — *(within-which all common words and substrings thereof, might/must be found)* — is...

$$n \times m = |a| * |b| = 28 \times 33 = 924$$

---
## solution overview
> *the solution in words*

Before next steps, we ought to detail the solution — the *"common words and substrings" themselves*.

Let $cws$ be the set of common-words-&-substrings for $a$ and $b$

$$cws = \lbrace \; longest{ \; }common{ \; }substring, \; longest{ \; }common, \; longest, \; common, \; substring, \; two, \; all\; \rbrace$$

> *the longest common substring then — (of length 3) — is no less than the string of words "longest common substring"*

