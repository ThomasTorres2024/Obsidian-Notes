---
title: Rayleigh Quotient
draft: "False"
tags:
---
# Definition
The Rayleigh quotient in some sense is a measure of how much a value, $\alpha \in \mathbb{R}$, is an [[eigen value]]. The [[Rayleigh Quotient]] is defined in the following, given that $x \in \mathbb{R}^n$, $\lambda \in \mathbb{R}$, and $A \in \mathbb{R}^{m \times m}$:
$$r(x)=\frac{x^TAx}{x^Tx}$$
If $x$ is an [[eigen vectors]] of $A$, then it follows that $r(x)=\lambda$. Our motivation for this formula comes in the optimization problem of the following function:
$$\|Ax-\alpha x\|_{2}$$
Which is fully minimized to $0$, iff $x$ is an eigen vector of $A$. Because we rely on iterative methods for finding eigen values, then if $r(x)$ returns a good value based on $x$, then we can infer that $x$ is a good approximation for an eigen vector of $A$. 