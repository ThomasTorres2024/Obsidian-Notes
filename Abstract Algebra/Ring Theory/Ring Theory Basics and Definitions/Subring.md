---
title: Subring
tags:
  - AbstractAlgebra
draft: "False"
---
# Subring 
Related to the idea of a [[Subgroup]]. A [[Subring]] is a [[Ring]] $S$ of some ring $R$ such that $S \subseteq R$, which has the same operations as $R$. 

There is a similar test for subrings as their is for subgroups. 

---
# Theorem Subring Test 
A non-empty subset $S$ of a ring $R$ is a __subring__ of $R$ if $S$ is closed under subtraction and multiplication, if for $a,b \in S$ then $a-b,ab \in S$. 

$Proof.$ 
We know that the one step subgroup test satisfies that $S\neq \emptyset$ and that $S$ is an [[Abelian Group]]. 

We inherit associativity and distributivity from the parent ring $R$, which leaves only closure to be checked. 

If it passes the one step subgroup test and the multiplicative closure rule, then it follows that $S$ is a [[Ring]].

---
# Examples 
### Example 1.)
For any ring $R$, it is trivially true that $R$ and $\{0\}$ are [[Subring]]s of any [[Ring]]. These are known as the __Trivial Subrings__ of $R$. 
### Example 2.) 
$\{0,2,4,\}$ is a subring of $\mathbb{Z}_{6}$. Note that $1$ is the identity in $\mathbb{Z}_{6}$ but $4$ is the identity in $\{ 0,2,4\}$.

### Example 3.)
For each $n \in \mathbb{N}$, we have that: 
$$n\mathbb{Z} = \{0, \pm n, 2\pm n, \cdots \}$$
Is a subring of $\mathbb{Z}$. 

### Example 4.)
$R=\{f : f \text{ is cts on }[0,1] \}$ and $S = \{ f : f \text{ is cts on }[0,1], f(0)=0\}$. 

Then $S$ is a [[Subring]] of $R$ where we use pointwise multiplication and addition of functions. 