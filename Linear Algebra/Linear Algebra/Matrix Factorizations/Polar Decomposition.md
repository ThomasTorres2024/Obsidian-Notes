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

The [[Polar Decomposition]] is in contrast to the "Cartesian Decomposition" (see [[Spectral Theorem]]) namely the fact that:
$$A=\frac{1}{2}(A+A^H) + \frac{1}{2}(A-A^H)  $$
---
An alternative way to think about obtaining a polar decomposition is through $\sqrt{M} \in \mathbb{C}^{n \times n}$ which has the same eigen vectors as $M$ and its eigen values are the square roots of $M$.  It must be the case that $M$ has a full set of eigen values and is diagonalizable. 

To construct $M$, we need to diagonalize it: 

$$M=PDP^{-1}=PD^{\frac{1}{2}}D^{\frac{1}{2}}P^{-1}$$
If we assume that $A=SQ$ then $A^T=Q^TS^T$:

$$A^TA=Q^T$$
---
# Criteria For [[Normal Matrices]] 

### Theorem).
If $A=UP$ is a polar decomposition of a linear transformation $A$ then a necessary and sufficient condition that $A$ is normal is that $PU=UP$.  

$Proof).$
$U$ is not uniquely determined by $A$, thus we should interpret the statement s if $A$ is normal then $P$ commutes with every $U$ and if $P$ commutes with some $U$ then $A$ is normal. Consider the following:
$$AA^H=UP^2U^H  \quad A^HA=P^2$$
Then it must be the case that $A$ is normal iff $U$ and $P^2$ commute which is actually the equivalent of $P$ and $U$ commuting, which thus shows the result. 