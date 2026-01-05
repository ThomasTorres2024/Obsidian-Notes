---
title: Circulant Matrices
tags:
draft: "false"
---
# Circulant Matrices
Circulant Matrices are a special type of matrix related to the process of [[Convolution]], which thus has relevance to [[Machine Learning]] and Signal Processing. 

A Circulant matrix is a "Cyclical Convolution Matrix".  A [[Convolution Matrix]] has constant entries on each diagonal. The cyclical meaning means that the entries of the matrix cycles around to itself.  In a matrix of $n \times n$, we have that any given element in the matrix appears $n$ many times, and that all values along every diagonal are the same. For instance let us consider the following:
$$A=\begin{bmatrix}  2 & 5 & 1 & 0\\ 0 & 2 & 5 & 1\\
1 & 0 & 2 & 5 \\
5 & 1 & 0 & 2 
\end{bmatrix}$$
Notice that each diagonal has the same value entered. Also notice that each value appears $n=4$ many times in the matrix. Furthermore, observe how the matrix wraps around. Every value on the principal diagonal is fine since it has $n=4$ many entries. The super diagonal has 5, the sub has 3. And at opposite ends we place the opposing values. 

In fact, we can store this matrix in memory just by knowing a single column or row vector of our entry through the following fact:

It turns out that we can describe any [[Circulant Matrices]] of degree 4 as the following (We take for granted here the fact that for circulant matrix $P \in \mathbb{R}^{n \times n}, P^n=I_{n})$ :
$$\text{for n = } 4, A =c_{0}I_{n}+c_{1}P +c_{2}P^2+c_{3}P^3$$
We can write out the following [[Circulant Matrices]] to the degrees of $1$,2 and $3:$

$$P=\begin{bmatrix} 0 & 1 & 0 & 0 \\
					0 & 0 & 1 & 0 \\
					0 & 0 & 0 & 1 \\
					1 & 0 & 0 & 0 
\end{bmatrix}$$
$$P^2=\begin{bmatrix} 0 & 0 & 1 & 0 \\
					0 & 0 & 0 & 1 \\
					1 & 0 & 0 & 0 \\
					0 & 1 & 0 & 0 
\end{bmatrix}$$
$$P^3=\begin{bmatrix} 0 & 0 & 0 & 1 \\
					1 & 0 & 0 & 0 \\
					0 & 1 & 0 & 0 \\
					0 & 0 & 1 & 0 
\end{bmatrix}$$
The [[Circulant Matrices]] (I think by extension it forms a Vector Space, and this set of matrices generated from computing $P$ from the powers of $1-n$ is enough to provide a [[basis]] for said [[Vector Spaces and Vector Subspaces]]) form a nice [[Group]] and are closed under matrix additional and matrix multiplication. 

It helps to think of multiplication of some $P^k$ by $k$ as shifting the position of the band of $1$s up by 1 diagonal, and then moving the lower band up by 1 as well. 

---
# Eigen Vectors of [[Circulant Matrices]] and [[eigen values]] of [[Circulant Matrices]] 

The [[Eigen Vectors]] of every circulant matrix is going to be the same. This comes from the fact that:
$$Av=\lambda v \implies A(Av)=\lambda Av=A^2v=\lambda ^2 v \implies v \text{ is an eigen vector of } A^2 $$
We can use induction on this result and conclude it is true for $n$. Since we know that all of our [[Circulant Matrices]] are just powers of one another, we know that they must share the same [[eigen vectors]]. 

---
# Interpretation of [[Circulant Matrices]] as Polynomials 
In order to connect [[Convolution]] with [[Circulant Matrices]], we can consider [[Circulant Matrices]] as polynomials of some corresponding degree. Let the [[Group]] of [[Circulant Matrices]] be denoted by $\mathcal{C}$:

For $C,D\in \mathcal{C}$, if $C$ and $D$ are interpreted as polynomials it should be the case that $C \cdot D \in \mathcal{C}$, but under normal interpretations of $C$ ad $D$ we exceed the degree and are no longer closed. However, with [[Circulant Matrices]], we get the periodic assumption and can instead maintain the property of closure. 

Under normal assumptions, the following polynomials would result in a polynomial of degree 5, but under [[Circulant Matrices]] the [[Convolution]] of them results in another polynomial of degree 2:

(At the time of me writing this, I am not going to even remotely pretend to know what is going on here, that is on future me to try and decipher)
$$(3,1,2) \otimes (4,6,1)$$
Both are different under cyclic and non-cyclic convolution (I don't understand this.)

