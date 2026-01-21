---
title: General Linear Group
tags:
draft: "False"
---
# General Linear Group
The [[General Linear Group]] consists of all $2 \times 2$ matrices over the reals with a non-zero [[Determinant]]. We denote the group by:
$$GL(2,\mathbb{R}) = \left\{ A=\begin{bmatrix} a & b\\ c & d \end{bmatrix} : \det(A) \neq 0 \right\}$$
The [[Binary Operation]] over this group is [[Matrix Multiplication]]. 

# Proof of Being a [[Group]]: 
Consider, $A,B \in GL(2,\mathbb{R})$. Then $A \cdot B$ we have that $\det(AB)=\det(A) \cdot \det(B) \neq 0 \implies AB \in GL(2,\mathbb{R}$, so we have that the group is closed. [[Matrix Multiplication]] is associative. The identity matrix is the identity element of the group, and is in the group since it has a [[Determinant]] of 1. 

The general form for an [[Inverse Matrix]] is:
$$A^{-1}= \frac{1}{\det(A)} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$
And can be algebraically verified to yield that $AA^{-1}=A^{-1}A=I_2$. 

Therefore, it is a [[Group]]. 
