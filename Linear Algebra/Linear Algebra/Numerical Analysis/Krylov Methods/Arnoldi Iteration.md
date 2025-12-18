---
title: Arnoldi Iteration
draft: "False"
tags:
---
# Arnoldi Iteration
Arnoldi iteration is an [[orthogonal]]ization algorithm similar to the [[The Gram-Schmidt Process]]. Typically, we have 2 main ideas for orthogonalizing a Matrix, [[Householder Transformation]]s or Gram-Schmidt. This particular process allows us to implicitly generate an equivalent [[basis]] for the [[Krylov Subspace]] based on matrix $A$ and vector we are trying to solve $b$. 

Arnoldi iteration allows us to efficiently express $A$ as $A=QHQ^H$. 

The [[The Gram-Schmidt Process]] is famously [[numerically unstable]], but it has a key advantage of [[House Holder Reflectors]] in being able to stop short and not needing to do all of the computations to get an approximate $Q$. We can be satisfied with the first $k$ $q_{i}$ here instead of having to do the whole thing.

To reiterate the point of the method we are interested in obtaining the first $n$ [[orthonormal]] vectors of $Q$

















