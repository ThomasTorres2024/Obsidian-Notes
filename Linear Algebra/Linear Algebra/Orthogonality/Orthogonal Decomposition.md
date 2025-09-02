---
title: Orthogonal Decomposition
tags: 
draft: "false"
---
# Orthogonal Basis and Orthonormal Basis 

Given a set of vectors, $V=\{\vec{v}_{1},\vec{v}_{2},\cdots,\vec{v}_{n} \}$, all of which are nonzero, we have an "[[orthogonal set]]" if for any $\vec{v}_{i},\vec{v}_{j} \in V$ we have that:

$$\vec{v}_{i}^T\vec{v}_{j}=0 \text{ if } i \neq j $$
A set is said to be [[orthonormal]] if 

$$ \vec{v}_{i}^T\vec{v}_{j}  =\begin{cases}  
0  & i \neq j \\  
1  & i = j  
\end{cases}$$
Say we have an orthonormal set given by $\beta=\{\vec{v}_{1},\vec{v}_{2},\cdots,\vec{v}_{n} \}$ where each $\vec{v}_{i} \in \mathbb{R}^n$. Consider $\vec{u} \in \text{span}(\beta)$:

$$\vec{u}=\alpha_{1}\vec{v}_{1}+\alpha_{2}\vec{v}_{2}+\cdots+\alpha_{n}\vec{v}_{n}$$
Let us consider $\vec{v}_{j}^T\vec{u}$:

$$\vec{v}_{j}^T\cdot\vec{u}=\vec{v}_{j}^T\cdot(\alpha_{1}\vec{v}_{1}+\alpha_{2}\vec{v}_{2}+\cdots+\alpha_{n}\vec{v}_{n})$$
$$\vec{v}_{j}^T\vec{u}=\alpha_{j}\vec{v}_{j}^T\vec{v}_{j}=\alpha_{j}$$
This follows due to the properties of all vectors in $\beta$ being orthonormal, since all other vectors are zeroed out, and the dot product of a vector with itself evaluates to 1.

We can prove that an orthogonal set is a [[linearly independent]] set. Consider $V=\{\vec{v}_{1},\vec{v}_{2},\cdots,\vec{v}_{n} \} \subseteq \mathbb{R}^n$, which is an orthogonal set. 

Let us consider the zero vector expressed as a [[linear combination]] of vectors in $V$:

$$\vec{0}=\alpha_{1}\vec{v}_{1}+\alpha_{2}\vec{v}_{2}+\cdots+\alpha_{n}\vec{v}_{n}$$
If we multiply both sides by each $\vec{v}_{j}$ where $1 \leq j \leq n$, then at each stage, we will get that:

$$\vec{v}_{j}^T\vec{0}=\alpha_{j}\vec{v}_{j}^T\vec{v}_{j}=\alpha_{j}$$
Thus, each $\alpha_{j}=0$, so the only linear combination of vectors from $V$ that results in the zero vector is the zero vector. Therefore, $V$ is a linearly independent set. So, an orthogonal set is a linearly independent one. 