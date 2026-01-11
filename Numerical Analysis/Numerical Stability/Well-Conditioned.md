---
title: Well-Conditioned
tags:
draft: "False"
---
# Well-Conditioned 
A [[Well-Conditioned]] problem or algorithm in numerical analysis is a problem where a small perturbation results in a small change. We can gain insight into the [[Conditioning]] of a problem or algorithm by considering its [[Condition Number]]. 

An example of a problem that is [[Well-Conditioned]] is the computation of the [[eigen value]]s of a [[Symmetric Matrix]].

if we have that $Ax=\lambda x$ and $(A+\delta I_n)x=(\lambda + \delta)x$ then we have that the eigen values of each matrix is respectively $\lambda$, and $\lambda + \delta$. 

It follows that:
$$|\delta \lambda | \leq \|\delta A\|_2$$
I am not sure how the following is obtained, however the absolute condition number is given by $\hat{\kappa}=1$ and the relative [[Condition Number]] is given by $\kappa=1$. The relative condition number is given by $\kappa=\frac{\|A\|_2}{|\lambda|}$. 