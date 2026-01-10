---
title: Householder Transformations
tags:
draft: "false"
---
# Introduction
Computation of the [[QR Factorization]] in introductory examples makes use of the numerically unstable [[The Gram-Schmidt Process]] and [[Modified Gram-Schmidt Process]], both of which are [[numerically unstable]] after several hundred iterations. Via [[Householder Transformation]]s, we can express a matrix $A\in \mathbb{R}^{m \times n}$ where $m \geq n$ as the product of a matrix with orthonormal columns, $Q \in \mathbb{R}^{m \times n}$, and an upper triangular matrix $R \in \mathbb{R}^{n \times n}$ which is guaranteed to have [[Linear Algebra/Vector Spaces/Rank|Rank]] $n$, at least this is the case when we compute a [[Reduced QR]] factorization.

---
# Main Idea
The main idea of the [[Householder Transformation]] is to iteratively take out the remaining $m-k-1$ entries of each column where $k=0$, and increments by $1$ each time we go through a new column. We want to express $R$ in the [[Full QR]] Factorization, and it turns out we can do this by left multiplying $A$ by a sequence of orthogonal matrices which eventually yields matrix $R$. 

![[Pasted image 20251006075759.png]]
Our way of being able to construct matrices $Q_{k}$ comes from [[House Holder Reflectors]]. We make each $Q_{k}$ a unitary matrix where $Q_{k} \in \mathbb{R}^{m \times m}$. We define each $Q_{k}$ to be:
$$Q_{k}= \begin{bmatrix} I & 0 \\ 0 & F \end{bmatrix}$$
The way that I intuitively understand [[Householder Transformation]]s is that, we are trying to find some multiple of $e_1=[1,0,0, \dots,0]^T$. We want to obtain this vector by some [[Unitary Matrices]], and so we get the corresponding $i$th column, to, be some constant multiple of $e_1$.  By repeating this process, if we can find some transformation to achieve this starting at each $ii$, for our matrix, such that every intermediary transformation is Unitary, then we can write out:
$$\prod_{i=1}^{n}Q_i^HA=R$$
At each iteration we thus want to be able to find some reflection matrix, $F$ such that:
$$Fx=\|x\|e_1$$
It turns out that we can do this, and we need to make use of the [[House Holder Reflectors]] Matrix. In order to derive this matrix, we need to find the [[Hyperplane]] which has a [[normal vector]] corresponding to $v=\|x\|e_1-x$. Visually, $v$ is the vector such that:
$$v+x=\|x\|e_1$$
![[Pasted image 20260108145912.png]]

In order to define our reflector, $F$, we can begin with trying to find an appropriate projection matrix ([[Projection Matrices]]) onto $H$ and orthogonal to $v$. We can do this with the following matrix:
$$H=I-\frac{vv^H}{v^Hv}$$
We can turn $H$ into a reflector by realizing that for any $y \in \mathbb{R}^n$, we have that $y$ is projected onto the [[span]] of $H$. However, if we continue going by one more step of $\frac{vv^H}{v^Hv}$, it turns out that we end up just on the other side of $H$. We use this idea to construct our reflector, $F$. 

Where $I \in \mathbb{R}^{(k-1) \times (k-1)}$, and $F \in \mathbb{R}^{(m-k+1)\times(m-k+1)}$ where $F$ is unitary as well. We want to introduce zeroes into column $k$ when we multiply by $F$. Householder transformation matrices are given by:
$$H=I-2\frac{xx^T}{x^Tx}$$
$H$ satisfies the conditions of being [[Hermitian]] and also being a Unitary Matrix ([[Unitary Matrices]]) , both of which easily can be verified. We can interpret a matrix vector product with $H$ as a mapping. When computing $Hy$ we can see that:
$$Hy=\left(I-2\frac{xx^T}{x^Tx}\right)=y-2\frac{xx^Ty}{x^Tx}$$
Notice that from this formula, given 2 very special vectors, $y=x$ and $y$ that tis orthogonal to $y$ yields:
$$Hy=y \text{ when y is orthogonal to x}$$
$$Hx=-x \text{ when the vector orthogonal to the plane is x}$$
From this we obtain the interpretation that $H$ is in essence a reflector, that anything orthogonal is flipped over its side, and that anything which is already on it, stays on it. It's also a mirror because the vector length doesn't change during the process.

---
# From [[House Holder Reflectors]] to [[QR Factorization]]
We hope to apply our house holder transforms to successfully left multiply our matrix $A$ to obtain $R$ implicitly. We need to be able to find $H_{i}$ such that $H_{i}u=v$ This is important for finding each new column of our matrix $r$. We have another additional condition on top of this that $\|u\|_{2}=\|v\|_{2}$. 

It turns out that if $x=u-v$ then our Householder matrix can be formed using this particular $x$. Given our matrix $A$ which has column $u=a_{i}$:
$$a_{i}=[a_{1i}, a_{2i}, a_{3i},\cdots,a_{mi}]^T$$
It follows that we want our $v$ to be $e\cdot\alpha$ where $\|e \cdot \alpha\| = |\alpha|=v_{i}$. So we have that, $v_{i}=\pm \|a_{i}\|e_{i}$  We can choose to take the plus or minus version of $v_{i}$, and generally we choose plus to reduce the chance of numerical errors due to cancelation. 

---
# Householder Least Squares and [[Numerical Stability]]
It turns out that when we compute the $QR$ for $A$ using house holder, and then go to do least squares with this QR it turns out we are not actually minimizing $\|Ax-b\|$ anymore, but due to errors in precision we actually have $QR$ give us the following matrix:
$$A+\delta A$$
So, we are minimizing the following quantity, which turns out is [[backward stable]], meaning that the following condition holds true, which is to say that the difference between the norms of the two vectors is negligible, at the level of machine precision. 
$$\|(A+\delta A)\tilde{x}-b\|_{2}=\min\frac{\|\delta A\|}{\|A\|}=O(\epsilon_{\text{machine}})$$
It also turns out that we are still backward stable even if we compute $Q^Hb$ implicitly or explicitly. 

Another result is that we are backward stable even if we do column pivoting:
$$AP=\hat{Q}\hat{R}$$

---
# The [[Householder Transformation]] Algorithm
The [[Householder Transformation]] is an in-place algorithm, which transforms some matrix, $A \in \mathbb{R}^{m \times n}$, and implicitly forms $Q$ and transforms $A$ to be an [[Upper Triangular Matrix]]. We expect that for $A, m \geq n$, and we thus have the following algorithm:

* for $k=1$ to $n$:
	* $x=A_{k:m,k}$
	* $v_k = \text{sign}(x_1)\|x\|_2e_1+x$ 
	* $v_k=v_k/\|v_k\|_2$
	* $A_{k:m,k:n}=A_{k:m,k:n}-2v_k(v_k^HA_{k:m,k:n})$

We select some portion that we wish to convert to $e_1$ in our process, and then we construct some $v_k$ that we use as a part of the [[House Holder Reflectors]], this is the hyperplane that we want our matrix to be orthogonal to. We implicitly obtain $F$, and then we do $FA$, but since a portion of the matrix, the previous work we have done, is preserved, we can ignore these spots and carry out the computation. 

We also have algorithms to handle $Q^Hb$ and $Qb$ computations, which essentially just apply the series of householder reflectors to $b$ when are trying to solve $Ax=b$. If we can express:
$$Ax=b \iff QRx=b \iff Rx=Q^Hb$$
Then we can easily just use [[back-substitution]] to solve this system of equations. But that requires the computation of $Q^Hb$:
##### Algorithm for Computing some $Q^Hb$:
* for $k=1$ to $n$:
	* $b_{k:m}=b{k:m}-2v_k(v_k^Hb_{k:m})$
Notice again the same underlying pattern of computing the steps for the [[Householder Transformation]], we also preserve the previous work done. just by virtue of how our House Holder matrices are formed. 

We can compute $Qb$ by doing the products just in reverse order:
##### Algorithm for Computing some $Qb$: (here I am doing 1 based indexing since we are using MatLab syntax)
* for $k=n, k >0, k--$:
	* $x_{k:m}=x_{k:m}-2v_k(v_k^Hx_{k:m})$

We can construct our matrix $Q$ by the algorithm for some $Qb$ if we consider each $b=e_1.e_2,\dots e_n$. 

---
# [[Time Complexity]] of [[Householder Transformation]]s: 
The work for [[Householder Transformation]]s is:
$$\approx 2mn^2-\frac{2}{3}n^3 \text{ flops }$$
Using big o notation we have that for a square $A$ the algorithm is of $O(n^3)$, and for rectangular $A$ our algorithm is of $O(n^2m)$. 
