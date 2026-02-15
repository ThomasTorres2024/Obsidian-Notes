---
title: Chinese Remainder Theorem
tags:
  - NumberTheory
draft: "False"
---
# Chinese Remainder Theorem 
Consider $k$ natural numbers, $n_1,n_2,\dots, n_k$ where the numbers are pairwise [[Relatively Prime]], that is to say $\gcd(n_i,n_j)=1$, and $b_1,b_2, \dots , b_k \in \mathbb{Z}$, then  the following [[system of equations]] has the solution:
$$x \equiv b_1 \mod(n_1)$$
$$\vdots$$
$$x \equiv b_k \mod(n_k)$$
### Proof.) 
The proof of the theorem is constructive. Let $N$ be the following product:
$$N = \prod_{i=1}^k n_i$$
And let $N_i$ be:
$$N_i = \frac{N}{n_i}$$
###### Claim.) 
We claim that $\gcd(n_i,N_i)=1$. 
Suppose that $d | n_i$ and $d | N_i$. Since all of the $n_j$ are relatively prime to $n_i$ and $N_i$, then this indicates that $\exists n_j$ in the product of $N_i$ such that $d | n_j$, but notice that this contradicts the assumption that $\gcd(n_i,n_j)=1$ if we are to assume $d \neq 1$. 
$$\tag*{$\Diamond$}$$
Now we know that $\gcd(n_i,N_i)=1$. Using [[Bézout’s Identity]], we know that $N_i$ in our system has a modular inverse $x_i$ given by:
$$N_i x_i \equiv  1 \mod(n_i)$$
Also note that for $j \neq i$ we have that:
$$x_i  N_i \equiv 0 \mod(n_j)$$
Consider the following where $X$ is:
$$X= \sum_{i=1}^k x_iN_ib_i$$
And consider it $\mod(n_i)$. Since every term except $N_i$ contains $n_i$, then:
$$X \mod(n_i) = \left[ \sum_{i=1}^k x_iN_ib_i \right] \mod(n_i) = 0+0+\dots + x_iN_ib_i + 0 + \dots +0$$
But we know that $x_iN_i \equiv 1 \mod(n_i)$ so:
$$X \mod(n_i) = \left[ \sum_{i=1}^k x_iN_ib_i \right] \mod(n_i) = b_i$$
It then follows that:
$$X \equiv b_i \mod(n_i) : 1 \leq i \leq k$$
Therefore, we have shown by a constructive proof that the solution exists. Furthermore, we want to show that it is unique. 

If $x$ and $y$ are both solutions where: 
$$x= b_i \mod(n_i), y=b_i \mod(n_i) : 1 \leq i \leq k$$
Then:
$$x-y \equiv 0 \mod(n_i) $$
Then we have that:
$$n_i | x-y  \implies N |x-y \implies x \equiv \mod(n)$$