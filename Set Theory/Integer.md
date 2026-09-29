---
title: Integers
tags:
  - Set_Theory
draft: "False"
---
# Integers 
From an analysis perspective we can think of the [[Integer]]s as a subset of the [[Real Number]]s. The integers can be defined as an [[Inductive Set]]. 

We can define the set of positive integers to be the __real numbers that belong to every inductive set__. 

#### Definition -
A real number is called a positive integer if it belongs to every inductiive set. The set of positive integers is denoted by $\mathbb{Z}^+$. Note that by the definition of [[Inductive Set]], $1$ and its $n$th successor must be included in every possible inductive set, therefore it encompasses all of $\mathbb{Z}^+$. 

# Unique Factorization Theorem for Integers 
If $n$ and $d$ are integers where $n=cd$ for some integer $c$, then we say that $d$ is a divisor of $n$ or that $n$ is a multiple of $d$. 

From this we obtain the [[Fundamental Theorem of Arithmetic]]. This states that:
1. Every integer $n>1$ can be presented as a product of prime factors 
2. This factorization is unique up to their ordering of the factors 
###  Theorem - 1 
Every Integer $n>1$ is either a [[Prime]] or a product of primes.  

$Proof).$ 
We can use induction on this result for $n$. The result trivially holds for $n=2$. Assume it is true for any integer $k$ where $1<k<n$. 

If $n$ is not prime, it has a positive divisor $d$ such that $1<d<n$. Hence $n=cd$ for $1<c<n$, where $c,d<n$, each is either prime or a product of primes. This then entails that $n$ is a product of primes. 

Thus we have shown that for any given $n$ that either $n$ is prime or a product of primes. 

### Theorem - Unique Factorization Theorem
Every integer $n>1$ can be represented as a product of prime factors in only way, except for the order. 

$Proof)$.
Let uus induct on $n$. The result is trivial for $n=2$. Assume this is true for all integers $k$ where $1<k<n$. If $n$ is prime there is nothing more to prove, so now assume $n$ is commposite and that $n$ has two _distinct_ prime factorizations:

$$\begin{align}
n=p_{1}p_{2} \cdots p_{s} \\
n=q_{1}q_{2} \cdots q_{t} 
\end{align}$$
We need to show that $s=t$ and that each $p$ corresponds to some $q$. Notice that $p_1$ divides the product $q_{1}q_{2}\dots q_{t}$, so it must divide at least one of these, and since $p_1,q_1$ are prime and $p_{1}|q_{1} \implies p_{1}=q_{1}$. Now we can cancel both from each side and obtain:
$$\frac{n}{p_{1}}=p_{2}\cdots p_{s} = q_{2} \cdots q_{t}$$
Since $n$ is composiite, $1< \frac{n}{p_{1}} <n$, by the induction hypothesis then it must be  the case that the factorization are identical, which satisfies trhe criterion we were looking to show and thus completes the proof. 

