---
title: Vector Convergence
tags:
  - LinearAlgebra
  - Real_Analysis
draft: "False"
---
# Vector Convergence 
Let $(x_{n})$ be a sequence of vectors in a [[Vector Space]] $V$ such that these vectors converge to a [[Vector]] $x \in V$, which gives:

* $\|x_{n} -x\| \to 0 \text{ as } n\to \infty$
* $\langle x_{n} -x,y \rangle \to0 \text{ as }n\to \infty$

If $(1)$ holds, then we have that:
$$\langle x_{n}-x,y \rangle \leq \|x_{n}-x\| \cdot \|y\| \to 0 $$
Which entails $(2)$. In finite dimensional vector spaces we have that $(2) \to (1)$.  

Let $\{z_{1},z_{2},\dots,z_{n} \}$ be an [[Orthonormal]] [[Basis]] in $V$. Let us assume $(2)$:
$$\langle x_{n}-x , z_{i} \rangle   \to 0 \quad i=1,\dots,N $$
Then we have that:
$$ \|x_{n} -x \|^2 = \sum_{i} |\langle x_{n}-x,z_{i} \rangle |^2 $$
Which entails that $\|x_{n}-x\|\to0$. We also can assume that this is a complete vector space after assuming it is on an inner product and then thereby normed vector space.