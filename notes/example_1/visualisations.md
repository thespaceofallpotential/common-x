# visualisations
> *seeing things, in spaces*

## visualising input-strings

### a
> *[a (clean)](/data/a-clean.txt) | [A (original)](/data/a.txt)*

![](images/example-1--a-empty.png)

> Fig x: represents the input string $a$ of length $28$

### b
> *[b (clean)](/data/b-clean.txt) | [B (original)](/data/b.txt)*

![](images/example-1--b-empty.png)

> Fig x: represents the input string $b$ of length $33$

---
## visualising problem-space

For two input-strings $a,b$ of lengths $n,m$, set to aes $x,y$, *respectively*; the area of the corresponding two-dimensional problem-space is equal to $n \times m$

> or $O(n \times m)$

![](images/example-1--empty.png)

> Fig x: depicts a $28 * 33$ grid, which represents the higher-dimensional projection of $a \times b$ , or problem-space, within which the solution is to be found

> $$n \times m = |a| * |b| = 28 \times 33 = 924$$

---
## visualising the solution within problem-space

![](images/example-1--solution.png)

> Fig x: depicts the solution to the common-substring problem for input-strings $a$ and $b$ within a $28 * 33$ grid; with common-words marked by orange dots/squares; and common-substrings *(of words)* represented by diagonal-lines

Earlier, we noted that the longest common-substring is 3 words long.

Now as we visualise the solution within problem-space, note that the longest common-substring appears twice in $a$, yet only once in $b$.

> *(so therefore twice along the $x$ ais, but only once on the $y$ ais — represented by the fact that the two respective diagonal-lines of length 3, occupy the same vertical space)*

---
## visualising problem-space *"polarity"*: positive-space, and negative-space

The *(above and)* below image depicts the distribution of solution-space within problem-space.

We will sometimes refer to the solution within *"problem-space"* in the absolute term: *"solution-space"*.

Other times, it will be useful to refer to both *"solution-space"*, and *"problem-space which is not solution-space"*

For convenience, we'll refer to:-

- the former as *"positive-space" (or, solution-positive space)*, and;

- the latter as *"negative-space" (or solution-negative space)*

![](images/example-1--solution.png)

> Fig x: depicts the positive-space by orange dots/squares; with negative-space uncolored

This distinction between positive and negative space will form the basis of several generalised methods for *"finding things, in spaces"*.

---
## visualising the relationship between lower-dimensional input-strings, and higher-dimensional problem-space

All common-form must exist in both lower-dimensional spaces

Now that we can visualise *"positive-space"* within the two-dimensions of *"problem-space"*, let's also take a look at inter-dimensional correspondence/ alignment, between higher andd lower dimensional space

![](images/example-1--solution-frame.png)

> Fig x : depicts the correspondence between lower and higher dimensional representations of positive-space; where input-strings are lower-dimensions, and problem-space as the higher-dimensional product; with a on top; and b down the left

### a (top)

![](images/example-1--a.png)

> Fig x : depicts the elements of input-string $a$ which correspond with positive-space by orange dots/squares, (with negative-space uncolored)

### b (left)

![](images/example-1--b.png)

> Fig x : depicts the elements of input-string $b$ which correspond with positive-space by orange dots/squares, (with negative-space uncoloured)

Higher-dimensional spaces are inherently arbtrarily-plural lower-dimensional spaces, and the relationship between dimensions *(/reference-frames)* will form the basis for several generalised methods for *"finding things, in spaces"*.

---
## visualising positive possiblity-space

> *as the unchecked/unbound projection of lower-dimensional positive-space, between input-strings*

![](images/example-1--projection-frame.png)

> Fig x : depicts positive possiblity-space as an unchecked projection between the positive elements of two lower-dimensional input-strings, coloured purple

Over the course of defining several generalised methods for *"finding things, in spaces"* — based upon the identification and isolation of polarity *(/quality)* between dimensions *(/reference-frames)*, introduced above — a curious phenomenon of unchecked/unbound possiblity-space emerged, which at scale visually resembles wave interference patterns, which define approximate outer-bounds of all positive-space

---
## visualising hallucination-space

> *as the resultant invalid checked/bound projection of lower-dimensional positive-space, between input-strings*

![](images/example-1--hallucination.png)

> Fig x : depicts resultant invalid positive possiblity-space, as after projection between the positive elements of two lower-dimensional input-strings is cross-verified, with solution in orange, and hallucination-space in purple

We are all now familiar with the notion of LLM hallucination: which we might define as structure which is technically valid, although does not correspond with extrinsic constrants *(of reality, in the case of LLMs)*

Here within common-x: notice that, from the reference-frame of either input-string, all projection-space is technically valid, and only by cross-correlation with some extrinsic frame of reference, the other input-string in this case, can contextual validity be defined; at which point, all positive projection-space which is left unrealised, is directly analogous to LLM hallucination

---
