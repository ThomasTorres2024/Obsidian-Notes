---
title: Condition Number of Matrix-Vector Multiplication
tags:
draft: "False"
---
# Condition Number of Matrix-Vector Multiplication
This is a key [[Condition Number]] for numerical linear algebra. Let us consider some $A \in \mathbb{C}^{m \times n}$ and $x \in \mathbb{C}^n$ then we can express the condition number by considering the infinitesimal increment $\delta x$. We will also use an arbitrary [[Vector Norms]] The [[Condition Number]] for our problem is given by:
$$\kappa = \sup_{\delta x} \left( \frac{\|A(x+\delta x)-Ax\|}{\|Ax\|} \bigg / \frac{\|\delta x\|}{\|x\|  } \right)$$
$$= \sup_{\delta x} \left( \frac{\|A\delta x \| }{\|\delta x\|} \bigg / \frac{\|A x\|}{\|x\| } \right)$$
$$=\|A\|\frac{\|x\|}{\|Ax\| }$$
By the sub multiplicative property of [[Matrix Norms]], we have that:
$$\frac{\|x\|}{\|Ax\|} \leq \|A^{-1}\|$$
So:
$$\kappa \leq \|A\|\cdot \|A^{-1}\|$$
Which is true if we assume that $A$ is square and invertible. We can use the [[Moore-Penrose Pseudo Inverse]] of $A$ and obtain a similar result, so this assumption that is not necessary. 

For some choices of $x$ it follows that:
$$\kappa = \|A\|\cdot \|A^{-1}\|$$
Applying this information, we can determine the [[Condition Number]] of multiplying the inverse of a matrix by $b$, say if we have $Ax=b$, then:

$$\kappa = \|A^{-1}\| \frac{\|x\|}{\|b\|} \leq \|A\|\cdot \|A^{-1}\|$$

