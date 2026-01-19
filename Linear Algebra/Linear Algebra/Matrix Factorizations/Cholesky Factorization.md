---
title: Cholesky Factorization
draft: "false"
tags:
---
# Cholesky Factorization Definition

A matrix, $A \in \mathbb{C}^{n \times n}$ can be said to have a Cholesky factorization if $A$ [[Hermitian matrix]] [[Positive Definite Matrix]] (HPD). 

We can also obtain a Cholesky factorization if we can express $A=LU=LDV=LDL^T$ where all diagonal entries of $D$, $D_{ii} \in \mathbb{R}^{+}$ so that we can express $A$ as:

$$A=LDL^T=LD^{\frac{1}{2}}D^{\frac{1}{2}}L^T=LD^{\frac{1}{2}}(LD^{\frac{1}{2}})^T=RR^H$$

If we restrict ourselves to positive diagonal entries, then the factorization is unique. Otherwise, the factorization is not unique. 

We can think of the Cholesky factorization as finding $R$, a lower triangular matrix, which is the equivalent of a square root, since $RR^H=A$

---
# Numerical Computation of [[Cholesky Factorization]]

---
