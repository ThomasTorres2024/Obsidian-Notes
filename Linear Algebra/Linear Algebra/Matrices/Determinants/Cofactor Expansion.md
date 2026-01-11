---
title: Cofactor Expansion
tags:
draft: "false"
---
# Cofactor Expansion 
[[Cofactor Expansion]] is a method for computing the [[Linear Algebra/Linear Algebra/Matrices/Determinants/Determinant|Determinant]] of a matrix, $A \in \mathbb{R}^{n \times n}$. It is given using the following formula:
$$\sum_{i=1}^n (-1)^{i+1} \cdot a_{ij} \det(A_i)$$
Let $A_i$ be the [[Matrix of Minors]] which is the matrix found by deleting the corresponding row and column of our given $a_{ij}$ and then grouping the remaining indices into a new matrix. For example in the case of a $3 \times 3$ matrix, we can determine its [[Linear Algebra/Linear Algebra/Matrices/Determinants/Determinant|Determinant]] by choosing $j=1$ and doing:
$$\det\left( \begin{bmatrix} a_{11}&a_{12} & a_{13}\\
a_{21} & a_{22} & a_{23}\\
a_{31} & a_{32} & a_{33} 
\end{bmatrix}\right) = a_{11}\begin{bmatrix} a_{22} & a_{23}\\ a_{32} & a_{33} \end{bmatrix} - a_{12}\begin{bmatrix} a_{11} & a_{13}\\ a_{31} & a_{33} \end{bmatrix} +  a_{13}\begin{bmatrix} a_{21} & a_{22}\\ a_{31} & a_{33} \end{bmatrix}$$
The formula for the [[Linear Algebra/Linear Algebra/Matrices/Determinants/Determinant|Determinant]] with [[Cofactor Expansion]] is recursive, meaning we calculate the determinant of a $3 \times 3$ using the formula of a $2\times 2$, and the formula for a $4 \times 4$ uses a $3 \times 3$, and the formula of an $n \times n$ uses an $(n-1) \times (n-1)$. 