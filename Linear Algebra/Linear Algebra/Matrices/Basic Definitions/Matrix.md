---
title: Matrix
tags:
  - LinearAlgebra
  - AbstractAlgebra
draft: "false"
---
# Matrix Overview and Definition
Every [[Linear Transformation]] between finite [[Dimension]]al [[Vector Space]]s can be described using a [[Matrix]]. For [[Linear Transformation]]s between infinite dimensional [[Vector Space]]s other mathematical objects are required. More formally, for the set of matrices $\mathbb{F}^{m \times n}$ there is an [[Isomorphism]] to set of linear transformations from the vector space $\mathcal{M} \to \mathcal{N}$ where $\text{dim}(\mathcal{M})=m ,\text{dim}(\mathcal{N})=n$, symbolically:
 $$\mathbb{F}^{n \times n} \cong \mathcal{L}(\mathcal{M},\mathcal{N})$$
The addition of matrices is commutative and forms an [[Abelian Group]], and multiplication of matrices form a [[Ring]] which has an identity element, but is not commutative and has zero divisors. 

### Definition).
Let $\mathcal{V}$ be an $n$ dimensional [[Vector Space]], and let $\mathcal{X}=\{ x_{1},x_{2},x_{3},\cdots,x_{n} \}$ is a [[Basis]] of the [[Vector Space]]. Let $A$ be a linear transformation on $\mathcal{V}$, then we define the following for some vector in $\mathcal{V}$ transformed by $A$:

$$\begin{align}
Ax_{j}= \sum_{i} \alpha_{ij} x_{i}
\end{align}$$
For $j=1,\cdots,n$. The set of $(\alpha_{ij})$ of $n^2$ scalars (this assumes that the linear transformation is endomorphic). We express a matrix as a square array of its scalars in the following form: 
$$A=\begin{bmatrix}
\alpha_{11} & \alpha_{12} & \cdots & \alpha_{1n} \\
\alpha_{21} & \alpha_{22} & \cdots & \alpha_{2n} \\
\large \vdots & \large  \vdots  &  \large \ddots &  \large \vdots \\
\alpha_{n1} & \alpha_{n2} & \cdots & \alpha_{nn}
\end{bmatrix}$$
A matrix fixes the order of the elements of a basis, which is mostly irrelevant, which is a note worthy point of being mentioned.  

---
# Definition). Arithmetic of Matrices
For matrices of conformable size we write the operations of addition, multiplication of matrices, and scalar multiplication as:

$$\begin{align}
(\alpha_{ij})+(\beta_{ij})
=(\alpha_{ij}+\beta_{ij}) \\ 
\alpha(\alpha(ij))=(\alpha \alpha_{ij}) \\
(\alpha_{ij})(\beta_{ij}) = \sum_{k}\alpha_{ik}\beta_{kj}
\end{align}$$

# Theorem). 
Following the above definition for scalar multiplication, addition, and matrix multiplication, there is an [[Isomorphism]] between a set of matrices on a [[Vector Space]] and the set of [[Linear Transformation]]s on that space. 