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

Notice that we can express any $L_k$ as the following [[Rank 1 Perturbation]] given the following matrix $$\mathcal{l}_k= \begin{bmatrix} 0 & 0 & \dots & l_{k,k+1} & l_{k,k+2} \dots & l_{k,k+m} \end{bmatrix}^H$$, and the $k$th identity vector:
$$L_k=I-\mathcal{l}_ke_{k}^H$$
We can also easily determine the inverses of these matrices. Notice that the matrix 
$$L_k^{-1}=I+\mathcal{l}_ke_k^H$$
Is the inverse of $L_k$, and can be worked out to be the case algebraically. If we were to compute multiple $m-1$ many inverses:
$$L=\prod_{i=1}^{m-1}L_{i}^{-1}=\begin{pmatrix}
1      &        &        &        &        \\
\ell_{21} & 1      &        &        &        \\
\ell_{31} & \ell_{32} & 1      &        &        \\
\vdots & \vdots & \ddots & \ddots &        \\
\ell_{m1} & \ell_{m2} & \cdots & \ell_{m,m-1} & 1
\end{pmatrix}$$

When practically implementing this algorithm, we do not actually form and multiply by the inverses of the $L_k$ matrices. They are formed implicitly. The following are the steps to our algorithm:
#### Algorithm Steps
* $U=A,L=I$ 
* for $k=1$ to $m=1$:
	* for $j=k+1$ to $m$:
		* $l_{jk} = u_{jk}/u_{kk}$
		* $u_{j,k:m}=u_{j,k:m}-l_{jk}u_{k,k:m}$

We do not actually need to write out $U$ and $L$ in our algorithm, this is just easier for instructional purposes, we tend to do everything in place for $A$ and form it into $U$. 

The work for [[Gaussian Elimination]] is $\frac{2}{3}m^3$ many flops and is of [[Time Complexity]] $O(n^3)$. We prefer using [[Gaussian Elimination]] over some techniques like [[Householder Transformation]] because of a significantly lower flop count.
### Solving $Ax=b$ with [[LU Factorization]]:
We can factor $A$ into the matrices $L$ and $U$:
$$Ax=b \iff LUx=b\iff Ux=L^{-1}b$$
We can then solve this system via [[back-substitution]] since $U$ is [[Upper Triangular Matrix]]. 

---
# Pivoting and [[Numerical Stability]] of [[Gaussian Elimination]]
Under the correct conditions, it is possible for [[Gaussian Elimination]] without pivoting to fail. Consider the algorithm applied to the following matrix:
$$B=\begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix}$$
We would automatically fail since $A_{11}=0$ with our algorithm. If we perturb the 0 entry by even a little, say by $10^{-20}$ then, from the algorithm we would obtain the following $LU$ decomp:
$$A=\begin{bmatrix} 10^{-20} & 1 \\ 1 & 1 \end{bmatrix}$$
$$L=\begin{bmatrix} 1 & 0\\ 10^{20} & 1 \end{bmatrix},U=\begin{bmatrix} 10^{-20} & 1\\ 0 & 1-10^{20} \end{bmatrix}$$
Due to numerical considerations, our approximate LU decomp would actually, on some computer system, be represented by:
$$\hat{L}=\begin{bmatrix} 1 & 0\\ 10^{20} & 1 \end{bmatrix},\hat{U}=\begin{bmatrix} 10^{-20} & 1\\ 0 & -10^{20} \end{bmatrix}$$
Computing $\hat{L}\hat{U}$ is significantly different than $A$:
$$\hat{L}\hat{U}=\begin{bmatrix} 10^{-20} & 1 \\ 1 & 0 \end{bmatrix}$$
Using $\hat{L}$ and $\hat{U}$ to solve $\hat{L}\hat{U}x=b$, we will get a resulting $x$ which would not solve the original system. We say that [[LU Factorization]] is not [[backward stable]]. Our $L$ matrices may have a [[Condition Number of a Matrix]] which are potentially unstable.  