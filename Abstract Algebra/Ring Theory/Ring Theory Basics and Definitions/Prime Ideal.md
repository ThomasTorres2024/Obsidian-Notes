---
title: Prime Ideal
tags:
  - AbstractAlgebra
draft: "False"
---
# Prime Ideal Definition
A [[Prime Ideal]] is an [[Ideal (Rings)]] of a commutative [[Ring]] $R$ is a proper ideal of $R$ such that $a,b \in R$ and $ab \in A$ imply that $a\in A$ or $b\in A$. Motivation for this particular definition comes from the structure of $\mathbb{Z}$. 

---
# Examples.)

### Example 1).
Let $n \in \mathbb{N}$, then in $\mathbb{Z}$ the ideal $n\mathbb{Z}$ is prime $\iff n$ is prime. 

$\implies$
By contrapositive, suppose that $n$ is not prime, then $\exists1<s,t<n$ such that $st=n$. Then it follows that $1<s,t<n \implies s,t \not\in n\mathbb{Z}$. But since $st=n \implies st\in n\mathbb{Z}$ which gives the fact that $n\mathbb{Z}$ is __not__ a prime ideal. 

$\Longleftarrow$ 
Suppose now that $n=p$ is a prime and that $s,t \in \mathbb{Z}$ are such that $s,t \in p\mathbb{Z}$. Then, $st=pk$ for some $k \in \mathbb{Z}$, and so we have that, $p\bigg|st$. 

Since $p$ is a prime then either $p\bigg|s$ or $p\bigg|t$, such that either $s\in p\mathbb{Z}$ or $t \in p\mathbb{Z}$, which entails that either $s=p$ or $t=s$.

Since in both cases $p\mathbb{Z}$ is a prime ideal, then the proof holds. 

### Example 2.)
The ideal $\langle x^2+1 \rangle$ is not prime in $\mathbb{Z}_{2}[x]$, but it is a maximal ideal.  

For example consider $x+1 \not \in \langle x^2+1\rangle$. 

Then:
$$(x+1)^2=x^2+2x+1=x^2+1 \in \langle x^2+1 \rangle$$

