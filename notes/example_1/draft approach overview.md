
# approach overview - draft
> *based on [example 1 data](/notes/example_1/data.md)*

> *"Solve the common-substring problem without enumerating "negative-space" within higher-dimensional space*
> 
> - [objective](/notes/example_1/objective)

- polarity insight
- symmetry mechanism
- cost: reason

---
## approach
> *not all problem-space is equal*

### divide & dismiss

The cause of the challenge of problem-space type problems, like common-x, is due to the exponential relationship between the size of inputs and resultant possibility-space/ problem-space.

For this reason, the first order of business ought to be the minimisation of input size 

The well-known problem solving method *"divide and conquer"* is solution focused — emphasis is on what is being sought.

The inverse — *"divide & dismiss"* — instead focuses on what what can be eliminated from further analysis.




It can be useful to think of *(abstract problem-)* space in terms of the characteristics of the form which exists within it.

The space within which common elements exist *(coloured orange)*, is *"solution positive-space"*, and the remainder *(coloured black)* as *"solution negative-space"*.

---
## symmetry
> *see: [symmetric index](/notes/symmetric%20index)*

Framing the higher-dimensional area by lower-dimensional inputs helps illuminate the alignment & symmetry between higher and lower dimensions.

We can think of the alignment of positive-space between dimensions in terms of:-

1. **quality of form**: qualitative value

2. **spatial coordinates**: positions

Due to this symmetry between higher and lower dimensions, we can index higher-dimensional space via lower-dimensional space.

---
## costs

In *(very casual)* mathematical terms, *(indexing in)* lower-dimensional space is ***additive***, whereas enumeration of higher-dimensional space is ***multiplicative***. 

> ***higher-dimensional cost** (multiplicative)*: $n \times m = |a| * |b| = 28 \times 33 = 924$

> ***lower-dimensional cost** (additive)*: $n + m = |a| + |b| = 28 + 33 = 61$

---