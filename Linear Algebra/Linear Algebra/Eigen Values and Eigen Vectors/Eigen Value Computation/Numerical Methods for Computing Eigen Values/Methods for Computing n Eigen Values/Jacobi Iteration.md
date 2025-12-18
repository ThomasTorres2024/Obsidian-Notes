---
title: Jacobi Iteration
draft: "False"
tags:
---
# Jacobi Iteration
A very old algorithm for computing [[eigen value]]s of matrices introduced in 1845. The algorithm recently has gained attention, and is a part of an active area of research, especially due to parallel computing. For $A \in \mathbb{R}^{m \times m}$, if $m \geq 5$, by [[Abel's Theorem]], it follows that no single step exists to force the matrix into a [[diagonal matrix]] or a [[triangular matrix]] via [[Schur's Triangularization]]. 

Jacobi iteration asks us to apply a diagonalization algorithm on submatrices that can be handled in a single step. There have been attempts to use $4 \times 4$ matrices for this reduction, but the standard approach is to apply a $2 \times 2$ [[Givens Matrix]]. We assume here that $A=A^T$ and that $A$ is real. $A$ is [[diagonalizeable]] in the following form:
$$J^TAJ=J^T \begin{bmatrix} a & d\\ d & b \end{bmatrix} J = \begin{bmatrix} \neq 0 & 0\\ 0 & \neq 0 \end{bmatrix}$$
We can make use of [[House Holder Reflectors]] if we wish, but the standard approach is to use [[Givens Matrix]](ces) to accomplish our task. 

If we look for the matrix $J$ that diagonalizes $A$, it turns out that the appropriate angle for our cosine and sine functions is actually:
$$\tan(2 \theta)=\frac{2d}{b-a}$$
This particular kind of Matrix here is known as "[[Jacobi Rotation]]". The only difference here is that we are trying to force a diagonalization rather than a triangular matrix. 

We can generalize this idea to take on symmetric $m \times m$ matrices instead of just 2 by 2. When we apply a [[Jacobi Rotation]] to $A$, we introduce 2 pairwise zeros in two rows, and 2 pairwise zeros in 2 columns. Subsequent iterations of Jacobi Iteration may destroy zeros that we already introduced. However, the non-zeros shrink at each stage. Jacobi iteration is ultimately has a quadratic runtime, or somewhat better than quadratic. We do not do any initial [[Tridiagnolization]] on the matrix $A$, because then applying the Jacobi matrices would destroy the structure. Practically, [[Jacobi Iteration]] is not nearly as good as the [[QR Algorithm without Shifts]] or [[Divide and Conquer Algorithm for Eigen Values]]. Though, it is close. 

























