---
title: Matrix Multiplication
tags:
draft: "False"
---
# Matrix Vector Product
Let $a_{j}$ by the $j$th column of the matrix $A \in \mathbb{R}^{m \times n}$ and $\vec{x} \in \mathbb{R}^n$. We can represent $A\vec{x}=\vec{b}$ using:
$$\vec{b}=A\vec{x}=\sum_{j=1}^n \vec{a}_{j} \cdot x_{j}$$
Which is to say that we are scaling each column in $A$ by each corresponding $j$th entry in $\vec{x}$ and summing them together to obtain our result. 

#### (Example) [[Vandermonde Matrix]]
We can use Vanermonde Matrices to represent polynomials. If we let $p$ and $q$ both be polynomials of degree $< n$ and also consider the fixed set of numbers $\{x_{1},x_{2},\cdots,x_{m} \}$. 

We can see that our polynomials satisfy [[Linearity]] as the following is true:
$$(p+q)(x_{i})=p(x_{i})+q(x_{i})$$
$$(\alpha p)(x_{i})=\alpha \cdot p(x_{i})$$
Any linear map, including [[Polynomial]]s, can be represented using Matrices, here for instance we would use a [[Vandermonde Matrix]]:
$$A = \begin{bmatrix}
1 & x_1 & x_1^2 & \cdots & x_1^{n-1} \\
1 & x_2 & x_2^2 & \cdots & x_2^{n-1} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x_m & x_m^2 & \cdots & x_m^{n-1}
\end{bmatrix}.$$
If we consider the product between $A$ and $\vec{c}=[c_{0} c_{1} \cdots c_{n-1}]^T$ we would see that each $i$th entry is given by:
$$(Ac)_{i} = \sum_{i=0}^n c_{i} \cdot x_{i}^i$$
# Matrix-Matrix Products
Let $B=AC$ where $A \in \mathbb{R}^{l \times m}$ and $B \in \mathbb{R}^{m \times n}$. We have that each column in $B$ is a linear combination of columns in $A$. That is to say that:
$$\vec{b}_{j}=\sum_{k=1}^n \vec{a}_{k} \cdot c_{kj}$$
We also have an entry-wise formula for entry $b_{ij}$ of $B$, which is given by:
$$b_{ij}= \sum_{k=1}^n a_{ik}\cdot c_{kj}$$
#### (Example) [[Outer Product]]
The [[Outer Product]] is a matrix product that involves multiplying vectors $\vec{v}^T \in \mathbb{R}^{1 \times n}$ and $\vec{u} \in \mathbb{R}^n$ to yield:
$$A=\vec{u} \cdot \vec{v}^T$$
Which yields a [[rank]] one matrix which each column of $A$, $\vec{a}_{j}$ corresponds to:
$$\vec{a}_{j}=\vec{u}\cdot v_{j}$$
Which is to say we just scale our vector $\vec{u}$ by an entry in $\vec{v}^T$.

#### (Example) [[Upper Triangular Matrix]]
We can express the product of an upper triangular, $R$ and $A$ by the following for $B=AR$:
$$\vec{b}_{j}=A\vec{r}_j= \sum_{k=1}^j \vec{a}_{k}\cdot r_{jk}$$
This works out nicely because we go down to the diagonal in each entry, and we do not need to continue computing extra entries. 