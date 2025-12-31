---
title: Computing SVD
tags:
draft: "False"
---
# Standard Method of Computing SVD 
[[Reduced SVD]] of a matrix $A \in \mathbb{R}^{m \times n}$ where $m \geq n$ (an SVD of $A$ that does not satisfy this condition can just as equal be found by computing the SVD of $A^T$ and then computing its [[Transpose]]) can be computed efficiently if $m >> n$ by the standard/by hand way of computing SVD:

* Form $A^TA \in \mathbb{R}^{n \times n}$, and compute an [[Eigen Value Decomposition]] of the symmetric matrix: $A^TA=V\Lambda V^T$. 
* We know that $\Sigma= \sqrt{\Lambda}$. 
* We can solve $U \Sigma = AV$ since we know $A,V,\Sigma$. 

This approach is typically the naïve approach done by hand. 

# Numerical Approach for Computing SVD 

 Our approach for computing the SVD of a matrix will use something similar to a [[similarity transformation]] which is meant to preserve the eigen values of a matrix. Here we want to preserve the [[singular value]]s of a matrix.  This approach is for matrices where $A \in \mathbb{R}^{m \times n}$ is medium sized, and fails at matrices that are absolutely massive.

It turns out for $A=U\Sigma V^H$ that, left and right multiplication by orthogonal matrices doesn't effect the singular values. 

This should make sense since the product of [[orthogonal]] matrices is another orthogonal matrix. For instance, take $U$ and $V$ of the same size. and consider:
$$UV$$
But $(UV)^{-1}=(UV)^T=V^T U^T$ because:
$$V^TU^TUV=UVV^TU^T=I$$
The resulting singular values of the matrix are unmodified when we do this, consider orthogonal matrix $Q_{1}$ conformable with $Q$:
$$Q_{1}\cdot Q \Sigma V^H$$
Notice that we have the same singular values for this matrix since $\Sigma$ is preserved. We don't need to worry about multiply by the same orthogonal matrix on the left and right, like in similarity transformations. 

Similar to the unshifted QR algorithm, we want to start by reducing $A$ to a simpler form. Here we reduce it to a [[Bidiagonal Matrix]]. It is a lot easier to work with this matrix.

### Summary of the Numerical Approach:

The algorithm performs with an efficiency of $O(n^3)$. This method is excellent up until we obtain a massive value of $n$. 

* 1.) Obtain a [[Bidiagonal Matrix]], $B$ from $A$ 
* 2.) Form $B^TB$, which is a [[triangular matrix]]
* 3.) Calculate the eigen values of $B^TB$ using [[QR Algorithm without Shifts]] and obtain their square roots  



