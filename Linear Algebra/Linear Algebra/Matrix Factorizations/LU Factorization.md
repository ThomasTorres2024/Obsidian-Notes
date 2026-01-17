---
title: LU Factorization
tags:
draft: "False"
---
# LU Factorization
A matrix has an $LU$ factorization if it can be expressed as the product of a [[Lower Triangular Matrices]] multiplied by an [[Upper Triangular Matrix]]:
$$A=LU$$
We can obtain $A$ by applying a series of [[Elementary Row Operations]] except for operations that are not lower triangular. We can get the following form by applying the operations:
$$\left(\prod_{i=1}^M L_{i}\right)\cdot A=U$$
Which then we can invert each $L_i$ and then obtain an $LU$ decomposition. The diagonal of each $L_{ii}$ and $L_{ii}^{-1}$ are 1. $LU$ decompositions are also unique. 