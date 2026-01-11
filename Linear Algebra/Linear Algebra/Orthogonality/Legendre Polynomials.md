---
title: Legendre Polynomials
tags:
draft: "False"
---

# [[QR Factorization]] for Continuous Functions 

There is analogue for expanding complex functions that is an extension of that of vectors. Instead of considering $\mathbb{C}^m$ we choose $L^2[-1,1]$, which consists of a [[Vector Space]] of complex functions on the interval $[-1,1]$. 

The inner product of two functions $f,g\in L^2[-1,-1]$ then the [[inner product]] between these two functions is:
$$\langle f, g\rangle = \int_{-1}^1\overline{f(x)}g(x)dx$$
For example, we can consider the matrix consisting of monomials of $x^j$ where $1 \leq j \leq n:$ 
$$
A = \left[
\begin{array}{c|c|c|c|c}
\rule{0pt}{2.5ex}1 &
\rule{0pt}{2.5ex}x &
\rule{0pt}{2.5ex}x^2 &
\rule{0pt}{2.5ex}\cdots &
\rule{0pt}{2.5ex}x^{n-1}
\end{array}
\right]

$$
$$
A = QR =
\begin{bmatrix}
q_0(x) \mid q_1(x) \mid \cdots \mid q_{n-1}(x)
\end{bmatrix}
\begin{bmatrix}
r_{11} & r_{12} & \cdots & r_{1n} \\
0      & r_{22} & \cdots & r_{2n} \\
\vdots & 0      & \ddots & \vdots \\
0      & \cdots & 0      & r_{nn}
\end{bmatrix}
$$

Then we can express $A$ using a QR factorization where each $q$ is a function from an orthonormal basis of functions on $L^2[-1,1]$, and  

We are able to construct an orthonormal basis of functions $q_{i}(x)$ that satisfy:
$$\int_{-1}^1\overline{q_{i}(x)}q_{j}(x)dx= \delta_{ij} =\begin{cases} 1 \text{ if i =j}\\0 \text{ if i} \neq j \end{cases}$$
$q_{j}$ is a polynomial of degree $j$. We can describe the [[Vector Space]] of polynomials using the Legendre polynomials, $P_{j}$ which have the basis given by: 
$$P_{0}(x)=1,P_{1}(x)=x,P_{2}(x)=\frac{3x^2-1}{2},P_{3}(x)=\frac{5x^3-3x}{2}$$
The [[Legendre Polynomials]] are a basis for the polynomials of degree $j$, but they are furthermore an [[orthogonal]] basis that spans the set of polynomials. 

We can define [[Projection Matrices]] with respect to the [[Legendre Polynomials]] by a "matrix" on $[-1,1] \times [-1,1]$, which is an integral operator of the form: 
$$f(\cdot) \mapsto \sum_{j=0}^{n-1} q_{j}(\cdot) \int_{-1}^1 \overline{q_{j}(x)}f(x)dx $$
which really is a map $L^2[-1,1] \to L^2[-1,1]$.  