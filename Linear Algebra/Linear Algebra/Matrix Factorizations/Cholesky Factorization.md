---
title: Cholesky Factorization
draft: "false"
tags:
---
# Cholesky Factorization Definition

A matrix, $A \in \mathbb{C}^{n \times n}$ can be said to have a Cholesky factorization if $A$ [[Hermitian]] Matrix and is [[Positive Definite Matrix]] (HPD). 

We can also obtain a Cholesky factorization if we can express $A=LU=LDV=LDL^T$ where all diagonal entries of $D$, $D_{ii} \in \mathbb{R}^{+}$ so that we can express $A$ as:

$$A=LDL^T=LD^{\frac{1}{2}}D^{\frac{1}{2}}L^T=LD^{\frac{1}{2}}(LD^{\frac{1}{2}})^T=RR^H$$

If we restrict ourselves to positive diagonal entries, then the factorization is unique. Otherwise, the factorization is not unique. 

We can think of the Cholesky factorization as finding $R$, a lower triangular matrix, which is the equivalent of a square root, since $RR^H=A$

---
# Cholesky Algorithm
Given that a matrix $A$ is Hermitian positive definite, it follows that $A$ can be factored into a corresponding lower triangular matrix on the left, a diagonal matrix in the center, and an upper triangular matrix on the right. Let $A$ be defined in the following way:

$$A=\begin{bmatrix} a_{11} & w^T\\ w & K \end{bmatrix}$$
Let $K$ be symmetric positive definite as well and let $a_{11} >0$ (for an SPD matrix it must be the case that all principal submatrices of $A$ must be SPD, so $a_{11} >0$). 

Notice that given this matrix the following factorization is possible:
$$A=\begin{bmatrix} \alpha & 0\\ w/\alpha & I \end{bmatrix} \cdot \begin{bmatrix} 1 & 0\\ 0 & K-ww^H/a_{11} \end{bmatrix} \cdot \begin{bmatrix} \alpha & w^H/a\\ 0 & I  \end{bmatrix}$$
We then apply the formula recursively to obtain a factorization of $K-ww^H/\alpha_{11}$. Note that this matrix is positive definite as well. By assumption, it must also be the case that $(K-ww^H/\alpha_{11})_{11} >0$. This allows our algorithm to be fully defined and deterministic  

The resulting expression is the following sequence:
$$A= R_n^H \dots R_2^HR_{1}^HR_{1}R_{2} \dots R_n$$
Which compresses down into the product of an [[Upper Triangular Matrix]] and a [[Lower Triangular Matrices]]:
$$A=R^HR$$
We can express this computation as an in-place algorithm that is performed on the upper part of $A$. It is not necessary to perform the whole result on both portions of the matrix as $R$ is upper triangular. We obtain the following algorithm:

* $R=A$
* for $k=1$ to $m$:
	* for $j=k+1$ to $m$:
		* $R_{j,j:m}=R_{j,j:m}-R_{k,j:m}\overline{R}_{kj}/R_{kk}$ 
		* $R_{k,k:m}=R_{k,k:m}/\sqrt{R_{kk}}$

The amount of operations required to form $A$ using big $O$ notation ([[Time Complexity]]) is $O(m^3)$. Similarly the number of flops is $\frac{1}{3}m^3$. 

---
# [[Numerical Stability]] of the [[Cholesky Factorization]]
The [[Cholesky Factorization]] is said to always be stable. For some $A$ that is [[Hermitian]] [[Positive Definite Matrix]], it follows that $A$ is always stable.

---
# Solving [[system of equations]] with [[Cholesky Factorization]]
Given some SPD $A$, we can express $A$ as $A=R^HR$. We can then solve $Ax=b$ by writing:
$$R^HRx=b$$
$$R^Hy=b$$
We can begin by solving this system of equations.
Then we can solve the second system of equations given by:
$$y=Rx$$
Once $x$ is solved we obtain a solution to the system of linear equations. The time complexity is still $O(n^3)$ for this operation, and also still takes $\frac{1}{3}m^3$ many flops to perform. 


---
