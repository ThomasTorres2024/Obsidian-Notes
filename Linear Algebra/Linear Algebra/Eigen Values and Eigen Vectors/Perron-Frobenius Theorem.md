---
title: Perron-Frobenius Theorem
tags: 
draft: "false"
---
# Definition of the Perron-Frobenius Theorem

The Perron-Frobenius Theorem states that for $A \in \mathbb{R}^{n \times n}$ where $A^T=A$ that:

* There is an [[eigen value]] $\lambda_{0}$ such that for all other eigen values $\lambda$ in the [[spectrum]] of $A$ that $\lambda_{0} > \lambda$, that is $\lambda_{0} = \text{max}(\lambda)$
* The eigen value $\vec{x}$ corresponding to $\lambda_{0}$ has all positive values 
* $\text{alg mult}(\lambda_{0})=1$

We can look at a brief sketch of this proof. 

All eigen values of $A$ are known to be real since $A$ is a symmetric matrix, and by [[Spectral Theorem Definition and Proof]] all of its eigen values must be real. 

---
# Intuition 

If we examine and plot some of the eigen values of any $A \in \mathbb{R}^{n \times n}$ and plot the eigen values in $\mathbb{C}$, we observe what appear to be symmetries in some of the eigen values, and also see that one of the eigen values is significantly larger than the others. 

