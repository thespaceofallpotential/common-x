# common-x:  *—from "knowledge culture" and a "universal solver", to a basic model of "organic general-intelligence"*

Yeah-yeah, ***finding*** solutions (within some problem-space) is cool... *—but did you ever think about **growing** them?*

Terms:-

-  **knowledge culture**:  *~~finding~~ **growing** solutions within (cultivated) problem-space*

- **universal solver**:  *symmetry based problem-reformulation makes respective solutions "compositionally accessible" ([notes](./notes/universal%20solver.md))*

- **organic general-intelligence**:  *against brute-force — domain invariant intelligence, from first-principles*

---
## overview

This repository ~~describes~~ *will eventually describe*:-

1. an [introduction](#introduction) to the premise of *"knowledge culture"*, to build intuition

2. problem background, & motivation

3. a generalised approach & method for solving *"common-x"* type problems — *(like "common-substring" and "common-subsequence")* — *([generation 1](./src/generation_1.ts))*

4. detail on approach & algorithmic extensibility *(& transformation)*, to handle different kinds of *"common-x"* problems

5. an account of the ways in which all "*problem-space problems*" are reformulable in terms of *"common-x"*; and a discussion on the approach and significance of reformulating problems to *"well-formed common-x"*

6. a discussion on the *"ideal form"* of *"common-x solvers"*, including data-structures & hardware

> Practical demonstrations:
> - [generation 1: basic substring — *(natural language)*](./src/generation_1.ts)
> - generation 2: substring — *(DNA)*
> - generation x: subsequence
> 
> Solvers *(generation 1)*:
>  - [Brute Force Runner](./src/gen_1/runners/bruteForceRunner.ts) | [Solver](./src/gen_1/solvers/BruteForceSolver.ts)
>  - [Constituent Runner](./src/gen_1/runners/constituientRunner.ts) | [Solver](./src/gen_1/solvers/ConstituientSolver.ts)
>  - [Cultivated Runner](./src/gen_1/runners/cultivatedRunner.ts) | [Solver](./src/gen_1/solvers/CultivatedSolver.ts)
>  - [Deductive Runner](./src/gen_1/runners/deductiveRunner.ts) | [Solver](./src/gen_1/solvers/DeductiveResolver.ts)
>  - [(Lazy Fake) Suffix-Tree Runner](./src/gen_1/runners/lazyFakeSuffixTreeRunner.ts) | [Solver](./src/gen_1/solvers/LazyFakeSuffixTreeSolver.ts)
>  - [Positive Projection Runner](./src/gen_1/runners/projectionSolver.ts) | [Solver](./src/gen_1/solvers/ProjectionSolver.ts)

---

## introduction
> *common-x: knowledge-culture — to understand (any) complexity, we must first understand it's simplicities, and how the two relate*

So, it turns out that we can reformulate some *"finding things, in spaces"* type-problems, to *"growing things, in spaces"* type-problems

> *—which is interesting, right?*
> 
> for intuition, think of the difference between recall and derivation — *(the difference between being told something to remember, like LLMs, say; and independently working things out from "first-principles")*

Like independent derivation, we can grow solutions *(to problem-space type problems)* piece-by-piece: from first-principles, to final structural form; and all without being told what to look for — without knowing in advance the *"special-domain structural forms" (which are subsequently grown)*

> for intuition, think of intellectual/cognitive creativity & insight — *the genesis of new domains of knowledge*

More than the difference between recall & derivation, perhaps the most apt analogy for this kind of *"remarkably organic"* problem-solving, is biological-growth.

Specifically, when we want to artificially engineer *(only very simple)* biological-form, we must first isolate and prepare a special environment, free from pollutants, full of all of the *"right kinds"* of ingredients, the *(chemical & biological)* *"ingredients"* from which the intended forms will grow. 

And this is exactly what must be done to *"**grow** solutions, to problem-space problems"* —  we first identify and isolate only the right kinds of *"ingredients"* from which the structural form of the final solution will grow...

> *...like a petri-dish in a laboratory environment...*
> 
> *...but within the entirely abstract domains of "**information & computation**"...*

Knowledge, it seems, is like a physical crop; and must be cultivated.

Learning, it seems, depends upon situationally appropriate *"knowledge culture"*, from which "structural representational forms" are cultivated, and grown to maturity. And just like physical-crops — *(in the physical environments of reality)* — it is sometimes quicker and easier to cultivate and grow a crop, than to find the same volume of form, arbitrarily distributed throughout some terrain...

> *Wild...* *—right?*
> 
> *musing:*
> 
> 	*consider, that with the [Cultivated Solver](./src/gen_1/runners/cultivatedRunner.ts), **might** we be looking at **the domestication of "wild-knowledge"** (almost as a physical biological artefact) — albeit one cultivated, grown (farmed?!), and evolved (bred?), within abstract realms... ([notes](./notes/cultivated%20solver.md))*

---
## problem background, & motivation


---
## generalised approach & method

2. a generalised approach & method for solving *"common-x"* type problems — *(like "common-substring" and "common-subsequence")* — *([generation 1](./src/generation_1.ts))*


## tbc

...


## appendix

Additional notes:
- [approach](./notes/approach.md)
- [cultivated solver](./notes/cultivated%20solver.md)
- [deductive resolver](./notes/deductive%20resolver.md)
- [organic general-intelligence](./notes/organic%20general%20intelligence.md)
- [symmetric index](./notes/symmetric%20index.md)
- [universal solver](./notes/universal%20solver.md)


