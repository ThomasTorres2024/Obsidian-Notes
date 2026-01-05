---
title: Numerical Stability
tags:
draft: "False"
---
# Numerical Stability Introduction
Computers use floating point arithmetic to represent numbers. Smaller numbers require more and more precision and more storage to properly render. Datatypes like long only really preserve a couple digits, and then we get garbage after that. When we take larger values, we tend to get less and less errors.

Especially if we have iterative methods, we need to make sure that what we are using is numerically stable, so that when we perform hundreds of iterations our answer does not diverge from the expected results. In [[Least Squares]] problems, we have a plethora of possible solutions, [[Householder Transformation]] [[QR Factorization]], [[The Gram-Schmidt Process]]/[[Modified Gram-Schmidt Process]] [[QR Factorization]] (unstable), [[normal equation]]s (highly unstable), and [[Single Value Decomposition]] which all differ in stability. Some solutions tend to be safer and thus nicer than other solutions. 

---
# Condition Number of a Matrix $A$ 
We can determine if a matrix is well conditioned, and thereby would be nice to compute and work with, by the following formula:
$$\mathcal{K}(A)=\|A\|\|A^{\dagger}\|=\frac{\sigma_{1}}{\sigma_{n}}$$
Which is the ratio of the greatest [[Singular Value]] to the lowest [[Singular Value]] that is non-zero. 