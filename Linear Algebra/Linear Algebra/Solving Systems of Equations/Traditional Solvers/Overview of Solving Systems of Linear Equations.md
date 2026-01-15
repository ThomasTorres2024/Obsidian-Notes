---
title: Overview of Solving Systems of Linear Equations
tags:
draft: "False"
---
# Overview of Solving Systems of Linear Equations
For solving systems of linear equations we have the following options:

# [[QR Factorization]]:
We have for some $A=QR$, that $Ax=b \implies Rx=Q^Tb$ which can then be solved by [[back-substitution]]. We can obtain a [[QR Factorization]] by either:
* [[The Gram-Schmidt Process]] ("triangular orthogonalization")
* [[Householder Transformation]]s ("orthogonal triangularization")

# [[Gaussian Elimination]]:
We determine an [[LU Factorization]] of a matrix $A$, giving us $U$, which allows us to use [[back-substitution]] to solve the system $Ax=b$. 