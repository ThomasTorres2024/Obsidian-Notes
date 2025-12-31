---
title: QR Algorithm With Shifts
tags:
draft: "false"
---

# Introduction
The [[QR Algorithm without Shifts]] has a [[cubic convergence]]. This a fantastic feat for an algorithm. It turns out that the speed of it can be increased by using [[Shifts]]. Instead of determining the eigen values of $A_{0}$, we consider the eigen values of:
$$A_{0}-\mu I$$
Notice that the eigen values of this matrix are jus the eigen values of $A$ shifted by $\mu$:
$$\det(A_{0}-\mu I-\lambda I)=\det(A_{0}-I(\mu+\lambda))$$
This simply shifts the eigen values over by a factor of $\mu$. The eigen vectors of $A_{0}$ and $A_{0} - \mu I$ are the same also, for ev $v$:
$$(A_{0}-\mu I)v= \lambda v- \mu v=(\lambda-\mu)v$$
Therefore, we have the [[QR Algorithm With Shifts]] algorithm. 

It turns out that the performance of the algorithm can be further improved if $A_{0}$ is an [[Upper Hessenberg Matrix]] instead of any regular matrix. We can determine an [[Upper Hessenberg Matrix]] factorization using a [[QR Factorization]] of $A$. 

The zeros in the [[Upper Hessenberg Matrix]] remain in the f

---
# QR Method With Shifts Algorithm 
* 1.) Improve the matrix $A$ by converting $A$ to an [[Upper Hessenberg Matrix]] $A_{0}$, by finding a [[similarity transformation]] between $A$ and $H$: 
$$A=Q^HHQ$$
* 2.) Use the [[QR Algorithm With Shifts]] in order to determine the eigen values of $A$ by using the eigen values of $H$ 

We get even better performance if $A$ is [[Hermitian]], because then doing the same process would result just in an [[Upper Hessenberg Matrix]], but instead a [[tridiagonal]] matrix. This goes very very quickly. 