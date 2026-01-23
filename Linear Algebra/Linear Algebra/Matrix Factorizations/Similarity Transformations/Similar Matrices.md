---
title: Similar Matrices
draft: "false"
tags:
---
# Similar Matrices Definition 

Consider $A,B \in \mathbb{R}^{n \times n}$.  If $A$ and $B$ are similar, then for some [[invertible matrix]] $M$ we can write that 

$$B=M^{-1}AM$$

We can prove that $A$ and $B$ will have the same eigen values if there is a [[similarity transformation]] between the two. It is also the case that $A$ and $B$ have the same number of [[linearly independent]] [[eigen vectors]]. 

Consider the eigen value $\lambda$ in the spectrum of $A$ and the eigen vector $\vec{x}$ associated with $\lambda$
$$A\vec{x}=\lambda \vec{x}$$
$$AMM^{-1}\vec{x}=\lambda \vec{x}$$
$$M^{-1}AMM^{-1}\vec{x}=\lambda M^{-1}\vec{x}$$
$$BM^{-1}\vec{x}=\lambda M^{-1}\vec{x}$$
Note that $\vec{y}=M^{-1}\vec{x} \in \mathbb{R}^n$ and is simply just another vector:

$$B\vec{y}=\lambda \vec{y}$$

Therefore, if $A$ and $B$ are similar, they have the same eigen-values, but their eigen vectors are not guaranteed to be the same. 

We can also prove this using the definition of an [[Eigen Value]] by using the definition with the [[Characteristic Polynomial]]:
$$p_B(\lambda )=\det(B-I_n\lambda)=\det(M^{-1}AM-I_n\lambda)$$
$$=\det(A-I_n\lambda)\cdot \det(M)\cdot \frac{1}{\det(M)}=p_A(\lambda)$$

Examples of similarity transformations consist of [[Eigen Value Decomposition]] ($A=PDP^{-1}$). The matrices $A$ and $B$ have the same [[eigen values]] with the same [[algebraic multiplicities]] and thus the same [[characteristic equation]]. 

Since these matrices have the same eigen values it follows that they must have the same [[traces]] and [[determinants]]. 

There are many different kinds of similarity transformations. Some of the relevant ones include: 

1. Matrix Diagonalization/[[Eigen Value Decomposition]]
2. [[Jordan Canonical Form]] 
3. [[Schur's Triangularization]] 

---
# Intuition 

We can think of diagonalization, and moreover similarity transformations, as essentially changing the base of our original problem. 

A matrix factorization of $A=M^{-1}BM$ can reduce the complexity the operation of $A^{5000}$ significantly, meaning that it is a lot easier to carry our the operation in the basis of $B$ rather than in $A$, since $B$ is taken to be a nicer matrix. 

If it were the case that $B$ is diagonal, then: 

$$A^{5000}= \prod_{i=1}^{5000} M^{-1}BM=M^{-1}B^{5000}M$$
#


