---
title: Quotient Transformation
tags:
  - LinearAlgebra
draft: "False"
---
# Definition and Notation). 
If $A$ is a [[Linear Transformation]] that is on a [[Vector Space]] $V$ where $M$ is a [[Vector Subspace]] of $V$ where $M$ is an [[Invariant Subspace]] under $A$, then we can define a Quotient Transformation. 

Consider the [[Quotient Vector Space]] formed by $\frac{V}{M}$ with the associated transformation $\frac{A}{M}$ on this space. We denote $V/M=V^{-}$ and $\frac{A}{M}=A^{-}$. 

The elements of this space are [[Coset]]s of the form:
$$x^- =x+M \quad x^- \in V^- $$
We define the transformation $A/M$ by:
$$A^-x^-=(Ax)^- \quad : \forall x \in V$$
In other words, in order to find the transformation of the coset $x^-=x+M$ by $A^-$ find the coset of $Ax$, namely $Ax+M$. 

When dealing with cosets we must show that they are well defined. Let $x+M=y+M$. Then, $x-y \in M$ via properties of Cosets. This tell us that $A(x-y) \in M$ as well since it is invariant, and thus $Ax+M=Ay+M$ also via cosets, so it is well defined. 

---
# If $M$ is [[Reducible Subspace]] 
Suppose $M$ is reducible alongside an appropriate vector space $N$, then it follows that:
$$A= B \oplus  C$$
Where $B,C$ are transformations defined on $M,N$ respectively of $V$. We want to ascertain the relationship between $A^-$ and $C$. 

In a sense, $B$ describes what $A$ does to $M$, and both $A^-$ and $C$ describe what $A$ does outside of these two. 

Let $T$ be the correspondence that assigns each $x\in N$ the coset $x^- =x+M$. $T$ is an [[Isomorphism]] (should be clear by first isomorphism theorem) between $N$ and $\frac{V}{M}$. 

$C$ "carries the transformation over to" $A^-$. This can be shown. Let $Cx=y, x\in N$, then:
$$A^-x^-=(Ax)^-=(Cx)^-=y^-$$
It then follows that:
$$TCx=Ty=T(Ax)=Ax+M=A^-Tx$$
Thus, $TC=A^-T$. In other words, $A^-$ and $C$ are isomorphic to one another. This is a useful fact for working with [[Quotient Vector Space]]s. 