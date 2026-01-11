---
title: Recursive Least Squares
tags:
draft: "false"
---
# Recursive Least Squares Overview 
If $A \in \mathbb{R}^{m \times n}$ where $m \geq n$. Using the [[normal equation]]s for solving [[Least Squares]], then we express some new data matrix for our points. Here is our [[normal equation]]s expression: $$Ax=b \to A^TAx=A^Tb$$
Our new data point can be included as: $$B=\begin{bmatrix} A\\ v^T\end{bmatrix}x =\begin{bmatrix} b\\ \delta\end{bmatrix}$$
Our [[normal equation]]s now can be re-expressed with $B$ by:
$$B^TB\hat{x}=B^Tb$$
$$\begin{bmatrix} A^T& v\end{bmatrix} \begin{bmatrix} A\\ v^T\end{bmatrix} \hat{x}=B^Tb$$
$$(A^TA+vv^T)\hat{x}=B^Tb=A^Tb+v\delta$$
$$(A^TA+vv^T)\hat{x}=A^Tb+v\delta$$
Notice that this is a [[Rank 1 Perturbation]] of our given [[system of equations]]. We want to avoid doing additional computations, and just work with the perturbation and the new point, ideally we want to minimize new computations or re-computations of [[Least Squares]]. 

Speaking only in terms of theory, we can invert the above matrix by using the [[Rank 1 Perturbation]] formula that we just computed. We can go beyond this formulation to an improved version that takes account of the probability that the incoming data points for our new function are correct. This method is a significantly more robust variant of [[Least Squares]], and is known as the [[Kalman Filter]]. 