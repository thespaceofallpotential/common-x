# sanitisation

An initial musing on the relation between sanitisation and common-x...

To be refined

> from: https://hachyderm.io/@smooch/115172905137976219
> 
> Huh, 
> 
> common-x -> sanitiation -> regex -> finite-automata
> 
> So while reimplementing sanitisation features -- (necessary to prepare my 5k+ markdown notes for processing, say, but also necessary for all the other textual demonstrations to follow here) -- I realised that sanitisation is also a "common-x problem"
> 
> Which means that we can think of sanitisation in terms of both positive and negative form/space, and switch between common-x methods:-
> 
> - "whittling" (of negative-space -- the common-x "deductive resolver")
> 
> - "growing" (positive-space -- the common-x "cultivated solver")
> 
> I typically think of sanitisation as whittling -- the iterative removal of unwanted patterns -- phrases, words, characters, etc
> 
> But there's another way to think of sanitisation -- reimplementation by finite set of valid characters, words, phrases, etc -- so growing (or regrowing) the sanitised version from "positive" elements
> 
> Just as with the cultivated solver, the latter involves curation up front, in a way which removes negative-form/space from the subsequent process, at the level of simplest forms (characters, then words built from those characters, then phrases ...)
> 
> As i thought about implementing this, (by using regex to identify the positive set), i realised that i would be then building something like a "custom structured regex" to then parse and sanitise
> 
> So i looked at regex engine implementation details, and lo-and-behold (Nate), i see finite automata...
> 
> So explicitly, i'm saying this cultivated solver process, which i'm referring to as "cultivated solution growth" maps directly to finite automata (and i might reimplement it like that to demonstrate)  
> 
> Stepping back, what i'll be doing then, is using these common-x patterns both to prepare and sanitise, and then to subsequently define and solve 
> 
> ---
> edit: nope -- the first is per string, the second is for a pair... still, the correspondence is making me think that there's more interesting observations to come...
>   
> re: I think, once the two stages are compiled, they'll consolidate, which (would if true) mean sanitising and solving on the same O(n)-ish pass (ignoring O(n)-ish preparation pass)
> Which has to be some "holy grail" type scenario...
> ---
> 
> 