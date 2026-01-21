---
title: General Linear Group
tags:
draft: "False"
---
# General Linear Group
The [[General Linear Group]] consists of all $2 \times 2$ matrices over the reals with a non-zero [[Determinant]]. We denote the group by:
$$GL(2,\mathbb{R}) = \left\{ A=\begin{bmatrix} a & b\\ c & d \end{bmatrix} : \det(A) \neq 0 \right\}$$
The [[Binary Operation]] over this group is [[Matrix Multiplication]]. 

We can further extend this to any [[Field]], and we can express:
$$GL(2,\mathbb{F}) = \left\{ A=\begin{bmatrix} a & b\\ c & d \end{bmatrix} : \det(A) \neq 0 \right\}$$
Where $\mathbb{F}$ typically is one of the following: $$\mathbb{Z,R,Q,C}$$
# Proof of Being a [[Group]]: 
Consider, $A,B \in GL(2,\mathbb{R})$. Then $A \cdot B$ we have that $\det(AB)=\det(A) \cdot \det(B) \neq 0 \implies AB \in GL(2,\mathbb{R}$, so we have that the group is closed. [[Matrix Multiplication]] is associative. The identity matrix is the identity element of the group, and is in the group since it has a [[Determinant]] of 1. 

The general form for an [[Inverse Matrix]] is:
$$A^{-1}= \frac{1}{\det(A)} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$
And can be algebraically verified to yield that $AA^{-1}=A^{-1}A=I_2$. 

In the case where we are not dealing with $2 \times 2$, we know a [[Determinant]] of non-zero implies the existence of some inverse matrix.

Therefore, it is a [[Group]]. 
