---
title: Conjugate Gradient
tags:
draft: "False"
---
# Conjugate Gradient
The [[Conjugate Gradient]] method is a [[Krylov Methods]] for solving linear [[system of equations]] for some $Ax=b$ where $A$ is a symmetric [[Positive Definite Matrix]].  The method is intended to work with Sparse Matrices ([[Sparse Matrix]]). 

Since $A$ is SPD, we know that $x$ has a solution. We can find an approximate solution Instead of directly solving for the value of $x$ in the [[Krylov Subspace]] of dimension $j$ rather than the full $x$, meaning that we have a method iteratively computing the following with respect to some arbitrary [[norm]] with respect to the $j$th iterate:
$$\|r\|=\|Ax_j-b\|$$
Once we have crossed some threshold value, $\epsilon$, we terminate and obtain an approximate $\hat{x}=x_j$. 

Because $A$ is SPD, then its [[Quadratic Form]] has a unique global minimum ([[global minima]]). Recall that the [[Quadratic Form]] is defined by:
$$\phi(x)=\frac{1}{2}x^TAx-x^Tb$$
And that the [[Gradient]] of this expression is:
$$-\nabla\phi(x)=-(Ax-b)=b-Ax=r$$Where $r$ is the residual. 

The [[Conjugate Gradient]] method calculates iterates of $x_k$ by the following equation:
$$x_{k+1}=x_k+\alpha_kp_k$$
Where $p_k$ is the search direction and $\alpha_k$ is the magnitude we are searching by. Our goal of this optimization problem is to minimize $\phi(x_k+ \alpha_k p_k)$. 

Here, our search direction is determined by:
$$a_k=\frac{r_k^Tp_k}{p_k^TAp_k}$$
Here we choose $p_k$ to be A-conjugate to orthogonal to the previous direction. We want this to be the case because a natural result of this is the condition that:
$$p_k^TAp_j = 0, j < k$$