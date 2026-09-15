---
title: Reducible
tags:
  - LinearAlgebra
draft: "False"
---
# Reduced/Decomposed Definition
If $M,N$ are [[Invariant Subspace]]s both invariant under $A$, and $V= M \oplus N$, then $A$ is a "Reduced" [[Linear Transformation]].   

Another way of thinking of this idea is that given any $M$ vector space invariant under $A$, then there are many ways to find some vector space $N$ such that $V= M \oplus N$, and it is not always the case that some $N$ exists. 

We can reverse the process here. If we let $M,N$ be two vector spaces and let $A,B$, be linear transformations on these spaces respectively. Let $V=M\oplus N$, then we can define a linear transformation $C$ be the direct sum of  such that:
$$Cz=C(x,y)=(Ax,By)$$
