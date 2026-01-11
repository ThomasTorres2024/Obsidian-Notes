---
title:
tags:
draft: "False"
---
# Condition Number of a System of Equations 
Given $Ax=b$ and $A$ has an [[Inverse Matrix]], we want to find the [[Condition Number]] of the system. Here we increment both $x$ and $A$ so:
$$Ax=b \to (A+\delta A)(x+ \delta x)=b$$

$$\iff Ax+\delta Ax + \delta Ax + \delta^2Ax =b$$
Here $Ax=b$ and for $\delta^2$ is treated as 0 so we can write:
$$\implies (\delta A)x+A(\delta x)=0$$
$$\implies (\delta x)=-A^{-1}(\delta A)$$
$$\implies \|\delta x\| \leq\|A^{-1}\| \|\delta A\| \|x\|$$
Which is equivalent to:
$$\frac{\|\delta x\|}{\|x\|} \bigg/ \frac{\|\delta A \|}{\|A\|} \leq \|A^{-1}\|\|A\| =\kappa(A)$$
Therefore, for solving any linear system we expect to have a [[Condition Number]] of the [[Condition Number of a Matrix]]. 

For some ill-conditioned matrix, $A$, we expect to lose $\log_{10}k(A)$ many digits. 