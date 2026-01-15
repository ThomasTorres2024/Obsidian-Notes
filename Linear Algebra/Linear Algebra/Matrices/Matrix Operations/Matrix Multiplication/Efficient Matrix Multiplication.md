---
title: Efficient Matrix Multiplication
tags:
draft: "False"
---
# Efficient Matrix Multiplication 
[[Matrix Multiplication]] is generally $O(n^3)$ in time complexity. It is a very expensive operation that we want to make more efficient. 

We can theoretically speed up the process of [[Matrix Multiplication]] via the [[Strassen Matrix Multiplication Algorithm]], which is useful for matrices, perhaps square, where $n > 100$. 

There are many improvements which provide better time complexities, but ultimately are useless. We would need a matrix in the size of billions for this idea to actually beat traditional methods. 

---
# [[Divide and Conquer Algorithm]]

[[Matrix Multiplication]] can also be implemented using a [[Divide and Conquer Algorithm]], which partitions each matrix recursively into the following, which only works for square matrices:
$$\begin{bmatrix} C_{11} & C_{12}\\ C_{21} & C_{22} \end{bmatrix} = \begin{bmatrix} A_{11} & A_{12}\\ A_{21} & A_{22} \end{bmatrix} \begin{bmatrix} B_{11} & B_{12}\\ B_{21} & B_{22} \end{bmatrix}= \begin{bmatrix} A_{11}B_{11}+A_{12}B_{21} & A_{11}B_{12}+ A_{12}B_{22}\\ A_{21}B_{11}+A_{22}B_{21} & A_{21}B_{12}+A_{22}B_{22} \end{bmatrix}$$
The general cost function for this algorithm is $T(1)=\Theta(1)$ for a scalar operation, and for the recursive part we obtain:
$$T(n)=8T(n/2)+\Theta(n^2)$$
The result still has a time complexity of $\Theta(n^3)$ in the end. 
# Efficient Computation of 3 Matrices By Order of Operation
Let us consider the following example for 3 matrices which are of sizes:
$$A \in \mathbb{R}^{m \times n},B \in \mathbb{R}^{n \times p},C \in \mathbb{R}^{p \times q}$$
Where we are trying to compute the matrix:
$$ABC$$
If we do the computation of $BC$ we need to do $npq$ operations. This is because the resulting matrix will be of size $\mathbb{R}^{n \times q}$. Every number inside  is an inner product, there are $n \times q$ many inner products, and each inner product took roughly $p$ operations (not counting scalars). We then have:
$$A\cdot (BC) \in \mathbb{R}^{m \times q}$$
This has a cost of $mq \times n$ many operations. We have $m \times q$ many entries, of which each costs roughly $n$ operations to compute. The total cost with this order is thus:
$$mqn+npq=nq(m+p)$$
Let us consider a different order, where we instead do $AB$ first. We will then be doing $mpn$ many operations for this first computation. Then when doing $(AB)\cdot C$ we need to do $mqp$ many operations. This has the resulting cost of:
$$mpn+mqn=mn(q+p)$$
The cost $n$ is going to remain the same across both examples so the costs we are comparing actually consist of:
$$q(m+p) \text{ vs } m(q+p)$$
Depending upon the sizes of our matrices, we would choose the one which has the smallest overall operation cost. If we consider the case where $C$ is a vector, then, we would clearly want to do $BC$ first, since this a vector, and computing vectors is much easier. Here $q=1$, and we would thus be computing either:
$$m+p \text{ vs } mp+m$$
Obviously, for most cases we would want to do $m+p$ meaning that we do $BC$ first for most $m$ and $p$. This gives us the example that there can be a substantial difference in the total number of operations. 