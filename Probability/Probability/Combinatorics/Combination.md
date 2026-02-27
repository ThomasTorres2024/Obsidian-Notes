---
title: Combination
tags:
  - Probability
  - Combinatorics
draft: "False"
---
# Combinations

Sometimes the order of our experiments is not relevant, as [[Permutation]]s take order into account. We want to be able to skirt around this, so we divide by the total number of trials, $k$. 

We denote this as "n choose k" which is given below:

$$C(n,k)= {n \choose k} = \dfrac{n!}{k!(n-k)!}$$
Notice that this is the same as dividing the permutations on $n$ items with $k$ slots, and then dividing it by $k!$. This is also known as the [[Binomial Coefficient]] and related to [[Pascal's Triangle]].  

For combinations if repetitions are allowed we have the following:
$$C(n+k_1-1,k)= {n \choose k} = \dfrac{(n+k-1)!}{k!(n-k)!}$$