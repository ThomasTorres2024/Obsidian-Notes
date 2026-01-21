---
title: Special Linear Group
tags:
draft: "False"
---
# Special Linear Group 
The [[Special Linear Group]] consists of all $2 \times 2$ matrices where:
$$SL(2,\mathbb{R})= \left\{ A= \begin{bmatrix} a & b\\ c & d \end{bmatrix} : \det(A)=1 \right\}$$
But we can extend this to $n \in \mathbb{N}$:
$$SL(n,\mathbb{R})= \left\{ A= \begin{bmatrix} a & b\\ c & d \end{bmatrix} : \det(A)=1 \right\}$$
# Proof of being a Group 
Clearly $I_n$ the identity matrix $n \times n$ is the identity element here since $\det(I_n)=1$. 
[[Matrix Multiplication]] is associative. Also for $A,B \in SL(n,\mathbb{R})$ we have that $\det(AB)=\det(A)\det(B)=1$ so $AB \in SL(n,\mathbb{R})$. The inverse of some $A$ exists since its [[Determinant]] is non-zero, and furthermore its determinant is the reciprocal of $A$, so $\det(A^{-1})=1 \implies A^{-1} \in SL(n,\mathbb{R})$. 

$$\therefore SL(n,\mathbb{R}) \text{ is a Group}$$

