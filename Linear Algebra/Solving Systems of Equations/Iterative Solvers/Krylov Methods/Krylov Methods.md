---
title: Krylov Methods
tags:
draft: "False"
---
# Krylov Methods
If a matrix is massive, the only thing that can be done to it is iteratively multiply it by some vector $b$. 

Let assume that the Krylov space $\mathcal{K}_{n}$ spans $\mathbb{R}^n$:
$$\mathcal{K}_{n} = \langle b,Ab,A^2b,\cdots, A^{n-1}b \rangle $$
We assume that if we are looking for an eigen-vector that it can be found in $\mathcal{K}_{n}$. We can thus express our vector we are looking to find as :
$$v=\sum_{i=0}^{n-1} c_{i}A^ib$$
We can usually expect the vector be approximated or found in some space of dimension $r < n$ so we can reduce this to the following plus an error term. Let's suppose $n=1000$, and so we examine $r=100$ instead:
$$v=\left(\sum_{i=0}^{99} c_{i}A^ib \right) + \vec{\epsilon}$$
We can successfully reduce a problem that is of size 