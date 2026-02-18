---
title: Symmetric Group
tags:
  - AbstractAlgebra
draft: "False"
---
# Symmetric Group
The [[Symmetric Group]] is a [[Group]] takes $A$ where:
$$A=\{1,2,3, \dots , n \}$$
The set of all permutations of $A$ is the [[Symmetric Group]] of degree $n$ which we denote by $S_{n}$. 

In table form, we can express elements of $S_{n}$ as the following:
$$\alpha = \begin{bmatrix}
1 & 2 & 3 & \dots & n \\ 
\alpha(1) & \alpha(2) & \alpha(3) & \dots  & \alpha(n)
\end{bmatrix}$$
The [[Order]] of the group, as we would intuitively expect for a group involving permutation is:
$$O(S_{n})=n!$$
For any given $\alpha$, we first have $n$ choices to begin with for $\alpha(1)$, and then $\alpha(2)$ has $n-1$ choices, and then $\alpha(3)$ has $n-3$ choices and so forth until we get to $\alpha(n)$ which has $1$ choice. Since $\alpha$ is a bijective function, we have no repeats and must hit every element in $A$. 

If $n \geq 3 \implies$ $S_{n}$ is NOT an [[Abelian Group]]. 