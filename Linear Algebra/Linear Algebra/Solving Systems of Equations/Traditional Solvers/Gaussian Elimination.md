---
title: Gaussian Elimination
tags:
draft: "False"
---
# Gaussian Elimination 
[[Gaussian Elimination]] is the repeated application of [[Elementary Row Operations]] such that we can bring a matrix $A$ to  [[Row Echelon Form]] or [[Reduced Row Echelon Form]].  We can then easily solve a linear [[system of equations]] using [[back-substitution]]. 

In the case where $A$ is square, then we convert $A$ to an [[Upper Triangular Matrix]]. We achieve this by multiplying $A$ by a sequence of [[Lower Triangular Matrices]]:
$$L_{m-1}^{-1}\dots L_{2}^{-1}L_{1}^{-1}A=U$$
In turn we obtain an [[LU Factorization]] of the matrix $A$. 

# Algorithm 
We choose each $L_{k}$ by the following observation. Given the $k$th column of the matrix $A$, we want every $j$ such that $m \geq j > k$ to satisfy the following:
$$x_k=\begin{bmatrix} x_{1k}\\ \vdots \\x_{kk} \\ x_{k+1,k} \\ \vdots \\ x_{mk} \end{bmatrix} \to L_{k}x_k \begin{bmatrix} x_{1k}\\ \vdots \\x_{kk} \\ 0 \\ \vdots \\ 0 \end{bmatrix} $$
We go about this by choosing each $L_{jk}$ so that:
$$L_{jk}=\frac{x_{jk}}{x_{kk}}$$
Therefore the corresponding $L_k$ is of the form:
$$L_k=\begin{bmatrix} 1\\ & \ddots \\ & & 1 \\
& & -l_{k+1,k} &1 \\ & & \vdots & & \ddots \\
& & -l_{mk} &  & & 1
\end{bmatrix}$$
Matrices of this form are easily invertible. The only thing that needs to be done to create inverses using these matrices is to flip the negative signs 
to positive signs. Since we never touch the diagonal values of the matrix, we have that all of the diagonal entries of our lower triangular matrices will be 1. 

When practically implementing this algorithm, we do not actually form and multiply by the inverses of the $L_k$ matrices. They are formed implicitly. The following are the steps to our algorithm:

#### Algorithm Steps
* $U=A,L=I$ 
* for $k=1$ to $m=1$:
	* for $j=k+1$ to $m$:
		* $l_{jk} = u_{jk}/u_{kk}$
		* $u_{j,k:m}=u_{j,k:m}-l_{jk}u_{k,k:m}$

We do not actually need to write out $U$ and $L$ in our algorithm, this is just easier for instructional purposes, we tend to do everything in place for $A$ and form it into $U$. 

The work for [[Gaussian Elimination]] is $\frac{2}{3}m^3$ many flops and is of [[Time Complexity]] $O(n^3)$. We prefer using [[Gaussian Elimination]] over some techniques like [[Householder Transformation]] because of a significantly lower flop count.

---
# Pivoting 