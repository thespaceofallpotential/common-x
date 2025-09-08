# generation 1
> *based on [example 1 data](/notes/example_1/data.md)*

- [inputs](#inputs)
- [problem-space](#problem-space)
- [solution](#solution)
- [objective](#objective)
- [solvers](#solvers)

---
## inputs

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

---
## problem-space

For two input-strings $a,b$ , of lengths $n,m$ , set to axis $x,y$ , respectively, the area of the corresponding two-dimensional problem-space is equal to $n \times m$

Given:-

$$n = |a| = 28$$

![](/images/example-1--a-empty.png)
> figure 1. *Spatial representation of $a$*

...and...

$$m = |b| = 33$$

![](/images/example-1--b-empty.png)
> figure 2. *Spatial representation of $b$*

The corresponding area of the *"problem-space"* of *"example 1"* — *(within-which all common words and substrings thereof, might/must be found)* — is...

$$n \times m = |a| * |b| = 28 \times 33 = 924$$

![](/images/example-1--empty.png)
> figure 3. *Spatial representation of $a \times b$*

---
## solution

![](/images/example-1--solution-frame.png)
> figure 4. *Spatial representation of the solution to $a \cap b$ , framed by the lower-dimensional inputs $a$ above and $b$ left, with common elements (in both higher and lower dimensions) coloured orange*

---
## objective

Solve the common-substring problem without enumerating *"negative-space"* within higher-dimensional space.

![](/images/example-1--hallucination.png)
> figure 5. *Spatial representation of the solution to $a \cap b$ (coloured orange), and positive projection space (coloured purple), within problem-space (large square area), framed by lower-dimensional inputs (top and left)* 

---
# costs

In *(very casual)* mathematical terms, *(indexing in)* lower-dimensional space is ***additive***, whereas enumeration of higher-dimensional space is ***multiplicative***. 

> ***higher-dimensional cost** (multiplicative)*: $n \times m = |a| * |b| = 28 \times 33 = 924$

> ***lower-dimensional cost** (additive)*: $n + m = |a| + |b| = 28 + 33 = 61$

---
## solvers

### brute-force
> *[solver](/src/gen_1_solvers/brute_force_solver.py) | [runner](/src/generation_1_runner.py)*

The brute-force solver:-
1. does not pre-filter *"polarity"* *(ignore negative-space)*, and;
2. enumerates the entire problem-space area

$$a \times b = 924$$

> ***lower-dimensional** spatial cost: $0$*

> ***higher-dimensional** spatial cost: $924$*

> ***total** spatial cost: $924$*

---
### positive projection
> *[solver](/src/gen_1_solvers/positive_projection_solver.py) | [runner](/src/generation_1_runner.py)*

The positive projection solver:-
1. pre-filters *"polarity"* *(ignores negative-space)*, but;
2. does not cross-correlate the projection from lower to higher dimensional spaces, and;
3. enumerates only the area coloured purple *(within higher-dimensional problem-space)*

Twenty discreet areas:
$$[2 \times 4] + [2 \times 1] + [2 \times 2] + [2 \times 3] +$$
$$[1 \times 4] + [1 \times 1] + [1 \times 2] + [1 \times 3] +$$
$$[2 \times 4] + [2 \times 1] + [2 \times 2] + [2 \times 3] +$$
$$[1 \times 4] + [1 \times 1] + [1 \times 2] + [1 \times 3] +$$
$$[3 \times 4] + [3 \times 1] + [3 \times 2] + [3 \times 3]$$
$$= 90$$

> ***lower-dimensional** spatial cost: $61$*

> ***higher-dimensional** spatial cost: $90$*

> ***total** spatial cost: $151$*

---
### cultivated
> *[solver](/src/gen_1_solvers/cultivated_solver.py) | [runner](/src/generation_1_runner.py)*

The cultivated solver:-
1. pre-filters *"polarity"* *(ignores negative-space)*, and;
2. cross-correlates the projection from lower to higher dimensional spaces, and;
3. enumerates only the area coloured orange *(within higher-dimensional problem-space)*

> ***lower-dimensional** spatial cost: $61$*

> ***higher-dimensional** spatial cost: $20$*

> ***total** spatial cost: $81$*
