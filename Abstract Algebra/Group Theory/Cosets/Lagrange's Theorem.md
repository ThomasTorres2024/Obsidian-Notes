---
title: Lagrange's Theorem
tags:
  - AbstractAlgebra
draft: "False"
---
# Theorem.) [[Lagrange's Theorem]]
Lagrange's Theorem states that for a [[Finite Group]], $G$ and a [[Subgroup]] $H \leq G$, then $|H| \bigg| |G|$. 

Moreover, the number distinct left (also true for right) [[Coset]]s of the $H$ over $G$ is given by $\frac{||G||}{||H||}$. 

### Proof.) 
Let the distinct cosets of $H$ in $G$ be:
$$a_{1}H,a_{2}H,\dots, a_{r}H$$
Where there are $r \in \mathbb{N}$ many distinct cosets. By $5$ of the lemma for cosets, it follows that each of the distinct cosets are disjoint. 

Furthermore, we know that:
$$\bigcup_{i=1}^r a_{i}H = G$$
If this were not the case then, $\exists a \in G \textbackslash (\bigcup_{i=1}^r a_{i}H )$. Since we supposed that $a_{i}H: 1 \leq i \leq  r$ are all of the distinct cosets of our set, and that by $5$ of the lemma again all of the cosets are disjoint, this contradicts the fact that these are __all__ of the distinct cosets of $H$ in $G$. 

Therefore it is valid to say that:
$$\bigcup_{i=1}^r a_{i}H = G$$
Furthermore we have that:
$$|G| = |a_{1}H|+|a_{2}H|+\dots + |a_{r}H| = \sum_{i=1}^r |a_{i}H|$$
For lemma $7$ we also have that for $a_i=e$:
$$|a_{i}H|=|eH|=|H|$$
Since the size of each [[Coset]] is equivalent it follows that every [[Coset]] has size $|H|$. We finally obtain that:
$$|G|=r|H|$$
Which concludes the proof that $|H| \bigg |G|$ and that there are $r$ many [[Coset]]s of $H$ over $G$

---
# Corollary .)  $\large [G:H]=\frac{|G|}{|H|}$
If $G$ is a finite group and $H \leq G$ then:
$$\large [G : H ] = \frac{|G|}{|H|} = r \quad (\text{ from above example})$$
# Corollary .)  $\large |a| \bigg| |G|$
In a [[Finite Group]], 