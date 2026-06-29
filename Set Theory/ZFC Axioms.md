---
title: Zermelo–Fraenkel Axioms
tags:
  - Set_Theory
draft: "False"
---
# ZFC Axioms
The [[ZFC Axioms]] are intended to provide an axiotimatic system supporting [[Set]] theory free of paradoxes such as [[Russel's Paradox]]. 

The ZFC axioms include the axioms from Zeremelo and Frankel, and a controversial [[Axiom of Choice]]. 

The ZFC axioms have been studied extensively as a branch of metamathematics. From this we have obtained the independence of the ZF axioms from the [[Axiom of Choice]] as well as the [[Continuum Hypothesis]]. 

Furthermore, the consistency of ZFC cannot be proven within its own theory, which is what [[Godel's Second Incompleteness Theorem]] reveals. 

---
# The $9$ Axioms
The first $1-8$ axioms consist of the Zemelo-Franklin axioms, and the $9$th consists of the Axiom of Choice or Well Ordered Principle (WOP). There are many equivalent formulations of these axions. These are taken from Wikipedia which source from Kunen. 

#### Axiom 1.) Extensionsality 
Two [[Set]]s are equivalent if they contain the same elements:
$$\forall x \forall y [ \forall z ( z\in x \iff z \in y ) \implies x = y ].$$
#### Axiom 2.) Regularity 
Every non-empty [[Set]] $x$ contains a member $y$ such that $x$ and $y$ are [[Disjoint Set]]s. 
$$\forall x (x \neq \emptyset \implies \exists y (y \in x \wedge y \cap x = \emptyset))$$
This axiom combined with the axiom of pairing and union entails that no element is an element of its own set. 

### Axiom Schema of Specification 
