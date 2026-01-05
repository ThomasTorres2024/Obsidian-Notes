---
title: Efficient Matrix Multiplication
tags:
draft: "False"
---
# Efficient Matrix Multiplication 
[[Matrix Multiplication]] is generally $O(n^3)$ in time complexity. It is a very expensive operation that we want to make more efficient. Let us consider the following example for 3 matrices which are of sizes:
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