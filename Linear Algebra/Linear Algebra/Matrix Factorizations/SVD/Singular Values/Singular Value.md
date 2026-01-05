---
title: Singular Value
tags:
draft: "false"
---
# Singular Value
The [[Singular Value]]s of a matrix are the diagonal entries of the matrix $\Sigma$ from $A=U \Sigma V^T$, satisfying:
$$\sigma_{1}\geq \sigma_{2} \geq \dots \geq \sigma_{p} \geq 0$$
It turns out that each [[Singular Value]] is given by the square roots of the [[eigen value]]s of the matrix $AA^T$/$A^TA$ (these matrices have the same [[eigen value]]s up to the number of 0's):
$$\sigma_{i}=\sqrt{ \lambda_{i} }$$
If $A$ is [[Hermitian]]/[[Symmetric Matrix]] then each $\sigma_{i}=|\lambda_{i}|$, as using the traditional [[Computing SVD]] algorithm would yield the same singular vectors and only remove any minus sign from the [[eigen values]]. 

The minimum and maximum $\sigma_{i}$ are especially relevant. For example it determines the rate of convergence in [[Gradient Descent]] algorithms. 

It also turns out that the singular values of a matrix satisfy some interesting properties of [[Matrix Norm]]s. For some $A \in \mathbb{R}^{m \times n}$:
$$\|A\|_{2}=\max \sigma_{i}$$
This is the equivalent to the maximum amount of dilation a matrix can achieve for some unit vector. 

The smallest singular value is equivalent to the smallest contraction performed by a Matrix:
$$\sigma_{p}= \inf \frac{\|Mx\|_{2}}{\|x\|_{2}}=\min \sigma_{i} = \|M^{-1}\|^{-1}$$
We can think of the least singular value as a measure of how [[Invertible]] a matrix is. If $M$ is 0, the matrix is not invertible, if it is smaller, the less invertible the matrix. 
