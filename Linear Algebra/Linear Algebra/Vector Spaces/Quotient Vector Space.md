---
title: Quotient Vector Space
draft: "False"
tags:
  - AbstractAlgebra
  - LinearAlgebra
---
# Definition [[Quotient Vector Space]]

A [[Quotient Vector Space]] is a [[Vector Space]] formed by taking two vector spaces, $V$ and $W$, and forming the space $\frac{V}{W}$ such that Let $W$ be a [[Vector Subspace]] of $V$. Then we can form the vector space $\frac{V}{W}$, which is the set of all [[Coset]]s of the form $x+W$ where $x\in V$, namely:

$$\frac{V}{W}= \{ x+W :x \in V \}$$
Following the properties of [[Coset]]s, we have that the following results are true:

Since [[Coset]]s are equivalent classes, note that in the following it is not necessarily the case that $x=y$. Also the [[Identity Element]] of this [[Vector Space]] is $W$ itself namely $0+W$. 
$$x+W=y+W \iff x,y \in W$$

---
# Theorem
If $M$ and $N$ are complementary [[Vector Space]]s of the vector space $V$, then the correspondence $y \mapsto y+M$ for $y \in N$, is an [[Isomorphism]] between $N$ and $\frac{V}{M}$, in symbols $N \cong \frac{V}{M}$. 