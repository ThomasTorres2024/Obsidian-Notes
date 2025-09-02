---
title: Polar Decomposition
draft: "false"
tags:
---
# Polar Decomposition 

Every matrix, $A$ can be factored into some $QS$ where $S$ is a [[symmetric matrix]] and $Q$ is an [[orthogonal matrix]]. 

We can obtain this result from SVD:
$$A= U \Sigma V^T = U \Sigma U^T U V^T$$
Notice that $U \Sigma U^T$ is a symmetric matrix and that $UV^T$ is orthogonal because the product of two orthogonal matrices is another orthogonal matrix. 

---
An alternative way to think about obtaining a polar decomposition is through $\sqrt{M} \in \mathbb{C}^{n \times n}$ which has the same eigen vectors as $M$ and its eigen values are the square roots of $M$.  It must be the case that $M$ has a full set of eigen values and is diagonalizable. 

To construct $M$, we need to diagonalize it: 

$$M=PDP^{-1}=PD^{\frac{1}{2}}D^{\frac{1}{2}}P^{-1}$$
If we assume that $A=SQ$ then $A^T=Q^TS^T$:

$$A^TA=Q^T$$