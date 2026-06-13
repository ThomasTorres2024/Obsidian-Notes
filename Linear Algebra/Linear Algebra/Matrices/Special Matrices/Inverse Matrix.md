---
title: Inverse Matrix
tags:
  - LinearAlgebra
draft: "False"
---
# Inverse Matrix
The [[Inverse Matrix]] is a [[Matrix]] $B$ that for some $A \in \mathbb{F}^{n \times n}$ satisfies:
$$AB=BA=I_{n}$$

---
# Invertible Matrix Theorem
The following conditions are equivalent:

1. $A$ is an invertible matrix
2. $A$ is row equivalent to $I_n$ 
3. $A$ has $n$ pivot positions
4. The equation $Ax=0 \implies x =0$
5. The columns of $A$ form a [[Linearly Independent]] set 
6. The [[Linear Transformation]] $x \mapsto Ax$ is [[injective]] 
7. The equation $Ax=b$ has a unique solution each $b \in \mathbb{F}^n$
8. The [[Column Space]] of $A$ [[Span]]s $\mathbb{F}^n$
9. The linear transformation $x\mapsto Ax$ is an [[Automorphism]] from $\mathbb{F}^n \to \mathbb{F}^n$. 
10. $\exists C \in \mathbb{F}^{n \times n}$ such that $CA=I_{n}$
11. . $\exists D \in \mathbb{F}^{n \times n}$ such that $AD=I_{n}$
12. The [[Transpose]] of $A$, $\exists A^{-T}$. 