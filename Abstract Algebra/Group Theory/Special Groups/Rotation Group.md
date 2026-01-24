---
title: Rotation Group
tags:
draft: "False"
---
# [[Rotation Group]]
The Rotation Group consists of rotation matrices of an angle $\theta$ about the origin, $0,0$ such that every member of the [[Group]] is of the form:
$$R_\theta=\begin{bmatrix} \cos(\theta) &-\sin(\theta)
\\ \sin(\theta) & \cos(\theta)
\end{bmatrix}$$
Notice that each $R_\theta$ is a [[Unitary Matrices]], so $\det(R_\theta)=1 \implies$  all of the matrices here are invertible and furthermore the [[Dihedral Group]] $\leq SL(2,\mathbb{R}) \leq GL(2,\mathbb{R})$. 

If $n \in \mathbb{N}$ then, by theorem $3.4$ for [[Abstract Algebra/Group Theory/Special Groups/Cyclic Group|Cyclic Group]]s, $\left\langle R_{\frac{2\pi}{n}} \right\rangle$ is a [[Subgroup]] of $SL(2,\mathbb{R})$ and $GL(2,\mathbb{R})$. ([[General Linear Group]], [[Special Linear Group]])

The set generated is:
$$\left\langle R_{\frac{2\pi}{n}} \right\rangle=\left\{R_{0},R_{\frac{2\pi}{n}},R_{\frac{4\pi}{n}}, \dots R_{\frac{2\pi(n-1)}{n}}  \right\}$$
