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
We need to be handle if 


