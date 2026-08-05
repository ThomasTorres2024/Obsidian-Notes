---
title: Normal Matrices
draft: "false"
tags:
---
# Normal Matrices and Spectral Theorem Proof 

A normal matrix, $A \in \mathbb{C}^{n \times n}$ is normal if $A^HA=AA^H$. 

We know that unitary matrices, Hermitian matrices, skew-Hermitian matrices, and  diagonal matrices are also normal matrices.

If $A$ is a unitary matrix, then $A^HA=I_{n}$ and $AA^H=I_{n}$ then $A^HA=AA^H=I_{n} \implies A$ is normal. 

If $A$ is Hermitian then $A^H=A$, so $A^HA=A^2$ and $AA^H=A^2$ so $AA^H=A^HA=A^2 \Longrightarrow A$ is normal

If $A$ is Skew-Hermitian then $A^H=-A$ so $A^HA=-A^2$ and $AA^H=-A^2 \implies AA^H=A^HA=-A^2$ is normal  

If $A$ is Diagonal then $A^H=A$, so $A$ is Hermitian, so $A$ is normal

The total class of normal matrices is NOT limited to the aforementioned special types of matrices. Any matrix that satisfies the definition of normal is simply normal. 

---

# Complex Spectral Decomposition 

We will prove that any matrix $A \in \mathbb{C}^{n \times n}$ is unitarily diagonalizable. 

Suppose $A \in \mathbb{C}^{n \times n}$ then exists a unitary matrix $U,D \in \mathbb{C}^{n\times n}$ where $U$ is orthogonal and $D$ is a diagonal matrix such that we can express $A$ as:

$$A=UDU^H$$

$\textbf{if and only if } A$ is normal. 

## Proof 

### Case 1. If $A=UDU^H \implies A$ is normal:

$$AA^H=(UDU^H)(UDU^H)^H=UDU^HUD^HU^H=UD^HDU^H $$

Due to commutativity of the complex numbers, it follows that:

$$ UD^HDU^H=U \cdot \begin{bmatrix} d_{11}\bar{d_{11}} & 0 & 0 & \dots & 0\\ 0 &d_{22}\bar{d_{22}}  & 0 & \dots & 0\\
\vdots & \vdots & \ddots & \dots & \vdots\\
0 & 0 & 0 & 0 &d_{nn}\bar{d_{nn}} 
\end{bmatrix} \cdot U^H =  $$
$$U\begin{bmatrix} \bar{d_{11}}d_{11} & 0 & 0 & \dots & 0\\ 0 &\bar{d_{22}}d_{22}  & 0 & \dots & 0\\
\vdots & \vdots & \ddots & \dots & \vdots\\
0 & 0 & 0 & 0 &\bar{d_{nn}}d_{nn}
\end{bmatrix}U^H=UDD^HU^H = A^HA$$

If $A$ is unitarily diagonalizable, then $AA^H=A^HA$, so $A$ must be normal.

### Case 2. If $A$ is normal, then $\exists U,D \in \mathbb{C}^{n \times n}$ where $U$ is orthogonal and $D$ is a diagonal matrix 

Via Schur's Triangularization we can state that $\exists U, T_{A} \in \mathbb{C}^{n \times n}$ such that 
$$A = UT_{A}U^H$$
$$A^H=UT_{A}^HU^H$$
$$AA^H = UT_{A}U^H\cdot UT_{A}U^H=UT_{A}T_{A}^HU^H$$
$$A^HA=UT_{A}^HT_{A}U^H$$

Since $A$ is a normal matrix, it follows that: 

$$A^HA=AA^H=UT_{A}^HT_{A}U^H=UT_{A}T_{A}^HU^H $$
$$T_{A}^HT_{A}=T_{A}T_{A}^H$$

We can argue that $T_{A}^HT_{A}$ and $T_{A}T_{A}^H$ are both diagonal matrices. This is a bit tedious to do, but I will outline the logic of why this is the case. If we carry out matrix multiplication on each side and equate both sides we will see that many elements in the equality will have to be zero to be true. 

From this, the only values that are not guaranteed to be zero are the diagonal values of the upper triangular matrices. It follows that $T_{A}$ is a diagonal matrix, which is our desired result. 

---
# Results of Spectral Theorem 

Since $A$ is normal $\Longleftrightarrow A=UDU^H$ we can draw the following conclusions:
* Normal matrices are unitarily diagonalizable, that is we can express any normal matrix as $UDU^H$
* The eigen vectors of $A$ form an orthonormal basis of $\mathbb{R}^n$. Since $UDU^H$ is a diagonalization of $A$ and a similarity transformation, it follows that $U$ consists of all eigen vectors of $A$, and furthermore that each vector in it must be normal since $U$ is an orthogonal matrix 