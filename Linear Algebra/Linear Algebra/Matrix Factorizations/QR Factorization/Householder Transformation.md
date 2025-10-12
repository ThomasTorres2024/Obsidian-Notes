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
Where $I \in \mathbb{R}^{(k-1) \times (k-1)}$, and $F \in \mathbb{R}^{(m-k+1)\times(m-k+1)}$ where $F$ is unitary as well. We want to introduce zeroes into column $k$ when we multiply by $F$. Householder transformation matrices are given by:
$$H=I-2\frac{xx^T}{x^Tx}$$
$H$ satisfies the conditions of being [[Hermitian]] and also being [[orthogonal]], both of which easily can be verified. We can interpret a matrix vector product with $H$ as a mapping. When computing $Hy$ we can see that:
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




