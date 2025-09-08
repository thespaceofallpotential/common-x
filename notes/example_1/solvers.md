# solvers
> *based on [example 1 data](/notes/example_1/data.md)*

---
## brute-force
> *[solver](/src/gen_1_solvers/solvers/BruteForceSolver.py) | [runner](/src/gen_1_solvers/runners/bruteForceRunner.py)*

The brute-force solver does not enumerates the entire problem-space area.

$$a \times b = 924$$

> ***lower-dimensional** spatial cost: $0$*

> ***higher-dimensional** spatial cost: $924$*

> ***total** spatial cost: $924$*

---
## positive projection
> *[solver](/src/gen_1_solvers/solvers/PositiveProjectionSolver.py) | [runner](/src/gen_1_solvers/runners/positiveProjectionRunner.py)*

The positive projection solver enumerates the area coloured purple.

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
## cultivated
> *[solver](/src/gen_1_solvers/solvers/PositiveProjectionSolver.py) | [runner](/src/gen_1_solvers/runners/positiveProjectionRunner.py)*

The cultivated solver enumerates only the area coloured orange *(within higher-dimensional problem-space)*.

> ***lower-dimensional** spatial cost: $61$*

> ***higher-dimensional** spatial cost: $20$*

> ***total** spatial cost: $81$*

