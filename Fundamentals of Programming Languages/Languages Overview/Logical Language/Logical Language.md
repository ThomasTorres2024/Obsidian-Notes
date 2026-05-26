---
title: Logical Language
tags:
draft: "False"
---
# Logical Language 
A [[Logical Language]] is a [[Fundamentals of Programming Languages/Languages Overview/Programming Language]] which is constructed by essentially constructing a large set of facts. During execution, we check to see if a fact is true or if it lines up with our expectations, and we are able to evaluate output from that. Examples of [[Logical Language]]s include Prolog. 

---
# Logic as a Programming Language 

Logic can be used a form of programming language, using "__propositional logic__". A __proposition__ is a statement which has a truth value, meaning that is either true or false (of course no paradoxes). 

__Propositional Logic__ uses propositions and various rules of inference to allow us to deduce results using the __modus ponens__, essentially if $A \implies B$ and $A$ is true then $\therefore B$. 

Propositional logic  required something more powerful and complex in order to do computation and useful things using for all and there exist statement. First order logic introduces universal quantifiers and existential quantifiers.  with existential and universal quantifiers. 

---
# First-Order Logic (FOL)
Predicates are functions that map arguments into true/false. A predicate's signature is of the following form: 

$$p: \text{ Objects  } : \longrightarrow \{ \text{ True, False} \}$$

Some of the following are predicated:

* human(X) (Evaluates true if $X$ is a human)
* mother(X,Y) (Evaluates true if $X$ is the mother of $Y$) 

Predicates and quantifiers can be used to create statements about sets of objects for instance: 

* $\exists X[$mother($X$,Paul)$]$ 
* $\forall Y[$human($Y)$]

We can also use and, or, not (connectives), to create more complicated statements. There are also if-then rules. 

We can use the "Horn Clause" in order to computation with many predicates, and pool them into a single implication statement with a single consequent. For example consider the following where each $P_i$ is a predicate: 

$$P_{1} \wedge P_{2}  \wedge \cdots \wedge P_{n} \implies P_{0}$$

Reasoning with the Horn Clause is equivalent to reasoning via modus ponens, which allows us to things mechanically. Using this information gives rise to the Prolog language. 