---
title: Rank of a Matrix
tags:
draft: "False"
---
# Rank Definition
We can think of the rank of a matrix as the [[dimension]] of the [[Column Space]] and the [[Row Space]], which are always equivalent, and we just refer to this quantity as the rank:
$$\text{dim}(\text{col}(A))=\text{dim}(\text{row}(A))=r$$
A matrix which has a full rank has the maximum possible rank. For a matrix, $A \in \mathbb{F}^{m \times n}$, the matrix has rank:
$$r=\text{min}(m,n)$$
$A$ also has $n$ [[linearly independent]] columns. A [[full rank]] matrix is one which is [[injective]], meaning that for $x,y \in \mathbb{F}^n$, we have that:
$$A\vec{x} = A\vec{y} \Longleftrightarrow \vec{x} = \vec{y}$$
If $A$ has rank $r < \text{min}(m,n)$ it follows that there is a non-trivial zero given by $\vec{c}$ such that $A\vec{c}=\vec{0}$, meaning that for any $z \in Col(A)$, that we can obtain $z$ infinitely many ways using the non-trivial zero in the nullspace.   

---
# Rank Properties 
For $A \in \mathbb{F}^{m \times n}$ where $\text{rk}(A)=n$ and $m \geq n$ and $B \in \mathbb{F}^{n \times d}$ then:
$$\text{rk}(AB)=\text{rk}(B)$$
