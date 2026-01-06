---
title: Circulant Matrices
tags:
draft: "false"
---
# Circulant Matrices
Circulant Matrices are a special type of matrix related to the process of [[Convolution]], which thus has relevance to [[Machine Learning]] and Signal Processing. 

A Circulant matrix is a "Cyclical Convolution Matrix".  A [[Toeplitz Matrix]] has constant entries on each diagonal. The cyclical meaning means that the entries of the matrix cycles around to itself.  In a matrix of $n \times n$, we have that any given element in the matrix appears $n$ many times, and that all values along every diagonal are the same. For instance let us consider the following:
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

More generally, we can express any family of circulant matrices for $A \in \mathbb{R}^{n \times n}$ by:
$$A=\sum_{i=0}^{n-1}c_{i}P^{i}: c_{i} \in \mathbb{C}$$
### Motivation
The reason that we care about this class of matrices is because of their applications to signal processing and to machine learning generally. [[Circulant Matrices]] can be used as filters in signal processing, and also help make [[Convolutional Neural Networks]] as well. Furthermore, [[Circulant Matrices]] are connected to the [[Discrete Fourier Transform]] 

When we perform [[Convolution]], we apply [[Circulant Matrices]] in [[Cyclic Convolution]] (closure under some polynomial [[Group]]). Otherwise, we would apply a [[Toeplitz Matrix]], where 

---
# Eigen Vectors of [[Circulant Matrices]] and [[eigen values]] of [[Circulant Matrices]] 

The [[Eigen Vectors]] of every circulant matrix is going to be the same. This comes from the fact that:
$$Av=\lambda v \implies A(Av)=\lambda Av=A^2v=\lambda ^2 v \implies v \text{ is an eigen vector of } A^2 $$
We can use induction on this result and conclude it is true for $n$. Since we know that all of our [[Circulant Matrices]] are just powers of one another, we know that they must share the same [[eigen vectors]]. 

Note that every circulant matrix $A$ is a linear combination of the $n$ [[Circulant Matrices]] of the same corresponding size. Notice that each of the matrices:
$$A=\sum_{i=0}^{n-1}c_{i}P^{i}: c_{i} \in \mathbb{C}$$
Notice that each $P$ in this sum is also a [[Permutation Matrix]], which implies each $P$ is an [[orthogonal matrix]], which means that $PP^T=I_{n} \implies$ that every singular value of $P$ is going to be 1. We also know that since $P$ is an [[orthogonal matrix]], all of its eigen-values must have a modulus of 1. Let us consider the following [[Circulant Matrices]]:

$$\det(P-\lambda I_{n})= \det \left( \begin{bmatrix} -\lambda & 1 & 0 & 0\\
0 & -\lambda & 1 & 0\\
0 & 0 & -\lambda & 1\\
1 & 0 & 0 & -\lambda
\end{bmatrix} \right) =0$$
Using [[Cofactor Expansion]] we can quickly see that for this particular $P$ that:
$$\det(P-\lambda I_{n})=1-\lambda^4 = 0\iff \lambda ^4=1$$
Which entails that the [[eigen value]]s of [[Circulant Matrices]] are actually the corresponding [[Roots of Unity]] for some given power, $n$. Here it corresponds to the fourth roots of unity. Let us denote each root of unity by:
$$\large w^k=e^{\frac{2\pi ki}{n}}$$
Where $k$ corresponds to the $k$th entry for the $n$th root of unit where $1 \leq k \leq n$. 

Furthermore notice that since $P$ is an [[orthogonal matrix]] $P^{-1}=P \implies$ $P$ is also [[Normal Matrices]], which furthermore means that $P$ and furthermore all [[Circulant Matrices]] are  [[unitarily diagonalizable]], thus:
$$P=Q\Lambda Q^H$$
Another way we can look at this fact is that any two circulant matrices will commute with one another, implying that they are all normal. 

So, we get a full set of [[eigen vectors]] that are guaranteed to be mutually [[orthonormal]] to one another. The general form for $Q$ for some $P$ actually tends to be the [[Vandermonde Matrix]] formed by taking the $n$ roots of unity and subsequently applying their power to $0,1,\dots, n-1$. 

Let us consider some $P \in \mathbb{C}^{4 \times 4}$, then we can write its [[eigen vectors]] in the following way:
$$L=\begin{bmatrix} 1 & 1 & 1&1\\
1 & w & w^2 & w^3\\
1 & w^2 & w^{4} & w^{6}\\
1 & w^3 & w^6 & w_{9}
\end{bmatrix}$$
We can normalize each column of $L$, and it would result in a nice corresponding matrix $Q$ that could be used for the diagonalization of a circulant matrix. We know that any $P$ has the same eigen-vectors as any [[Circulant Matrices]]. So, this $Q$ should also work. We also know that for a corresponding root of unity for $n$, we have that $w^n=1$ which leads us to a much nicer expression:
$$L=\begin{bmatrix} 1 & 1 & 1&1\\
1 & w & w^2 & w^3\\
1 & w^2 & 1 & w^{2}\\
1 & w^3 & w^2 & w
\end{bmatrix}$$
We can determine the [[eigen value]]s  for any [[Circulant Matrices]] by considering the following. Let us consider some degree 4 [[Circulant Matrices]], $A$ which can thus be expressed by:
$$A=c_{0}I_{n}+c_{1}P+c_{2}P^2+c_{3}P^3$$
We claim that we can obtain the [[eigen vectors]] of $A$ by computing the following for its corresponding $L$. Let us condense the coefficients into $\vec{c}=[c_{0},c_{1},c_{2},c_{3}]^T$

Then, it should follow that for:
$$L\vec{c}_{i}=\lambda_i$$
I think if you look at the corresponding rows of $L$, and recall the fact that for some $A$, that $\lambda^2$ is an eigen value of $A^2$ if $\lambda$ is an ew of $A$, then this identity becomes a lot more obvious. Let us consider the eigen vector $v$ of $A$, then:
$$Av=(c_{0}I_{n}+c_{1}P+c_{2}P^2+c_{3}P^3)v=(c_{0}+c_{1}\mu+c_{2}\mu^2+c_{3}\,u^3)$$

---
# Interpretation of [[Circulant Matrices]] as Polynomials 
In order to connect [[Convolution]] with [[Circulant Matrices]], we can consider [[Circulant Matrices]] as polynomials of some corresponding degree. Let the [[Group]] of [[Circulant Matrices]] be denoted by $\mathcal{C}$:

For $C,D\in \mathcal{C}$, if $C$ and $D$ are interpreted as polynomials it should be the case that $C \cdot D \in \mathcal{C}$, but under normal interpretations of $C$ ad $D$ we exceed the degree and are no longer closed. However, with [[Circulant Matrices]], we get the periodic assumption and can instead maintain the property of closure. 

Under normal assumptions, the following polynomials would result in a polynomial of degree 5, but under [[Circulant Matrices]] the [[Convolution]] of them results in another polynomial of degree 2:

(At the time of me writing this, I am not going to even remotely pretend to know what is going on here, that is on future me to try and decipher)
$$(3,1,2) \otimes (4,6,1)$$
Both are different under cyclic and non-cyclic convolution (I don't understand this.)

