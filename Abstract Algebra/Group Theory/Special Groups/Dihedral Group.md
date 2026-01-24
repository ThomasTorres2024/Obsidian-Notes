---
title: Dihedral Group
tags:
draft: "False"
---
# Dihedral Group
The Dihedral Group, $D_{2n}$, consists of rotation matrices of an angle $\theta$ about the origin, $0,0$ such that every member of the [[Group]] is of the form:
$$R_\theta=\begin{bmatrix} \cos(\theta) &-\sin(\theta)
\\ \sin(\theta) & \cos(\theta)
\end{bmatrix}$$
And of reflection matrices of the form:
$$F= \begin{bmatrix} 1 & 0\\ 0 & -1
\end{bmatrix}$$

Notice that each $R_\theta,F$ are a [[Unitary Matrices]], so $\det(F)\neq0,\det(R_\theta) \neq 0$. Thus, the [[Dihedral Group]] is a [[Subgroup]] of $GL(2,\mathbb{R})$, the [[General Linear Group]]. 

The set generated is:
$$\left\{R_{0},R_{\frac{2\pi}{n}},R_{\frac{4\pi}{n}}, \dots nR_{\frac{2\pi(n-1)}{n}},FR_{0},FR_{\frac{2\pi}{n}},FR_{\frac{4\pi}{n}}, \dots FR_{\frac{2\pi(n-1)}{n}}   \right\}$$
Notice that this is a [[Subgroup]] of $GL(2,\mathbb{R})$ but not $SL(2,\mathbb{R})$ since $\det(F) =-1.$ 
Our group is of [[Order]] $2n$ to account for the reflector and the rotation matrices. 

Notice that the [[Rotation Group]]:
$$\left\langle R_{\frac{2\pi}{n}} \right\rangle=\left\{R_{0},R_{\frac{2\pi}{n}},R_{\frac{4\pi}{n}}, \dots R_{\frac{2\pi(n-1)}{n}}  \right\}$$
Is clearly a [[Subgroup]] of the [[Dihedral Group]], thus:
$$\left\langle R_{\frac{2\pi}{n}} \right\rangle \leq D_{2n}$$
