---
title: Bisection
draft: "False"
tags:
---
# Bisection
Bisection is the standard method that we can use to obtain a subset of the $n$ [[eigen value]]s of a matrix, instead of all $n$ of them. For instance, we can find all eigen values on the interval $[1,2]$, the largest ten percent of eigen values, or the smallest thirty eigen values. We can then determine the [[eigen vectors]] using our computed [[eigen value]]s, from one iteration of the [[Inverse Iteration]] method. 

# Algorithm
It doesn't matter where we start for finding an [[eigen value]]. We use bisection to determine the eigenvalues of a [[Symmetric Matrix]], $A$, so we are guaranteed to have real eigen values already, meaning we can do searches along the real line to find our eigen values. We thus will look for roots of the [[characteristic equation]]:
$$p(x)=\det(A-xI)$$
There's a consideration, which is mentioned earlier in the section about finding solutions to general polynomial equations using the [[Companion Matrix]]. We cannot use the coefficients of our matrix to find our result and expect a good result, but if we instead had some method to continually evaluate $p(x)$ for different values for $x$, that is a perfectly fine method. 

Let us consider the principal submatrices of an irreducible (meaning that the sub and super diagonals are non-zero for all elements) and [[tridiagonal]] [[Symmetric Matrix]] $A$. Because $A$ is a [[tridiagonal]] matrix, it follows that $A$ has distinct [[eigen value]]s. So for the principal submatrix, $A^{(k)}$, it follows that the eigen values of $A^{(k)}$ satisfy the following property:
$$\lambda_{1}^{(k)} < \lambda_{2}^{(k)}  <  \cdots \lambda_{n}^{(k)} $$





